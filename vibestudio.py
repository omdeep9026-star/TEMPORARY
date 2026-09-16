# -*- coding: utf-8 -*-
"""vibestudio — coding-agent harness for GPU video editing on Colab
Primitives: trim, music mix, reframe, color grade, text overlay, subtitle burn, Drive upload.
Agent composes these inside run_pipeline() to accomplish the task.
"""

# ── Setup (runs once per Colab session) ────────────────────────────────────────
import subprocess, sys

def _setup():
    subprocess.run(
        ["apt-get", "update", "-qq"], check=True,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    subprocess.run(
        ["apt-get", "install", "-y", "-qq",
         "cmake", "build-essential", "fonts-freefont-ttf", "libass-dev"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    subprocess.run(
        "bash <(curl -s https://raw.githubusercontent.com/XniceCraft/ffmpeg-colab/master/install)",
        shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", "--no-cache-dir", "faster-whisper"],
        check=True
    )
    print("✅ Environment ready")

_setup()

# ── Imports ────────────────────────────────────────────────────────────────────
import shutil
from pathlib import Path
from faster_whisper import WhisperModel

# ── Helpers ────────────────────────────────────────────────────────────────────

def _run(cmd: list, silent=False):
    """Run a subprocess, streaming output unless silent=True."""
    kwargs = dict(check=True)
    if silent:
        kwargs.update(stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(cmd, **kwargs)

def _srt_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def _make_manifest(clip_paths: list[str], manifest_path="inputs.txt") -> str:
    with open(manifest_path, "w") as f:
        for p in clip_paths:
            f.write(f"file '{Path(p).resolve()}'\n")
    return manifest_path

# ── Edit Primitives ────────────────────────────────────────────────────────────

def trim(input: str, start: str, end: str, output: str) -> str:
    """Trim a single clip. start/end as 'HH:MM:SS' or seconds."""
    print(f"✂️  Trimming {input} [{start} → {end}]")
    _run(["ffmpeg", "-y", "-i", input, "-ss", str(start), "-to", str(end),
          "-c", "copy", output], silent=True)
    return output

def add_music(video: str, music: str, output: str, music_vol: float = 0.12) -> str:
    """Mix background music under the video's audio, ducked to music_vol."""
    print(f"🎵 Mixing music: {music} at vol={music_vol}")
    _run([
        "ffmpeg", "-y", "-i", video, "-i", music,
        "-filter_complex",
        f"[1:a]volume={music_vol}[bg];[0:a][bg]amix=inputs=2:duration=first[aout]",
        "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        output
    ])
    return output

def reframe(input: str, output: str, target: str = "9:16") -> str:
    """Crop/scale to target aspect ratio. target: '9:16' or '16:9' or '1:1'."""
    print(f"📐 Reframing to {target}")
    ratio_map = {
        "9:16": "ih*9/16:ih",   # portrait — crop width
        "16:9": "iw:iw*9/16",   # landscape — crop height
        "1:1":  "ih:ih",
    }
    crop = ratio_map.get(target, "ih*9/16:ih")
    w, h = crop.split(":")
    _run([
        "ffmpeg", "-y", "-i", input,
        "-vf", f"crop={w}:{h},scale=1080:1920" if target == "9:16" else f"crop={w}:{h}",
        "-c:v", "h264_nvenc", "-preset", "p4", "-cq", "23",
        "-c:a", "copy", output
    ])
    return output

def color_grade(input: str, output: str, lut: str = None, preset: str = "warm") -> str:
    """Apply a LUT file, or a built-in ffmpeg preset: 'warm', 'cold', 'cinematic'."""
    print(f"🎨 Color grading ({lut or preset})")
    presets = {
        "warm":       "curves=r='0/0 0.5/0.6 1/1':g='0/0 0.5/0.5 1/1':b='0/0 0.5/0.4 1/0.9'",
        "cold":       "curves=r='0/0 0.5/0.4 1/0.9':g='0/0 0.5/0.5 1/1':b='0/0 0.5/0.6 1/1'",
        "cinematic":  "curves=all='0/0 0.08/0.1 0.92/0.9 1/1',eq=contrast=1.05:saturation=0.85",
    }
    vf = f"lut3d={lut}" if lut else presets.get(preset, presets["warm"])
    _run([
        "ffmpeg", "-y", "-i", input, "-vf", vf,
        "-c:v", "h264_nvenc", "-preset", "p4", "-cq", "23",
        "-c:a", "copy", output
    ])
    return output

def overlay_text(input: str, output: str, text: str,
                 position: str = "bottom", fontsize: int = 48,
                 color: str = "white") -> str:
    """Burn a text overlay. position: 'top', 'center', 'bottom'."""
    print(f"📝 Overlaying text: '{text}'")
    y_map = {"top": "h*0.08", "center": "(h-text_h)/2", "bottom": "h*0.85"}
    y = y_map.get(position, "h*0.85")
    drawtext = (
        f"drawtext=text='{text}':fontsize={fontsize}:fontcolor={color}:"
        f"x=(w-text_w)/2:y={y}:shadowcolor=black:shadowx=2:shadowy=2"
    )
    _run([
        "ffmpeg", "-y", "-i", input, "-vf", drawtext,
        "-c:v", "h264_nvenc", "-preset", "p4", "-cq", "23",
        "-c:a", "copy", output
    ])
    return output

# ── Core Pipeline ──────────────────────────────────────────────────────────────

def _extract_audio(manifest: str, audio_out: str = "timeline_audio.wav"):
    print("⏳ Extracting audio for transcription...")
    _run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", manifest,
        "-vn", "-c:a", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_out
    ], silent=True)
    return audio_out

def _transcribe(audio: str, srt_out: str = "captions.srt", model_size: str = "small"):
    print(f"🎙️ Transcribing with Whisper ({model_size})...")
    model = WhisperModel(model_size, device="cuda", compute_type="float16")
    segments, _ = model.transcribe(audio, beam_size=5)
    with open(srt_out, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            f.write(f"{i}\n{_srt_timestamp(seg.start)} --> {_srt_timestamp(seg.end)}\n{seg.text.strip()}\n\n")
    print(f"✅ Captions: {srt_out}")
    return srt_out

def _render(manifest: str, srt: str, output: str):
    print("🚀 Rendering with NVENC...")
    sub_style = (
        "FontSize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
        "BackColour=&H80000000,BorderStyle=3,Outline=1.5,Shadow=0,MarginV=35"
    )
    _run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", manifest,
        "-vf", f"subtitles={srt}:force_style='{sub_style}'",
        "-c:v", "h264_nvenc", "-preset", "p4", "-cq", "23",
        "-c:a", "aac", "-b:a", "192k", output
    ])
    print(f"🎉 Render complete: {output}")

def _upload_to_drive(file: str, drive_folder: str = "VibeStudio"):
    """Upload output to Google Drive via Colab's drive mount."""
    from google.colab import drive
    drive.mount("/content/drive", force_remount=False)
    dest_dir = Path(f"/content/drive/MyDrive/{drive_folder}")
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / Path(file).name
    shutil.copy(file, dest)
    print(f"☁️  Uploaded to Drive: MyDrive/{drive_folder}/{Path(file).name}")

# ── Entry Point ────────────────────────────────────────────────────────────────

def run_pipeline(clip_paths: list[str], output_filename: str = "final_video.mp4",
                 drive_folder: str = "VibeStudio"):
    """
    Default pipeline: concat → transcribe → subtitle burn → Drive upload.
    Agent should call the primitives above BEFORE this if trimming/grading/music is needed,
    then pass the processed clip paths here.
    """
    manifest = _make_manifest(clip_paths)
    audio    = _extract_audio(manifest)
    srt      = _transcribe(audio)
    _render(manifest, srt, output_filename)
    _upload_to_drive(output_filename, drive_folder)
