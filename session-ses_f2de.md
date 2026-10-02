# YouTube channel knowledge base research

**Session ID:** ses_f2de9ab4effeqefH6MpyhdfGAE
**Created:** 9/24/2026, 6:24:33 AM
**Updated:** 9/24/2026, 6:27:20 AM

---

## User

You are in RESEARCH + PLANNING MODE ONLY.

DO NOT IMPLEMENT ANYTHING.
DO NOT CREATE OR MODIFY PROJECT FILES.
DO NOT INSTALL DEPENDENCIES.
DO NOT CLONE/RUN candidate projects unless necessary for inspection.
DO NOT start coding after finding one plausible repository.

GOAL

I want to build a robust system that takes a public YouTube channel URL, such as:

https://www.youtube.com/@DailyCuriously/shorts

and turns the channel into a structured, LLM-friendly knowledge base.

The eventual system should be capable of collecting and organizing publicly available information such as:

CHANNEL
- channel metadata
- about/description
- creation information where available
- playlists
- public channel structure
- external links where available

VIDEOS
- complete public video inventory
- video IDs and URLs
- titles
- descriptions
- publication timestamps
- duration
- Shorts vs long-form
- thumbnails
- hashtags
- categories/tags where obtainable
- chapters where obtainable
- transcripts/captions where obtainable

COMMENTS
- public comments where obtainable
- top-level comments
- replies
- timestamps
- comment ordering
- earliest currently retrievable public comment
- pagination
- handling of disabled/deleted/unavailable comments

DERIVED/LLM INFORMATION
- topic classification
- topic evolution
- recurring subjects/entities
- title patterns
- format patterns
- publishing patterns
- audience questions/themes
- content clusters
- relationships between videos
- useful cross-video analysis

OUTPUT

Eventually I want a structure similar to:

channel.md
timeline.md
topics.md
audience.md
videos/
    VIDEO_ID.md
comments/
    VIDEO_ID.json
raw/
    channel.json
    videos.json
    comments.json

The exact architecture is NOT decided yet.

YOUR TASK

Research existing open-source projects that already solve parts of this problem.

I specifically do NOT want you to simply search for:

"YouTube to Markdown"

and choose the first result.

I want you to identify mature-enough projects with understandable software architecture that we can reuse, adapt, combine, or learn from.

SEARCH STRATEGY

Use the available research capabilities, GitHub MCP, web research, and repository inspection.

Search broadly for projects involving:

- YouTube channel extraction
- YouTube channel archiving
- YouTube transcript extraction
- YouTube comments extraction
- YouTube knowledge bases
- YouTube RAG
- YouTube MCP servers
- YouTube → Markdown
- YouTube → JSON
- YouTube research tools
- YouTube metadata extraction
- channel crawlers
- video knowledge bases

Do not restrict yourself to Python.

Consider Python, TypeScript, Go, Rust, etc.

REPOSITORY SELECTION

Do NOT use GitHub stars as a quality score.

Stars are only one signal.

Prefer the "moderately established and architecturally understandable" range.

Look for evidence such as:

- meaningful commit history
- multiple commits over time
- recent maintenance
- multiple contributors where applicable
- releases/tags
- tests
- clear dependency management
- sensible project structure
- documentation
- issues/PR activity
- real separation of concerns
- reusable modules
- clear interfaces
- reasonable licensing

Do not automatically reject a low-star project if its architecture is excellent.

Do not automatically trust a high-star project if its architecture is poor.

IMPORTANT ARCHITECTURE REQUIREMENT

For every serious candidate, inspect the actual source code.

Do NOT rely only on:
- README
- GitHub description
- stars
- screenshots
- marketing claims

Use Gitingest to ingest/inspect candidate repositories.

Our environment has Gitingest available through Python. If needed, determine the correct way to invoke the installed Gitingest tool/package and use it for repository inspection.

I want to understand:

1. Where does YouTube extraction happen?
2. Where are channel/video/comment models defined?
3. Where is pagination handled?
4. Where are retries/rate limits handled?
5. Where is data normalized?
6. Where is persistence handled?
7. Where is Markdown/JSON output generated?
8. Where would a new comments extractor belong?
9. Where would a new LLM-oriented Markdown exporter belong?
10. Where are tests located?
11. How easy would it be to replace one extraction mechanism with another?

ARCHITECTURAL TEST

For each promising repository, perform this thought experiment:

"If we needed to add complete public YouTube comment extraction and an LLM-optimized Markdown exporter, exactly where would those components go?"

Identify the existing modules/files that would be involved.

If the answer essentially becomes "put everything in main.py", treat that as a significant architectural weakness.

Look for an understandable pipeline resembling some version of:

YouTube source
    ↓
extraction
    ↓
normalization/domain models
    ↓
storage
    ↓
processing
    ↓
export
    ↓
LLM/RAG

The actual architecture does NOT need to match this exactly.

TECHNICAL INSPECTION

For each candidate, investigate:

A. Project structure
B. Main entry points
C. Dependencies
D. YouTube extraction mechanism
E. API requirements
F. yt-dlp usage if applicable
G. transcript implementation
H. comments implementation
I. pagination
J. rate limiting/retries
K. caching
L. persistence
M. output formats
N. Markdown generation
O. tests
P. error handling
Q. extensibility
R. maintenance
S. license

YOUTUBE-SPECIFIC RELIABILITY

Pay particular attention to:

- YouTube API quota requirements
- API keys/OAuth requirements
- yt-dlp dependence
- transcript availability
- videos without captions
- disabled comments
- deleted/private videos
- Shorts
- channel pagination
- comment pagination
- reply pagination
- age-restricted content
- rate limiting
- transient failures
- deleted videos
- unavailable metadata

Do not assume a feature exists because a README says it exists.

Verify it in the source where possible.

CANDIDATE COMPARISON

Find roughly 8–12 serious candidates if enough exist.

For each candidate produce:

- repository
- language
- approximate maturity
- maintenance status
- architecture quality
- channel support
- video support
- transcript support
- comments support
- metadata support
- Markdown support
- JSON support
- API requirements
- major dependencies
- testing situation
- license
- important weaknesses
- useful components we could reuse

Do not produce a simplistic "best repository" ranking.

Instead identify:

1. Strong candidates for channel enumeration
2. Strong candidates for transcript extraction
3. Strong candidates for comment extraction
4. Strong candidates for metadata extraction
5. Strong candidates for storage
6. Strong candidates for Markdown/LLM export
7. Strong candidates for search/RAG
8. Strong architectural references

COMPOSITION ANALYSIS

Determine whether one project is sufficient.

If not, identify a sensible composition of existing components.

For example:

Project A:
channel/video enumeration

Project B:
transcript extraction

Project C:
comments

Project D:
storage/search

Project E:
Markdown export

But do NOT decide implementation yet.

We need to know whether combining projects is actually practical and whether their licenses and architectures permit it.

LICENSE

Inspect the actual LICENSE file.

Record:

- license
- whether modification is permitted
- whether redistribution is permitted
- notable obligations

Do not make legal conclusions beyond the license text.

RESEARCH OUTPUT

At the end, produce a detailed research report with these sections:

# 1. Problem Definition

Precisely define what we're trying to build.

# 2. Search Strategy

Explain what categories of repositories were searched.

# 3. Candidate Repositories

A table covering the serious candidates.

# 4. Architecture Inspection

For each serious candidate, explain the actual architecture based on source inspection.

# 5. Capability Matrix

Compare:

Channel
Videos
Transcripts
Comments
Replies
Metadata
Playlists
Thumbnails
Markdown
JSON
Storage
Search/RAG
API requirements

# 6. Architecture Quality

For each serious candidate:

- separation of concerns
- modularity
- testability
- extensibility
- maintainability
- error handling
- data model quality

Use descriptive assessments such as:
CLEAR / PARTIAL / WEAK / UNKNOWN

Do not invent numerical scores.

# 7. Reusable Components

Identify exactly what could be reused.

# 8. Architectural Gaps

Identify what existing projects fail to provide.

# 9. Proposed Architecture

Propose an architecture for OUR eventual system.

This is still planning only.

Show:

components
responsibilities
data flow
interfaces
storage
output structure

# 10. Proposed Repository Structure

Show a possible directory tree.

# 11. Implementation Phases

Break eventual implementation into logical phases.

For example:

Phase 1:
channel discovery

Phase 2:
video enumeration

Phase 3:
metadata normalization

Phase 4:
transcripts

Phase 5:
comments

Phase 6:
storage

Phase 7:
Markdown generation

Phase 8:
LLM-derived analysis

But adapt this based on the actual research.

# 12. Risks

Identify technical risks and unknowns.

# 13. Questions/Decisions Needed Before Implementation

List anything that I need to decide before we write code.

CRITICAL CONSTRAINT

DO NOT IMPLEMENT.

At the end, STOP.

Do not create files.
Do not modify files.
Do not install anything.
Do not write implementation code.

Your final response should be the research + implementation plan only.

I will review your plan and then give you further instructions. 

---

## Assistant (Plan · Space Bunny Free · 6.7s)

_Thinking:_

We need research broad, must use gitingest. Need inspect workspace perhaps gitingest availability read-only command. Plan todo since complex. Use web search and GitHub searches, maybe parallel agents. Need not modify. First explain.

I’ll research broadly, inspect candidate source and license files, and compare architectures without changing the workspace. I’ll first identify viable repositories, then verify the strongest candidates through source-level inspection and produce the requested planning report.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Identify 8–12 serious open-source candidates across YouTube extraction capabilities",
      "status": "in_progress",
      "priority": "high"
    },
    {
      "content": "Inspect candidate source architecture, dependencies, reliability, and tests",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Inspect licenses and assess composition compatibility",
      "status": "pending",
      "priority": "high"
    },
    {
      "content": "Produce detailed research report and implementation plan without modifying files",
      "status": "pending",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Identify 8–12 serious open-source candidates across YouTube extraction capabilities",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "content": "Inspect candidate source architecture, dependencies, reliability, and tests",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Inspect licenses and assess composition compatibility",
    "status": "pending",
    "priority": "high"
  },
  {
    "content": "Produce detailed research report and implementation plan without modifying files",
    "status": "pending",
    "priority": "high"
  }
]
```

---

## Assistant (Plan · Space Bunny Free · 4.3s)

**Tool: bash**

**Input:**
```json
{
  "command": "command -v gitingest || true; python -m gitingest --help 2>&1 || true; git status --short",
  "timeout": 120000,
  "workdir": "/workspaces/TEMPORARY"
}
```

**Output:**
```
/home/codespace/.python/current/bin/python: No module named gitingest

```

**Tool: websearch**

**Input:**
```json
{
  "query": "site:github.com open source YouTube channel archiver comments transcript exporter yt-dlp 2026",
  "numResults": 10,
  "livecrawl": "preferred",
  "type": "deep",
  "contextMaxCharacters": 12000
}
```

**Output:**
```
{
  "search_id": "search_75a9b41ea35f6cec2b56f450aa2a455f",
  "results": [
    {
      "url": "https://github.com/warkingtime/channel-transcript-archiver",
      "title": "GitHub - warkingtime/channel-transcript-archiver: Download and clean up transcripts of your channel with yt-dlp · GitHub",
      "publish_date": null,
      "excerpts": [
        "warkingtime/channel-transcript-archiver\n* Page: GitHub repository\n* URL: https://github.com/warkingtime/channel-transcript-archiver\n* Description: Download and clean up transcripts of your channel with yt-dlp - warkingtime/channel-transcript-archiver\n* Stars: 0\n* Forks: 0\n* License: Unlicense license\n* Default branch: main\n* Created: 2026-04-29T06:10:55.000Z\n* Commits: 13\nTop-level files\n* src/\n* .gitignore\n* AGENTS.md\n* CLAUDE.md\n* LICENSE\n* README.md\n* channel-archiver\n* pyproject.toml\n* uv.lock\nREADME.md\n📺 YouTube & Patreon Channel Transcript Archiver\nA robust, generalized tool designed to archive metadata, descriptions, and intelligently cleaned transcripts from any YouTube channel or Patreon creator. This project automates the pipeline from discovery to high-quality text extraction.\nNote\nThis tool downloads existing subtitles and metadata; it does not use AI/TTS models to generate transcripts from audio.\n✨ Features\n* 🚀 Universal Sync : Archive full YouTube channels or Patreon creator posts with a single command.\n* 🧹 Smart Cleaning : Converts messy SRT subtitles into readable text documents with intelligent pause detection.\n* 🗣️ Speaker Heuristics : Customizable speaker-tagging heuristics for two-person conversations.\n* 🛡️ Secure Cookies : Opt-in browser cookie extraction (Chrome, Brave, Firefox, etc.) for age-restricted content.\n* 📂 Unique Naming : Automatically handles folder name collisions by tagging the source (e.g., Creator (youtube) vs Creator (patreon) ).\n🛠️ Installation\nPrerequisites\n* Python 3.10+\n* uv (High-performance Python package manager)\n* yt-dlp\nSetup\n1. Clone the repository:\n  git clone https://github.com/warkingtime/channel-transcript-archiver\n  cd channel-transcript-archiver\n2. Install dependencies:\n  uv sync\n🚀 Usage\nUnified CLI\nNew channel (requires URL)\n./channel-archiver sync <URL> [FOLDER_NAME] [--use-cookies] [--include-comments [N]]\nUpdate existing channel (uses folder name)\n./channel-archiver sync <FOLDER_NAME> [--use-cookies] [--include-comments [N]]\nExamples:\n./channel-archiver sync https://www.youtube.com/@ExampleChannel ExampleChannel\n./channel-archiver sync https://www.patreon.com/creatorslug CreatorName\nDownload a Single Video\nUpdate existing channel (uses folder name)\nIf you don't want to archive a whole channel, you can download a single transcript:\n./channel-archiver download <VIDEO_URL> [FOLDER_NAME] [--include-comments [N]]\nAge-Restricted Content & Cookies\nUpdate existing channel (uses folder name)\nTo see exactly what yt-dlp commands will be executed without actually performing any downloads:\n./channel-archiver sync <URL> --print-command\nConfiguration & Speaker ID\nUpdate existing channel (uses folder name)\n├── playlists/          # Playlist metadata (YouTube only)\n├── archive.txt         # Download history\n├── config.toml         # URL and speaker heuristics\n├── PLAYLISTS.md        # Playlist index\n└── TRANSCRIPTS.md      # Chronological video index"
      ]
    },
    {
      "url": "https://github.com/HanifCarroll/youtube-transcript",
      "title": "GitHub - HanifCarroll/youtube-transcript: Fast YouTube ...",
      "publish_date": null,
      "excerpts": [
        "GitHub - HanifCarroll/youtube-transcript: Fast YouTube ...\nIt uses yt-dlp to fetch YouTube caption tracks directly, then writes clean text, Markdown, and JSON artifacts that are easy for an agent to inspect.\nIt is built for the common case where captions already exist, so you can get a transcript in seconds without downloading video or running Whisper."
      ]
    },
    {
      "url": "https://github.com/dlovecreator-arch/youtube-transcript-exporter",
      "title": "GitHub - dlovecreator-arch/youtube-transcript-exporter: Bulk-download YouTube channel transcripts and build a cross-referenceable Obsidian/Notion second brain. · GitHub",
      "publish_date": null,
      "excerpts": [
        "dlovecreator-arch/youtube-transcript-exporter\n* Page: GitHub repository\n* URL: https://github.com/dlovecreator-arch/youtube-transcript-exporter\n* Description: Bulk-download YouTube channel transcripts and build a cross-referenceable Obsidian/Notion second brain. - dlovecreator-arch/youtube-transcript-exporter\n* Stars: 1\n* Forks: 0\n* License: MIT license\n* Default branch: main\n* Created: 2026-05-07T05:18:21.000Z\n* Commits: 54\nTop-level files\n* .github/workflows/\n* archive/historical_docs/\n* db/\n* docs/\n* examples/\n* src/\n* tests/\n* tools/\n* ytexporter/\n* ytx/\n* .env.example\n* .gitignore\n* CHANGELOG.md\n* CODE_OF_CONDUCT.md\n* CONTRIBUTING.md\n* CONVENTIONS.md\n* Dockerfile\n* INSTALL.md\n* LICENSE\n* QUICKSTART.md\n* README.md\n* SECURITY.md\n* TROUBLESHOOTING.md\n* channels.txt.example\n* config.json\n* docker-compose.yml\n* export.sh\n* pyproject.toml\n* requirements.txt\nREADME.md\nYouTube Transcript Exporter\nCI license python yt-dlp Whisper Obsidian\nDrop in a YouTube channel. Walk away. Get a clean, RAG-ready local dataset.\nProduction-tested on 60+ channels, 24,000+ videos, ~1.4 GB of indexed transcripts.\nWhy this exists\nAnd every other tool either trickles one video at a time, breaks at channel scale, or locks you into a SaaS.\nThis tool turns YouTube channels into a searchable, structured, RAG-friendly dataset you can:\n* read like a library (Markdown vault, Obsidian-ready)\n* analyze like a database (one canonical JSON)\n* index for semantic search / RAG (JSONL export)\n* never re-download (idempotent download archive)\nOne command UX\nAdd a channel and walk away\npython -m ytx add https://www.youtube.com/@LexFridman\nAdd a list of channels\npython -m ytx add channels.txt\nGenerate markdown only for missing channel folders or one channel\npython -m ytx markdown --missing-only\npython -m ytx markdown --channel \"Chris Williamson\"\nExport for RAG / embeddings\npython -m ytx export jsonl --out exports/transcripts.jsonl\npython -m ytx export chunks --out exports/chunks.jsonl\nDiagnose your environment\n├── db/canonical.json        # Single source of truth\n├── db/downloaded.txt        # yt-dlp idempotency archive\n├── markdown/                # Obsidian-ready vault\n├── archive/                 # Historical reports, never read by code\n├── tests/smoke_test.sh      # 10-step sanity check\nDiagnose your environment\n\"description\": \"...\",\n\"sources\": [\"BcWXVnZwJjA\"]\n}\n...and a matching markdown file at markdown/<Channel>/<slug>_<id>.md with full transcript and YAML frontmatter.\nDiagnose your environment\nRAG export\npython -m ytx export jsonl --out exports/transcripts.jsonl\npython -m ytx export chunks --out exports/chunks.jsonl\nVideo-level JSONL produces one JSON record per line with:\n1. Clone\ngit clone https://github.com/dlovecreator-arch/youtube-transcript-exporter.git\ncd youtube-transcript-exporter\n2. Install (Python deps minimal; yt-dlp required; Whisper optional)\npip install -r requirements.txt\nbrew install yt-dlp ffmpeg     # macOS; or: pipx install yt-dlp"
      ]
    },
    {
      "url": "https://gist.github.com/nker150/df88cb7ea519c0683e007995c7b9c3ab",
      "title": "How to archive YouTube channels · GitHub",
      "publish_date": null,
      "excerpts": [
        "Gist: How to archive YouTube channels\n* Page: GitHub gist\n* URL: https://gist.github.com/nker150/df88cb7ea519c0683e007995c7b9c3ab\n* Author: nker150\n* Gist: df88cb7ea519c0683e007995c7b9c3ab\n* Files: 1\nhowto.md\nHow to archive YouTube channels\nOnce upon a time we would have used youtube-dl, however the developer there didn't seem to keen on bypassing YouTube's throttling. yt-dlp is a fork of youtube-dl that performs far better on YouTube.\nHow you will get yt-dlp depends on which operating system you're using.\nThat command will take several minutes to run, but after it does yt-dlp should be fully functional, and it will work as well as it does on Linux.\nRunning yt-dlp to download an entire channel\nTypically using yt-dlp is simple. To download a single video, we would run something like the following:\nyt-dlp https://www.youtube.com/watch?v=dQw4w9WgXcQ\nBut that's not what we're after. We aim to make yt-dlp actually work for a living. So let me break down what we're going to do to accomplish that.\nOf course we're going to start with yt-dlp .\nBut we're going to add some options. The first option is --extractor-args youtube:player_client=android --throttled-rate 100K . This is one of the main improvements of yt-dlp over youtube-dl. This part of the command detects throttling by YouTube and bypasses it.\nWhat you can do with this option is export your cookies from Firefox using an extension called Export Cookies by Rotem Dan to a compatible cookies.txt file. That way for age restricted videos, you can sign into YouTube on Firefox, export your cookies to a text file, then use that signed in cookie with yt-dlp to download that video.\nAfter that we're going to add --download-archive ./archive.txt . This will create a file in the download directory called archive.txt. That file is a simple text-based database of all the videos that are downloaded in that folder. The idea here is that yt-dlp will not bother to check any links that it has already downloaded.\nYouTube is the only major platform that I know of that uses AI to automatically generate subtitles for uploaded videos, and these are invaluable. Most other people's YouTube channel archives that I've seen exclude these.\nPersonally I find it preferable to archive the thumbnail as well, you do that with --write-thumbnail .\nThe vast majority of devices can play an MP4 with no issues whatsoever. And for you Free Software snobs out there (picking on myself more than anyone, chill) Cisco has open sourced their H.264 codecs so it's not really a closed standard anymore. Really no reason not to use an MP4.\nyt-dlp --extractor-args youtube:player_client=android --throttled-rate 100K --cookies ~/cookies.txt --download-archive ./archive.txt --write-description --write-info-json --write-annotations --write-sub --write-auto-sub --write-thumbnail -i -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' -o '%(upload_date)s-%(title)s.%(ext)s'\nhttps://www.youtube.com/channel/UCuAXFkgsw1L7xaCfnd5JJOw"
      ]
    },
    {
      "url": "https://github.com/dmn001/youtube_channel_archiver",
      "title": "GitHub - dmn001/youtube_channel_archiver: Starting point for archiving entire YouTube channels using yt-dlp (originally youtube-dl) · GitHub",
      "publish_date": null,
      "excerpts": [
        "dmn001/youtube_channel_archiver\n* Page: GitHub repository\n* URL: https://github.com/dmn001/youtube_channel_archiver\n* Description: Starting point for archiving entire YouTube channels using yt-dlp (originally youtube-dl) - dmn001/youtube_channel_archiver\n* Stars: 512\n* Forks: 70\n* Default branch: master\n* Created: 2018-03-19T15:58:06.000Z\n* Commits: 8\nTop-level files\n* download_archive.bat\n* download_archive.sh\n* readme.md\n* yt-dlp-archive.txt\n* yt-dlp-channels.txt\n* yt-dlp.conf\nreadme.md\nyt-dlp config - downloading entire youtube channels for archival\nReadme\nThis repo contains a config file which makes it easy to download entire youtube channels, and also update them without having to re-download existing videos.\nUpdate 2022-09: It has been a while since youtube-dl was updated, so I have updated all the commands and config to use the current most popular youtube video downloader: yt-dlp .\nUsage\nEdit channel urls in yt-dlp-channels.txt .\nThe empty file yt-dlp-archive.txt is used to store downloaded video ids.\nLinux\nchmod +x download_archive.sh\nRun using ./download_archive.sh\nWindows\nRun download_archive.bat\nThanks\nThanks to https://www.reddit.com/user/Stephen304 for creating the original config, on the since deleted post: https://www.reddit.com/r/DataHoarder/comments/858ny5/my_youtubedl_config_downloading_entire_channels/\nThere is an archive of the original post at: https://archive.ph/T4sa2"
      ]
    },
    {
      "url": "https://github.com/mattwright324/youtube-comment-suite",
      "title": "GitHub - mattwright324/youtube-comment-suite: Download YouTube comments from numerous videos, playlists, and channels for archiving, general search, and showing activity. · GitHub",
      "publish_date": null,
      "excerpts": [
        "mattwright324/youtube-comment-suite\n* Page: GitHub repository\n* URL: https://github.com/mattwright324/youtube-comment-suite\n* Description: Download YouTube comments from numerous videos, playlists, and channels for archiving, general search, and showing activity. - mattwright324/youtube-comment-suite\n* Stars: 317\n* Forks: 54\n* License: MIT license\n* Default branch: main\nGithub All Releases GitHub release Github Releases\nYouTube Comment Suite lets you aggregate YouTube comments from numerous videos, playlists, and channels for archiving, general search, and showing activity. Achieve the functionality of the Community > Comments tool that is provided to YouTube creators and more.\nExamples\n* Want to see how often a keyword/topic comes up?\n* Have a question that may have been answered in the thousands of comments and videos?\n* Want to know who the most active and popular fans are?\n* Want to see a user's comment history over an entire channel or channels?\nFeatures\n* Cross-platform using Java 8 and JavaFX\n* Include multiple channels, playlists, and videos in a single group.\n* Search for comments by video, type, username, keyword, length, and date.\n* Display stats about videos: publishes per week, most popular, most commented, and disabled.\n* Display stats about comments: posts per week, most active posters, most popular posters.\n* Option to save thumbnails and profiles for archival and offline viewing.\n* View video context when selecting a comment.\nInstall\nGitHub Releases\nWindows\nExtract the latest release zip file and run youtube-comment-suite-#.#.#.jar .\n* Be sure that you have Java 8 installed, if not you can get it here from Oracle .\n* If you want to use Java 11 or higher, there is a workaround in the wiki here: Installation - Java 11+\nLinux / Ubuntu\nGetting Started\nWant to know more about how to use this program? Check out the Wiki!\nBuilding\nRefer to BUILD.md for instructions on how to build and run from source.\nContributing\nContributions are welcome, refer to CONTRIBUTING.md for more detail."
      ]
    },
    {
      "url": "https://github.com/sworcery/ChannelHoarder",
      "title": "GitHub - sworcery/ChannelHoarder: Self-hosted video channel archiver with a modern web UI. Monitors YouTube, Rumble, Twitch, Dailymotion, Vimeo, and Odysee channels and automatically downloads new videos in Plex-compatible format. · GitHub",
      "publish_date": null,
      "excerpts": [
        "sworcery/ChannelHoarder\n* Page: GitHub repository\n* URL: https://github.com/sworcery/ChannelHoarder\n* Description: Self-hosted video channel archiver with a modern web UI. Monitors YouTube, Rumble, Twitch, Dailymotion, Vimeo, and Odysee channels and automatically downloads new videos in Plex-compatible format. ...\n* Stars: 21\n* Forks: 3\n* License: MIT license\n* Default branch: main\n* Created: 2026-03-22T23:47:39.000Z\n* Commits: 199\nSelf-hosted YouTube channel archiver with a modern web UI, designed for Plex-compatible output. Runs as a single Docker container and automatically downloads new videos from your subscribed channels.\nFeatures\n* Multi-platform - Subscribe to channels (or YouTube playlists) from YouTube, Rumble, Twitch, Dailymotion, Vimeo, and Odysee by URL or @handle\n* Automatic archiving - Scheduled scans detect new videos and queue them, with per-channel quality (up to 4K), quality cutoff, title (keyword/regex) and duration filters, and per-channel storage paths\n* Smart authentication - Cookies (auto-sync via Windows exporter or Tampermonkey, or manual upload) with PO token fallback, optional YouTube Data API key, and a selectable yt-dlp player client\n* Anti-detection - Configurable download delays, random jitter, and user-agent rotation\n* Monitoring - Error classification with suggested fixes, diagnostic reports, searchable logs, and Telegram / Pushover / Discord notifications\n* Self-contained - Single Docker container (web UI, download engine, PO token server, scheduler) with dark-mode UI, current yt-dlp on every image build, and config import/export\n* If a YouTube Data API key is configured, it's used for faster and more reliable discovery; otherwise yt-dlp handles discovery directly\n* Manual scans can be triggered per-channel or for all channels at once Download pipeline\n* YouTube Data API key (optional)\nA YouTube Data API key improves channel scanning reliability and speed. Without it, yt-dlp handles discovery directly, which works but can be slower.\nTo get a free API key:\n* Naming - Output filename template with live preview and variable reference ( {channel_name} , {season} , {episode} , {title} , {upload_date} , {video_id} )\n* yt-dlp - Version info (yt-dlp ships current on every image build)\nSupported Platforms\n* Platform | Channel Discovery | Video Download | API Support\n* YouTube | RSS + API + yt-dlp | yt-dlp | YouTube Data API v3\n* Rumble | yt-dlp | yt-dlp | No\n* Twitch | yt-dlp | yt-dlp | No\n* Dailymotion | yt-dlp | yt-dlp | No\n* Vimeo | yt-dlp | yt-dlp | No\n* Odysee | yt-dlp | yt-dlp | No\nReference\nTech stack & volumes\nTech stack:\n* Set the player client to Default (automatic) in Settings → Authentication so yt-dlp picks a working client and adapts to YouTube's changes\n* If a specific video still fails, try ios or web_safari from the same dropdown\n* Make sure the image is up to date (each build ships current yt-dlp)\nPlex not showing downloaded videos"
      ]
    },
    {
      "url": "https://github.com/aliyasinozyuksel/yt-dlp-video-transcripts",
      "title": "GitHub - aliyasinozyuksel/yt-dlp-video-transcripts: Download YouTube channel, playlist, or video transcripts as TXT and Markdown using yt-dlp. · GitHub",
      "publish_date": null,
      "excerpts": [
        "aliyasinozyuksel/yt-dlp-video-transcripts\n* Page: GitHub repository\n* URL: https://github.com/aliyasinozyuksel/yt-dlp-video-transcripts\n* Description: Download YouTube channel, playlist, or video transcripts as TXT and Markdown using yt-dlp. - aliyasinozyuksel/yt-dlp-video-transcripts\n* Stars: 1\n* Forks: 0\n* License: MIT license\n* Default branch: main\n* Created: 2026-06-05T19:27:02.000Z\nTop-level files\n* .github/workflows/\n* scripts/\n* tests/\n* .gitignore\n* LICENSE\n* README.md\n* pyproject.toml\n* requirements-dev.txt\n* requirements.txt\nREADME.md\nYouTube Channel Transcripts\nCI Python License\nDownload subtitles/transcripts from YouTube channels, playlists, or individual videos and save them as plain .txt and agent-friendly .md files. English is the default language, but you can request any YouTube/yt-dlp subtitle language code with --lang .\nThis tool uses yt-dlp to fetch subtitles only.\nWhat it does\n* Lists videos from a channel, playlist, or single video URL\n* Downloads manual subtitles first, then auto-generated captions for your requested language(s)\n* Defaults to English ( --lang en ); accepts any valid YouTube subtitle language code\n* Converts VTT/SRT subtitles into clean transcript text\n* Writes both .txt and .md outputs with YAML frontmatter\n* Supports chunked processing for large channels (600+ videos)\n* Resumes safely by skipping completed transcript pairs\n* Repairs partial transcript files after interrupted runs\n* Detects existing transcripts by video_id , not just filename\nQuick start\ngit clone https://github.com/aliyasinozyuksel/yt-dlp-video-transcripts.git\ncd yt-dlp-video-transcripts\npip install -r requirements.txt\npython scripts/channel_transcripts.py \n\"https://www.youtube.com/@3blue1brown/videos\" \n-o ./output --max-videos 5\nPreview actions without downloading or writing files:\npython scripts/channel_transcripts.py \n\"https://www.youtube.com/@3blue1brown/videos\" \n-o ./output --max-videos 5 --dry-run\nInstallation\npip install yt-dlp\nOr:\npip install -r requirements.txt\nFor development:\npip install -r requirements-dev.txt\nUsage\nSingle video\npython scripts/channel_transcripts.py \n\"https://www.youtube.com/watch?v=VIDEO_ID\" \n-o ./output\nChannel\npython scripts/channel_transcripts.py \n\"https://www.youtube.com/@channel/videos\" \n-o ./output\nBare @channel URLs automatically use the /videos tab.\nPlaylist\npython scripts/channel_transcripts.py \n\"https://www.youtube.com/playlist?list=PLAYLIST_ID\" \n-o ./output\nLarge channel (600+ videos)\nMetadata only\nList selected videos without downloading subtitles or writing transcript files:\npython scripts/channel_transcripts.py \n\"https://www.youtube.com/@channel/videos\" \n-o ./output --metadata-only\nThis uses yt-dlp flat extraction to list videos and writes:\n* Problem | What to do\n* yt-dlp is not installed | Run pip install yt-dlp\n* No videos found for the provided URL | Check the URL and make sure the channel/playlist is public\n* The selected range contains no videos | Adjust --start-index / --end-index"
      ]
    },
    {
      "url": "https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/common.py",
      "title": "yt-dlp/yt_dlp/extractor/common.py at master · yt-dlp/yt-dlp · GitHub",
      "publish_date": null,
      "excerpts": [
        "yt-dlp/yt-dlp — yt_dlp/extractor/common.py\n* Page: GitHub code file\n* URL: https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/common.py\n* Repository: yt-dlp/yt-dlp\n* Path: yt_dlp/extractor/common.py\n* Ref: master\n* Lines: 4188\nimport base64\nimport collections\nimport contextlib\nimport functools\nimport getpass\nimport http.cookiejar\nimport inspect\nimport itertools\nimport json\n```\nlike_count:     Number of positive ratings of the video\ndislike_count:  Number of negative ratings of the video\nrepost_count:   Number of reposts of the video\naverage_rating: Average rating given by users, the scale used depends on the webpage\ncomment_count:  Number of comments on the video\n```\n```\ncomments:       A list of comments, each with one or more of the following\n                properties (all but one of text or html optional):\n                    * \"author\" - human-readable name of the comment author\n                    * \"author_id\" - user ID of the comment author\n```\n```\n                    * \"author_thumbnail\" - The thumbnail of the comment author\n                    * \"author_url\" - The url to the comment author's page\n                    * \"author_is_verified\" - Whether the author is verified\n                                             on the platform\n```\n```\n                    * \"author_is_uploader\" - Whether the comment is made by\n                                             the video uploader\n                    * \"id\" - Comment ID\n                    * \"html\" - Comment as HTML\n                    * \"text\" - Plain text of the comment\n```\n```\n                    * \"timestamp\" - UNIX timestamp of comment\n                    * \"parent\" - ID of the comment this one is replying to.\n                                 Set to \"root\" to indicate that this is a\n                                 comment to the original video.\n```\n```\n                    * \"like_count\" - Number of positive ratings of the comment\n                    * \"dislike_count\" - Number of negative ratings of the comment\n                    * \"is_favorited\" - Whether the comment is marked as\n                                       favorite by the video uploader\n```\n```\n                    * \"is_pinned\" - Whether the comment is pinned to\n                                    the top of the comments\n                    * \"start_time\" - Start time (in seconds) for displaying the comment\n                    * \"end_time\" - End time (in seconds) for displaying the comment\n```\n```\nage_limit:      Age restriction for the video, as an integer (years)\nwebpage_url:    The URL to the video webpage, if given to yt-dlp it\n                should allow to get the same result again. (It will be set\n                by YoutubeDL if it's missing)\ncategories:     A list of categories that the video falls in, for example\n```"
      ]
    },
    {
      "url": "http://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py",
      "title": "yt-dlp/yt_dlp/YoutubeDL.py at master · yt-dlp/yt-dlp · GitHub",
      "publish_date": null,
      "excerpts": [
        "'has already been recorded in the archive')) break_opt, break_err = 'break_on_existing', ExistingVideoReached else: try: reason = check_filter() except DownloadCancelled as e: ``` ... ```py self.to_screen(f'[download] {self._format_screen(temp_id, self.Styles.ID)}: ' 'has already been recorded in the archive') if self.params.get('break_on_existing', False): raise ExistingVideoReached ``` ... ```py except (DownloadError, OSError, ValueError, *network_exceptions): success = False finally: if os.path.exists(temp_file.name): try: os.remove(temp_file.name) except OSError: ``` ... ```py if evaluate_formats('b/bv+ba') != evaluate_formats('bv*+ba/b'): self.report_warning('ffmpeg not found. The downloaded format may not be the best available. ' ``` ... ```py or video only (imgur)) best/worst will fallback to best/worst {video,audio}-only format matches = list(filter(lambda f: f.get('vcodec') != 'none' or f.get('acodec') != 'none', formats)) ``` ... ```py if get_from_start and not formats: self.raise_no_formats(info_dict, msg=( '--live-from-start is passed, but there are no formats that can be downloaded from the start. ' ``` ... ```py return f'{filename_wo_ext}.{ext}' Ensure filename always has a correct extension for successful merge full_filename = correct_ext(full_filename) temp_filename = correct_ext(temp_filename) ``` ... ```py downloaded.append(fname) info_dict['url'] = '\\n'.join(f['url'] for f in info_dict['requested_formats']) success, real_download = self.dl(temp_filename, info_dict) ``` ... ```py 'You have requested merging of multiple formats ' 'while also allowing unplayable formats to be downloaded. ' 'The formats won\\'t be merged to prevent data corruption.') ``` ... ```py info_dict['__real_download'] = info_dict['__real_download'] or real_download success = success and partial_success if downloaded and merger.available and not self.params.get('allow_unplayable_formats'): info_dict['__postprocessors'].append(merger) info_dict['__files_to_merge'] = downloaded Even if there were no downloads, it is being merged only now info_dict['__real_download'] = True ``` ... ```py dl_filename = dl_filename or temp_filename info_dict['__finaldir'] = os.path.dirname(os.path.abspath(full_filename)) except network_exceptions as err: self.report_error(f'unable to download video data: {err}') return ``` ... ```py ffmpeg_fixup(downloader == 'web_socket_fragment', 'Malformed timestamps detected', FFmpegFixupTimestampPP) ffmpeg_fixup(downloader == 'web_socket_fragment', 'Malformed duration detected', FFmpegFixupDurationPP) fixup() ``` ... ```py self.write_debug(f'Adding to archive: {vid_id}') if is_path_like(fn): with locked_file(fn, 'a', encoding='utf-8') as archive_file: archive_file.write(vid_id + '\\n') self.archive.add(vid_id) @staticmethod ``` ... ```py ret.append((sub_filename, sub_filename_final)) except (DownloadError, ExtractorError, OSError, ValueError, *network_exceptions) as err: msg = f'Unable to download video subtitles\nyt-dlp/yt-dlp — yt_dlp/YoutubeDL.py ```py (or video) as a single JSON line. force_write_download_archive: Force writing download archive regardless of 'skip_download' or 'simulate'. simulate: Do not download the video files. If unset (or None), ``` ... ```py into a single file check_formats Whether to test if the formats are downloadable. Can be True (check all), False (check none), 'selected' (check selected formats), ``` ... ```py False: Sanitize filenames only minimally This option has no effect when running on Windows ignoreerrors: Do not stop on download/postprocessing errors. Can be 'only_download' to"
      ]
    }
  ],
  "warnings": null,
  "metadata": null,
  "session_id": "ses_f2de9ab4effeqefH6MpyhdfGAE"
}
```

**Tool: websearch**

**Input:**
```json
{
  "query": "site:github.com YouTube transcript extractor comments channel enumerator knowledge base RAG open source",
  "numResults": 10,
  "livecrawl": "preferred",
  "type": "deep",
  "contextMaxCharacters": 12000
}
```

**Output:**
```
{
  "search_id": "search_89f8239fc66ffc3ce80b5cddeeaa93e9",
  "results": [
    {
      "url": "https://github.com/nadimtuhin/ytranscript",
      "title": "GitHub - nadimtuhin/ytranscript: YouTube transcript extractor · GitHub",
      "publish_date": null,
      "excerpts": [
        "nadimtuhin/ytranscript\n* Page: GitHub repository\n* URL: https://github.com/nadimtuhin/ytranscript\n* Description: YouTube transcript extractor\n* Stars: 7\n* Forks: 1\n* License: MIT license\n* Default branch: main\n* Created: 2026-01-11T16:33:51.000Z\n* Commits: 46\nTop-level files\n* .github/\n* .omc/\n* src/\n* tests/\n* .gitignore\n* CHANGELOG.md\n* CODE_OF_CONDUCT.md\n* CONTRIBUTING.md\n* HOW_IT_WORKS.md\n* ISSUES.md\n* LICENSE\n* README.md\n* SECURITY.md\n* biome.json\n* bun.lockb\n* package.json\n* tsconfig.json\nREADME.md\nytranscript\nnpm version npm downloads CI CodeQL Trivy License: MIT\nExtract transcripts from your entire YouTube watch history in minutes. Build AI-powered video summaries, searchable archives, or feed transcripts directly to Claude, Cursor, and other AI assistants via the built-in MCP server.\nRead the blog post: \"Automating My Second Brain with YouTube Transcripts\"\nAdd to a project (for library usage)\nnpm add @nadimtuhin/ytranscript\nRuntimes supported: Node.js 18+ and Bun 1.0+\nMCP Server (AI Assistant Integration)\nytranscript includes an MCP (Model Context Protocol) server that lets Claude, Cursor, and other AI assistants fetch YouTube transcripts directly.\nAvailable Tools\nAdd to a project (for library usage)\n* Tool | Description\n* get_transcript | Fetch transcript with format options (text, segments, srt, vtt)\n* get_transcript_languages | List available caption languages for a video\n* extract_video_id | Extract video ID from various YouTube URL formats\nAdd to a project (for library usage)\n* \"Get the transcript for this YouTube video: https://youtube.com/watch?v=dQw4w9WgXcQ \"\n* \"Summarize the key points from this video\"\n* \"What languages are available for this video's captions?\"\n* \"Get transcripts for these 5 videos and compare their content\"\nCLI Usage\nSingle Video\nFrom URL\nytranscript get \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"\nFrom Google Takeout exports\nytranscript bulk \n--history \"Takeout/YouTube/history/watch-history.json\" \n--watch-later \"Takeout/YouTube/playlists/Watch later-videos.csv\" \n--out-jsonl transcripts.jsonl \n--out-csv transcripts.csv\nWith authentication\n* Takeout/YouTube and YouTube Music/history/watch-history.json\n* Takeout/YouTube and YouTube Music/playlists/Watch later-videos.csv\nAPI Reference\nTypes\ninterface Transcript {\nvideoId: string;\ntext: string;\nsegments: TranscriptSegment[];\nlanguage: string;\nisAutoGenerated: boolean;\n}\nWith authentication\ninterface TranscriptSegment {\ntext: string;\nstart: number;    // seconds\nduration: number; // seconds\n}\ninterface WatchHistoryMeta {\nvideoId: string;\ntitle?: string;\nurl?: string;\nchannel?: { name?: string; url?: string };\nwatchedAt?: string;\nsource: 'history' | 'watch_later' | 'manual';\n}\nWith authentication\ninterface TranscriptResult {\nmeta: WatchHistoryMeta;\ntranscript: Transcript | null;\nerror?: string;  // Present when transcript is null\n}"
      ]
    },
    {
      "url": "https://github.com/BrianGuo723/youtube-knowledge-base",
      "title": "GitHub - BrianGuo723/youtube-knowledge-base: Turn any YouTube channel into a searchable local knowledge base. Works with Claude Code, Codex, and any AI agent. · GitHub",
      "publish_date": null,
      "excerpts": [
        "BrianGuo723/youtube-knowledge-base\n* Page: GitHub repository\n* URL: https://github.com/BrianGuo723/youtube-knowledge-base\n* Description: Turn any YouTube channel into a searchable local knowledge base. Works with Claude Code, Codex, and any AI agent. - BrianGuo723/youtube-knowledge-base\n* Stars: 2\n* Forks: 0\n* License: MIT license\n* Default branch: main\n* Created: 2026-03-29T14:11:18.000Z\n* Commits: 10\nTop-level files\n* .env.example\n* .gitignore\n* LICENSE\n* README.md\n* ingest.py\n* requirements.txt\n* youtube-knowledge-base.md\nREADME.md\nYouTube Knowledge Base\nTurn any YouTube channel into a searchable local knowledge base. Ingest transcripts, search with AI-powered hybrid search (BM25 + vector + LLM re-ranking).\nBuilt for builders, researchers, and anyone who learns from YouTube but doesn't have time to rewatch 500 videos.\nHow It Works\n1. Ingest — Point at a YouTube channel, the script fetches all video transcripts and saves them as structured markdown files\n2. Search — Use QMD (Quick Markdown Search) to query across all transcripts with hybrid search\n  No server, no database, no account needed. Everything runs locally.\nQuick Start\nPrerequisites\n* Python 3.10+\n* QMD — npm install -g @tobilu/qmd\n* A YouTube Data API key\n* A transcriptapi.com API key\nSetup\ngit clone https://github.com/BrianGuo723/youtube-knowledge-base.git\ncd youtube-knowledge-base\npip install -r requirements.txt\ncp .env.example .env\nEdit .env with your API keys\nTip: If you're using Claude Code, just paste this README into a conversation and ask it to set everything up for you — it'll walk through the API keys, install dependencies, and run your first ingestion.\nIngest a Channel\npython3 ingest.py \"https://www.youtube.com/@StarterStory\" --since 2024-01-01\nThis will:\nEdit .env with your API keys\n* Resolve the channel handle to a channel ID\n* Fetch all videos published after the --since date\n* Download transcripts via transcriptapi.com\n* Save as markdown files with YAML frontmatter to data/<channel>/transcripts/\n* Create a QMD collection and generate vector embeddings\nEdit .env with your API keys\nRe-running is safe — it skips already-downloaded transcripts.\nEdit .env with your API keys\nSearch\nSearch across all indexed channels\nqmd query \"solo SaaS business ideas under $1000 to start\"\nSearch a specific channel > title: \"How I Built a $1M Business\"\nchannel: starter-story\nurl: https://www.youtube.com/watch?v=abc123\npublished: 2024-03-15\n[full transcript text]\nUse with Claude Code / Codex\nThis is where it gets powerful. Once you've ingested a few channels, the transcripts become local context that AI coding agents can reason over.\nSearch a specific channel > title: \"How I Built a $1M Business\"\nchannel: starter-story\nurl: https://www.youtube.com/watch?v=abc123\npublished: 2024-03-15\nCopy the skill file into your Claude Code skills directory:\ncp youtube-knowledge-base.md ~/.claude/skills/\nNow Claude Code can ingest channe"
      ]
    },
    {
      "url": "https://github.com/Akash9078/youtube-transcript-extractor",
      "title": "GitHub - Akash9078/youtube-transcript-extractor: A powerful YouTube transcript extractor that retrieves full transcripts, subtitles, and captions from YouTube videos. Returns structured JSON metadata and text suitable for search, AI/ML pipelines, SEO, and content workflows. · GitHub",
      "publish_date": null,
      "excerpts": [
        "Akash9078/youtube-transcript-extractor\n* Page: GitHub repository\n* URL: https://github.com/Akash9078/youtube-transcript-extractor\n* Description: A powerful YouTube transcript extractor that retrieves full transcripts, subtitles, and captions from YouTube videos. Returns structured JSON metadata and text suitable for search, AI/ML pipelines,...\n* Stars: 1\n* Forks: 0\nTop-level files\n* README.md\n* n8n-workflow.json\nREADME.md\nYouTube Transcript Extractor Actor\nA powerful YouTube transcript extractor that retrieves full transcripts, subtitles, and captions from YouTube videos. Returns structured JSON metadata and text suitable for search, AI/ML pipelines, SEO, and content workflows.\nApify Actor Rating Success Rate Users\nTable of Contents\n* Property | Value\n* Actor | akash9078/youtube-transcript-extractor\n* Developer | akash9078 (Community)\n* Rating | 5.00/5\n* Runs Succeeded | 99.8%\n* Total Users | 153\n* Monthly Users | 34\n* Categories | Automation, Developer Tools, Videos\n* Last Modified | 2026-02-27\nFeatures\n* youtube.com/shorts/\n* youtube.com/live/\n* Cloud-based Extraction - Automatic retry logic and proxy protection\n* Clean JSON Output - Structured metadata and text for downstream processing\n* No API Quota Limits - Extracts transcripts without using YouTube Data API\n* AI/ML Training Data - Build text datasets for training language models\n* Retrieval-Augmented Generation (RAG) - Feed transcript text into vector stores for AI search\n* Sentiment Analysis - Process transcript text for audience sentiment insights\nResearch & Accessibility\n* Internal Training - Turn training videos into searchable documentation\n* Lead Generation - Identify prospects discussing industry topics in videos\n* API Integration - Programmatic extraction for batch processing\nGetting Started\nUsing Apify Console\n1. Go to akash9078/youtube-transcript-extractor\n2. Enter a YouTube video URL\n3. Click Run\nSee the full API reference at https://docs.apify.com/api/v2\n{\n\"name\": \"YouTube Transcript Extractor\",\n\"type\": \"@apify/n8n-nodes-apify.apify\",\n\"typeVersion\": 1,\n\"position\": [250, 300],\n\"parameters\": {\n\"operation\": \"runActor\",\n\"actorId\": \"akash9078/youtube-transcript-extractor\",\nSee the full API reference at https://docs.apify.com/api/v2\n\"jsonBody\": \"={\\n    \"language\": \"en\",\\n    \"videoUrl\": \"https://youtu.be/dQw4w9WgXcQ\"\\n}\",\n\"options\": {}\n},\n\"id\": \"d945c450-f852-4507-98ce-2f5eda6ecdd3\",\n\"name\": \"YouTube Transcript Extractor\",\n\"type\": \"n8n-nodes-base.httpRequest\",\n\"typeVersion\": 4.2,\n\"position\": [\n-144,\n-160\n]\n}\nSee the full API reference at https://docs.apify.com/api/v2\n// Prepare Actor input\nconst input = {\n\"videoUrl\": \"https://youtu.be/dQw4w9WgXcQ\",\n\"language\": \"en\"\n};\n// Run the Actor and wait for it to finish\nconst run = await client.actor(\"akash9078/youtube-transcript-extractor\").call(input);\nRun the Actor and wait for it to finish\nrun = client.actor(\"akash9078/youtube-transcript-extractor\").call(run_input=ru"
      ]
    },
    {
      "url": "https://github.com/the-ai-entrepreneur-ai-hub/youtube-transcript-extractor",
      "title": "GitHub - the-ai-entrepreneur-ai-hub/youtube-transcript-extractor: Extract YouTube video transcripts and captions. AI training data, RAG pipelines, content repurposing. Supports 100+ languages. No API key required. · GitHub",
      "publish_date": null,
      "excerpts": [
        "the-ai-entrepreneur-ai-hub/youtube-transcript-extractor\n* Page: GitHub repository\n* URL: https://github.com/the-ai-entrepreneur-ai-hub/youtube-transcript-extractor\n* Description: Extract YouTube video transcripts and captions. AI training data, RAG pipelines, content repurposing. Supports 100+ languages. No API key required. - the-ai-entrepreneur-ai-hub/youtube-transcript-e...\n* Stars: 0\n* Forks: 0\n* License: ISC license\n* Default branch: master\n* Created: 2026-03-10T12:10:47.000Z\n* Commits: 4\nTop-level files\n* examples/\n* .gitignore\n* LICENSE\n* README.md\nREADME.md\nYouTube Transcript Extractor — Get Video Transcripts for AI, RAG & Content Repurposing\nExtract transcripts, subtitles, and captions from any YouTube video. Supports playlists, channels, 100+ languages, and both manual and auto-generated captions. Perfect for AI training data, RAG pipelines, content repurposing, and SEO analysis. No YouTube API key required.\nRun on Apify Available on RapidAPI License: ISC\nWhat It Does\nflowchart LR\nA[\"YouTube URLs<br/>Videos, Playlists, Channels\"] --> B[\"InnerTube API<br/>Android / iOS / TV clients\"]\nB --> C[\"Caption Tracks<br/>100+ Languages\"]\nC --> D[\"Structured Output<br/>Full Text + Timestamps\"]\nD --> E[\"Your Pipeline<br/>RAG / AI / Content\"]\nLoading\nThis extractor uses YouTube's internal InnerTube API to fetch caption tracks directly — no YouTube Data API key required, no OAuth, no quotas. It tries multiple client types (Android, iOS, TV) to maximize success rate, even for music videos and VEVO content.\nWhat Data You Get\nExtract transcripts from an entire playlist\nrun = client.actor(\"george.the.developer/youtube-transcript-scraper\").call(run_input={\n\"urls\": [\"https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID\"],\n\"language\": \"en\",\n\"outputFormat\": \"full-text\",\n\"includeMetadata\": True,\n\"maxVideos\": 100,\n})\nBuild documents for RAG/vector store\ndocuments = []\nfor video in client.dataset(run[\"defaultDatasetId\"]).iterate_items():\nif video.get(\"hasTranscript\"):\ndocuments.append({\n\"text\": video[\"transcriptText\"],\n\"metadata\": {\n\"source\": video[\"videoUrl\"],\n\"title\": video[\"title\"],\n\"channel\": video[\"channelName\"],\nvector_store.add(doc[\"text\"], metadata=doc[\"metadata\"])\nRun this actor on Apify — extract transcripts from hundreds of videos in minutes.\nAlso Available on RapidAPI\nPrefer a standard REST API? This extractor is also available on RapidAPI with simple API key authentication:\nvector_store.add(doc[\"text\"], metadata=doc[\"metadata\"])\n* Not all YouTube videos have captions/transcripts. The extractor reports hasTranscript: false for videos without available captions.\n* Auto-generated captions may contain errors (especially for technical jargon or non-English content).\nvector_store.add(doc[\"text\"], metadata=doc[\"metadata\"])\nISC License. See LICENSE for details.\nBuilt by george.the.developer on Apify ."
      ]
    },
    {
      "url": "https://github.com/Rishurajgautam24/YouTube-Comments-Extractor-and-Query-System",
      "title": "GitHub - Rishurajgautam24/YouTube-Comments-Extractor-and-Query-System: Extract YouTube comments and query them semantically using a local LLM via LM Studio · GitHub",
      "publish_date": null,
      "excerpts": [
        "Rishurajgautam24/YouTube-Comments-Extractor-and-Query-System\n* Page: GitHub repository\n* URL: https://github.com/Rishurajgautam24/YouTube-Comments-Extractor-and-Query-System\n* Description: Extract YouTube comments and query them semantically using a local LLM via LM Studio - Rishurajgautam24/YouTube-Comments-Extractor-and-Query-System\n* Stars: 2\n* Forks: 1\n* Topics: python, youtube, semantic-search, rag, llm, langchain, local-llm\n* Default branch: main\n* Created: 2024-05-16T12:25:40.000Z\n* Commits: 3\nTop-level files\n* .gitignore\n* README.md\n* chat_interface.py\n* main.py\n* pdf_upload.py\n* requirements.txt\n* youtube_comments.py\nREADME.md\nYouTube Comments Extractor and Query System\nThis project allows users to extract comments from YouTube videos, upload PDFs and query their contents, and interact with these data sources using a chatbot-like interface powered by an LLM (Language Model) from LM Studio.\nYou need to download LM Studio first,then download the microsoft/Phi-3-mini-4k-instruct-gguf/Phi-3-mini-4k-instruct-q4.gguf Model then Start the server of it\nFeatures\n1. Fetch YouTube Comments\n* Extract comments from YouTube videos using the YouTube Data API.\n* Save comments with a reference name.\n* Load and display saved comments.\n* Download comments as a text file.\n* Manage API keys for the YouTube Data API.\n2. Chat Interface\n* Load saved comments and interact with them using an LLM.\n* Save chat sessions with a reference name.\n* Load and continue from previous chat sessions.\n* Download chat history as a PDF.\n* Delete chat sessions.\n3. PDF Upload and Query\n* Upload PDFs and extract text from them.\n* Save extracted text with a reference name.\n* Load and display saved PDF text.\n* Interact with the PDF text using an LLM.\n* Save chat sessions with a reference name.\n* Load and continue from previous chat sessions.\n* Download chat history as a PDF.\n* Delete chat sessions.\nInstallation\nRun the Streamlit application: streamlit run main.py Open your web browser and navigate to http://localhost:8501 .\nUse the sidebar to navigate between the features:\n1. Fetch YouTube Comments\n2. Chat Interface\n3. PDF Upload\nFetch YouTube Comments\n├── main.py\n├── youtube_comments.py\n├── chat_interface.py\n├── pdf_upload.py\n├── api_keys.json\n├── history.json\n├── comments.json\n├── pdf_data.json\n├── chat_history.json\n├── pdf_chat_history.json\n└── README.md\n* main.py: The main script to run the Streamlit application.\n* youtube_comments.py: Module for fetching and managing YouTube comments.\n* chat_interface.py: Module for interacting with comments using the chatbot interface.\n* pdf_upload.py: Module for uploading PDFs, extracting text, and interacting with it using the chatbot interface.\n* api_keys.json: JSON file to store YouTube API keys.\n* history.json: JSON file to store the history of fetched comments.\n* comments.json: JSON file to store comments data.\n* pdf_data.json: JSON file to store PDF text data.\n* cha"
      ]
    },
    {
      "url": "https://github.com/xBartM/YouTube-Comment-Scraper",
      "title": "GitHub - xBartM/YouTube-Comment-Scraper: Scrape comments, descriptions and transcripts from YouTube · GitHub",
      "publish_date": null,
      "excerpts": [
        "xBartM/YouTube-Comment-Scraper\n* Page: GitHub repository\n* URL: https://github.com/xBartM/YouTube-Comment-Scraper\n* Description: Scrape comments, descriptions and transcripts from YouTube - xBartM/YouTube-Comment-Scraper\n* Stars: 1\n* Forks: 0\n* License: MIT license\n* Default branch: master\n* Created: 2025-01-15T16:33:23.000Z\n* Commits: 78\nTop-level files\n* configs/\n* database/\n* scripts/\n* .gitignore\n* LICENSE\n* README.md\n* channels.txt\nREADME.md\nYouTube Comment Scraper\nScrape comments, descriptions and transcripts from selected YouTube channels (or videos) and insert them into a database.\nTable of Contents\n* General Info\n* Setup\n* Run\n* Endnotes\n* Future Plans\nGeneral Info\nOverview\nThis repository allows you to download YouTube video data (comments, descriptions and transcripts) using yt-dlp and store it in a PostgreSQL database for further analysis. Below is an overview of how to set up and use this tool.\nRepo structure\nNote\nEach file contains extensive comments to help understand the functionality and purpose of the code.\nThe repository is structured as follows:\nconfigs : Configuration files for yt-dlp are stored in the configs/ directory. These files define how videos are downloaded and what metadata is extracted.\ndatabase : The database schema is defined in database/create_schema.sql . It includes tables for channels, videos, comments, transcripts, and sponsorblock data. The database/ folder also contains logs/ and temp/ folders that, while essential for the tool, are not important for the user.\nscripts : Various scripts in the scripts/ directory automate tasks like database initialization, video metadata updates, and channel synchronization. More on them in Setup and Run sections.\nSetup\nCaution\nIf you are using PostgreSQL for other projects, this repository can damage it! Review scripts/db_*.sh and database/*.sql files and make sure they fit your design.\nPrerequisites\nImportant\nI have developed and tested this solution exclusively on Termux (a terminal emulator for Android OS)\nThis repo requires the following software:\n1. yt-dlp - used for downloading comments, descriptions and transcripts from videos.\n2. PostgreSQL - used for storing video data (on termux install it by using pkg ).\n3. jq - Command-line JSON processor (on termux install it by using pkg ).\nRepo init and setup\n1. Clone this repository:\ngit clone https://github.com/xBartM/YouTube-Comment-Scraper.git\n2. Set YTKP_DIR environmental variable:\n3. Navigate to the repository:\ncd /path/to/YouTube-Comment-Scraper\n4. Set YTKP_DIR to current directory:\nexport YTKP_DIR=$(pwd)\n5.\n1. Tech Search:\n2. There are many communities that provide difficult-to-obtain and/or high-tech knowledge in an accessible way (e.g. Applied Science, Thought Emporium, Easy Composites).\n3. Video transcripts can be used for Semantic Search, for RAG, or other forms of NLP that would enhance the knowledge base of an individual.\n4."
      ]
    },
    {
      "url": "https://github.com/maloneype/youtube-transcript-extractor",
      "title": "GitHub - maloneype/youtube-transcript-extractor: A Python tool that extracts YouTube transcripts and saves them as markdown files with metadata · GitHub",
      "publish_date": null,
      "excerpts": [
        "maloneype/youtube-transcript-extractor\n* Page: GitHub repository\n* URL: https://github.com/maloneype/youtube-transcript-extractor\n* Description: A Python tool that extracts YouTube transcripts and saves them as markdown files with metadata - maloneype/youtube-transcript-extractor\n* Stars: 0\n* Forks: 0\n* Default branch: main\n* Created: 2025-07-13T20:03:25.000Z\n* Commits: 1\nTop-level files\n* extracted_transcripts/\n* README.md\n* requirements.txt\n* setup.py\n* youtube_transcript_extractor.py\nREADME.md\nYouTube Transcript Extractor\nThis tool extracts transcripts from YouTube videos and saves them as markdown files.\nFeatures\n* Extracts transcripts from any YouTube video with available captions\n* Creates two markdown files:\n1. With timestamps : Includes timestamps for easy reference\n2. Text only : Clean text for better readability\n* Supports various YouTube URL formats\n* Automatically selects English transcripts when available\nInstallation\n1. Create a virtual environment (recommended):\n  python -m venv venv\n  source venv/bin/activate  # On Windows: venv\\Scripts\\activate\n2. Install dependencies:\n  pip install -r requirements.txt\nUsage\n1. Run the script:\n  python youtube_transcript_extractor.py\n2. Enter a YouTube URL when prompted. The tool supports various formats:\n* https://www.youtube.com/watch?v=VIDEO_ID\n* https://youtu.be/VIDEO_ID\n* https://www.youtube.com/embed/VIDEO_ID\n3. The tool will create two markdown files in the extracted_transcripts folder:\n* {video_id}_with_timestamps.md : Transcript with timestamps\n* {video_id}_text_only.md : Clean text only\nExample Output\nWith Timestamps ( {video_id}_with_timestamps.md ):\nYouTube Transcript (with timestamps)\n**[00:00]** Hello and welcome to this video.\n**[00:03]** Today we'll be discussing...\n**[00:07]** Let's get started.\nText Only ( {video_id}_text_only.md ):\nYouTube Transcript (text only)\nHello and welcome to this video.\nToday we'll be discussing...\nLet's get started.\nNotes\nYouTube Transcript (text only)\n* The video must have captions/transcripts available\n* The tool will try to use English transcripts first, then fall back to other available languages\n* Files are saved in the extracted_transcripts subfolder\n* Video IDs are used in filenames to avoid conflicts\nRequirements\nYouTube Transcript (text only)\n* Python 3.6+\n* youtube-transcript-api library"
      ]
    },
    {
      "url": "https://github.com/JoelMoyal/YouTube-Transcript-Extractor",
      "title": "GitHub - JoelMoyal/YouTube-Transcript ...",
      "publish_date": null,
      "excerpts": [
        "JoelMoyal/YouTube-Transcript-Extractor\n* Page: GitHub repository\n* URL: https://github.com/JoelMoyal/YouTube-Transcript-Extractor\n* Stars: 1\n* Forks: 0\n* Default branch: main\n* Created: 2025-04-09T06:53:00.000Z\n* Commits: 636\nTop-level files\n* Reviews/\n* client/\n* scripts/\n* supabase/\n* trust by/\n* .DS_Store\n* .dockerignore\n* .env.example\n* .gitattributes\n* .gitignore\n* .node-version\n* CLAUDE.md\n* Dockerfile\n* JM_Logo_blue.png\n* Logo_400px.png\n* README.md\n* package-lock.json\n* package.json\n* railway.json\n* scribesnap_icon_wave.svg\n* scribesnap_name_logo__closer.png\n* scribesnap_name_logo__closer.svg\n* scribesnap_name_logo__gray.png\n* scribesnap_name_logo__gray.svg\n* scribesnap_name_logo__no background copy.svg\n* scribesnap_name_logo__no background.svg\n* server.js\n* vercel.json\nREADME.md\nScribeSnap\nNode version React Express Supabase License\nExtract transcripts from YouTube, Vimeo, TikTok, and more — then unlock AI-powered study tools in one click.\n🌐 scribesnap.ai\nAbout\nScribeSnap is a full-stack web application that pulls transcripts from videos across multiple platforms and enriches them with AI features: summaries, key insights, auto-generated flashcards, study guides, and interactive Q&A chat.\nWhether you're a student reviewing a lecture, a researcher skimming a conference talk, or a professional turning webinars into notes, ScribeSnap converts any video into structured, searchable knowledge — instantly.\nFeatures\nTranscript Extraction\n* Multi-platform support — YouTube, Vimeo, TikTok, Twitter/X, Instagram, Facebook, Loom, Wistia, Dailymotion\n* Auto-subtitle fallback — tries native captions first, then falls back to Supadata for videos without them\n* Streaming delivery — transcripts stream to the UI via Server-Sent Events (SSE) so you see content as it arrives\n* Timestamp preservation — retains original timecodes for navigation\nAI Tools (powered by Groq + OpenRouter fallback)\n* Summary — concise TL;DR of any video\n* Key Insights — bullet-point takeaways extracted from the transcript\n* Flashcards — auto-generated Q&A cards with topic tags; full-screen flip UI with known/unknown tracking\n* Study Guide — structured document with overview, learning objectives, key concepts, sections, and review questions\n* Chapter Detection — splits long videos into labeled chapters automatically\n* AI Chat — ask follow-up questions about the transcript in a conversational interface\n* Layer | Technology\n* Frontend | React 18 (CRA), inline styles design system, framer-motion\n* Backend | Node.js 20+, Express 4\n* AI — Primary | Groq ( llama-3.3-70b-versatile )\n* AI — Fallback | OpenRouter\n* Transcript API | youtube-transcript npm package + Supadata fallback\n* Auth & Database | Supabase (Postgres + Auth)\nGetting Started\nPrerequisites\n* Node.js ≥ 20\n* npm ≥ 9\n* A Supabase project (free tier works)\n* A Groq API key (free tier available)\n1. Clone & install\ngit clone https://github.com/JoelMoyal/YouTub"
      ]
    },
    {
      "url": "http://github.com/microsoft/graphrag",
      "title": "GitHub - microsoft/graphrag: A modular graph-based Retrieval-Augmented Generation (RAG) system · GitHub",
      "publish_date": null,
      "excerpts": [
        "Description: A modular graph-based Retrieval-Augmented Generation (RAG) system - microsoft/graphrag Stars: 33,661 Forks: 3,563 Topics: gpt, rag, gpt-4, gpt4, llm, llms, graphrag License: MIT license\nGraphRAG Overview The GraphRAG project is a data pipeline and transformation suite that is designed to extract meaningful, structured data from unstructured text using the power of LLMs.\nPage: GitHub repository URL: http://github.com/microsoft/graphrag"
      ]
    },
    {
      "url": "https://github.com/dougbarrett/youtube-transcript",
      "title": "GitHub - dougbarrett/youtube-transcript",
      "publish_date": null,
      "excerpts": [
        "dougbarrett/youtube-transcript\nmain\nBranches Tags\nGo to file\nCode\nOpen more actions menu\nFolders and files\n* Name | Name | Last commit message | Last commit date\n* Latest commit\nHistory\n2 Commits\n*\nHeavily inspired by the excellent Python library: https://github.com/jdepoix/youtube-transcript-api\n*** THIS IS PROBABLY NOT SUITABLE FOR ALL USE CASES, I THREW THIS TOGETHER IN A FEW HOURS ***\npackage main\nimport (\n\"log\"\n\"context\"\n```\n\"github.com/dougbarrett/youtube-transcript\" \n```\n)"
      ]
    }
  ],
  "warnings": null,
  "metadata": null,
  "session_id": "ses_f2de9ab4effeqefH6MpyhdfGAE"
}
```

**Tool: github_search_repositories**

**Input:**
```json
{
  "minimal_output": true,
  "order": "desc",
  "page": 1,
  "perPage": 10,
  "query": "YouTube transcript channel archive comments",
  "sort": "updated"
}
```

**Output:**
```
{"total_count":1,"incomplete_results":false,"items":[{"id":1152775654,"name":"YouTube-Channel-Archiver","full_name":"canarik/YouTube-Channel-Archiver","description":"A powerful Google Chrome extension designed to archive entire YouTube channels. It allows you to download transcripts, comments, and live chat replays from videos efficiently.","html_url":"https://github.com/canarik/YouTube-Channel-Archiver","language":"JavaScript","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-02-08T12:27:29Z","created_at":"2026-02-08T12:18:55Z","private":false,"fork":false,"archived":false,"default_branch":"main"}]}
```

**Tool: github_search_repositories**

**Input:**
```json
{
  "minimal_output": true,
  "order": "desc",
  "page": 1,
  "perPage": 10,
  "query": "youtube markdown exporter yt-dlp",
  "sort": "stars"
}
```

**Output:**
```
{"total_count":0,"incomplete_results":false,"items":[]}
```

---

## Assistant (Plan · Space Bunny Free · 11.0s)

_Thinking:_

Need more candidates established. Search known: youtube-transcript-api, yt-dlp, comment-downloader, ytdl? channel archiver. Maybe socialblade? "youtube-scraper" etc. Need use Gitingest requirement. Installed absent. Could use npx? no install. Maybe command gitingest not installed. We can state unavailable, use GitHub API/raw inspection? User explicitly says use gitingest. Need determine installed package maybe pip list read only.

The initial search surfaced several useful classes of projects, including dedicated comment scrapers, transcript libraries, channel-archival tools, and newer RAG-oriented repositories. The advertised `gitingest` module is not available in the current Python environment, so I’m checking for an alternate installed invocation while continuing repository inspection through read-only GitHub source access.

**Tool: bash**

**Input:**
```json
{
  "command": "python -m pip list --format=columns 2>/dev/null | grep -i gitingest || true; command -v uv || true; command -v gitingest || true; ls -la /home/codespace/.local/bin 2>/dev/null || true",
  "timeout": 120000,
  "workdir": "/workspaces/TEMPORARY"
}
```

**Output:**
```
total 200
drwxrwxr-x 2 codespace codespace 4096 Sep 10 12:35 .
drwxrwxr-x 1 codespace codespace 4096 Sep 21 13:24 ..
-rwxrwxr-x 1 codespace codespace  183 Sep 10 12:35 cffi-gen-src
-rwxrwxr-x 1 codespace codespace  185 Sep 10 12:34 debugpy
-rwxrwxr-x 1 codespace codespace  191 Sep 10 12:34 debugpy-adapter
-rwxrwxr-x 1 codespace codespace  192 Sep 10 12:35 git-nbdiffdriver
-rwxrwxr-x 1 codespace codespace  190 Sep 10 12:35 git-nbdifftool
-rwxrwxr-x 1 codespace codespace  193 Sep 10 12:35 git-nbmergedriver
-rwxrwxr-x 1 codespace codespace  191 Sep 10 12:35 git-nbmergetool
-rwxrwxr-x 1 codespace codespace  185 Sep 10 12:35 hg-nbdiff
-rwxrwxr-x 1 codespace codespace  188 Sep 10 12:35 hg-nbdiffweb
-rwxrwxr-x 1 codespace codespace  186 Sep 10 12:35 hg-nbmerge
-rwxrwxr-x 1 codespace codespace  189 Sep 10 12:35 hg-nbmergeweb
-rwxrwxr-x 1 codespace codespace  172 Sep 10 12:35 httpx
-rwxrwxr-x 1 codespace codespace  175 Sep 10 12:34 idna
-rwxrwxr-x 1 codespace codespace  192 Sep 10 12:35 ipython
-rwxrwxr-x 1 codespace codespace  192 Sep 10 12:35 ipython3
-rwxrwxr-x 1 codespace codespace  187 Sep 10 12:35 jlpm
-rwxrwxr-x 1 codespace codespace 1779 Sep 10 12:34 jsonpointer
-rwxrwxr-x 1 codespace codespace  181 Sep 10 12:35 jsonschema
-rwxrwxr-x 1 codespace codespace  187 Sep 10 12:34 jupyter
-rwxrwxr-x 1 codespace codespace  187 Sep 10 12:35 jupyter-builder
-rwxrwxr-x 1 codespace codespace  203 Sep 10 12:35 jupyter-dejavu
-rwxrwxr-x 1 codespace codespace  185 Sep 10 12:35 jupyter-events
-rwxrwxr-x 1 codespace codespace  179 Sep 10 12:35 jupyter-execute
-rwxrwxr-x 1 codespace codespace  191 Sep 10 12:35 jupyter-kernel
-rwxrwxr-x 1 codespace codespace  229 Sep 10 12:35 jupyter-kernelspec
-rwxrwxr-x 1 codespace codespace  184 Sep 10 12:35 jupyter-lab
-rwxrwxr-x 1 codespace codespace  191 Sep 10 12:35 jupyter-labextension
-rwxrwxr-x 1 codespace codespace  187 Sep 10 12:35 jupyter-labhub
-rwxrwxr-x 1 codespace codespace  187 Sep 10 12:34 jupyter-migrate
-rwxrwxr-x 1 codespace codespace  189 Sep 10 12:35 jupyter-nbconvert
-rwxrwxr-x 1 codespace codespace  208 Sep 10 12:35 jupyter-run
-rwxrwxr-x 1 codespace codespace  191 Sep 10 12:35 jupyter-server
-rwxrwxr-x 1 codespace codespace  192 Sep 10 12:34 jupyter-troubleshoot
-rwxrwxr-x 1 codespace codespace  220 Sep 10 12:35 jupyter-trust
-rwxrwxr-x 1 codespace codespace  181 Sep 10 12:34 mistune
-rwxrwxr-x 1 codespace codespace  183 Sep 10 12:35 nbdiff
-rwxrwxr-x 1 codespace codespace  190 Sep 10 12:35 nbdiff-web
-rwxrwxr-x 1 codespace codespace  200 Sep 10 12:35 nbdime
-rwxrwxr-x 1 codespace codespace  184 Sep 10 12:35 nbmerge
-rwxrwxr-x 1 codespace codespace  191 Sep 10 12:35 nbmerge-web
-rwxrwxr-x 1 codespace codespace  183 Sep 10 12:35 nbshow
-rwxrwxr-x 1 codespace codespace  201 Sep 10 12:34 normalizer
-rwxrwxr-x 1 codespace codespace  190 Sep 10 12:34 pybabel
-rwxrwxr-x 1 codespace codespace  183 Sep 10 12:34 pygmentize
-rwxrwxr-x 1 codespace codespace  177 Sep 10 12:34 pyjson5
-rwxrwxr-x 1 codespace codespace  186 Sep 10 12:34 send2trash
-rwxrwxr-x 1 codespace codespace  184 Sep 10 12:34 wsdump

```

**Tool: github_search_repositories**

**Input:**
```json
{
  "minimal_output": true,
  "order": "desc",
  "page": 1,
  "perPage": 10,
  "query": "youtube comments scraper language:Python",
  "sort": "updated"
}
```

**Output:**
```
{"total_count":156,"incomplete_results":false,"items":[{"id":1379792961,"name":"youtube-scraper","full_name":"2scraper/youtube-scraper","description":"YouTube comment scraper (Playwright, Selenium, Puppeteer, or the 2Captcha Scraping Browser API via CDP) - comment threads and replies, video metadata, search, captcha solving, proxies","html_url":"https://github.com/2scraper/youtube-scraper","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":1,"updated_at":"2026-09-23T15:33:16Z","created_at":"2026-09-21T13:27:26Z","topics":["captcha-solver","comments","fingerprints","innertube","playwright","proxy","puppeteer","scraper","scraping-browser","selenium","sentiment-analysis","social-media","web-scraping","youtube","youtube-comments"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1380420398,"name":"youtube-comments-scraper","full_name":"iamrahul25/youtube-comments-scraper","description":"Youtube Comments Scraper","html_url":"https://github.com/iamrahul25/youtube-comments-scraper","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-21T19:35:24Z","created_at":"2026-09-21T19:34:42Z","private":false,"fork":false,"archived":false,"default_branch":"master"},{"id":1372614677,"name":"termux-yt-scraper","full_name":"hmar-heritage-org/termux-yt-scraper","description":"Lightweight, resilient YouTube comments scraper optimized for Android Termux to collect linguistic conversational text.","html_url":"https://github.com/hmar-heritage-org/termux-yt-scraper","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-16T06:32:55Z","created_at":"2026-09-16T06:25:22Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1365903798,"name":"social-scraper-cli","full_name":"PIYUSHBISHT0101/social-scraper-cli","description":"Universal terminal CLI \u0026 interactive wizard for scraping, filtering, and analyzing comments from YouTube, Reddit, and Instagram into Excel, CSV, and JSONL.","html_url":"https://github.com/PIYUSHBISHT0101/social-scraper-cli","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-11T11:16:27Z","created_at":"2026-09-11T10:56:25Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1347995486,"name":"youdata","full_name":"edbarron/youdata","description":"YouTube Analytics Scraper – Extracts video metrics (views, likes, comments) from any channel, stores them in a database, and exports ranked reports to Excel. Built with Python, YouTube API, and Pandas.","html_url":"https://github.com/edbarron/youdata","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-11T06:36:34Z","created_at":"2026-08-27T02:42:03Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1347152611,"name":"yt-channel-scraper","full_name":"gauravluniyaai-coder/yt-channel-scraper","description":"Scrape an entire YouTube channel: video/shorts/live transcripts, comments, community posts + their comments into single JSON \u0026 TXT files","html_url":"https://github.com/gauravluniyaai-coder/yt-channel-scraper","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-26T10:01:52Z","created_at":"2026-08-26T09:36:20Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1323820854,"name":"scrape-youtube-comments","full_name":"data-scrape/scrape-youtube-comments","description":"Scrape YouTube comments - extract comments from any video","html_url":"https://github.com/data-scrape/scrape-youtube-comments","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-11T01:35:04Z","created_at":"2026-08-05T08:37:09Z","topics":["data-extraction","python","scraper","web-scraping","youtube","youtube-scraper"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1323311533,"name":"yt-scraper","full_name":"colintrachte/yt-scraper","description":"download the comments and transcript from a youtube playlist.","html_url":"https://github.com/colintrachte/yt-scraper","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-05T16:28:45Z","created_at":"2026-08-04T19:31:03Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1174542451,"name":"youtube-search-python","full_name":"SkyBotsDeveloper/youtube-search-python","description":"A lightweight Python library to search YouTube without using the YouTube Data API, with sync/async support for videos, channels, playlists, suggestions, transcripts, comments, and stream helpers.","html_url":"https://github.com/SkyBotsDeveloper/youtube-search-python","language":"Python","stargazers_count":7,"forks_count":5,"open_issues_count":0,"updated_at":"2026-08-05T08:26:54Z","created_at":"2026-03-06T15:04:49Z","topics":["asyncio","open-source","python","python-library","scraper","video-search","youtube","youtube-api","youtube-library","youtube-search"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1175210363,"name":"bright-data-youtube-scraper","full_name":"yaronbeen/bright-data-youtube-scraper","description":"Collect YouTube channels, videos, and comments via Bright Data Web Scraper API. Zero-dependency Python.","html_url":"https://github.com/yaronbeen/bright-data-youtube-scraper","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-03T16:11:20Z","created_at":"2026-03-07T11:44:30Z","private":false,"fork":false,"archived":false,"default_branch":"main"}]}
```

**Tool: github_search_repositories**

**Input:**
```json
{
  "minimal_output": true,
  "order": "desc",
  "page": 1,
  "perPage": 10,
  "query": "youtube channel downloader yt-dlp language:Python",
  "sort": "updated"
}
```

**Output:**
```
{"total_count":38,"incomplete_results":false,"items":[{"id":1370808210,"name":"Channel-Harvest","full_name":"jjsiew2014-art/Channel-Harvest","description":"A modern, clean, commercial-grade Windows desktop application for archiving and downloading entire YouTube channels and playlists.","html_url":"https://github.com/jjsiew2014-art/Channel-Harvest","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-24T04:09:38Z","created_at":"2026-09-15T03:11:23Z","topics":["deno","download","downloader","downloader-for-youtube","downloadmanager","esj","ffmpeg","javascript","metadata","python","software","subtitles","transcode","windows","youtube","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1377444704,"name":"youtubedl","full_name":"musicOverdose/youtubedl","description":"Production-grade, private Telegram YouTube downloader bot with web admin panel, persistent channel caching, strict quality matching, and AI subtitle translation.","html_url":"https://github.com/musicOverdose/youtubedl","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-22T06:03:55Z","created_at":"2026-09-19T17:34:38Z","topics":["aiogram","docker","fastapi","ffmpeg","portainer","redis-queue","self-hosted","subtitles","telegram-bot","youtube-downloader","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1111602664,"name":"channeldepot","full_name":"SanHsien/channeldepot","description":"Lightweight portable YouTube channel downloader with GUI, batch imports, sign-in cookies, and standalone Windows EXE. 輕巧可攜的 YouTube 頻道下載工具（GUI／批次匯入／Windows 免安裝），可登入下載自己有權觀看的內容。","html_url":"https://github.com/SanHsien/channeldepot","language":"Python","stargazers_count":5,"forks_count":4,"open_issues_count":1,"updated_at":"2026-09-21T11:07:05Z","created_at":"2025-12-07T09:26:18Z","topics":["ffmpeg","gui","local-first","portable","python","tkinter","video-downloader","windows","youtube","youtube-downloader","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1357971909,"name":"Magneto","full_name":"cedhuf/Magneto","description":"Self-hosted video downloader and reader. Paste a link and keep the file for a day, or follow YouTube channels and TikTok accounts and read them from your own server. Flask and yt-dlp, no build step. Forked from averygan/reclip.","html_url":"https://github.com/cedhuf/Magneto","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-21T08:23:19Z","created_at":"2026-09-05T08:17:06Z","topics":["flask","pwa","self-hosted","tiktok","youtube","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1322180001,"name":"media-tools","full_name":"edunavajas/media-tools","description":"Media tools service: channel whisper (YouTube transcriptions) + social video downloader (yt-dlp). Satellite of edunavajas-hub.","html_url":"https://github.com/edunavajas/media-tools","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-18T20:17:41Z","created_at":"2026-08-03T19:46:40Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1375971054,"name":"downloader","full_name":"ibrahimal22/downloader","description":"Desktop video downloader for YouTube playlists, channels and 1,800+ sites — with a searchable library, smart scheduling, subscriptions and a browser extension.","html_url":"https://github.com/ibrahimal22/downloader","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-18T16:33:37Z","created_at":"2026-09-18T14:14:36Z","topics":["desktop-app","download-manager","media-library","playlist-downloader","pyside6","python","qt6","scheduler","video-downloader","windows","youtube-downloader","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1368896874,"name":"YT_playlist_downloader_by_Valcheff","full_name":"valcheffnet/YT_playlist_downloader_by_Valcheff","description":"Download YouTube playlists and channels with yt-dlp: playlist-ordered filenames, resume across runs, and per-item error tolerance","html_url":"https://github.com/valcheffnet/YT_playlist_downloader_by_Valcheff","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-13T21:51:57Z","created_at":"2026-09-13T21:12:17Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1362760929,"name":"ytdl-downloader","full_name":"devrite4/ytdl-downloader","description":"Resumable YouTube channel downloader with SQLite inventory. Downloads in random order with randomised delays (60–180s), batch cooldowns, and quiet hours - designed to look organic and avoid rate limits.  Uses yt-dlp + ffmpeg + uv.","html_url":"https://github.com/devrite4/ytdl-downloader","language":"Python","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-09T14:15:44Z","created_at":"2026-09-09T14:02:26Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1358332572,"name":"wx-channels-downloader","full_name":"yanbf888/wx-channels-downloader","description":"免费下载微信视频号（finder / 视频号）视频，以及 B站/抖音/YouTube/小红书等 1000+ 站点视频。视频号走腾讯元宝解析接口（免费，需用户自己的元宝 Cookie），其他平台走内置 yt-dlp。","html_url":"https://github.com/yanbf888/wx-channels-downloader","language":"Python","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-05T15:45:09Z","created_at":"2026-09-05T15:44:43Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":720893233,"name":"yt-channel-downloader","full_name":"Sewer2K/yt-channel-downloader","description":"Download YouTube channel videos \u0026 Shorts with a modern desktop GUI — yt-dlp + PySide6, thumbnail/title/view-count previews, quality picker, download history, standalone .exe","html_url":"https://github.com/Sewer2K/yt-channel-downloader","language":"Python","stargazers_count":26,"forks_count":12,"open_issues_count":2,"updated_at":"2026-09-09T02:15:02Z","created_at":"2023-11-19T22:43:25Z","topics":["bulk-downloader","cross-platform","desktop-app","download-manager","ffmpeg","gui","mp3-downloader","open-source","pyinstaller","pyside6","python","video-downloader","windows","youtube-channel-downloader","youtube-downloader","youtube-shorts","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"}]}
```

**Tool: github_search_repositories**

**Input:**
```json
{
  "minimal_output": true,
  "order": "desc",
  "page": 1,
  "perPage": 10,
  "query": "youtube transcript api language:Python",
  "sort": "stars"
}
```

**Output:**
```
{"total_count":771,"incomplete_results":false,"items":[{"id":130369089,"name":"youtube-transcript-api","full_name":"jdepoix/youtube-transcript-api","description":"This is a python API which allows you to get the transcript/subtitles for a given YouTube video. It also works for automatically generated subtitles and it does not require an API key nor a headless browser, like other selenium based solutions do!","html_url":"https://github.com/jdepoix/youtube-transcript-api","language":"Python","stargazers_count":8366,"forks_count":840,"open_issues_count":32,"updated_at":"2026-09-24T02:42:02Z","created_at":"2018-04-20T13:55:04Z","topics":["asr","captions","cli","python","subtitle","subtitles","transcript","transcripts","translating-transcripts","youtube","youtube-api","youtube-asr","youtube-captions","youtube-subtitles","youtube-transcript","youtube-transcripts","youtube-video"],"private":false,"fork":false,"archived":false,"default_branch":"master"},{"id":973461176,"name":"VideoTranscriptAPI","full_name":"zlxlabs/VideoTranscriptAPI","description":"基于 Python 3.11+ FastAPI 的异步音视频转录服务，支持 YouTube、小宇宙、Bilibili、视频号等多平台解析，本地部署可实现说话人区分转录，调用 LLM 完成文本智能校对与内容总结，配套网页端查看 / 导出功能，支持企业微信消息推送","html_url":"https://github.com/zlxlabs/VideoTranscriptAPI","language":"Python","stargazers_count":214,"forks_count":30,"open_issues_count":5,"updated_at":"2026-09-22T00:40:30Z","created_at":"2025-04-27T03:22:12Z","topics":["personal"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1176226503,"name":"video-lens","full_name":"kar2phi/video-lens","description":"video-lens is a coding agent skill that fetches a YouTube transcript and generates a structured HTML report: executive summary, key points, analysis, takeaway, timestamped topic outline, and an embedded in-page player. No API keys, no external services beyond the coding agent itself.","html_url":"https://github.com/kar2phi/video-lens","language":"Python","stargazers_count":111,"forks_count":20,"open_issues_count":3,"updated_at":"2026-09-16T10:21:43Z","created_at":"2026-03-08T19:35:31Z","topics":["agent","skills","transcription","youtube"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":880607253,"name":"headwater","full_name":"HouseofLoops/headwater","description":"One self-hosted API for Google Maps, News, Trends and Autocomplete, plus YouTube transcripts. Normalised JSON, no per-call vendor pricing, runs in Docker.","html_url":"https://github.com/HouseofLoops/headwater","language":"Python","stargazers_count":64,"forks_count":10,"open_issues_count":0,"updated_at":"2026-09-24T03:41:45Z","created_at":"2024-10-30T02:39:25Z","topics":["api","autocomplete","docker","fastapi","google-maps","google-news","google-trends","python","scraping","self-hosted","serp","youtube-transcript"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":379852909,"name":"yt-sum-flask","full_name":"AnujK2901/yt-sum-flask","description":"YouTube Transcript Summarization over Flask: This back-end uses Flask framework to receive API calls from the client and then respond with the summarized text response. This API can work only on those YouTube videos which has well-formatted closed captions in it. The same backend also hosts a web version of the Summarizer.","html_url":"https://github.com/AnujK2901/yt-sum-flask","language":"Python","stargazers_count":53,"forks_count":26,"open_issues_count":2,"updated_at":"2025-07-26T14:21:32Z","created_at":"2021-06-24T08:15:20Z","topics":["flask","flask-api","flask-application","flask-webapp","gensim","nlp","nlp-machine-learning","nltk-python","python3","spacy-nlp","sumy"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1366190855,"name":"youtube-scout","full_name":"AgriciDaniel/youtube-scout","description":"Claude Code skill: one topic in, one ranked YouTube research workbook out. Searches YouTube Data API v3, ranks by views, engagement, momentum or breakout, and writes Videos, Channels, Summary, Comments and Transcripts sheets with hooks and replay hotspots. Appends into an existing social ads sheet.","html_url":"https://github.com/AgriciDaniel/youtube-scout","language":"Python","stargazers_count":50,"forks_count":7,"open_issues_count":0,"updated_at":"2026-09-22T06:51:28Z","created_at":"2026-09-11T13:38:59Z","topics":["agent-skill","ai-marketing","claude-code","claude-skill","cli","competitor-research","creator-research","hooks","marketing-research","openpyxl","python","shorts","social-ads","spreadsheet","transcripts","xlsx","youtube","youtube-data-api","youtube-research","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":644588875,"name":"openai-summary","full_name":"matatonic/openai-summary","description":"Summarize URL's or files (including YouTube videos via transcripts) using an OpenAI compatible API.","html_url":"https://github.com/matatonic/openai-summary","language":"Python","stargazers_count":43,"forks_count":6,"open_issues_count":0,"updated_at":"2026-06-04T11:59:40Z","created_at":"2023-05-23T20:51:50Z","private":false,"fork":false,"archived":true,"default_branch":"main"},{"id":1188570810,"name":"ytsearch","full_name":"Infatoshi/ytsearch","description":"Search YouTube transcripts from the terminal. No download, no API key, no whisper.","html_url":"https://github.com/Infatoshi/ytsearch","language":"Python","stargazers_count":43,"forks_count":4,"open_issues_count":1,"updated_at":"2026-08-25T13:04:15Z","created_at":"2026-03-22T09:16:57Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":955077398,"name":"Youtube-MCP","full_name":"IA-Programming/Youtube-MCP","description":"YouTube MCP Server is an AI-powered solution designed to revolutionize your YouTube experience. It empowers users to search for YouTube videos, retrieve detailed transcripts, and perform semantic searches over video content—all without relying on the official API. By integrating with a vector database, this server streamlines content discovery.","html_url":"https://github.com/IA-Programming/Youtube-MCP","language":"Python","stargazers_count":36,"forks_count":17,"open_issues_count":5,"updated_at":"2026-09-20T19:22:34Z","created_at":"2025-03-26T04:25:32Z","topics":["ai","machine-learning","mcp","mcp-server","python","semantic-search","transcripts","uv","vector-database","youtube"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":622208218,"name":"youtube-transcriber-api","full_name":"mongj/youtube-transcriber-api","description":"Simple REST API endpoints for retrieving transcripts for YouTube videos.","html_url":"https://github.com/mongj/youtube-transcriber-api","language":"Python","stargazers_count":30,"forks_count":311,"open_issues_count":1,"updated_at":"2026-06-12T00:01:18Z","created_at":"2023-04-01T12:50:28Z","topics":["api","flask","python","restful-api","youtube","youtube-api","youtube-transcripts"],"private":false,"fork":false,"archived":true,"default_branch":"main"}]}
```

**Tool: github_search_repositories**

**Input:**
```json
{
  "minimal_output": true,
  "order": "desc",
  "page": 1,
  "perPage": 10,
  "query": "youtube channel archive language:TypeScript",
  "sort": "updated"
}
```

**Output:**
```
{"total_count":8,"incomplete_results":false,"items":[{"id":1334820230,"name":"transcriptly","full_name":"liujiaqi222/transcriptly","description":"Free, open-source YouTube transcript downloader: a Chrome extension that batch-captures videos, playlists, and channels into timestamped Markdown you own — plus a public transcript archive at transcriptly.libmap.cn.","html_url":"https://github.com/liujiaqi222/transcriptly","language":"TypeScript","stargazers_count":3,"forks_count":0,"open_issues_count":8,"updated_at":"2026-09-23T15:07:12Z","created_at":"2026-08-15T05:34:37Z","topics":["chrome-extension","transcript","transcriptly","youtube","youtube-transcript","youtube-transcript-downloader"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1222011698,"name":"kavynex","full_name":"eduardoghi/kavynex","description":"Archive YouTube channels to your own disk, comments and live chat included, and play it all back offline. No server, no container.","html_url":"https://github.com/eduardoghi/kavynex","language":"TypeScript","stargazers_count":3,"forks_count":0,"open_issues_count":0,"updated_at":"2026-09-23T03:06:58Z","created_at":"2026-04-27T00:40:40Z","topics":["archiving","backup","desktop-app","digital-preservation","media-library","react","rust","tauri","typescript","video-player","youtube","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1254165127,"name":"channel-vault-nas","full_name":"hyeonsangjeon/channel-vault-nas","description":"Back up YouTube channels to your NAS. Reuse archive.txt and existing media, download only what is missing, and recover the index from disk.","html_url":"https://github.com/hyeonsangjeon/channel-vault-nas","language":"TypeScript","stargazers_count":10,"forks_count":0,"open_issues_count":2,"updated_at":"2026-09-06T15:11:53Z","created_at":"2026-05-30T08:09:11Z","topics":["archive","docker","docker-compose","fastapi","homelab","media-archive","nas","nas-storage","qnap","react","self-hosted","sqlite","synology","vite","youtube","youtube-archive","youtube-backup","yt-dlp"],"private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":1313317876,"name":"sroub","full_name":"im4tta/sroub","description":"Sroub (ស្រូប, \"to soak up / absorb\") is a self-hosted media archiver for YouTube, Spotify and Apple Music. Point it at channels, playlists, albums, artists or tracks and it quietly pulls everything down for you — as video or mp3 audio — then streams it back through a slick dark web UI, with optional Telegram delivery.","html_url":"https://github.com/im4tta/sroub","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-14T01:01:47Z","created_at":"2026-07-27T01:55:20Z","private":false,"fork":false,"archived":false,"default_branch":"master"},{"id":1232339697,"name":"lasso","full_name":"nsozturk/lasso","description":"Local-first desktop app: subscribe to a YouTube channel and archive every video to your disk. Tauri + React + yt-dlp.","html_url":"https://github.com/nsozturk/lasso","language":"TypeScript","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2026-08-12T05:25:30Z","created_at":"2026-05-07T20:43:26Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":687096354,"name":"hive","full_name":"killbasa/hive","description":"YouTube channel archiver","html_url":"https://github.com/killbasa/hive","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":15,"updated_at":"2025-04-22T00:58:11Z","created_at":"2023-09-04T15:47:59Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":748065358,"name":"ytsize","full_name":"xoltia/ytsize","description":"Size estimator for YouTube channel archiving","html_url":"https://github.com/xoltia/ytsize","language":"TypeScript","stargazers_count":1,"forks_count":0,"open_issues_count":0,"updated_at":"2024-08-07T04:03:53Z","created_at":"2024-01-25T07:45:17Z","private":false,"fork":false,"archived":false,"default_branch":"main"},{"id":345544244,"name":"ryaxArchives","full_name":"Dayton-IX/ryaxArchives","description":"A secure archive for the videos from the Ryax Youtube channel!","html_url":"https://github.com/Dayton-IX/ryaxArchives","language":"TypeScript","stargazers_count":0,"forks_count":0,"open_issues_count":0,"updated_at":"2021-04-20T02:38:20Z","created_at":"2021-03-08T05:44:56Z","private":false,"fork":false,"archived":false,"default_branch":"main"}]}
```

---

## Assistant (Plan · Space Bunny Free · 7.4s)

_Thinking:_

Interesting date current 2026 and future results okay. Need serious candidates 8-12. Choose:
jdepoix transcript-api
yt-dlp
xBartM scraper
mattwright comment suite
warkingtime archiver
dlove exporter
Brian KB
canarik extension
kavynex maybe
channel-hoarder
YouTube-MCP
perhaps youtube-search-python
Need source inspect. Gitingest unavailable, can use GitHub get contents tree and files. Need actual source. We'll use github_get_file_contents for key repos, perhaps tool output sizable. Parallel. First get READMEs, trees, licenses, package files.

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "jdepoix",
  "path": "/",
  "ref": "refs/heads/master",
  "repo": "youtube-transcript-api"
}
```

**Output:**
```
[{"name":".github","path":".github","type":"dir"},{"name":".gitignore","path":".gitignore","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"poetry.lock","path":"poetry.lock","type":"file"},{"name":"pyproject.toml","path":"pyproject.toml","type":"file"},{"name":"youtube_transcript_api","path":"youtube_transcript_api","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "yt-dlp",
  "path": "/",
  "ref": "refs/heads/master",
  "repo": "yt-dlp"
}
```

**Output:**
```
[{"name":".NO_AI","path":".NO_AI","type":"dir"},{"name":".editorconfig","path":".editorconfig","type":"file"},{"name":".gitattributes","path":".gitattributes","type":"file"},{"name":".github","path":".github","type":"dir"},{"name":".gitignore","path":".gitignore","type":"file"},{"name":".pre-commit-config.yaml","path":".pre-commit-config.yaml","type":"file"},{"name":".pre-commit-hatch.yaml","path":".pre-commit-hatch.yaml","type":"file"},{"name":"CONTRIBUTING.md","path":"CONTRIBUTING.md","type":"file"},{"name":"CONTRIBUTORS","path":"CONTRIBUTORS","type":"file"},{"name":"Changelog.md","path":"Changelog.md","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"Maintainers.md","path":"Maintainers.md","type":"file"},{"name":"Makefile","path":"Makefile","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"THIRD_PARTY_LICENSES.txt","path":"THIRD_PARTY_LICENSES.txt","type":"file"},{"name":"bundle","path":"bundle","type":"dir"},{"name":"devscripts","path":"devscripts","type":"dir"},{"name":"public.key","path":"public.key","type":"file"},{"name":"pyproject.toml","path":"pyproject.toml","type":"file"},{"name":"supportedsites.md","path":"supportedsites.md","type":"file"},{"name":"test","path":"test","type":"dir"},{"name":"uv.lock","path":"uv.lock","type":"file"},{"name":"yt-dlp.cmd","path":"yt-dlp.cmd","type":"file"},{"name":"yt-dlp.sh","path":"yt-dlp.sh","type":"file"},{"name":"yt_dlp","path":"yt_dlp","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "xBartM",
  "path": "/",
  "ref": "refs/heads/master",
  "repo": "YouTube-Comment-Scraper"
}
```

**Output:**
```
[{"name":".gitignore","path":".gitignore","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"channels.txt","path":"channels.txt","type":"file"},{"name":"configs","path":"configs","type":"dir"},{"name":"database","path":"database","type":"dir"},{"name":"scripts","path":"scripts","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "mattwright324",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
[{"name":".gitignore","path":".gitignore","type":"file"},{"name":"BUILD.md","path":"BUILD.md","type":"file"},{"name":"CONTRIBUTING.md","path":"CONTRIBUTING.md","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"PRIVACY.md","path":"PRIVACY.md","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"TERMS.md","path":"TERMS.md","type":"file"},{"name":"module-info.java","path":"module-info.java","type":"file"},{"name":"pom.xml","path":"pom.xml","type":"file"},{"name":"resources","path":"resources","type":"dir"},{"name":"src","path":"src","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "warkingtime",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "channel-transcript-archiver"
}
```

**Output:**
```
[{"name":".gitignore","path":".gitignore","type":"file"},{"name":"AGENTS.md","path":"AGENTS.md","type":"file"},{"name":"CLAUDE.md","path":"CLAUDE.md","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"channel-archiver","path":"channel-archiver","type":"file"},{"name":"pyproject.toml","path":"pyproject.toml","type":"file"},{"name":"src","path":"src","type":"dir"},{"name":"uv.lock","path":"uv.lock","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "dlovecreator-arch",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
[{"name":".env.example","path":".env.example","type":"file"},{"name":".github","path":".github","type":"dir"},{"name":".gitignore","path":".gitignore","type":"file"},{"name":"CHANGELOG.md","path":"CHANGELOG.md","type":"file"},{"name":"CODE_OF_CONDUCT.md","path":"CODE_OF_CONDUCT.md","type":"file"},{"name":"CONTRIBUTING.md","path":"CONTRIBUTING.md","type":"file"},{"name":"CONVENTIONS.md","path":"CONVENTIONS.md","type":"file"},{"name":"Dockerfile","path":"Dockerfile","type":"file"},{"name":"INSTALL.md","path":"INSTALL.md","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"QUICKSTART.md","path":"QUICKSTART.md","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"SECURITY.md","path":"SECURITY.md","type":"file"},{"name":"TROUBLESHOOTING.md","path":"TROUBLESHOOTING.md","type":"file"},{"name":"archive","path":"archive","type":"dir"},{"name":"channels.txt.example","path":"channels.txt.example","type":"file"},{"name":"config.json","path":"config.json","type":"file"},{"name":"db","path":"db","type":"dir"},{"name":"docker-compose.yml","path":"docker-compose.yml","type":"file"},{"name":"docs","path":"docs","type":"dir"},{"name":"examples","path":"examples","type":"dir"},{"name":"export.sh","path":"export.sh","type":"file"},{"name":"pyproject.toml","path":"pyproject.toml","type":"file"},{"name":"requirements.txt","path":"requirements.txt","type":"file"},{"name":"src","path":"src","type":"dir"},{"name":"tests","path":"tests","type":"dir"},{"name":"tools","path":"tools","type":"dir"},{"name":"ytexporter","path":"ytexporter","type":"dir"},{"name":"ytx","path":"ytx","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "BrianGuo723",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "youtube-knowledge-base"
}
```

**Output:**
```
[{"name":".env.example","path":".env.example","type":"file"},{"name":".gitignore","path":".gitignore","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"ingest.py","path":"ingest.py","type":"file"},{"name":"requirements.txt","path":"requirements.txt","type":"file"},{"name":"youtube-knowledge-base.md","path":"youtube-knowledge-base.md","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "canarik",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "YouTube-Channel-Archiver"
}
```

**Output:**
```
[{"name":".gitignore","path":".gitignore","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"background","path":"background","type":"dir"},{"name":"content","path":"content","type":"dir"},{"name":"icons","path":"icons","type":"dir"},{"name":"manifest.json","path":"manifest.json","type":"file"},{"name":"popup","path":"popup","type":"dir"},{"name":"utils","path":"utils","type":"dir"}]
```

---

## Assistant (Plan · Space Bunny Free · 5.8s)

_Thinking:_

Need actual files. Use get dirs for relevant.

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "jdepoix",
  "path": "youtube_transcript_api",
  "ref": "refs/heads/master",
  "repo": "youtube-transcript-api"
}
```

**Output:**
```
[{"name":"__init__.py","path":"youtube_transcript_api/__init__.py","type":"file"},{"name":"__main__.py","path":"youtube_transcript_api/__main__.py","type":"file"},{"name":"_api.py","path":"youtube_transcript_api/_api.py","type":"file"},{"name":"_cli.py","path":"youtube_transcript_api/_cli.py","type":"file"},{"name":"_errors.py","path":"youtube_transcript_api/_errors.py","type":"file"},{"name":"_settings.py","path":"youtube_transcript_api/_settings.py","type":"file"},{"name":"_transcripts.py","path":"youtube_transcript_api/_transcripts.py","type":"file"},{"name":"formatters.py","path":"youtube_transcript_api/formatters.py","type":"file"},{"name":"proxies.py","path":"youtube_transcript_api/proxies.py","type":"file"},{"name":"py.typed","path":"youtube_transcript_api/py.typed","type":"file"},{"name":"test","path":"youtube_transcript_api/test","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "warkingtime",
  "path": "src",
  "ref": "refs/heads/main",
  "repo": "channel-transcript-archiver"
}
```

**Output:**
```
[{"name":"__init__.py","path":"src/__init__.py","type":"file"},{"name":"analyze_durations.py","path":"src/analyze_durations.py","type":"file"},{"name":"analyze_gaps.py","path":"src/analyze_gaps.py","type":"file"},{"name":"browser.py","path":"src/browser.py","type":"file"},{"name":"clean_transcripts.py","path":"src/clean_transcripts.py","type":"file"},{"name":"cli.py","path":"src/cli.py","type":"file"},{"name":"compress.py","path":"src/compress.py","type":"file"},{"name":"extract.py","path":"src/extract.py","type":"file"},{"name":"extract_cookies.py","path":"src/extract_cookies.py","type":"file"},{"name":"find_long_blocks.py","path":"src/find_long_blocks.py","type":"file"},{"name":"fix_titles.py","path":"src/fix_titles.py","type":"file"},{"name":"format_and_summarize.py","path":"src/format_and_summarize.py","type":"file"},{"name":"get_patreon_collections.py","path":"src/get_patreon_collections.py","type":"file"},{"name":"get_playlists.py","path":"src/get_playlists.py","type":"file"},{"name":"list_channels.py","path":"src/list_channels.py","type":"file"},{"name":"populate_archive.py","path":"src/populate_archive.py","type":"file"},{"name":"precheck.py","path":"src/precheck.py","type":"file"},{"name":"reclean.py","path":"src/reclean.py","type":"file"},{"name":"remove_duplicates.py","path":"src/remove_duplicates.py","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "dlovecreator-arch",
  "path": "src",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
[{"name":"download_resilient.py","path":"src/download_resilient.py","type":"file"},{"name":"enhance_markdown_rag.py","path":"src/enhance_markdown_rag.py","type":"file"},{"name":"enhance_rag_schema.py","path":"src/enhance_rag_schema.py","type":"file"},{"name":"markdown_generator.py","path":"src/markdown_generator.py","type":"file"},{"name":"metadata_extractor.py","path":"src/metadata_extractor.py","type":"file"},{"name":"obsidian_formatter.py","path":"src/obsidian_formatter.py","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "dlovecreator-arch",
  "path": "tests",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
[{"name":"build_fixture.sh","path":"tests/build_fixture.sh","type":"file"},{"name":"smoke_test.sh","path":"tests/smoke_test.sh","type":"file"},{"name":"test_all.py","path":"tests/test_all.py","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "xBartM",
  "path": "scripts",
  "ref": "refs/heads/master",
  "repo": "YouTube-Comment-Scraper"
}
```

**Output:**
```
[{"name":"db_create_schema.sh","path":"scripts/db_create_schema.sh","type":"file"},{"name":"db_drop_schema.sh","path":"scripts/db_drop_schema.sh","type":"file"},{"name":"db_init.sh","path":"scripts/db_init.sh","type":"file"},{"name":"db_start.sh","path":"scripts/db_start.sh","type":"file"},{"name":"db_stop.sh","path":"scripts/db_stop.sh","type":"file"},{"name":"insert_videos.sh","path":"scripts/insert_videos.sh","type":"file"},{"name":"update_channels.sh","path":"scripts/update_channels.sh","type":"file"},{"name":"update_metadata.sh","path":"scripts/update_metadata.sh","type":"file"},{"name":"update_videos.sh","path":"scripts/update_videos.sh","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "xBartM",
  "path": "database",
  "ref": "refs/heads/master",
  "repo": "YouTube-Comment-Scraper"
}
```

**Output:**
```
[{"name":"create_schema.sql","path":"database/create_schema.sql","type":"file"},{"name":"drop_schema.sql","path":"database/drop_schema.sql","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "mattwright324",
  "path": "src",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
[{"name":"main","path":"src/main","type":"dir"},{"name":"test","path":"src/test","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "canarik",
  "path": "background",
  "ref": "refs/heads/main",
  "repo": "YouTube-Channel-Archiver"
}
```

**Output:**
```
[{"name":"service-worker.js","path":"background/service-worker.js","type":"file"}]
```

---

## Assistant (Plan · Space Bunny Free · 5.7s)

_Thinking:_

Need inspect key files content. Use github get file. Also licenses across candidates. Could read via GitHub.

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "jdepoix",
  "path": "youtube_transcript_api/_api.py",
  "ref": "refs/heads/master",
  "repo": "youtube-transcript-api"
}
```

**Output:**
```
successfully downloaded text file (SHA: b29449349ac56a1da90de18d91e1c10add76cac2)

from typing import Optional, Iterable

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from .proxies import ProxyConfig

from ._transcripts import TranscriptListFetcher, FetchedTranscript, TranscriptList


class YouTubeTranscriptApi:
    def __init__(
        self,
        proxy_config: Optional[ProxyConfig] = None,
        http_client: Optional[Session] = None,
    ):
        """
        Note on thread-safety: As this class will initialize a `requests.Session`
        object, it is not thread-safe. Make sure to initialize an instance of
        `YouTubeTranscriptApi` per thread, if used in a multi-threading scenario!

        :param proxy_config: an optional ProxyConfig object, defining proxies used for
            all network requests. This can be used to work around your IP being blocked
            by YouTube, as described in the "Working around IP bans" section of the
            README
            (https://github.com/jdepoix/youtube-transcript-api?tab=readme-ov-file#working-around-ip-bans-requestblocked-or-ipblocked-exception)
        :param http_client: You can optionally pass in a requests.Session object, if you
            manually want to share cookies between different instances of
            `YouTubeTranscriptApi`, overwrite defaults, specify SSL certificates, etc.
        """
        http_client = Session() if http_client is None else http_client
        http_client.headers.update({"Accept-Language": "en-US"})
        # Cookie auth has been temporarily disabled, as it is not working properly with
        # YouTube's most recent changes.
        # if cookie_path is not None:
        #     http_client.cookies = _load_cookie_jar(cookie_path)
        if proxy_config is not None:
            http_client.proxies = proxy_config.to_requests_dict()
            if proxy_config.prevent_keeping_connections_alive:
                http_client.headers.update({"Connection": "close"})
            if proxy_config.retries_when_blocked > 0:
                retry_config = Retry(
                    total=proxy_config.retries_when_blocked,
                    status_forcelist=[429],
                )
                http_client.mount("http://", HTTPAdapter(max_retries=retry_config))
                http_client.mount("https://", HTTPAdapter(max_retries=retry_config))
        self._fetcher = TranscriptListFetcher(http_client, proxy_config=proxy_config)

    def fetch(
        self,
        video_id: str,
        languages: Iterable[str] = ("en",),
        preserve_formatting: bool = False,
    ) -> FetchedTranscript:
        """
        Retrieves the transcript for a single video. This is just a shortcut for
        calling:
        `YouTubeTranscriptApi().list(video_id).find_transcript(languages).fetch(preserve_formatting=preserve_formatting)`

        :param video_id: the ID of the video you want to retrieve the transcript for.
            Make sure that this is the actual ID, NOT the full URL to the video!
        :param languages: A list of language codes in a descending priority. For
            example, if this is set to ["de", "en"] it will first try to fetch the
            german transcript (de) and then fetch the english transcript (en) if
            it fails to do so. This defaults to ["en"].
        :param preserve_formatting: whether to keep select HTML text formatting
        """
        return (
            self.list(video_id)
            .find_transcript(languages)
            .fetch(preserve_formatting=preserve_formatting)
        )

    def list(
        self,
        video_id: str,
    ) -> TranscriptList:
        """
        Retrieves the list of transcripts which are available for a given video. It
        returns a `TranscriptList` object which is iterable and provides methods to
        filter the list of transcripts for specific languages. While iterating over
        the `TranscriptList` the individual transcripts are represented by
        `Transcript` objects, which provide metadata and can either be fetched by
        calling `transcript.fetch()` or translated by calling `transcript.translate(
        'en')`. Example:

        ```
        ytt_api = YouTubeTranscriptApi()

        # retrieve the available transcripts
        transcript_list = ytt_api.list('video_id')

        # iterate over all available transcripts
        for transcript in transcript_list:
            # the Transcript object provides metadata properties
            print(
                transcript.video_id,
                transcript.language,
                transcript.language_code,
                # whether it has been manually created or generated by YouTube
                transcript.is_generated,
                # a list of languages the transcript can be translated to
                transcript.translation_languages,
            )

            # fetch the actual transcript data
            print(transcript.fetch())

            # translating the transcript will return another transcript object
            print(transcript.translate('en').fetch())

        # you can also directly filter for the language you are looking for, using the transcript list
        transcript = transcript_list.find_transcript(['de', 'en'])

        # or just filter for manually created transcripts
        transcript = transcript_list.find_manually_created_transcript(['de', 'en'])

        # or automatically generated ones
        transcript = transcript_list.find_generated_transcript(['de', 'en'])
        ```

        :param video_id: the ID of the video you want to retrieve the transcript for.
            Make sure that this is the actual ID, NOT the full URL to the video!
        """
        return self._fetcher.fetch(video_id)

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "jdepoix",
  "path": "youtube_transcript_api/_transcripts.py",
  "ref": "refs/heads/master",
  "repo": "youtube-transcript-api"
}
```

**Output:**
```
successfully downloaded text file (SHA: 55baa426ff89bad218339ce108d7c080351f66b4)

from dataclasses import dataclass, asdict
from enum import Enum
from itertools import chain

from html import unescape
from typing import List, Dict, Iterator, Iterable, Pattern, Optional

from defusedxml import ElementTree

import re

from requests import HTTPError, Session, Response

from .proxies import ProxyConfig
from ._settings import WATCH_URL, INNERTUBE_CONTEXT, INNERTUBE_API_URL
from ._errors import (
    VideoUnavailable,
    YouTubeRequestFailed,
    NoTranscriptFound,
    TranscriptsDisabled,
    NotTranslatable,
    TranslationLanguageNotAvailable,
    FailedToCreateConsentCookie,
    InvalidVideoId,
    IpBlocked,
    RequestBlocked,
    AgeRestricted,
    VideoUnplayable,
    YouTubeDataUnparsable,
    PoTokenRequired,
)


@dataclass
class FetchedTranscriptSnippet:
    text: str
    start: float
    """
    The timestamp at which this transcript snippet appears on screen in seconds.
    """
    duration: float
    """
    The duration of how long the snippet in seconds. Be aware that this is not the 
    duration of the transcribed speech, but how long the snippet stays on screen.
    Therefore, there can be overlaps between snippets!
    """


@dataclass
class FetchedTranscript:
    """
    Represents a fetched transcript. This object is iterable, which allows you to
    iterate over the transcript snippets.
    """

    snippets: List[FetchedTranscriptSnippet]
    video_id: str
    language: str
    language_code: str
    is_generated: bool

    def __iter__(self) -> Iterator[FetchedTranscriptSnippet]:
        return iter(self.snippets)

    def __getitem__(self, index) -> FetchedTranscriptSnippet:
        return self.snippets[index]

    def __len__(self) -> int:
        return len(self.snippets)

    def to_raw_data(self) -> List[Dict]:
        return [asdict(snippet) for snippet in self]


@dataclass
class _TranslationLanguage:
    language: str
    language_code: str


class _PlayabilityStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"
    LOGIN_REQUIRED = "LOGIN_REQUIRED"


class _PlayabilityFailedReason(str, Enum):
    BOT_DETECTED = "Sign in to confirm you’re not a bot"
    AGE_RESTRICTED = "This video may be inappropriate for some users."
    VIDEO_UNAVAILABLE = "This video is unavailable"


def _raise_http_errors(response: Response, video_id: str) -> Response:
    try:
        if response.status_code == 429:
            raise IpBlocked(video_id)
        response.raise_for_status()
        return response
    except HTTPError as error:
        raise YouTubeRequestFailed(video_id, error)


class Transcript:
    def __init__(
        self,
        http_client: Session,
        video_id: str,
        url: str,
        language: str,
        language_code: str,
        is_generated: bool,
        translation_languages: List[_TranslationLanguage],
    ):
        """
        You probably don't want to initialize this directly. Usually you'll access Transcript objects using a
        TranscriptList.
        """
        self._http_client = http_client
        self.video_id = video_id
        self._url = url
        self.language = language
        self.language_code = language_code
        self.is_generated = is_generated
        self.translation_languages = translation_languages
        self._translation_languages_dict = {
            translation_language.language_code: translation_language.language
            for translation_language in translation_languages
        }

    def fetch(self, preserve_formatting: bool = False) -> FetchedTranscript:
        """
        Loads the actual transcript data.
        :param preserve_formatting: whether to keep select HTML text formatting
        """
        if "&exp=xpe" in self._url:
            raise PoTokenRequired(self.video_id)
        response = self._http_client.get(self._url)
        snippets = _TranscriptParser(preserve_formatting=preserve_formatting).parse(
            _raise_http_errors(response, self.video_id).text,
        )
        return FetchedTranscript(
            snippets=snippets,
            video_id=self.video_id,
            language=self.language,
            language_code=self.language_code,
            is_generated=self.is_generated,
        )

    def __str__(self) -> str:
        return '{language_code} ("{language}"){translation_description}'.format(
            language=self.language,
            language_code=self.language_code,
            translation_description="[TRANSLATABLE]" if self.is_translatable else "",
        )

    @property
    def is_translatable(self) -> bool:
        return len(self.translation_languages) > 0

    def translate(self, language_code: str) -> "Transcript":
        if not self.is_translatable:
            raise NotTranslatable(self.video_id)

        if language_code not in self._translation_languages_dict:
            raise TranslationLanguageNotAvailable(self.video_id)

        return Transcript(
            self._http_client,
            self.video_id,
            "{url}&tlang={language_code}".format(
                url=self._url, language_code=language_code
            ),
            self._translation_languages_dict[language_code],
            language_code,
            True,
            [],
        )


class TranscriptList:
    """
    This object represents a list of transcripts. It can be iterated over to list all transcripts which are available
    for a given YouTube video. Also, it provides functionality to search for a transcript in a given language.
    """

    def __init__(
        self,
        video_id: str,
        manually_created_transcripts: Dict[str, Transcript],
        generated_transcripts: Dict[str, Transcript],
        translation_languages: List[_TranslationLanguage],
    ):
        """
        The constructor is only for internal use. Use the static build method instead.

        :param video_id: the id of the video this TranscriptList is for
        :param manually_created_transcripts: dict mapping language codes to the manually created transcripts
        :param generated_transcripts: dict mapping language codes to the generated transcripts
        :param translation_languages: list of languages which can be used for translatable languages
        """
        self.video_id = video_id
        self._manually_created_transcripts = manually_created_transcripts
        self._generated_transcripts = generated_transcripts
        self._translation_languages = translation_languages

    @staticmethod
    def build(
        http_client: Session, video_id: str, captions_json: Dict
    ) -> "TranscriptList":
        """
        Factory method for TranscriptList.

        :param http_client: http client which is used to make the transcript retrieving http calls
        :param video_id: the id of the video this TranscriptList is for
        :param captions_json: the JSON parsed from the YouTube pages static HTML
        :return: the created TranscriptList
        """
        translation_languages = [
            _TranslationLanguage(
                language=translation_language["languageName"]["runs"][0]["text"],
                language_code=translation_language["languageCode"],
            )
            for translation_language in captions_json.get("translationLanguages", [])
        ]

        manually_created_transcripts = {}
        generated_transcripts = {}

        for caption in captions_json["captionTracks"]:
            if caption.get("kind", "") == "asr":
                transcript_dict = generated_transcripts
            else:
                transcript_dict = manually_created_transcripts

            transcript_dict[caption["languageCode"]] = Transcript(
                http_client,
                video_id,
                caption["baseUrl"].replace("&fmt=srv3", ""),
                caption["name"]["runs"][0]["text"],
                caption["languageCode"],
                caption.get("kind", "") == "asr",
                translation_languages if caption.get("isTranslatable", False) else [],
            )

        return TranscriptList(
            video_id,
            manually_created_transcripts,
            generated_transcripts,
            translation_languages,
        )

    def __iter__(self) -> Iterator[Transcript]:
        return chain(
            self._manually_created_transcripts.values(),
            self._generated_transcripts.values(),
        )

    def find_transcript(self, language_codes: Iterable[str]) -> Transcript:
        """
        Finds a transcript for a given language code. Manually created transcripts are returned first and only if none
        are found, generated transcripts are used. If you only want generated transcripts use
        `find_manually_created_transcript` instead.

        :param language_codes: A list of language codes in a descending priority. For example, if this is set to
        ['de', 'en'] it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if
        it fails to do so.
        :return: the found Transcript
        """
        return self._find_transcript(
            language_codes,
            [self._manually_created_transcripts, self._generated_transcripts],
        )

    def find_generated_transcript(self, language_codes: Iterable[str]) -> Transcript:
        """
        Finds an automatically generated transcript for a given language code.

        :param language_codes: A list of language codes in a descending priority. For example, if this is set to
        ['de', 'en'] it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if
        it fails to do so.
        :return: the found Transcript
        """
        return self._find_transcript(language_codes, [self._generated_transcripts])

    def find_manually_created_transcript(
        self, language_codes: Iterable[str]
    ) -> Transcript:
        """
        Finds a manually created transcript for a given language code.

        :param language_codes: A list of language codes in a descending priority. For example, if this is set to
        ['de', 'en'] it will first try to fetch the german transcript (de) and then fetch the english transcript (en) if
        it fails to do so.
        :return: the found Transcript
        """
        return self._find_transcript(
            language_codes, [self._manually_created_transcripts]
        )

    def _find_transcript(
        self,
        language_codes: Iterable[str],
        transcript_dicts: List[Dict[str, Transcript]],
    ) -> Transcript:
        for language_code in language_codes:
            for transcript_dict in transcript_dicts:
                if language_code in transcript_dict:
                    return transcript_dict[language_code]

        raise NoTranscriptFound(self.video_id, language_codes, self)

    def __str__(self) -> str:
        return (
            "For this video ({video_id}) transcripts are available in the following languages:\n\n"
            "(MANUALLY CREATED)\n"
            "{available_manually_created_transcript_languages}\n\n"
            "(GENERATED)\n"
            "{available_generated_transcripts}\n\n"
            "(TRANSLATION LANGUAGES)\n"
            "{available_translation_languages}"
        ).format(
            video_id=self.video_id,
            available_manually_created_transcript_languages=self._get_language_description(
                str(transcript)
                for transcript in self._manually_created_transcripts.values()
            ),
            available_generated_transcripts=self._get_language_description(
                str(transcript) for transcript in self._generated_transcripts.values()
            ),
            available_translation_languages=self._get_language_description(
                '{language_code} ("{language}")'.format(
                    language=translation_language.language,
                    language_code=translation_language.language_code,
                )
                for translation_language in self._translation_languages
            ),
        )

    def _get_language_description(self, transcript_strings: Iterable[str]) -> str:
        description = "\n".join(
            " - {transcript}".format(transcript=transcript)
            for transcript in transcript_strings
        )
        return description if description else "None"


class TranscriptListFetcher:
    def __init__(self, http_client: Session, proxy_config: Optional[ProxyConfig]):
        self._http_client = http_client
        self._proxy_config = proxy_config

    def fetch(self, video_id: str) -> TranscriptList:
        return TranscriptList.build(
            self._http_client,
            video_id,
            self._fetch_captions_json(video_id),
        )

    def _fetch_captions_json(self, video_id: str, try_number: int = 0) -> Dict:
        try:
            html = self._fetch_video_html(video_id)
            api_key = self._extract_innertube_api_key(html, video_id)
            innertube_data = self._fetch_innertube_data(video_id, api_key)
            return self._extract_captions_json(innertube_data, video_id)
        except RequestBlocked as exception:
            retries = (
                0
                if self._proxy_config is None
                else self._proxy_config.retries_when_blocked
            )
            if try_number + 1 < retries:
                return self._fetch_captions_json(video_id, try_number=try_number + 1)
            raise exception.with_proxy_config(self._proxy_config)

    def _extract_innertube_api_key(self, html: str, video_id: str) -> str:
        pattern = r'"INNERTUBE_API_KEY":\s*"([a-zA-Z0-9_-]+)"'
        match = re.search(pattern, html)
        if match and len(match.groups()) == 1:
            return match.group(1)
        if 'class="g-recaptcha"' in html:
            raise IpBlocked(video_id)
        raise YouTubeDataUnparsable(video_id)  # pragma: no cover

    def _extract_captions_json(self, innertube_data: Dict, video_id: str) -> Dict:
        self._assert_playability(innertube_data.get("playabilityStatus"), video_id)

        captions_json = innertube_data.get("captions", {}).get(
            "playerCaptionsTracklistRenderer"
        )
        if captions_json is None or "captionTracks" not in captions_json:
            raise TranscriptsDisabled(video_id)

        return captions_json

    def _assert_playability(self, playability_status_data: Dict, video_id: str) -> None:
        playability_status = playability_status_data.get("status")
        if (
            playability_status != _PlayabilityStatus.OK.value
            and playability_status is not None
        ):
            reason = playability_status_data.get("reason")
            if playability_status == _PlayabilityStatus.LOGIN_REQUIRED.value:
                if reason == _PlayabilityFailedReason.BOT_DETECTED.value:
                    raise RequestBlocked(video_id)
                if reason == _PlayabilityFailedReason.AGE_RESTRICTED.value:
                    raise AgeRestricted(video_id)
            if (
                playability_status == _PlayabilityStatus.ERROR.value
                and reason == _PlayabilityFailedReason.VIDEO_UNAVAILABLE.value
            ):
                if video_id.startswith("http://") or video_id.startswith("https://"):
                    raise InvalidVideoId(video_id)
                raise VideoUnavailable(video_id)
            subreasons = (
                playability_status_data.get("errorScreen", {})
                .get("playerErrorMessageRenderer", {})
                .get("subreason", {})
                .get("runs", [])
            )
            raise VideoUnplayable(
                video_id, reason, [run.get("text", "") for run in subreasons]
            )

    def _create_consent_cookie(self, html: str, video_id: str) -> None:
        match = re.search('name="v" value="(.*?)"', html)
        if match is None:
            raise FailedToCreateConsentCookie(video_id)
        self._http_client.cookies.set(
            "CONSENT", "YES+" + match.group(1), domain=".youtube.com"
        )

    def _fetch_video_html(self, video_id: str) -> str:
        html = self._fetch_html(video_id)
        if 'action="https://consent.youtube.com/s"' in html:
            self._create_consent_cookie(html, video_id)
            html = self._fetch_html(video_id)
            if 'action="https://consent.youtube.com/s"' in html:
                raise FailedToCreateConsentCookie(video_id)
        return html

    def _fetch_html(self, video_id: str) -> str:
        response = self._http_client.get(WATCH_URL.format(video_id=video_id))
        return unescape(_raise_http_errors(response, video_id).text)

    def _fetch_innertube_data(self, video_id: str, api_key: str) -> Dict:
        response = self._http_client.post(
            INNERTUBE_API_URL.format(api_key=api_key),
            json={
                "context": INNERTUBE_CONTEXT,
                "videoId": video_id,
            },
        )
        data = _raise_http_errors(response, video_id).json()
        return data


class _TranscriptParser:
    _FORMATTING_TAGS = [
        "strong",  # important
        "em",  # emphasized
        "b",  # bold
        "i",  # italic
        "mark",  # marked
        "small",  # smaller
        "del",  # deleted
        "ins",  # inserted
        "sub",  # subscript
        "sup",  # superscript
    ]

    def __init__(self, preserve_formatting: bool = False):
        self._html_regex = self._get_html_regex(preserve_formatting)

    def _get_html_regex(self, preserve_formatting: bool) -> Pattern[str]:
        if preserve_formatting:
            formats_regex = "|".join(self._FORMATTING_TAGS)
            formats_regex = r"<\/?(?!\/?(" + formats_regex + r")\b).*?\b>"
            html_regex = re.compile(formats_regex, re.IGNORECASE)
        else:
            html_regex = re.compile(r"<[^>]*>", re.IGNORECASE)
        return html_regex

    def parse(self, raw_data: str) -> List[FetchedTranscriptSnippet]:
        return [
            FetchedTranscriptSnippet(
                text=re.sub(self._html_regex, "", unescape(xml_element.text)),
                start=float(xml_element.attrib["start"]),
                duration=float(xml_element.attrib.get("dur", "0.0")),
            )
            for xml_element in ElementTree.fromstring(raw_data)
            if xml_element.text is not None
        ]

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "warkingtime",
  "path": "src/extract.py",
  "ref": "refs/heads/main",
  "repo": "channel-transcript-archiver"
}
```

**Output:**
```
successfully downloaded text file (SHA: 91afd0b0d6ea38bacad6487b2c724f4fe06db37e)

import argparse
import logging
import os
import re
import subprocess
import sys
from pathlib import Path

if sys.version_info >= (3, 11):
    import tomllib
else:
    try:
        import tomli as tomllib
    except ImportError:
        tomllib = None

from .browser import get_cookie_args
from .clean_transcripts import run_cleaner
from .format_and_summarize import (
    format_json_files,
    generate_transcripts_list,
    get_video_map,
    summarize_playlists,
)
from .get_patreon_collections import download_patreon_collections
from .populate_archive import populate_archive
from .remove_duplicates import (
    find_cross_folder_duplicates,
    remove_intra_folder_duplicates,
)

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)


def sanitize_folder_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]", "_", name)


def extract_folder_name(url: str) -> str:
    """Extracts a default folder name from a YouTube or Patreon URL."""
    if "@" in url:
        return url.split("@")[-1].split("/")[0]
    elif "/channel/" in url:
        return url.split("/channel/")[-1].split("/")[0]
    elif "/c/" in url:
        return url.split("/c/")[-1].split("/")[0]
    elif "patreon.com" in url:
        # Handle Patreon URL patterns: https://www.patreon.com/c/SimoneAndMalcolmCollins/
        return url.rstrip("/").split("/")[-1]
    return "channel"


def get_channel_source(url: str) -> str:
    if "patreon.com" in url:
        return "patreon"
    return "youtube"


def resolve_unique_folder_name(proposed_name: str, url: str) -> str:
    """Resolves a unique folder name in the channels/ directory.

    If the proposed name exists and points to a different URL, it appends the source
    (e.g. ' (youtube)') and then numbers if needed.
    """
    base_dir = Path("channels")
    proposed_name = sanitize_folder_name(proposed_name)
    target_dir = base_dir / proposed_name

    def is_same_channel(path: Path, target_url: str) -> bool:
        readme_path = path / "README.md"
        if readme_path.exists():
            return target_url in readme_path.read_text()
        return False

    if not target_dir.exists() or is_same_channel(target_dir, url):
        return proposed_name

    # Collision! Try adding source
    source = get_channel_source(url)
    sourced_name = f"{proposed_name} ({source})"
    target_dir = base_dir / sourced_name

    if not target_dir.exists() or is_same_channel(target_dir, url):
        return sourced_name

    # Still colliding! Start adding numbers
    counter = 1
    while True:
        numbered_name = f"{sourced_name} {counter}"
        target_dir = base_dir / numbered_name
        if not target_dir.exists() or is_same_channel(target_dir, url):
            return numbered_name
        counter += 1


def rename_descriptions(channel_dir: Path) -> None:
    """Renames all .description files to .description.txt for better compatibility."""
    desc_files = list(channel_dir.glob("data/**/*.description"))
    if desc_files:
        log.info(f"Renaming {len(desc_files)} description files to .txt...")
        for f in desc_files:
            f.rename(f.with_suffix(".description.txt"))


def clean_title_whitespace(name: str) -> str:
    """Replaces all whitespace types with standard space and strips edges and spaces before dots."""
    # Replace all whitespace (including NBSP, tabs, etc.) with standard space
    name = re.sub(r"\s+", " ", name)
    # Remove spaces before dots
    name = re.sub(r" \.", ".", name)
    return name.strip()


def cleanup_trailing_whitespace(channel_dir: Path) -> None:
    """Trims trailing whitespace from all files and directories in the channel directory."""
    log.info(f"Trimming trailing whitespace in {channel_dir}...")
    # Use topdown=False to ensure we rename children before parents
    for root, dirs, files in os.walk(channel_dir, topdown=False):
        # Rename files
        for name in files:
            p = Path(root) / name
            new_name = name

            # Handle our specific multi-part extensions
            found_ext = False
            for ext in [".info.json", ".en.srt", ".en.txt", ".description.txt", ".description"]:
                if name.endswith(ext):
                    base = name[: -len(ext)]
                    new_name = clean_title_whitespace(base) + ext
                    found_ext = True
                    break

            if not found_ext:
                # Fallback for single extensions or no extension
                stem = clean_title_whitespace(p.stem)
                suffix = p.suffix
                new_name = stem + suffix

            if new_name != name:
                new_p = Path(root) / new_name
                if not new_p.exists():
                    log.info(f"Renaming file: '{name}' -> '{new_name}'")
                    p.rename(new_p)
                else:
                    log.warning(f"Could not rename '{name}' to '{new_name}': target exists")

        # Rename directories
        for name in dirs:
            p = Path(root) / name
            new_name = clean_title_whitespace(name)
            if new_name != name:
                new_p = Path(root) / new_name
                if not new_p.exists():
                    log.info(f"Renaming directory: '{name}' -> '{new_name}'")
                    p.rename(new_p)
                else:
                    log.warning(f"Could not rename directory '{name}' to '{new_name}': target exists")


def setup_channel_directory(channel_dir: Path, channel_url: str) -> None:
    """Sets up the channel directory with README.md and config.toml if they don't exist."""
    data_dir = channel_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    # Create README.md if it doesn't exist
    readme_path = channel_dir / "README.md"
    if not readme_path.exists():
        log.info(f"Creating README.md in {channel_dir}...")
        source_type = "Patreon" if "patreon.com" in channel_url else "YouTube"
        folder_name = channel_dir.name
        readme_content = f"""# 📺 {source_type} Archive: {folder_name}

This directory contains an automated archive of metadata, descriptions, and
transcripts for: {channel_url}

## 📂 Contents
- **data/**: Chronological folders for each post containing:
    - `.info.json`: Pruned metadata.
    - `.description.txt`: Original description.
    - `.en.srt`: Original subtitles.
    - `.en.txt`: Cleaned, speaker-tagged transcript.
- **playlists/**: Metadata for all playlists (if applicable).
- **archive.txt**: A record of all synced items to ensure incremental updates.
- **config.toml**: Heuristics used for speaker identification.
- **PLAYLISTS.md**: An index organized by playlist.
- **TRANSCRIPTS.md**: A chronological index of all available transcripts.

## 🔄 How to Update
To sync new content or re-process existing ones, use the [Channel Transcript Archiver](https://github.com/warkingtime/channel-transcript-archiver):

1. Install the tool.
2. Run the sync command from the project root:
   ```bash
   uv run channel-archiver sync "{channel_url}" "{folder_name}"
   ```

## 🛠️ Tooling
Generated by [warkingtime/channel-transcript-archiver](https://github.com/warkingtime/channel-transcript-archiver).
"""
        readme_path.write_text(readme_content)

    # Create default config.toml if it doesn't exist
    config_path = channel_dir / "config.toml"
    if not config_path.exists():
        log.info("Creating default config.toml...")
        config_content = f"""# Configuration for speaker identification and transcript processing
url = "{channel_url}"
uses_dual_speaker_heuristic = false

# Define speakers and identifying phrases
# The script looks for these strings (case-insensitive) to identify the speaker
speaker_a = "SPEAKER_1"
speaker_a_strings = ["hello speaker 2", "hi speaker 2"]

speaker_b = "SPEAKER_2"
speaker_b_strings = ["hello speaker 1", "hi speaker 1"]

# Pause detection threshold in seconds (default: 3.0)
# A new paragraph is started if the gap between segments exceeds this.
# pause_threshold = 3.0
"""
        config_path.write_text(config_content)


def finalize_channel_update(channel_dir: Path, force: bool = False) -> None:
    """Performs post-download tasks: renaming, deduplication, cleaning, and reporting."""
    # Rename descriptions to .txt
    rename_descriptions(channel_dir)

    # Trim trailing whitespace from filenames and directories
    cleanup_trailing_whitespace(channel_dir)

    # Deduplicate
    log.info("Deduplicating files...")
    remove_intra_folder_duplicates(str(channel_dir))
    find_cross_folder_duplicates(str(channel_dir))

    # Clean transcripts
    log.info("Cleaning transcripts...")
    run_cleaner(str(channel_dir), force=force)

    # Format and Summarize
    log.info("Updating reports and formatting JSON files...")
    format_json_files(str(channel_dir))
    v_map = get_video_map(str(channel_dir))
    summarize_playlists(v_map, str(channel_dir))
    generate_transcripts_list(v_map, str(channel_dir))


def sync_channel(
    channel_url: str,
    folder_name: str | None = None,
    force: bool = False,
    cookies_file: str | None = None,
    cookies_browser: str | None = None,
    use_cookies: bool = False,
    print_command: bool = False,
    include_comments: int | None = None,
) -> None:
    # Check if channel_url is actually a folder name
    potential_dir = Path("channels") / channel_url
    if not channel_url.startswith(("http://", "https://")) and potential_dir.is_dir():
        log.info(f"Detected folder name '{channel_url}', resolving URL...")
        folder_name = channel_url
        channel_dir = potential_dir
        found_url = None

        # 1. Try config.toml
        config_path = channel_dir / "config.toml"
        if config_path.exists() and tomllib:
            try:
                with open(config_path, "rb") as f:
                    config_data = tomllib.load(f)
                    found_url = config_data.get("url")
            except Exception:
                pass

        # 2. Try README.md fallback
        if not found_url:
            readme_path = channel_dir / "README.md"
            if readme_path.exists():
                text = readme_path.read_text()
                match = re.search(r"transcripts for: (https?://\S+)", text)
                if match:
                    found_url = match.group(1)

        if found_url:
            log.info(f"Resolved folder '{folder_name}' to URL: {found_url}")
            channel_url = found_url
        else:
            log.error(f"Could not find a URL for folder '{folder_name}'. Please provide the URL.")
            return

    if not folder_name:
        folder_name = extract_folder_name(channel_url)

    folder_name = resolve_unique_folder_name(folder_name, channel_url)
    channel_dir = Path("channels") / folder_name

    if not print_command:
        log.info(f"Syncing channel: {channel_url} into {channel_dir} (Force: {'on' if force else 'off'})")
        setup_channel_directory(channel_dir, channel_url)

        # Update archive.txt from existing files
        log.info("Updating archive.txt from local files...")
        populate_archive(str(channel_dir))

    cookie_args = get_cookie_args(
        cookies_file=cookies_file, cookies_from_browser=cookies_browser, use_cookies=use_cookies
    )

    # yt-dlp content sync
    if not print_command:
        log.info(f"Starting yt-dlp sync for {channel_url}...")
    
    yt_dlp_cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-description",
        "--write-info-json",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        "en.*",
        "--convert-subs",
        "srt",
        "--ignore-errors",
        "--ignore-no-formats-error",
        "--allow-unplayable-formats",
        "--remote-components",
        "ejs:github",
        "--output",
        f"{channel_dir}/data/%(upload_date)s - %(title)s/%(title)s.%(ext)s",
        "--sleep-requests",
        "1",
        "--sleep-interval",
        "1",
    ]

    import shutil
    if shutil.which("deno"):
        yt_dlp_cmd.extend(["--js-runtime", "deno"])
    elif shutil.which("node"):
        yt_dlp_cmd.extend(["--js-runtime", "node"])

    if not force:
        yt_dlp_cmd.extend(["--download-archive", str(channel_dir / "archive.txt")])

    if include_comments:
        yt_dlp_cmd.extend(["--write-comments", "--extractor-args", f"youtube:max-comments={include_comments}"])
    yt_dlp_cmd.extend(cookie_args)
    yt_dlp_cmd.append(channel_url)

    if print_command:
        import shlex

        print(f"\n[DRY RUN] Would execute: {shlex.join(yt_dlp_cmd)}")
    else:
        subprocess.run(yt_dlp_cmd)

    # yt-dlp playlist metadata (YouTube only for now)
    if ("youtube.com" in channel_url or "youtu.be" in channel_url) and not print_command:
        log.info("Extracting playlist metadata...")
        playlists_dir = channel_dir / "playlists"
        playlists_dir.mkdir(parents=True, exist_ok=True)
        playlist_cmd = [
            "yt-dlp",
            "--write-info-json",
            "--flat-playlist",
            "--allow-unplayable-formats",
            "--output",
            f"{channel_dir}/playlists/%(title)s.%(ext)s",
        ]
        playlist_cmd.extend(cookie_args)
        playlist_cmd.append(f"{channel_url}/playlists")

        subprocess.run(playlist_cmd)

        # Remove playlists directory if it's empty
        if playlists_dir.exists() and not any(playlists_dir.iterdir()):
            playlists_dir.rmdir()
    elif print_command and ("youtube.com" in channel_url or "youtu.be" in channel_url):
        import shlex

        playlist_cmd = [
            "yt-dlp",
            "--write-info-json",
            "--flat-playlist",
            "--allow-unplayable-formats",
            "--output",
            f"{channel_dir}/playlists/%(title)s.%(ext)s",
        ]
        playlist_cmd.extend(cookie_args)
        playlist_cmd.append(f"{channel_url}/playlists")
        print(f"[DRY RUN] Would execute: {shlex.join(playlist_cmd)}")
    elif "patreon.com" in channel_url and not print_command:
        log.info("Extracting Patreon collections metadata...")
        cookies_path = cookies_file or "cookies.txt"
        # If cookies_browser is provided, we might want to extract them first,
        # but for now we assume they are in cookies.txt or .browser handled by get_cookie_args
        # Actually, get_cookie_args returns yt-dlp arguments.
        # We need a path for the requests session.
        if cookies_file:
            path = cookies_file
        elif Path("cookies.txt").exists():
            path = "cookies.txt"
        else:
            path = "cookies.txt"  # Fallback
        
        download_patreon_collections(channel_url, channel_dir, cookies_path=path)
    else:
        log.info("Skipping playlist metadata extraction (non-YouTube/Patreon URL).")

    if not print_command:
        finalize_channel_update(channel_dir, force=force)
        log.info(f"Sync complete for {folder_name}!")


def download_video(
    video_url: str,
    folder_name: str | None = None,
    force: bool = False,
    cookies_file: str | None = None,
    cookies_browser: str | None = None,
    use_cookies: bool = False,
    print_command: bool = False,
    include_comments: int | None = None,
) -> None:
    cookie_args = get_cookie_args(
        cookies_file=cookies_file, cookies_from_browser=cookies_browser, use_cookies=use_cookies
    )

    if not folder_name:
        if not print_command:
            log.info(f"Detecting uploader for {video_url}...")
        try:
            cmd = [
                "yt-dlp",
                "--print",
                "uploader_url",
                "--ignore-errors",
                "--allow-unplayable-formats",
                video_url,
            ] + cookie_args
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            uploader_url = result.stdout.strip()
            folder_name = extract_folder_name(uploader_url)
        except Exception as e:
            log.warning(f"Could not detect uploader: {e}. Using 'downloads' folder.")
            folder_name = "downloads"

    folder_name = resolve_unique_folder_name(folder_name, video_url)
    channel_dir = Path("channels") / folder_name

    if not print_command:
        log.info(f"Downloading video: {video_url} into {channel_dir}")
        setup_channel_directory(channel_dir, video_url)

    # yt-dlp content download
    if not print_command:
        log.info(f"Starting yt-dlp download for {video_url}...")
    yt_dlp_cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-description",
        "--write-info-json",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        "en.*",
        "--convert-subs",
        "srt",
        "--ignore-errors",
        "--ignore-no-formats-error",
        "--no-playlist",
        "--allow-unplayable-formats",
        "--remote-components",
        "ejs:github",
        "--output",
        f"{channel_dir}/data/%(upload_date)s - %(title)s/%(title)s.%(ext)s",
    ]

    import shutil
    if shutil.which("deno"):
        yt_dlp_cmd.extend(["--js-runtime", "deno"])
    elif shutil.which("node"):
        yt_dlp_cmd.extend(["--js-runtime", "node"])

    if include_comments:
        yt_dlp_cmd.extend(["--write-comments", "--extractor-args", f"youtube:max-comments={include_comments}"])
    yt_dlp_cmd.extend(cookie_args)
    yt_dlp_cmd.append(video_url)

    if print_command:
        import shlex

        print(f"\n[DRY RUN] Would execute: {shlex.join(yt_dlp_cmd)}")
    else:
        subprocess.run(yt_dlp_cmd)

    if not print_command:
        finalize_channel_update(channel_dir, force=force)
        log.info(f"Download complete for {folder_name}!")


def main() -> None:
    parser = argparse.ArgumentParser(description="YouTube Channel Transcript Archiver")
    parser.add_argument("url", help="YouTube Channel URL")
    parser.add_argument("name", nargs="?", help="Folder name for the channel")
    parser.add_argument("--force", action="store_true", help="Force re-cleaning of transcripts")
    parser.add_argument("--cookies", help="Path to cookies.txt file")
    parser.add_argument("--cookies-from-browser", help="Browser to extract cookies from")

    args = parser.parse_args()

    sync_channel(
        args.url,
        folder_name=args.name,
        force=args.force,
        cookies_file=args.cookies,
        cookies_browser=args.cookies_from_browser,
    )


if __name__ == "__main__":
    main()

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "warkingtime",
  "path": "src/get_playlists.py",
  "ref": "refs/heads/main",
  "repo": "channel-transcript-archiver"
}
```

**Output:**
```
successfully downloaded text file (SHA: d4f86a5ddf77e2d0a5196207493a4d96aaecda1e)

import json
import os
import subprocess
from typing import Any

CHANNEL_URL = "https://www.youtube.com/@ExampleChannel/playlists"
OUTPUT_DIR = "playlists"


def get_playlist_data(channel_url: str = CHANNEL_URL, output_dir: str = OUTPUT_DIR) -> None:
    os.makedirs(output_dir, exist_ok=True)

    print("Fetching playlist list...")
    cmd = [
        "yt-dlp",
        "--get-id",
        "--flat-playlist",
        channel_url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    playlist_ids = result.stdout.strip().split("\n")

    for p_id in playlist_ids:
        if not p_id:
            continue
        url = f"https://www.youtube.com/playlist?list={p_id}"
        print(f"Fetching metadata for playlist: {p_id}")

        cmd_meta = [
            "yt-dlp",
            "--dump-single-json",
            "--flat-playlist",
            url,
        ]
        result_meta = subprocess.run(cmd_meta, capture_output=True, text=True, check=False)
        if result_meta.returncode == 0:
            try:
                data: dict[str, Any] = json.loads(result_meta.stdout)
                title = str(data.get("title", p_id)).strip()
                safe_title = "".join(c for c in title if c.isalnum() or c in (" ", ".", "_")).strip()
                output_path = os.path.join(output_dir, f"{safe_title}.info.json")
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                print(f"  Saved metadata for: {title}")
            except Exception as e:
                print(f"  Error parsing JSON for {p_id}: {e}")
        else:
            print(f"  Error fetching metadata for {p_id}")


if __name__ == "__main__":
    get_playlist_data()

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "dlovecreator-arch",
  "path": "src/metadata_extractor.py",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
successfully downloaded text file (SHA: 85fe3dd4aafbd286d994ec6b4239ab91888d1b26)

#!/usr/bin/env python3
"""Metadata extractor: Parse all .info.json files into canonical database.

Extracts:
- Guest names (from title/description heuristics)
- YouTube tags/categories
- View/like counts
- Deduplicates across channels
"""
import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_BASE = REPO_ROOT / "out"
DB_FILE = REPO_ROOT / "db" / "canonical.json"
DB_FILE.parent.mkdir(exist_ok=True)


def extract_guest(title: str, description: str = "") -> str | None:
    """Extract guest name from title/description using heuristics.
    
    Patterns:
    - "Title | Guest Name"
    - "Title with Guest Name [INTERVIEW]"
    - "Guest Name REVEALS..." (starts title)
    """
    # Pattern: Title | Guest
    match = re.search(r'\|\s*([A-Z][A-Za-z\s\.]+)(?:\s*\[|$)', title)
    if match:
        guest = match.group(1).strip()
        if guest and len(guest) > 2 and guest != "Emilio Ortiz" and guest != "Viviane Chauvet":
            return guest
    
    # Pattern: starts with Name REVEALS/SHOWS/TELLS/WARNS
    match = re.match(r'^([A-Z][A-Za-z\s]+?)\s+(REVEALS|SHOWS|TELLS|WARNS|DISCUSSES|EXPLAINS|SHARES|PREDICTS)', title)
    if match:
        guest = match.group(1).strip()
        if len(guest) > 2:
            return guest
    
    # Last resort: description first line
    if description:
        first_line = description.split('\n')[0]
        match = re.match(r'^([A-Z][A-Za-z\s]+)\s+(?:is|discusses|talks)', first_line)
        if match:
            return match.group(1).strip()
    
    return None


def extract_topics(tags: list, description: str, title: str) -> list:
    """Extract topic tags from YouTube tags + title keywords."""
    topics = set()
    
    if tags:
        # Filter out low-value tags
        for tag in tags[:8]:  # Top 8 tags only
            tag_lower = tag.lower()
            if tag_lower not in ['interview', 'podcast', 'youtube', '2024', '2025', 'new']:
                topics.add(tag_lower)
    
    # Extract from title: ALL_CAPS words are usually topics
    for word in title.split():
        if word.isupper() and len(word) > 2:
            topics.add(word.lower())
    
    return sorted(list(topics))


def build_canonical_db():
    """Scan all .info.json files and build canonical database."""
    
    db = {
        "version": "1.0",
        "generated": datetime.now().isoformat(),
        "videos": [],
        "channels": defaultdict(int),
        "duplicates": defaultdict(list),
    }
    
    video_by_id = {}  # Track duplicates
    
    for info_path in sorted(OUT_BASE.rglob("*.info.json")):
        # Skip quarantined channel metadata folders. These hold @handle/UCxxx
        # channel-listing metadata, not video records, and must never become
        # canonical channels.
        if "_channel_meta" in info_path.parts:
            continue

        try:
            data = json.loads(info_path.read_text(errors="ignore"))
        except:
            continue
        
        # Skip channel metadata and malformed IDs. Real YouTube video IDs are
        # exactly 11 chars. Channel IDs are usually UC + 22 chars.
        video_id = (data.get("id") or "").strip()
        if not video_id or video_id.startswith("UC") or len(video_id) != 11:
            continue
        
        # Build canonical record
        # Use the folder name as the canonical channel (humans curate these for clean naming).
        # Fall back to YT's `channel` field if the folder is unusual.
        # The folder layout is out/<channel>/<video_id>/<file>.info.json,
        # so info_path.parent.parent.name is the channel folder name.
        folder_channel = info_path.parent.parent.name if info_path.parent.parent != OUT_BASE else None
        yt_channel = (data.get("channel") or "").strip()
        yt_uploader = (data.get("uploader") or "").strip()
        canonical_channel = (folder_channel or yt_channel or yt_uploader or "Unknown").strip()

        record = {
            "id": video_id,
            "title": data.get("title", "Untitled"),
            "channel": canonical_channel,
            "channel_id": data.get("channel_id", ""),
            "uploader": yt_uploader or "Unknown",
            "date": data.get("upload_date", ""),
            "duration": data.get("duration", 0),
            "views": data.get("view_count", 0),
            "likes": data.get("like_count", 0),
            "url": f"https://youtu.be/{video_id}",
            "description": (data.get("description") or "")[:300],
            "category": data.get("categories", [None])[0] if data.get("categories") else None,
            "guest": extract_guest(data.get("title", ""), data.get("description", "")),
            "tags": extract_topics(data.get("tags", []), data.get("description", ""), data.get("title", "")),
            "sources": [str(info_path.parent.name)],
        }
        
        db["channels"][record["channel"]] += 1
        
        # Dedup: if we've seen this video_id before, link it
        if video_id in video_by_id:
            db["duplicates"][video_id].append(record["sources"][0])
            existing_idx = video_by_id[video_id]
            db["videos"][existing_idx]["sources"].extend(record["sources"])
        else:
            video_by_id[video_id] = len(db["videos"])
            db["videos"].append(record)
    
    # Convert defaultdicts to regular dicts for JSON
    db["channels"] = dict(db["channels"])
    db["duplicates"] = dict(db["duplicates"])
    
    # Write canonical database
    DB_FILE.write_text(json.dumps(db, indent=2))
    
    print(f"✓ Canonical DB created: {DB_FILE}")
    print(f"  - Total videos: {len(db['videos'])}")
    print(f"  - Channels: {len(db['channels'])}")
    print(f"  - Duplicates: {len(db['duplicates'])}")
    print(f"  - Videos with guests: {sum(1 for v in db['videos'] if v['guest'])}")
    
    return db


if __name__ == "__main__":
    db = build_canonical_db()

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "dlovecreator-arch",
  "path": "src/markdown_generator.py",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
successfully downloaded text file (SHA: 805b113fe6e12454c24253252465b5c5019f7148)

#!/usr/bin/env python3
"""Generate Markdown transcripts with optimized YAML frontmatter.

Improvements:
- Full AI-agent-ready schema (token_count, reading_time, etc)
- Slug field for Obsidian safe filtering
- Word count for transcript length tracking
- Confidence scores for guest extraction quality
- Both .md and .txt outputs (Obsidian compatibility)
- Proper string formatting for Notion API compatibility
"""
import json
import os
import re
import sys
import math
import argparse
import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_FILE = REPO_ROOT / "db" / "canonical.json"
OUT_BASE = REPO_ROOT / "out"
MARKDOWN_BASE = REPO_ROOT / "markdown"
MARKDOWN_BASE.mkdir(exist_ok=True)

# Approximate token count (1 token ≈ 4 characters, conservative estimate)
def estimate_tokens(text: str) -> int:
    """Estimate token count for Claude/GPT consumption."""
    return max(1, len(text) // 4)

def estimate_reading_time(text: str) -> int:
    """Estimate reading time in minutes (avg 200 words/minute)."""
    word_count = len(text.split())
    return max(1, word_count // 200)

def extract_guest_with_confidence(title: str, description: str = "") -> tuple:
    """Extract guest name and return (name, confidence_score)."""
    confidence = 0.0
    
    # Pattern 1: "Title | Guest Name" (highest confidence)
    match = re.search(r'\|\s*([A-Z][A-Za-z\s\.]+)(?:\s*\[|$)', title)
    if match:
        guest = match.group(1).strip()
        if guest and len(guest) > 2 and guest not in ["Emilio Ortiz", "Viviane Chauvet", "The Alchemist"]:
            return (guest, 0.95)
    
    # Pattern 2: "Name REVEALS/SHOWS/etc" (high confidence)
    match = re.match(r'^([A-Z][A-Za-z\s]+?)\s+(REVEALS|SHOWS|TELLS|WARNS|DISCUSSES|EXPLAINS|SHARES|PREDICTS)', title)
    if match:
        guest = match.group(1).strip()
        if len(guest) > 2:
            return (guest, 0.85)
    
    # Pattern 3: Description first line (medium confidence)
    if description:
        first_line = description.split('\n')[0]
        match = re.match(r'^([A-Z][A-Za-z\s]+)\s+(?:is|discusses|talks)', first_line)
        if match:
            return (match.group(1).strip(), 0.65)
    
    return (None, 0.0)

def clean_vtt_text(vtt_path: Path) -> str:
    """Extract clean text from VTT caption file."""
    lines = vtt_path.read_text(errors="ignore").splitlines()
    blocks = []
    current_block = []
    
    for line in lines:
        line = line.strip()
        
        # Skip headers, timestamps, cue IDs
        if line in {"WEBVTT", "Kind: captions", "Language: en"} or line.startswith("NOTE") or line.startswith("STYLE"):
            continue
        if "-->" in line or re.match(r"^\d{2}:\d{2}:\d{2}\.\d{3}$", line):
            continue
        if re.fullmatch(r"\d+", line):
            continue
        
        if not line:
            if current_block:
                blocks.append(" ".join(current_block))
                current_block = []
        else:
            # Clean HTML tags and markers
            line = re.sub(r"<\d{2}:\d{2}:\d{2}\.\d{3}>", "", line)
            line = re.sub(r"<[^>]+>", "", line)
            line = line.replace("[music]", "").replace("[Applause]", "").replace("[Music]", "")
            line = line.strip()
            if line:
                current_block.append(line)
    
    if current_block:
        blocks.append(" ".join(current_block))
    
    # Remove near-duplicates (YouTube progressive captions)
    cleaned = []
    for block in blocks:
        if cleaned and len(block) > 0:
            if similarity(block, cleaned[-1]) > 0.8:
                continue
            if block in cleaned[-1]:
                continue
        cleaned.append(block)
    
    final = "\n\n".join(cleaned)
    final = re.sub(r"\s+", " ", final)
    
    return final.strip()

def similarity(a: str, b: str) -> float:
    """Simple similarity check (0-1)."""
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio()

def slugify(text: str) -> str:
    """Create safe slug for Obsidian filename."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def generate_markdown(record: dict, transcript_text: str) -> str:
    """Generate Markdown with optimized YAML frontmatter."""
    
    # Parse date
    upload_date = record.get("date", "")
    if len(upload_date) == 8:
        date_obj = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
    else:
        date_obj = upload_date or "1970-01-01"
    
    # Guest extraction with confidence
    guest, confidence = extract_guest_with_confidence(
        record.get("title", ""),
        record.get("description", "")
    )
    
    # Calculate metrics
    word_count = len(transcript_text.split())
    token_count = estimate_tokens(transcript_text)
    reading_time = estimate_reading_time(transcript_text)
    slug = slugify(record["title"])
    generated_marker = record.get("captured_date") or record.get("date") or "unknown"
    
    # Format sources as comma-separated (Notion compatible)
    sources_str = ", ".join(record.get("sources", []))
    
    # Format tags as comma-separated
    tags_str = ", ".join(record.get("tags", []))
    
    # Build YAML frontmatter
    frontmatter = f"""---
id: {record['id']}
title: "{record['title'].replace('"', '\\"')}"
slug: {slug}
guest: "{guest if guest else ""}"
guest_confidence: {confidence:.2f}
channel: {record['channel']}
uploader: {record['uploader']}
date: {date_obj}
duration_sec: {record['duration']}
views: {record['views']}
likes: {record['likes']}
url: {record['url']}
category: {record.get("category") or "Uncategorized"}
tags: [{tags_str}]
description: "{(record.get("description", "").replace('"', '\\"')[:200])}"
word_count: {word_count}
token_count: {token_count}
reading_time_min: {reading_time}
language: en
transcript_complete: {len(transcript_text) > 100}
sources: {sources_str}
generated: {generated_marker}
---
"""
    
    # Build content
    title = record['title']
    guest_line = f" | {guest}" if guest else ""
    
    content = f"""# {title}{guest_line}

**Channel**: {record['channel']}  
**Published**: {date_obj}  
**Guest**: {guest if guest else "N/A"}  
**Duration**: {record['duration']} seconds ({record['duration']//60} min)  
**Views**: {record['views']:,} | **Likes**: {record['likes']:,}  
**Link**: {record['url']}

---

## Transcript

{transcript_text}

---

*Automatically extracted from YouTube captions by YouTube Transcript Exporter.*
"""
    
    return frontmatter + "\n" + content

def build_video_folder_index() -> dict[str, Path]:
    """Build O(1) lookup from video_id -> out/<channel>/<video_id> folder.

    The old implementation did `OUT_BASE.glob(f"*/{video_id}")` once per
    record. On a 29k-video corpus that repeatedly scans the same directories
    and can take 10+ minutes. This index walks out/ once and makes markdown
    generation scale linearly.
    """
    index: dict[str, Path] = {}
    for folder in OUT_BASE.glob("*/*"):
        if not folder.is_dir() or folder.name == "_channel_meta":
            continue
        # Real YouTube video IDs are 11 chars. Skip playlist/channel meta dirs.
        if len(folder.name) != 11 or folder.name.startswith("UC"):
            continue
        index.setdefault(folder.name, folder)
    return index


def process_all_transcripts(channels: set[str] | None = None, missing_only: bool = False):
    """Generate Markdown for all videos in canonical DB.

    IMPORTANT: This is incremental by default.
    Historically this script wiped the entire markdown/ vault on each run.
    That was destructive, slow, and caused the "all my markdown disappeared"
    incident when a run was interrupted.

    Use --clean if you explicitly want to delete and regenerate everything.
    """
    
    # Load canonical DB
    try:
        db = json.loads(DB_FILE.read_text())
    except FileNotFoundError:
        print(f"Error: {DB_FILE} not found. Run metadata_extractor.py first.")
        return
    
    videos = db.get("videos", [])

    if channels:
        videos = [v for v in videos if v.get("channel") in channels]

    if missing_only:
        md_channels = {p.name for p in MARKDOWN_BASE.iterdir() if p.is_dir()} if MARKDOWN_BASE.exists() else set()
        videos = [v for v in videos if v.get("channel") not in md_channels]

    print(f"Processing {len(videos)} videos...")
    if channels:
        print(f"  Channel filter: {', '.join(sorted(channels))}")
    if missing_only:
        print("  Mode: missing markdown channel folders only")

    # Non-destructive by default. We never wipe markdown/ during normal runs.
    MARKDOWN_BASE.mkdir(exist_ok=True)

    stats = {
        "success": 0,
        "no_transcript": 0,
        "error": 0,
    }

    print("Building video folder index...")
    folder_index = build_video_folder_index()
    print(f"  Indexed {len(folder_index)} video folders")

    for i, record in enumerate(videos, 1):
        video_id = record['id']

        # Find transcript file by video_id using the O(1) folder index.
        transcript_text = None
        indexed_folder = folder_index.get(video_id)
        candidate_folders = [indexed_folder] if indexed_folder else []
        actual_channel_folder = None  # Track which out/ folder it was in
        
        for folder in candidate_folders:
            if not folder.is_dir():
                continue
            # Look for canonical VTT file: "<title> [<id>].en.vtt"
            vtt_files = [f for f in folder.glob("*.en.vtt") if f"[{video_id}]" in f.name]
            if not vtt_files:
                vtt_files = list(folder.glob("*.en.vtt"))
            if vtt_files:
                try:
                    transcript_text = clean_vtt_text(vtt_files[0])
                    # Also write transcript.en.txt back to the source folder
                    # so each video folder has consistent contents.
                    (folder / "transcript.en.txt").write_text(transcript_text, encoding='utf-8')
                    # Remember the actual channel folder name from out/
                    actual_channel_folder = folder.parent.name
                    break
                except Exception as e:
                    print(f"  ! Error reading {vtt_files[0]}: {e}")
                    stats["error"] += 1

        if not transcript_text:
            stats["no_transcript"] += 1
            continue

        # Generate Markdown
        md_content = generate_markdown(record, transcript_text)

        # Create channel folder structure using the ACTUAL name from out/
        # This ensures markdown/ mirrors out/ exactly (avoiding pipe/slash normalization issues)
        if actual_channel_folder:
            channel_dir = MARKDOWN_BASE / actual_channel_folder
        else:
            channel_dir = MARKDOWN_BASE / safe_channel_dir(record.get('channel', 'Unknown'))
        channel_dir.mkdir(parents=True, exist_ok=True)

        # Stable, filesystem-safe filename. Never use raw title.
        md_file = channel_dir / safe_markdown_filename(record.get('title', ''), video_id)

        # Write only if changed (saves time + avoids churn)
        try:
            new_hash = sha256_text(md_content)
            if md_file.exists():
                old_hash = sha256_text(md_file.read_text(encoding='utf-8', errors='ignore'))
                if old_hash == new_hash:
                    # No change.
                    pass
                else:
                    md_file.write_text(md_content, encoding='utf-8')
            else:
                md_file.write_text(md_content, encoding='utf-8')
        except Exception as e:
            print(f"  ! Error writing {md_file}: {e}")
            stats["error"] += 1
            continue

        if (i % 100) == 0:
            print(f"  ✓ {i}/{len(videos)} ({stats['success']} success)")

        stats["success"] += 1
    
    print(f"\n✓ Markdown generation complete:")
    print(f"  - Success: {stats['success']}")
    print(f"  - No transcript: {stats['no_transcript']}")
    print(f"  - Errors: {stats['error']}")
    print(f"  - Output: {MARKDOWN_BASE}")
    print(f"  - Files: {stats['success']} .md files")

def sanitize_filename(name: str) -> str:
    """Make string safe for filename."""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name)
    return name[:80]

def safe_channel_dir(channel: str) -> str:
    """Channel folder name MUST match out/ folder exactly (with spaces).

    Per NAMING_CONVENTION.md: markdown/Channel Name/ must equal out/Channel Name/.
    Only strip filesystem-illegal characters; preserve spaces.
    """
    s = (channel or "Unknown").strip()
    # Strip only truly illegal filesystem characters (no slash mangling, keep spaces)
    s = re.sub(r'[<>:"/\\?*]', '', s)
    # Collapse multiple spaces
    s = re.sub(r"\s+", " ", s).strip()
    return s[:120] or "Unknown"


def safe_markdown_filename(title: str, video_id: str) -> str:
    """Stable markdown filename. Avoids slashes/emojis and long paths."""
    base = slugify(title)[:80] or "untitled"
    return f"{base}_[{video_id}].md"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Generate markdown transcripts (incremental by default).")
    parser.add_argument("--clean", action="store_true", help="Delete markdown channel folders before regenerating (dangerous)")
    parser.add_argument("--channel", action="append", help="Only generate markdown for this exact channel name (repeatable)")
    parser.add_argument("--missing-only", action="store_true", help="Only generate channels that do not yet have markdown folders")
    args = parser.parse_args()

    # Single-instance lock: prevent multiple concurrent runs that race
    # and recreate folders the user just deleted.
    import fcntl
    lock_path = REPO_ROOT / ".markdown_generator.lock"
    lock_file = open(lock_path, "w")
    try:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print("❌ Another markdown_generator.py is already running. Exiting.")
        print(f"   (Lock file: {lock_path})")
        sys.exit(2)
    lock_file.write(str(os.getpid()))
    lock_file.flush()

    if args.clean:
        import shutil
        for child in MARKDOWN_BASE.iterdir():
            if child.is_dir():
                shutil.rmtree(child)

    process_all_transcripts(channels=set(args.channel or []), missing_only=args.missing_only)


if __name__ == "__main__":
    main()

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "xBartM",
  "path": "scripts/update_videos.sh",
  "ref": "refs/heads/master",
  "repo": "YouTube-Comment-Scraper"
}
```

**Output:**
```
successfully downloaded text file (SHA: a7cdbfe67862e6c0c622f0d29844904f5e043112)

#!/bin/sh
# this script adds vid URLs to ytkp.video
# running this script will:
# 1. get the channel URL which has the lowest scrape_date, but older than 30 (?) days and store it in a temp file
# 2. run yt-dlp with config dl-urls.conf to obtain a list of all videos on the channel and playlists
# 3. sort and remove duplicates from the list of videos
# 4. insert into database; on conflict do nothing (if there is a duplicate of the video)
# 5. update scrape_date in channel table
# 6. update archival vid_urls.txt file

# check if YTKP_DIR is set
if [ -z "${YTKP_DIR}" ] ; then
    echo "${0##*/}: YTKP_DIR is not set."
    exit 1
fi

# get the top channel URL from the channel table
db_channel=$( \
  psql \
    --dbname=postgres \
    --tuples-only \
    --no-align \
    --command="SELECT channel_url FROM ytkp.channel WHERE scrape_date < NOW() - INTERVAL '7 days' ORDER BY scrape_date ASC, insert_date ASC LIMIT 1;"
)

# check if there is work to do
if [ -z "${db_channel}" ] ; then
    echo "${0##*/}: no work to do. exiting"
    exit 1
fi

# run yt-dlp to save URLs of all videos from the channel
yt-dlp \
  --config-locations ${YTKP_DIR}/configs/dl-urls.conf \
  --print-to-file url ${YTKP_DIR}/archive/temp/video_urls.txt \
  "${db_channel}"

# run yt-dlp to save URLs of all playlists from the channel
yt-dlp \
  --config-locations ${YTKP_DIR}/configs/dl-urls.conf \
  --print-to-file url ${YTKP_DIR}/archive/temp/playlist_urls.txt \
  "${db_channel}/playlists"

# run yt-dlp to expand playlists into a list of video URLs; this will append all URLs to the specified file
yt-dlp \
  --config-locations ${YTKP_DIR}/configs/dl-urls.conf \
  --print-to-file url ${YTKP_DIR}/archive/temp/video_urls.txt \
  --batch-file ${YTKP_DIR}/archive/temp/playlist_urls.txt

# check if yt-dlp wrote anything
if [ ! -s ${YTKP_DIR}/archive/temp/video_urls.txt ]; then
    echo "${0##*/}: might\'ve been banned by YT. exiting"
    exit 1
fi

# remove shorts. write to temp file and then mv back to the original file
awk \
  '!/shorts/' \
  ${YTKP_DIR}/archive/temp/video_urls.txt \
  > ${YTKP_DIR}/archive/temp/video_urls.txt.tmp \
  && mv ${YTKP_DIR}/archive/temp/video_urls.txt.tmp ${YTKP_DIR}/archive/temp/video_urls.txt

# sort and remove duplicates from the list of videos
sort \
  --unique \
  --output=${YTKP_DIR}/archive/temp/video_urls.txt \
  ${YTKP_DIR}/archive/temp/video_urls.txt

# create INSERT INTO .sql with ON CONFLICT clause
awk \
  '{ print "INSERT INTO ytkp.video (video_url) VALUES (\047"$0"\047) ON CONFLICT (video_url) DO NOTHING;" }' \
  ${YTKP_DIR}/archive/temp/video_urls.txt \
  > ${YTKP_DIR}/database/temp/db_video_urls_insert.sql

# run INSERT INTO if there is anything to insert
if [ -s ${YTKP_DIR}/database/temp/db_video_urls_insert.sql ] ; then
    psql \
      --dbname=postgres \
      --quiet \
      --file=${YTKP_DIR}/database/temp/db_video_urls_insert.sql
fi

# update scrape_date in channel row
psql \
  --dbname=postgres \
  --quiet \
  --command="UPDATE ytkp.channel SET scrape_date = NOW() WHERE channel_url = '${db_channel}';"

# update archival vid_urls.txt file
cat \
  ${YTKP_DIR}/archive/temp/video_urls.txt \
  >> ${YTKP_DIR}/archive/vid_urls.txt
sort \
  --unique \
  --output=${YTKP_DIR}/archive/vid_urls.txt \
  ${YTKP_DIR}/archive/vid_urls.txt

# remove temp files
rm ${YTKP_DIR}/archive/temp/video_urls.txt
rm ${YTKP_DIR}/archive/temp/playlist_urls.txt
rm ${YTKP_DIR}/database/temp/db_video_urls_insert.sql

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "xBartM",
  "path": "database/create_schema.sql",
  "ref": "refs/heads/master",
  "repo": "YouTube-Comment-Scraper"
}
```

**Output:**
```
successfully downloaded text file (SHA: cb42bbb9635142581f8e76e7b3d1e1593122e11e)

-- Create a new schema
CREATE SCHEMA ytkp;


-- Create the channel table
CREATE TABLE  ytkp.channel (
    channel_id SERIAL PRIMARY KEY,
    channel_url TEXT UNIQUE NOT NULL,
    channel_name TEXT UNIQUE NOT NULL,
    insert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    scrape_date TIMESTAMP DEFAULT '1970-01-01 00:00:00' NOT NULL
);

-- Create functions for triggers in the channel table
CREATE FUNCTION ytkp.extract_channel_name_from_url() RETURNS TRIGGER AS $$
    BEGIN
        NEW.channel_name := RIGHT(NEW.channel_url, -24);
        RETURN NEW;
    END;
$$ LANGUAGE PLPGSQL;

-- Create triggers in the channel table
CREATE TRIGGER insert_channel_name
    BEFORE INSERT
    ON ytkp.channel
    FOR EACH ROW
    EXECUTE FUNCTION ytkp.extract_channel_name_from_url();

-- Add comments for the channel table and its columns
COMMENT ON TABLE ytkp.channel IS 'Table containing channel information';
COMMENT ON COLUMN ytkp.channel.channel_id IS 'Unique identifier for each channel, auto-incremented';
COMMENT ON COLUMN ytkp.channel.channel_url IS 'URL of the channel, must be provided';
COMMENT ON COLUMN ytkp.channel.channel_name IS 'Name of the channel, derived from the channel_url';
COMMENT ON COLUMN ytkp.channel.insert_date IS 'Timestamp of row insertion';
COMMENT ON COLUMN ytkp.channel.scrape_date IS 'Timestamp of the last time the channel was scraped for video URLs';
-- Add comments for functions
COMMENT ON FUNCTION ytkp.extract_channel_name_from_url() IS 'Function for a trigger; Trim first 24 characters from video url to obtain channel name';
-- Add comments for triggers
COMMENT ON TRIGGER insert_channel_name ON ytkp.channel IS 'Trigger to insert channel_name based on channel_url';


-- Create the video table
CREATE TABLE ytkp.video (
    video_id SERIAL PRIMARY KEY,
    video_yt_id TEXT UNIQUE NOT NULL,
    channel_id INT REFERENCES ytkp.channel(channel_id),
    video_avail TEXT,
    video_lang TEXT,
    video_url TEXT UNIQUE NOT NULL,
    video_name TEXT,
    video_description TEXT,
    upload_date DATE,
    insert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    scrape_date TIMESTAMP DEFAULT '1970-01-01 00:00:00' NOT NULL
);

-- Create triggers for the video table
CREATE FUNCTION ytkp.extract_vid_id_from_url() RETURNS TRIGGER AS $$
    BEGIN
        NEW.video_yt_id := RIGHT(NEW.video_url, 11);
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER insert_yt_id
    BEFORE INSERT
    ON ytkp.video
    FOR EACH ROW
    EXECUTE FUNCTION ytkp.extract_vid_id_from_url();

-- Create functions for the video table
CREATE FUNCTION ytkp.find_channel_id(_channel_name TEXT) RETURNS INT AS $$
    DECLARE
        _channel_id INT;
    BEGIN
        SELECT channel_id INTO _channel_id
        FROM ytkp.channel
        WHERE channel_name = _channel_name;

        IF NOT FOUND THEN
            RETURN NULL;
        END IF;

        RETURN _channel_id;
    END;
$$ LANGUAGE plpgsql;

-- Add comments for the video table and its columns
COMMENT ON TABLE ytkp.video IS 'Table containing video information';
COMMENT ON COLUMN ytkp.video.video_id IS 'Unique identifier for each video, auto-incremented';
COMMENT ON COLUMN ytkp.video.video_yt_id IS 'Unique identifier for each video generated by YouTube';
COMMENT ON COLUMN ytkp.video.channel_id IS 'Foreign key referencing the associated channel';
COMMENT ON COLUMN ytkp.video.video_avail IS 'Availability status of the video - it might be used to download videos that arent public no more';
COMMENT ON COLUMN ytkp.video.video_lang IS 'Language of the video - it might be used to swap embedding models';
COMMENT ON COLUMN ytkp.video.video_url IS 'URL of the video, must be provided';
COMMENT ON COLUMN ytkp.video.video_name IS 'Name of the video';
COMMENT ON COLUMN ytkp.video.video_description IS 'Description of the video';
COMMENT ON COLUMN ytkp.video.upload_date IS 'Original upload date of the video';
COMMENT ON COLUMN ytkp.video.insert_date IS 'Timestamp of row insertion';
COMMENT ON COLUMN ytkp.video.scrape_date IS 'Timestamp of the last time the video was scraped for data (comments, description, transcript)';
-- Add comments for triggers
COMMENT ON FUNCTION ytkp.extract_vid_id_from_url() IS 'Function for a trigger; Extract last 11 characters from video url to obtain YouTube ID';
COMMENT ON TRIGGER insert_yt_id ON ytkp.video IS 'Trigger to insert video_yt_id based on video_url';
-- Add comments for functions
COMMENT ON FUNCTION ytkp.find_channel_id(_channel_name TEXT) IS 'Find the corresponding Channel ID based on channel_name';


-- Create the comment table
CREATE TABLE ytkp.comment_section (
    comment_id SERIAL PRIMARY KEY,
    comment_yt_id TEXT NOT NULL,
    comment_yt_parent TEXT NOT NULL,
    video_id INT REFERENCES ytkp.video(video_id),
    user_name TEXT,
    comment_text TEXT,
    like_count INT NOT NULL,
    is_verified BOOLEAN NOT NULL,
    is_favourited BOOLEAN NOT NULL,
    is_pinned BOOLEAN NOT NULL,
    comment_date TIMESTAMP NOT NULL,
    insert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Create functions for the comment_section table
CREATE FUNCTION ytkp.find_video_id(_video_yt_id TEXT) RETURNS INT AS $$
    DECLARE
        _video_id INT;
    BEGIN
        SELECT video_id INTO _video_id
        FROM ytkp.video
        WHERE video_yt_id = _video_yt_id;

        IF NOT FOUND THEN
            RETURN NULL;
        END IF;

        RETURN _video_id;
    END;
$$ LANGUAGE plpgsql;

-- Add comments for the comment table and its columns
COMMENT ON TABLE ytkp.comment_section IS 'Table containing comments on videos';
COMMENT ON COLUMN ytkp.comment_section.comment_id IS 'Unique identifier for each comment, auto-incremented';
COMMENT ON COLUMN ytkp.comment_section.comment_yt_id IS 'Comment ID generated by YouTube';
COMMENT ON COLUMN ytkp.comment_section.comment_yt_parent IS 'Comment ID generated by YouTube that this comment refers to';
COMMENT ON COLUMN ytkp.comment_section.video_id IS 'Foreign key referencing the associated video';
COMMENT ON COLUMN ytkp.comment_section.user_name IS 'Name of the user that wrote the given comment';
COMMENT ON COLUMN ytkp.comment_section.comment_text IS 'Text of the comment';
COMMENT ON COLUMN ytkp.comment_section.like_count IS 'Number of likes the comment has';
COMMENT ON COLUMN ytkp.comment_section.is_verified IS 'Flag if the author of the comment is verified';
COMMENT ON COLUMN ytkp.comment_section.is_favourited IS 'Flag if the comment is favourited by video author';
COMMENT ON COLUMN ytkp.comment_section.is_pinned IS 'Flag if the comment is pinned by video author';
COMMENT ON COLUMN ytkp.comment_section.comment_date IS 'Original submit date of the comment to YT service';
COMMENT ON COLUMN ytkp.comment_section.insert_date IS 'Date of insertion of the comment to the database';
-- Add comments for functions
COMMENT ON FUNCTION ytkp.find_video_id(_video_yt_id TEXT) IS 'Find the corresponding Video ID based on video_yt_id';


-- Create the video transcript table
CREATE TABLE ytkp.video_transcript (
    id SERIAL PRIMARY KEY,
    video_id INT REFERENCES ytkp.video(video_id),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    transcript_text TEXT,
    is_sponsorblocked BOOLEAN DEFAULT false NOT NULL
);

-- Add comments on the transcript table and its columns
COMMENT ON TABLE ytkp.video_transcript IS 'Table containing transcripts of the videos as they appear in the transcript file (sliced into chunks with start and end times';
COMMENT ON COLUMN ytkp.video_transcript.id IS 'Unique identifier for each entry; not really used aside from being a PRIMARY KEY';
COMMENT ON COLUMN ytkp.video_transcript.video_id IS 'ID of the video that the transcript relates to';
COMMENT ON COLUMN ytkp.video_transcript.start_time IS 'Start time of the transcribed chunk';
COMMENT ON COLUMN ytkp.video_transcript.end_time IS 'End time of the transcribed chunk';
COMMENT ON COLUMN ytkp.video_transcript.transcript_text IS 'Transcript text chunk from VTT sub file';
COMMENT ON COLUMN ytkp.video_transcript.is_sponsorblocked IS 'Flag to differentiate sponsored chunks of the transcript and non-sponsored';


-- Create the sponsorblock timestamp table
CREATE TABLE ytkp.sponsorblock (
    id SERIAL PRIMARY KEY,
    video_id INT REFERENCES ytkp.video(video_id),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

-- Create triggers for the sponsorblock table
CREATE FUNCTION ytkp.update_sponsorblocked_chunks() RETURNS TRIGGER AS $$
    BEGIN
        UPDATE ytkp.video_transcript
        SET is_sponsorblocked = true
        WHERE 1=1
            AND end_time >= NEW.start_time
            AND start_time <= NEW.end_time;
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;
CREATE TRIGGER insert_is_sponsorblocked
    AFTER INSERT
    ON ytkp.sponsorblock
    FOR EACH ROW
    EXECUTE FUNCTION ytkp.update_sponsorblocked_chunks();

-- Add comments for the sponsorblock table and its columns
COMMENT ON TABLE ytkp.sponsorblock IS 'Table containing information about sponsored (or otherwise useless) parts of the video';
COMMENT ON COLUMN ytkp.sponsorblock.id IS 'Unique identifier for each entry; not really used aside from being a PRIMARY KEY';
COMMENT ON COLUMN ytkp.sponsorblock.video_id IS 'ID of the video that has a sponsored part';
COMMENT ON COLUMN ytkp.sponsorblock.start_time IS 'Start time of the sponsored segment in the video';
COMMENT ON COLUMN ytkp.sponsorblock.end_time IS 'End time of the sponsored segment in the video';
-- Add comments for triggers
COMMENT ON FUNCTION ytkp.update_sponsorblocked_chunks() IS 'Function for a trigger; Set is_sponsorblocked flag into ytkp.video_transcript';
COMMENT ON TRIGGER insert_is_sponsorblocked ON ytkp.sponsorblock IS 'Trigger to set video_transcript.is_sponsorblocked flag when inserting into ytkp.sponsorblock';

```

---

## Assistant (Plan · Space Bunny Free · 5.7s)

_Thinking:_

We have enough source for several. Need inspect comment suite Java structure maybe actual extraction. Also YouTube Channel Archiver service. Need licenses. We can gather key files.

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "mattwright324",
  "path": "src/main",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
[{"name":"java","path":"src/main/java","type":"dir"},{"name":"resources","path":"src/main/resources","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "mattwright324",
  "path": "src/test",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
[{"name":"java","path":"src/test/java","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "mattwright324",
  "path": "src/main/java",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
[{"type":"dir","size":0,"name":"io","path":"src/main/java/io","sha":"c7947b0ed71fa25da2b7bb22242b61bbc9f108dd","url":"https://api.github.com/repos/mattwright324/youtube-comment-suite/contents/src/main/java/io?ref=de766c2a3f5106dc2b4886dd1a5f4ae74b6aed81","git_url":"https://api.github.com/repos/mattwright324/youtube-comment-suite/git/trees/c7947b0ed71fa25da2b7bb22242b61bbc9f108dd","html_url":"https://github.com/mattwright324/youtube-comment-suite/tree/de766c2a3f5106dc2b4886dd1a5f4ae74b6aed81/src/main/java/io"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "canarik",
  "path": "background/service-worker.js",
  "ref": "refs/heads/main",
  "repo": "YouTube-Channel-Archiver"
}
```

**Output:**
```
successfully downloaded text file (SHA: 8a918a7cd59a136561d29d976028ac70624ab0d3)

import { NCaptureGenerator } from '../utils/ncapture-generator.js';
import { XLSXExporter } from '../utils/xlsx-exporter.js';

// ... (Rest of imports if any, but YCA structure is sparse here)

// ...

// In saveVideoData function (I need to target the specific block)
// I will use a larger block replacement to ensure I catch the logic.

// ...


/**
 * Background Service Worker
 * Opens tabs for each video and orchestrates data extraction
 */

console.log('[YCA Background] Service worker started');

function nestComments(flatComments) {
    if (!flatComments || flatComments.length === 0) return [];

    const commentMap = new Map();
    const rootComments = [];

    // First pass: Create map and identify root comments
    flatComments.forEach(comment => {
        commentMap.set(comment.id, { ...comment, replies: [] });
        if (!comment.isReply) {
            rootComments.push(commentMap.get(comment.id));
        }
    });

    // Second pass: Nest replies under their parents
    flatComments.forEach(comment => {
        if (comment.isReply && comment.parentId) {
            const parent = commentMap.get(comment.parentId);
            if (parent) {
                parent.replies.push(commentMap.get(comment.id));
            }
        }
    });

    return rootComments;
}

let videoQueue = [];
let currentChannelId = null;
let currentChannelName = null;
let currentOptions = {}; // Store options for current batch
let isProcessing = false;
let mainTabId = null; // Store the tab ID that initiated the download

// Listen for download requests
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log('[YCA Background] Received:', message.type);

    if (message.type === 'YCA_START_DOWNLOAD') {
        const { videos, channelId, channelName } = message.payload;
        console.log(`[YCA Background] Starting download for ${videos.length} videos`);

        // Store the initiating tab ID to send completion message later
        if (sender.tab) {
            mainTabId = sender.tab.id;
            console.log(`[YCA Background] Main tab ID: ${mainTabId}`);
        }
        console.log(`[YCA Background] Channel: ${channelName} (${channelId})`);

        videoQueue = [...videos];
        currentChannelId = channelId;
        currentChannelName = channelName || channelId; // Fallback to ID if name not provided
        currentOptions = message.payload.options || {}; // Extract options

        // Persist state to storage for reliability
        chrome.storage.local.set({
            'yca_session': {
                channelName: currentChannelName,
                options: currentOptions
            }
        }, () => {
            console.log('[YCA Background] Options saved to storage:', JSON.stringify(currentOptions));
            isProcessing = true;
            processNextVideo();
        });
    }

    if (message.type === 'YCA_VIDEO_DATA_READY') {
        // Data extracted from the tab
        const { videoId, title, transcript, comments, chatReplay, options, channelName, duration } = message.payload;
        console.log(`[YCA Background] Received data for ${videoId}`);
        console.log(`[YCA Background] - Duration: ${duration} seconds`);
        console.log(`[YCA Background] - Transcript: ${transcript ? transcript.length + ' chars' : 'NULL'}`);
        console.log(`[YCA Background] - Comments: ${comments ? comments.length + ' items' : 'NULL'}`);
        console.log(`[YCA Background] - Chat: ${chatReplay ? 'YES' : 'NULL'}`);
        console.log(`[YCA Background] - Options: ${JSON.stringify(options || {})}`);

        // Save the data, passing options and channel name if available
        saveVideoData(videoId, title, transcript, comments, chatReplay, options, channelName, duration);

        // Close the tab after extraction ONLY if part of a batch process (YCA Scan)
        // Single videos opened manually should stay open
        if (sender.tab && isProcessing) {
            console.log(`[YCA Background] Closing tab ${sender.tab.id} (Batch Mode)`);
            chrome.tabs.remove(sender.tab.id);
        } else if (sender.tab) {
            console.log(`[YCA Background] Keeping tab ${sender.tab.id} open (Single/Manual Mode)`);
        }

        // Script-based extraction is fast (~4-5 seconds total)
        // Wait 1 second before processing next video to avoid overwhelming the browser
        console.log(`[YCA Background] Waiting 1 second before next video...`);
        setTimeout(processNextVideo, 1000);
    }
});

function processNextVideo() {
    if (videoQueue.length === 0) {
        console.log('[YCA Background] All videos processed!');
        isProcessing = false;

        // Notify the main tab that all downloads are complete
        if (mainTabId) {
            console.log(`[YCA Background] Sending completion message to main tab ${mainTabId}`);
            chrome.tabs.sendMessage(mainTabId, {
                type: 'YCA_QUEUE_COMPLETE'
            }).catch(err => console.log('[YCA Background] Could not notify main tab (closed?):', err));
            mainTabId = null; // Reset
        }

        return;
    }

    const video = videoQueue.shift();

    // Encode state into URL to survive service worker suspension/restarts
    const channelParam = encodeURIComponent(currentChannelName || '');
    const ncaptureParam = currentOptions.ncapture ? '1' : '0';

    // Append parameters for content script to read
    const videoUrl = `https://www.youtube.com/watch?v=${video.videoId}&autoplay=0&yca=1&yca_channel=${channelParam}&yca_ncapture=${ncaptureParam}`;

    console.log(`[YCA Background] Opening tab for ${video.videoId} (${videoQueue.length} remaining)`);
    console.log(`[YCA Background] URL: ${videoUrl}`);

    // Open video in new tab with yca=1 parameter to trigger automatic extraction
    // MUST be active:true so transcript button clicking works!
    chrome.tabs.create({
        url: videoUrl,
        active: true
    }, (tab) => {
        console.log(`[YCA Background] Tab created: ${tab.id}`);
        // We also set up a listener for this specific tab to trigger extraction when ready
        // This is a fallback/redundant trigger in case the URL param based trigger fails
        const listener = function (tabId, changeInfo, tabInfo) {
            if (tabId === tab.id && changeInfo.status === 'complete') {
                console.log(`[YCA Background] Tab ${tabId} loaded, sending trigger command...`);
                chrome.tabs.sendMessage(tabId, {
                    type: 'YCA_TRIGGER_EXTRACTION',
                    videoId: video.videoId,
                    options: currentOptions // Pass options to content script
                });
                // Remove listener after triggering (or we could keep it? better remove to avoid dupes)
                chrome.tabs.onUpdated.removeListener(listener);
            }
        };
        chrome.tabs.onUpdated.addListener(listener);
    });
}

function saveVideoData(videoId, title, transcript, comments, chatReplay, options = null, channelName = null, duration = 0) {
    console.log(`[YCA Background] saveVideoData called for ${videoId}`);
    console.log(`[YCA Background] - Title: ${title}`);
    console.log(`[YCA Background] - Duration: ${duration} seconds`);
    console.log(`[YCA Background] - Transcript: ${transcript ? 'YES' : 'NO'}`);
    console.log(`[YCA Background] - Comments: ${comments ? comments.length : 0}`);
    console.log(`[YCA Background] - Chat: ${chatReplay ? chatReplay.length : 0}`);

    const safeTitle = title.replace(/[<>:"/\\|?*]/g, '_').substring(0, 100);

    // Logic: Favor currentChannelName (Bulk/Global) if available.
    let effectiveChannelName = currentChannelName;

    if (!effectiveChannelName && channelName && channelName !== 'Unknown Channel') {
        effectiveChannelName = channelName;
    }

    if (!effectiveChannelName) {
        effectiveChannelName = "Unknown Channel";
    }

    const folder = `${effectiveChannelName}/${safeTitle}_${videoId}`;

    console.log(`[YCA Background] Folder path: ${folder}`);

    // Save transcript
    if (transcript) {
        console.log(`[YCA Background] Calling downloadTextFile for transcript`);
        const textContent = typeof transcript === 'object' ? transcript.text : transcript;
        downloadTextFile(`${folder}/transcript.txt`, textContent, true); // true = UTF-16LE encoding for NVivo
    } else {
        console.log(`[YCA Background] No transcript to save`);
    }

    // Save comments
    if (comments && comments.length > 0) {
        console.log(`[YCA Background] Calling downloadTextFile for comments`);
        downloadTextFile(`${folder}/comments.json`, JSON.stringify(comments, null, 2));
    } else {
        console.log(`[YCA Background] No comments to save`);
    }

    // Save chat replay
    if (chatReplay && chatReplay.length > 0) {
        console.log(`[YCA Background] Calling downloadTextFile for chat`);
        downloadTextFile(`${folder}/chat_replay.json`, JSON.stringify(chatReplay, null, 2));
    } else {
        console.log(`[YCA Background] No chat to save`);
    }

    // Save XLSX (Replacing NCapture)
    let xlsxEnabled = true; // Default to true

    if (options && typeof options.exportXlsx === 'boolean') {
        xlsxEnabled = options.exportXlsx;
    }

    console.log('[YCA Background] Checking XLSX export condition:');
    console.log(`[YCA Background] - Enabled: ${xlsxEnabled}`);

    if (xlsxEnabled && comments && comments.length > 0) {
        try {
            console.log(`[YCA Background] Generating XLSX file for ${comments.length} comments...`); // DEBUG LOG
            console.log(`[YCA Background] Sample comment:`, comments[0]); // DEBUG LOG

            const videoDataForXlsx = {
                videoId,
                title,
                url: `https://www.youtube.com/watch?v=${videoId}`,
                comments,
                duration: duration && duration > 0 ? String(duration) : "0"
            };

            const xlsxContent = XLSXExporter.generate(videoDataForXlsx);

            // Filename format: "Title Comments.xlsx"
            const filename = `${safeTitle} Comments.xlsx`;
            const fullPath = `${folder}/${filename}`;

            downloadTextFile(fullPath, xlsxContent, false, true); // isBase64 = true
        } catch (err) {
            console.error('[YCA Background] XLSX generation failed:', err);
        }
    }

    console.log(`[YCA Background] Saved data for ${videoId}`);
}

function downloadTextFile(filename, content, forceUTF16LE = false, isBase64 = false) {
    console.log(`[YCA Background] Attempting download: ${filename}`);
    console.log(`[YCA Background] Content length: ${content.length} chars`);

    let dataUrl;

    if (isBase64) {
        // Content is already base64 (e.g. XLSX)
        dataUrl = `data:application/octet-stream;base64,${content}`;
        console.log('[YCA Background] Using provided Base64 content');
    } else if (filename.endsWith('.nvcx') || forceUTF16LE) {
        // Special handling for UTF-16LE
        let str = content;
        if (!filename.endsWith('.nvcx')) {
            str = '\uFEFF' + str;
        }

        const codeUnits = new Uint16Array(str.length);
        for (let i = 0; i < str.length; i++) {
            codeUnits[i] = str.charCodeAt(i);
        }

        let binary = '';
        const bytes = new Uint8Array(codeUnits.buffer);
        const len = bytes.byteLength;
        for (let i = 0; i < len; i++) {
            binary += String.fromCharCode(bytes[i]);
        }

        const base64Content = btoa(binary);
        dataUrl = `data:application/octet-stream;base64,${base64Content}`;
        console.log('[YCA Background] Encoded as UTF-16LE');
    } else {
        // Standard UTF-8
        const base64Content = btoa(unescape(encodeURIComponent(content)));
        dataUrl = `data:text/plain;charset=utf-8;base64,${base64Content}`;
    }

    console.log(`[YCA Background] Data URL created, length: ${dataUrl.length}`);

    chrome.downloads.download({
        url: dataUrl,
        filename: filename,
        saveAs: false
    }, (downloadId) => {
        if (chrome.runtime.lastError) {
            console.error('[YCA Background] Download FAILED:', chrome.runtime.lastError);
        } else {
            console.log(`[YCA Background] Download SUCCESS: ${filename} (ID: ${downloadId})`);
        }
    });
}

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "dlovecreator-arch",
  "path": "src/download_resilient.py",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
successfully downloaded text file (SHA: a86b21bec1ce9a426b6f3845b7462ec4038b0976)

#!/usr/bin/env python3
"""
YouTube Channel Downloader with Intelligent Rate Limiting & Resilience

Core strategy:
- Increased inter-video sleep (2.5s instead of 1.5s)
- Rotating user agents to avoid fingerprinting
- Exponential backoff on batch failure
- Adaptive timeout: scales based on estimated video count
  * Small channels (<500): 600s (10 min)
  * Medium channels (500-2000): 3600s (60 min)
  * Large channels (2000+): 7200s (120 min)
- Resume-safe: can re-run indefinitely to accumulate all videos
"""

import subprocess
import sys
import time
import random
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "out"
LOG_FILE = REPO_ROOT / "archive" / "logs" / f"yt_download_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
]

def log(msg):
    """Log to both file and stdout."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')

def count_videos(out_dir):
    """Count .info.json files (completed downloads)."""
    return len(list(out_dir.glob("*/*.info.json")))

def estimate_timeout(video_count):
    """
    Calculate adaptive timeout based on estimated video count.
    
    At 2.5s per video:
    - 100 videos = 250s (4 min)
    - 500 videos = 1250s (21 min) -> use 600s (10 min) for small channels
    - 1000 videos = 2500s (42 min) -> use 3600s (60 min) for medium
    - 2000 videos = 5000s (83 min) -> use 7200s (120 min) for large
    
    Add 50% safety margin.
    """
    if video_count < 500:
        return 600  # 10 minutes
    elif video_count < 2000:
        return 3600  # 60 minutes
    else:
        return 7200  # 120 minutes

def normalize_channel_url(url):
    """
    YouTube channels can be accessed via multiple URL formats.
    
    /videos tab: https://www.youtube.com/@handle/videos
    - Only returns recent videos (client-side pagination limit)
    - Typical: 8-20 recent items only
    
    Channel root: https://www.youtube.com/@handle
    - Returns full video history
    - Typical: all videos available
    
    This function doesn't modify URLs -- just documents the pattern.
    The heuristic below will retry with channel root if /videos is suspiciously small.
    """
    return url

def download_with_backoff(url, max_attempts=5):
    """Download with exponential backoff and user agent rotation."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    
    log(f"Starting download: {url}")
    log("Strategy: exponential backoff + rotating user agents + adaptive timeout + channel format detection")
    
    attempt = 1
    backoff = 5
    last_count = 0
    
    while attempt <= max_attempts:
        user_agent = random.choice(USER_AGENTS)
        log(f"Attempt {attempt}/{max_attempts} (UA rotation: {USER_AGENTS.index(user_agent) + 1}/{len(USER_AGENTS)})")
        
        # Estimate timeout based on current download count (assume similar size)
        current_count = count_videos(OUT_DIR)
        estimated_total = max(500, current_count * 2)  # Conservative estimate
        timeout_seconds = estimate_timeout(estimated_total)
        timeout_minutes = timeout_seconds // 60
        log(f"Using timeout: {timeout_minutes} minutes ({timeout_seconds} seconds) for estimated {estimated_total} videos")
        
        try:
            # Core yt-dlp call with aggressive rate limit workarounds
            subprocess.run(
                [
                    "yt-dlp",
                    "--skip-download",
                    "--write-info-json",
                    "--write-auto-subs",
                    "--sub-langs", "en",
                    "--sub-format", "vtt",
                    "--socket-timeout", "8",
                    "--retries", "1",
                    "--retry-sleep", "5",  # Increased from 3s
                    "--max-sleep-interval", "10",  # Increased from 6s
                    "--sleep-interval", "3.5",  # Increased from 2.5s
                    "--sleep-requests", "2",  # Add sleep between requests
                    "--ignore-errors",
                    "--no-warnings",
                    "--user-agent", user_agent,
                    "--output", f"{OUT_DIR}/%(uploader)s/%(id)s/%(title)s [%(id)s].%(ext)s",
                    url
                ],
                timeout=timeout_seconds,  # Adaptive based on channel size
                check=False
            )
        except subprocess.TimeoutExpired:
            log(f"Attempt {attempt} timed out after {timeout_seconds}s ({timeout_minutes} min)")
            # On timeout, wait longer before retry
            log(f"Rate-limited: waiting 30 seconds before retry...")
            time.sleep(30)

        except Exception as e:
            log(f"ERROR in attempt {attempt}: {e}")
        
        current_count = count_videos(OUT_DIR)
        log(f"Progress: {current_count} videos (gained {current_count - last_count} this attempt)")
        last_count = current_count
        
        # HEURISTIC: If /videos tab returned suspiciously small count, retry with channel root
        if attempt == 1 and current_count < 20 and "/videos" in url:
            log(f"⚠️  WARNING: /videos tab only returned {current_count} videos (likely incomplete)")
            log(f"  Retrying with channel root (remove /videos suffix)")
            url_root = url.replace("/videos", "")
            log(f"  New URL: {url_root}")
            url = url_root
            # Reset counter for this new attempt chain
            last_count = current_count
        
        # If we made progress, continue with next attempt
        if current_count > 0 and attempt < max_attempts:
            log(f"Sleeping 120s before next attempt (inter-batch cool-down)...")
            time.sleep(120)
        
        # Exponential backoff
        if attempt < max_attempts:
            log(f"Backoff: sleeping {backoff}s before next attempt")
            time.sleep(backoff)
            backoff = min(backoff * 1.5, 120)
        
        attempt += 1
    
    final_count = count_videos(OUT_DIR)
    log(f"Download complete: {final_count} total videos downloaded")
    return final_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: download_resilient.py <YouTube URL> [max_attempts]")
        sys.exit(1)
    
    url = sys.argv[1]
    max_attempts = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    download_with_backoff(url, max_attempts)
    log("Downloader done")

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "dlovecreator-arch",
  "path": "src/enhance_rag_schema.py",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
successfully downloaded text file (SHA: 0ce7984a9cb1877c0033949a3e6b94887b784142)

#!/usr/bin/env python3
"""
Enhanced metadata extraction with RAG-optimized schema.

Upgrades canonical.json to include:
- source_id: youtube_channelslug_videoid
- captured_date: ISO timestamp
- transcript_source: youtube_caption | whisper | manual
- confidence: 0.85 (YouTube auto-captions accuracy baseline)
- tradition: [] (can be manually enriched later)

Features:
  - Comprehensive error handling
  - Input validation
  - Recovery on partial failure
"""

import json
import re
import logging
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_BASE = REPO_ROOT / "out"
DB_FILE = REPO_ROOT / "db" / "canonical.json"

def sanitize_slug(name: str) -> str:
    """Convert channel name to URL-safe slug."""
    try:
        return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')
    except Exception as e:
        logger.warning(f"Error sanitizing slug for '{name}': {e}")
        return "unknown"

def extract_guest(title: str, description: str = "") -> str | None:
    """Extract guest name from title/description."""
    try:
        # Pattern: "Title | Guest Name"
        match = re.search(r'\|\s*([A-Z][A-Za-z\s\.]+)(?:\s*\[|$)', title)
        if match:
            guest = match.group(1).strip()
            if guest and len(guest) > 2 and guest not in ["Emilio Ortiz", "Viviane Chauvet", "The Alchemist"]:
                return guest
        
        # Pattern: "Guest Name REVEALS/SHOWS/etc"
        match = re.match(r'^([A-Z][A-Za-z\s]+?)\s+(REVEALS|SHOWS|TELLS|WARNS|DISCUSSES|EXPLAINS|SHARES|PREDICTS)', title)
        if match:
            guest = match.group(1).strip()
            if len(guest) > 2:
                return guest
        
        return None
    except Exception as e:
        logger.debug(f"Error extracting guest from '{title}': {e}")
        return None

def extract_topics(tags: list, description: str, title: str) -> list:
    """Extract topic tags."""
    try:
        topics = set()
        if tags and isinstance(tags, list):
            for tag in tags[:8]:
                tag_lower = str(tag).lower()
                if tag_lower not in ['interview', 'podcast', 'youtube', '2024', '2025', 'new']:
                    topics.add(tag_lower)
        
        if title and isinstance(title, str):
            for word in title.split():
                if word.isupper() and len(word) > 2:
                    topics.add(word.lower())
        
        return sorted(list(topics))
    except Exception as e:
        logger.debug(f"Error extracting topics: {e}")
        return []

def enhance_canonical_db():
    """
    Load existing canonical.json, add RAG-optimized fields, save back.
    """
    try:
        logger.info("Loading existing canonical.json...")
        
        if not DB_FILE.exists():
            logger.error(f"canonical.json not found at {DB_FILE}")
            logger.info("Initialize with: mkdir -p db && python3 << 'EOF'")
            logger.info("import json")
            logger.info("db = {'videos': [], 'metadata': {'total_videos': 0, 'total_channels': 0, 'last_sync': None, 'version': '1.0'}}")
            logger.info("with open('db/canonical.json', 'w') as f: json.dump(db, f, indent=2)")
            logger.info("EOF")
            sys.exit(1)
        
        try:
            db = json.loads(DB_FILE.read_text())
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON: {e}")
            logger.error(f"File may be corrupted. Backup is recommended.")
            sys.exit(1)
        
        videos = db.get("videos", [])
        
        if not videos:
            logger.warning("No videos found in database")
            return
        
        captured_now = datetime.utcnow().isoformat() + "Z"
        
        logger.info(f"Enhancing {len(videos)} videos with RAG schema...")
        
        enhanced_count = 0
        skipped_count = 0
        
        for i, video in enumerate(videos):
            try:
                if i % 500 == 0:
                    logger.info(f"  Progress: {i}/{len(videos)}")
                
                channel = video.get("channel", "")
                video_id = video.get("id", "")
                
                if not channel or not video_id:
                    skipped_count += 1
                    logger.debug(f"Skipping video with missing channel or id")
                    continue
                
                # Add source_id: youtube_channelslug_videoid
                if not video.get("source_id"):
                    channel_slug = sanitize_slug(channel)
                    video["source_id"] = f"youtube_{channel_slug}_{video_id}"
                
                # Add captured_date
                if not video.get("captured_date"):
                    video["captured_date"] = captured_now
                
                # Add transcript_source (we're using YouTube auto-captions)
                if not video.get("transcript_source"):
                    video["transcript_source"] = "youtube_caption"
                
                # Add confidence (YouTube auto-captions ~85% accurate)
                if not video.get("confidence"):
                    video["confidence"] = 0.85
                
                # Add tradition (empty for now, can be manually enriched)
                if not video.get("tradition"):
                    video["tradition"] = []
                
                enhanced_count += 1
            
            except Exception as e:
                skipped_count += 1
                logger.warning(f"Error enhancing video {i}: {e}")
                continue
        
        # Write back with error handling
        try:
            logger.info("Saving enhanced canonical.json...")
            DB_FILE.write_text(json.dumps(db, indent=2))
        except Exception as e:
            logger.error(f"Failed to write database: {e}")
            logger.error("Database may not have been updated")
            sys.exit(1)
        
        logger.info(f"✓ Enhanced {enhanced_count} videos, skipped {skipped_count}")
        logger.info(f"  - Added source_id (youtube_channelslug_videoid)")
        logger.info(f"  - Added captured_date ({captured_now})")
        logger.info(f"  - Added transcript_source (youtube_caption)")
        logger.info(f"  - Added confidence (0.85)")
        logger.info(f"  - Added tradition ([])")
    
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    enhance_canonical_db()

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "sworcery",
  "path": "LICENSE",
  "ref": "refs/heads/main",
  "repo": "ChannelHoarder"
}
```

**Output:**
```
successfully downloaded text file (SHA: b118ae2da34dec1da659ff7fc33b5eab0d860fe1)

MIT License

Copyright (c) 2025 sworcery

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "IA-Programming",
  "path": "LICENSE",
  "ref": "refs/heads/main",
  "repo": "Youtube-MCP"
}
```

**Output:**
```
successfully downloaded text file (SHA: e676f5fb64d4eea71afd840c798f9a60c234084c)

MIT License

Copyright (c) 2024 FarhaParveen919

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Assistant (Plan · Space Bunny Free · 5.5s)

_Thinking:_

Need perhaps inspect licenses for key candidates and ytdlp. Could report based known. Need comments source suite paths. Get nested.

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "mattwright324",
  "path": "src/main/java/io",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
[{"name":"mattw","path":"src/main/java/io/mattw","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "mattwright324",
  "path": "src/test/java",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
[{"type":"dir","size":0,"name":"io","path":"src/test/java/io","sha":"dcd0b5818c71462d0b0672e158d00538fc299b67","url":"https://api.github.com/repos/mattwright324/youtube-comment-suite/contents/src/test/java/io?ref=de766c2a3f5106dc2b4886dd1a5f4ae74b6aed81","git_url":"https://api.github.com/repos/mattwright324/youtube-comment-suite/git/trees/dcd0b5818c71462d0b0672e158d00538fc299b67","html_url":"https://github.com/mattwright324/youtube-comment-suite/tree/de766c2a3f5106dc2b4886dd1a5f4ae74b6aed81/src/test/java/io"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "yt-dlp",
  "path": "LICENSE",
  "ref": "refs/heads/master",
  "repo": "yt-dlp"
}
```

**Output:**
```
successfully downloaded text file (SHA: 68a49daad8ff7e35068f2b7a97d643aab440eaec)

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "jdepoix",
  "path": "LICENSE",
  "ref": "refs/heads/master",
  "repo": "youtube-transcript-api"
}
```

**Output:**
```
successfully downloaded text file (SHA: 14f48678bfe2baa69dc9ecf1f1cd62c930408312)

MIT License

Copyright (c) 2018 Jonas Depoix

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "xBartM",
  "path": "LICENSE",
  "ref": "refs/heads/master",
  "repo": "YouTube-Comment-Scraper"
}
```

**Output:**
```
successfully downloaded text file (SHA: 50e530bf612b43a727061df71cf9f43a3bf1ba76)

MIT License

Copyright (c) 2025 xBartM

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "mattwright324",
  "path": "LICENSE",
  "ref": "refs/heads/main",
  "repo": "youtube-comment-suite"
}
```

**Output:**
```
successfully downloaded text file (SHA: e7f1a3872a274b621d1ea6c0cbee2d087b14b46b)

MIT License

Copyright (c) 2020 Matthew Wright

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "warkingtime",
  "path": "LICENSE",
  "ref": "refs/heads/main",
  "repo": "channel-transcript-archiver"
}
```

**Output:**
```
successfully downloaded text file (SHA: 68a49daad8ff7e35068f2b7a97d643aab440eaec)

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "dlovecreator-arch",
  "path": "LICENSE",
  "ref": "refs/heads/main",
  "repo": "youtube-transcript-exporter"
}
```

**Output:**
```
successfully downloaded text file (SHA: 28688d47d81d0982414a8f5bcf2e10bbac8d7f59)

MIT License

Copyright (c) 2026 Daniel Love

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

---

## Assistant (Plan · Space Bunny Free · 5.8s)

_Thinking:_

Need likely no need more. But user asks detailed report, need credible matrix 10 candidates. Need mention some not fully inspected? We can include 10 with source inspection at least key. Need inspect ChannelHoarder architecture maybe source tree. Youtube MCP. YouTube Channel Archiver no license listed =&gt; unknown. dlove etc. Get roots/trees.

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "sworcery",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "ChannelHoarder"
}
```

**Output:**
```
[{"name":".github","path":".github","type":"dir"},{"name":".gitignore","path":".gitignore","type":"file"},{"name":"CHANGELOG.md","path":"CHANGELOG.md","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"backend","path":"backend","type":"dir"},{"name":"docker","path":"docker","type":"dir"},{"name":"docs","path":"docs","type":"dir"},{"name":"frontend","path":"frontend","type":"dir"},{"name":"project_history.md","path":"project_history.md","type":"file"},{"name":"tools","path":"tools","type":"dir"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "IA-Programming",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "Youtube-MCP"
}
```

**Output:**
```
[{"name":".gitignore","path":".gitignore","type":"file"},{"name":".python-version","path":".python-version","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"pyproject.toml","path":"pyproject.toml","type":"file"},{"name":"server.py","path":"server.py","type":"file"},{"name":"uv.lock","path":"uv.lock","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "IA-Programming",
  "path": "README.md",
  "ref": "refs/heads/main",
  "repo": "Youtube-MCP"
}
```

**Output:**
```
successfully downloaded text file (SHA: 7810aa513ca04a75b4e875f241c5347cb1099552)

# YouTube MCP Server

A Model Context Protocol (MCP) server that provides tools for searching YouTube videos, retrieving transcripts, and performing semantic search over video content.

## Support Us

If you find this project helpful and would like to support future projects, consider buying us a coffee! Your support helps us continue building innovative AI solutions.

<a href="https://www.buymeacoffee.com/blazzmocompany"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=blazzmocompany&button_colour=40DCA5&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00"></a>

Your contributions go a long way in fueling our passion for creating intelligent and user-friendly applications.

## Table of Contents

- [YouTube MCP Server](#youtube-mcp-server)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Server](#running-the-server)
  - [1. Direct Method](#1-direct-method)
  - [2. Configure for Claude.app](#2-configure-for-claudeapp)
- [Available Tools](#available-tools)
- [Using with MCP Clients](#using-with-mcp-clients)
  - [Example Usage](#example-usage)
- [Debugging](#debugging)
- [Contributing](#contributing)
- [License](#license)

## Features

- Search YouTube videos without using the official API
- Retrieve video transcripts
- Store video information and transcripts in a vector database
- Perform semantic search over stored video transcripts

## Prerequisites

- Python 3.8+
- Google API key for embeddings
- uv package manager

## Installation

1. Clone this repository

2. Create and activate a virtual environment using uv:
```bash
uv venv
# On Windows:
.venv\Scripts\activate
# On Unix/MacOS:
source .venv/bin/activate
```

3. Install dependencies using uv:
```bash
uv pip install -r requirements.txt
```

4. Create a `.env` file with your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## Running the Server

There are two ways to run the MCP server:

### 1. Direct Method

To start the MCP server directly:

```bash
uv run python server.py
```

### 2. Configure for Claude.app

Add to your Claude settings without using any package manager this works for windows:
```json
"mcpServers": {
  "youtube": {
    "command": "C:\\Path\\To\\Your\\Project\\.venv\\Scripts\\python.exe",
    "args": ["C:\\Path\\To\\Your\\Project\\server.py"],
    "env": {
      "GOOGLE_API_KEY": "your_api_key_here"
    }
  }
}
```

Using Uv package manager this works for windows:

```json
"mcpServers": {
  "youtube": {
    "command": "uv",
    "args": ["--directory", "C:\\Path\\To\\Your\\Project", "run", "server.py"],
    "env": {
      "GOOGLE_API_KEY": "your_api_key_here"
    }
  }
}
```

## Available Tools

The server provides the following tools:

1. `search-youtube`: Search for YouTube videos based on a query
   - Parameters:
     - query: Search query string
     - max_results: Maximum number of results to return (default: 5)

2. `get-transcript`: Get the transcript of a YouTube video
   - Parameters:
     - video_url: URL of the YouTube video

3. `store-video-info`: Store video information and transcript in the vector database
   - Parameters:
     - video_url: URL of the YouTube video
     - metadata: Optional metadata about the video

4. `search-transcripts`: Search stored video transcripts using semantic search
   - Parameters:
     - query: Search query
     - limit: Maximum number of results to return (default: 3)

## Using with MCP Clients

This server can be used with any MCP-compatible client, such as Claude Desktop App. The tools will be automatically discovered and made available to the client.

### Example Usage

1. Start the server using one of the methods described above
2. Open Claude Desktop App
3. Look for the hammer icon to verify that the YouTube tools are available
4. You can now use commands like:
   - "Search for Python tutorial videos"
   - "Get the transcript of this video: [video_url]"
   - "Search through stored video transcripts about machine learning"

## Debugging

If you encounter any issues:

1. Make sure your Google API key is correctly set in the `.env` file
2. Check that all dependencies are installed correctly
3. Verify that the server is running and listening for connections
4. Look for any error messages in the server output

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "sworcery",
  "path": "README.md",
  "ref": "refs/heads/main",
  "repo": "ChannelHoarder"
}
```

**Output:**
```
successfully downloaded text file (SHA: a79adada93a9c6a7a03d01888fb0e2972f0c02e1)

<p align="center">
  <img src="frontend/public/logo.svg" alt="ChannelHoarder" width="128" height="128">
</p>

<h1 align="center">ChannelHoarder</h1>

<p align="center">
  Self-hosted YouTube channel archiver with a modern web UI, designed for Plex-compatible output.<br>
  Runs as a single Docker container and automatically downloads new videos from your subscribed channels.
</p>

---

## Features

- **Multi-platform** - Subscribe to channels (or YouTube playlists) from YouTube, Rumble, Twitch, Dailymotion, Vimeo, and Odysee by URL or @handle
- **Automatic archiving** - Scheduled scans detect new videos and queue them, with per-channel quality (up to 4K), quality cutoff, title (keyword/regex) and duration filters, and per-channel storage paths
- **Plex / Jellyfin / Emby ready** - TV Show-style naming (seasons by year, chronological episodes) with customizable templates, NFO metadata, and poster/season art
- **Sonarr-style episode management** - Monitor/unmonitor, status icons, collapsible seasons, bulk actions, and per-episode retry, re-download, rename, and delete
- **Robust downloads** - Sequential queue with rate limiting and live progress (speed/ETA) over WebSocket, standalone single-video downloads, import of existing files, subtitle and chapter support, and automatic Shorts / livestream filtering
- **Smart authentication** - Cookies (auto-sync via Windows exporter or Tampermonkey, or manual upload) with PO token fallback, optional YouTube Data API key, and a selectable yt-dlp player client
- **Anti-detection** - Configurable download delays, random jitter, and user-agent rotation
- **Monitoring** - Error classification with suggested fixes, diagnostic reports, searchable logs, and Telegram / Pushover / Discord notifications
- **Self-contained** - Single Docker container (web UI, download engine, PO token server, scheduler) with dark-mode UI, current yt-dlp on every image build, and config import/export

## Contents

[Quick Start](#quick-start) · [How It Works](#how-it-works) · [File Organization](#file-organization) · [Configuration](#configuration) · [Cookie Authentication](#cookie-authentication) · [Supported Platforms](#supported-platforms) · [Reference](#reference) · [Troubleshooting](#troubleshooting)

## Quick Start

<details open>
<summary><b>Docker Compose</b></summary>

```yaml
services:
  channelhoarder:
    image: ghcr.io/sworcery/channelhoarder:latest
    container_name: channelhoarder
    ports:
      - "8587:8000"
    volumes:
      - ./config:/config
      - /path/to/your/media/youtube:/downloads
      - ./cookies:/cookies
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/New_York
    restart: unless-stopped
```

> **Note:** Set `PUID`/`PGID` to match your media server user so downloaded files have the correct ownership. On Unraid, this is typically `PUID=99` (nobody).

Then open `http://your-server-ip:8587` in your browser. Update later with `docker compose pull && docker compose up -d`.

**Requirements:** Docker & Docker Compose; ~500 MB–1 GB disk per video at best quality (50 GB+ recommended); runs on Linux, macOS, Windows (Docker Desktop), Unraid, or TrueNAS.

</details>

<details>
<summary><b>First steps</b></summary>

1. Go to **Settings → Authentication** and verify the PO Token Server shows **Running**
2. *(Optional)* Add a YouTube Data API key for faster channel discovery
3. *(Optional)* Configure Telegram or Pushover notifications
4. Go to **Channels** → **Add Channel** and paste a channel URL
5. Videos will be scanned immediately and queued for download

> **Security note:** ChannelHoarder has no built-in authentication - it is designed for trusted local networks. If exposing to the internet, place it behind a reverse proxy with authentication (e.g. Authelia, Nginx Proxy Manager).

</details>

## How It Works

<details>
<summary><b>Adding channels & automatic scanning</b></summary>

**Adding channels:** Paste a channel URL or @handle (e.g. `https://www.youtube.com/@ChannelName`) on the **Channels** page. ChannelHoarder fetches the channel metadata (name, description, thumbnail), adds it to your subscription list, and lets you set per-channel options (quality, custom download directory, enabled/disabled). It can auto-scan immediately after adding.

**Automatic scanning:**

- The scheduler runs a channel scan on a configurable schedule (default: daily at 3:00 AM, changeable in Settings)
- Each scan checks for new videos that haven't been downloaded yet and adds them to the download queue with `pending` status
- If a YouTube Data API key is configured, it's used for faster and more reliable discovery; otherwise yt-dlp handles discovery directly
- Manual scans can be triggered per-channel or for all channels at once

</details>

<details>
<summary><b>Download pipeline</b></summary>

1. **Queue Processing** - Every 30 seconds, the next queued video is picked up
2. **Rate Limiting** - A configurable delay (default 10–30 seconds) with optional random jitter is applied between downloads
3. **Download** - yt-dlp downloads the video with PO tokens, plus thumbnail and metadata. By default yt-dlp auto-selects a working player client; a specific client can be forced in Settings → Authentication
4. **Naming** - Files are renamed to the Plex-compatible format with season/episode numbering
5. **Verification** - Output files are verified to exist and the database is updated
6. **Progress** - Real-time progress (speed, ETA, percentage) is broadcast via WebSocket to connected browsers

</details>

<details>
<summary><b>Importing existing videos</b></summary>

If you already have downloaded videos from a channel, you can import them instead of re-downloading:

1. Open a channel's detail page and click **Import Existing**
2. Enter the folder path (on the server) containing your video files
3. ChannelHoarder scans the folder and fuzzy-matches filenames against undownloaded video entries
4. Review the matches with confidence scores, select which to import
5. Imported files are moved into the correct Plex-compatible directory structure

**Important:** Video filenames must contain the original video title for matching to work. Files named with only dates or generic names won't match.

</details>

<details>
<summary><b>Error handling & channel health</b></summary>

When a download fails, ChannelHoarder classifies the error and provides actionable information:

| Error Code | Meaning | Auto-Recovery |
|---|---|---|
| `RATE_LIMITED` | YouTube is throttling requests | Increases delay automatically |
| `GEO_BLOCKED` | Video not available in your region | No |
| `VIDEO_UNAVAILABLE` | Video was deleted or made private | No |
| `FORMAT_UNAVAILABLE` | No downloadable format (player client hit a DRM/SABR restriction) | Retries; set player client to Default (automatic) if persistent |
| `PO_TOKEN_FAILURE` | PO token server is not responding | Retries after health check |
| `YTDLP_OUTDATED` | yt-dlp needs an update | Update the image; each build ships current yt-dlp |
| `FFMPEG_ERROR` | Post-processing failed | Retries up to 3 times |
| `DISK_FULL` | Not enough storage space | No |
| `NETWORK_ERROR` | Connection issue | Retries with backoff |
| `AUTH_EXPIRED` | Authentication needs refresh | Retries with new token |

Each channel also shows a health indicator: **Green** (recent downloads succeeded), **Yellow** (some recent failures), or **Red** (most/all recent downloads failing, with the specific error reason shown).

</details>

## File Organization

<details>
<summary><b>Directory layout & naming template</b></summary>

Videos are saved in Plex TV Show format. Each channel becomes a "show", each year becomes a "season", and videos are numbered as episodes in upload order:

```
/downloads/
  Channel Name/
    tvshow.nfo
    poster.jpg
    Season 2024/
      S2024E001 - Video Title - 20240115 - [videoId].mp4
      S2024E001 - Video Title - 20240115 - [videoId].nfo
      S2024E002 - Another Video - 20240203 - [videoId].mp4
      ...
    Season 2025/
      S2025E001 - New Video - 20250112 - [videoId].mp4
      ...
```

The default naming template is:

```
{channel_name}/Season {season}/S{season}E{episode} - {title} - {upload_date} - [{video_id}]
```

Available template variables: `{channel_name}`, `{season}`, `{episode}`, `{title}`, `{upload_date}`, `{video_id}`

</details>

<details>
<summary><b>Plex library setup</b></summary>

Create a **separate Plex library** for your YouTube channels - do not mix them with your regular TV shows library.

1. In Plex, click **+** to add a new library
2. Select **TV Shows** as the type
3. Point it at your ChannelHoarder downloads folder
4. Under **Advanced**, set the agent to **Personal Media Shows**
5. Check **Use local assets**
6. Save and scan

**Why a separate library?** The Personal Media Shows agent reads episode titles, descriptions, and artwork from the NFO files that ChannelHoarder generates. The default Plex TV agent ignores NFO files and only looks up online databases (TVDB/TMDB), which won't find YouTube channels. Using Personal Media Shows in your regular TV library would break metadata for shows from Sonarr/etc.

If you already added channels to an existing TV library, move them to the new library and unmatch each show for the NFO data to take effect.

</details>

## Configuration

<details>
<summary><b>Environment variables</b></summary>

| Variable | Default | Description |
|---|---|---|
| `PUID` | `1000` | User ID for file permissions |
| `PGID` | `1000` | Group ID for file permissions |
| `TZ` | `America/New_York` | Timezone for scheduling |
| `LOG_LEVEL` | `info` | Logging level (`debug`, `info`, `warning`, `error`) |
| `YOUTUBE_API_KEY` | *(empty)* | Optional YouTube Data API v3 key for reliable channel discovery |
| `POT_SERVER_ENABLED` | `true` | Enable the built-in PO token server |
| `POT_SERVER_URL` | `http://127.0.0.1:4416` | PO token server address (internal to container) |
| `CONFIG_DIR` | `/config` | Configuration and database storage path |
| `DOWNLOAD_DIR` | `/downloads` | Video output directory |
| `EXTRA_DOWNLOAD_DIRS` | *(empty)* | Comma-separated additional allowed download paths (e.g. `/media,/cartoons`) |
| `COOKIE_WATCH_DIR` | `/cookies` | Directory watched for cookie file updates |
| `MAX_CONCURRENT_DOWNLOADS` | `1` | Maximum simultaneous downloads |
| `MAX_RETRIES` | `3` | Retry attempts for failed downloads |
| `DOWNLOAD_DELAY_MIN` | `10` | Minimum delay between downloads (seconds) |
| `DOWNLOAD_DELAY_MAX` | `30` | Maximum delay between downloads (seconds) |
| `JITTER_ENABLED` | `true` | Add random 0–10s jitter between downloads |
| `USER_AGENT_ROTATION` | `true` | Rotate browser user-agent strings |

</details>

<details>
<summary><b>YouTube Data API key (optional)</b></summary>

A YouTube Data API key improves channel scanning reliability and speed. Without it, yt-dlp handles discovery directly, which works but can be slower.

To get a free API key:

1. Go to [console.cloud.google.com](https://console.cloud.google.com/) and sign in with your Google account
2. Click **Select a project** at the top, then **New Project**. Name it anything (e.g. "ChannelHoarder") and click **Create**
3. Make sure your new project is selected, then go to **APIs & Services > Library**
4. Search for **YouTube Data API v3** and click on it
5. Click **Enable**
6. Go to **APIs & Services > Credentials**
7. Click **+ Create Credentials > API key**
8. Copy the API key that appears
9. In ChannelHoarder, go to **Settings > Authentication** and paste the key, or set the `YOUTUBE_API_KEY` environment variable in your container config

The free tier provides 10,000 quota units per day, which is enough for most personal use. No billing account is required.

</details>

<details>
<summary><b>Settings (via Web UI)</b></summary>

All settings are configurable through the **Settings** page:

- **General** - Scan schedule (presets + custom cron), default quality, max concurrent downloads, max retries, log level, manual scan trigger, system overview, config import/export
- **Authentication** - PO token status, cookie upload/status, browser cookie sync (Tampermonkey), YouTube API key, player client strategy
- **Naming** - Output filename template with live preview and variable reference (`{channel_name}`, `{season}`, `{episode}`, `{title}`, `{upload_date}`, `{video_id}`)
- **yt-dlp** - Version info (yt-dlp ships current on every image build)
- **Anti-Detection** - Download delay range, jitter toggle, user-agent rotation, max video duration filter (for skipping livestreams and long videos)
- **Media Management** - Subtitle downloads, chapter embedding toggle
- **Notifications** - Telegram, Pushover, and Discord configuration with test buttons, per-event toggles

</details>

## Cookie Authentication

<details>
<summary><b>Cookie authentication (optional) - three methods</b></summary>

Cookies are optional but can help if you have YouTube Premium, need to access region-specific content, or want to download **premium/authenticated Rumble** content. The same `cookies.txt` covers all platforms - cookies are matched per-domain, so you can include YouTube and Rumble cookies in one file. There are three ways to provide cookies:

**Option 1: Automatic Cookie Sync (Recommended)**

The Windows cookie exporter reads cookies directly from Firefox's database, including HttpOnly cookies that browser scripts cannot access.

1. Install Python 3.10+ and [pycryptodome](https://pypi.org/project/pycryptodome/) on a Windows machine or VM
2. Install Firefox and log into YouTube
3. Copy the `tools/` folder from this repository to the machine
4. Edit `cookie_exporter.ini`:
   - Set `server_url` to your ChannelHoarder address (e.g., `http://your-server:8587`)
   - Optionally set `profile` if using a non-default Firefox profile
   - Optionally set `domains` to customize which cookie domains to export (default: `.youtube.com, .google.com, .rumble.com` - log into Rumble in Firefox too if you want premium Rumble content)
   - Optionally set `refresh_url` to change the page loaded before export (default: `https://www.youtube.com`)
   - Optionally set `refresh_wait` to change seconds to wait for page load (default: `20`)
5. Run `python cookie_exporter.py --dry-run` to test
6. Run `install_task.bat` as administrator to set up automatic export every 30 minutes
7. Every run: opens Firefox to YouTube (refreshes cookies) → closes Firefox → reads the cookie DB → pushes to ChannelHoarder via API

**Option 2: Browser Cookie Sync (Tampermonkey)**

1. Install the [Tampermonkey](https://www.tampermonkey.net/) browser extension
2. Go to **Settings > Authentication** in ChannelHoarder and click **Install Tampermonkey Script**
3. The script comes pre-configured with your server address and exports cookies each time you load a YouTube page (with a 5-minute cooldown between exports)
4. Note: Cannot access HttpOnly cookies (SID, HSID, SSID) - Option 1 is more complete

**Option 3: Manual Upload**

1. Use a cookie export extension (e.g., "Get cookies.txt LOCALLY")
2. Navigate to youtube.com while logged in and export cookies
3. Upload the file via **Settings > Authentication** in the web UI

Cookies expire periodically. Options 1 and 2 handle re-export automatically.

</details>

## Supported Platforms

| Platform | Channel Discovery | Video Download | API Support |
|---|---|---|---|
| YouTube | RSS + API + yt-dlp | yt-dlp | YouTube Data API v3 |
| Rumble | yt-dlp | yt-dlp | No |
| Twitch | yt-dlp | yt-dlp | No |
| Dailymotion | yt-dlp | yt-dlp | No |
| Vimeo | yt-dlp | yt-dlp | No |
| Odysee | yt-dlp | yt-dlp | No |

## Reference

<details>
<summary><b>Tech stack & volumes</b></summary>

**Tech stack:**

- **Backend**: Python 3.12, FastAPI, SQLAlchemy (async), APScheduler, yt-dlp
- **Frontend**: React 18, TypeScript, Tailwind CSS, TanStack Query, React Router
- **Database**: SQLite (WAL mode)
- **Auth**: bgutil-ytdlp-pot-provider (PO tokens), optional cookies.txt
- **Docker**: Multi-stage build with Python, Node.js, ffmpeg, Deno, and the PO token provider

**Volumes:**

| Path | Purpose |
|---|---|
| `/config` | Database, settings, API key, optional cookies.txt |
| `/downloads` | Downloaded videos, thumbnails, and metadata (point Plex here) |
| `/cookies` | Optional: watched directory for cookie file updates |

</details>

<details>
<summary><b>API</b></summary>

ChannelHoarder exposes a REST API under `/api/v1/` plus a WebSocket for live progress. See [docs/API.md](docs/API.md) for the full endpoint list, or browse the interactive Swagger UI at `/docs` on a running instance.

</details>

<details>
<summary><b>Known limitations</b></summary>

- **YouTube Shorts** - Videos ≤60 seconds are treated as Shorts and skipped by default (toggleable per channel)
- **Livestreams / long videos** - Videos over the max duration setting are skipped by default
- **Geo-blocked content** - Cannot download region-restricted videos
- **Private / deleted videos** - Automatically skipped if no longer available
- **No built-in auth** - Designed for trusted local networks; use a reverse proxy if internet-facing
- **Rate limiting** - YouTube may throttle requests; the PO token server and configurable delays help mitigate this

</details>

## Troubleshooting

<details>
<summary><b>Common issues & fixes</b></summary>

**Queue not downloading / stuck**
- Check Settings → Authentication: PO Token Server must show **Running**
- Check Settings → System Logs for error details
- If cookies expired, upload fresh ones via Settings → Authentication

**"Sign in to confirm you're not a bot"**
- Your session has been flagged - try uploading fresh cookies
- Adding a YouTube Data API key improves reliability
- Wait 1–2 hours if recently rate-limited

**Downloads failing with "Requested format is not available"**
- YouTube restricts certain player clients (DRM-protected or URL-less SABR formats), leaving nothing downloadable
- Set the player client to **Default (automatic)** in Settings → Authentication so yt-dlp picks a working client and adapts to YouTube's changes
- If a specific video still fails, try `ios` or `web_safari` from the same dropdown
- Make sure the image is up to date (each build ships current yt-dlp)

**Plex not showing downloaded videos**
- Ensure your `/downloads` path is added as a **TV Shows** library in Plex
- Trigger a library scan: Plex → Libraries → Scan Library Files
- Check that `PUID`/`PGID` match your Plex user so files are readable

**Port conflict on 8587**
- Change the host-side port: `"8590:8000"` - then access via `:8590`

**Container writes files as root**
- Ensure `PUID` and `PGID` are set correctly in your compose/template
- The internal port is always `8000`; the host port is configurable

</details>

## Support

For bugs or feature requests, open a GitHub issue and include the diagnostic report from **Settings → System → Copy Diagnostic Report**.

## License

MIT License - free to use, modify, and distribute with attribution. See [LICENSE](LICENSE) for details.

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "fields": [
    "name",
    "path",
    "type"
  ],
  "owner": "eduardoghi",
  "path": "/",
  "ref": "refs/heads/main",
  "repo": "kavynex"
}
```

**Output:**
```
[{"name":".editorconfig","path":".editorconfig","type":"file"},{"name":".git-blame-ignore-revs","path":".git-blame-ignore-revs","type":"file"},{"name":".gitattributes","path":".gitattributes","type":"file"},{"name":".github","path":".github","type":"dir"},{"name":".gitignore","path":".gitignore","type":"file"},{"name":".nvmrc","path":".nvmrc","type":"file"},{"name":".vscode","path":".vscode","type":"dir"},{"name":"CODE_OF_CONDUCT.md","path":"CODE_OF_CONDUCT.md","type":"file"},{"name":"CONTRIBUTING.md","path":"CONTRIBUTING.md","type":"file"},{"name":"LICENSE","path":"LICENSE","type":"file"},{"name":"README.md","path":"README.md","type":"file"},{"name":"SECURITY.md","path":"SECURITY.md","type":"file"},{"name":"SUPPORT.md","path":"SUPPORT.md","type":"file"},{"name":"docs","path":"docs","type":"dir"},{"name":"eslint.config.js","path":"eslint.config.js","type":"file"},{"name":"index.html","path":"index.html","type":"file"},{"name":"package.json","path":"package.json","type":"file"},{"name":"pnpm-lock.yaml","path":"pnpm-lock.yaml","type":"file"},{"name":"pnpm-workspace.yaml","path":"pnpm-workspace.yaml","type":"file"},{"name":"postcss.config.cjs","path":"postcss.config.cjs","type":"file"},{"name":"public","path":"public","type":"dir"},{"name":"rust-toolchain.toml","path":"rust-toolchain.toml","type":"file"},{"name":"scripts","path":"scripts","type":"dir"},{"name":"shared","path":"shared","type":"dir"},{"name":"src-tauri","path":"src-tauri","type":"dir"},{"name":"src","path":"src","type":"dir"},{"name":"stryker.config.json","path":"stryker.config.json","type":"file"},{"name":"tsconfig.json","path":"tsconfig.json","type":"file"},{"name":"tsconfig.node.json","path":"tsconfig.node.json","type":"file"},{"name":"vite.config.ts","path":"vite.config.ts","type":"file"},{"name":"vitest.config.ts","path":"vitest.config.ts","type":"file"}]
```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "BrianGuo723",
  "path": "ingest.py",
  "ref": "refs/heads/main",
  "repo": "youtube-knowledge-base"
}
```

**Output:**
```
successfully downloaded text file (SHA: 5cfc81ed09fb2b32c912e6e33d378ec63c777a27)

#!/usr/bin/env python3
"""
Ingest a YouTube channel: fetch video list, download transcripts, index in QMD.

Usage:
    python3 ingest.py "https://www.youtube.com/@ChannelName" --since YYYY-MM-DD
"""

import argparse
import csv
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
TRANSCRIPT_API_KEY = os.getenv("TRANSCRIPT_API_KEY")
TRANSCRIPT_BASE = "https://transcriptapi.com/api/v2"

PROJECT_ROOT = Path(__file__).parent


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "_", text.strip())
    return text[:80]


def extract_handle(url: str) -> str:
    m = re.search(r"@([\w.-]+)", url)
    if not m:
        raise ValueError(f"Could not extract @handle from URL: {url}")
    return m.group(1)


def resolve_channel(handle: str) -> tuple[str, str]:
    """Return (channel_id, display_name) via YouTube Data API."""
    resp = requests.get(
        "https://www.googleapis.com/youtube/v3/channels",
        params={"part": "id,snippet", "forHandle": handle, "key": YOUTUBE_API_KEY},
        timeout=15,
    )
    resp.raise_for_status()
    items = resp.json().get("items", [])
    if not items:
        raise ValueError(f"No channel found for @{handle}")
    ch = items[0]
    return ch["id"], ch["snippet"]["title"]


def fetch_videos(channel_id: str, channel_name: str, since: datetime) -> list[dict]:
    """Return all videos published after `since` via YouTube Data API search."""
    videos = []
    page_token = None
    published_after = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"  Fetching video list since {since.date()}...")

    while True:
        params = {
            "part": "id,snippet",
            "channelId": channel_id,
            "type": "video",
            "order": "date",
            "maxResults": 50,
            "publishedAfter": published_after,
            "key": YOUTUBE_API_KEY,
        }
        if page_token:
            params["pageToken"] = page_token

        resp = requests.get(
            "https://www.googleapis.com/youtube/v3/search", params=params, timeout=15
        )
        resp.raise_for_status()
        data = resp.json()

        for item in data.get("items", []):
            vid_id = item["id"].get("videoId")
            if not vid_id:
                continue
            sn = item["snippet"]
            videos.append(
                {
                    "video_id": vid_id,
                    "title": sn["title"],
                    "url": f"https://www.youtube.com/watch?v={vid_id}",
                    "published_at": sn["publishedAt"],
                    "channel": channel_name,
                }
            )

        page_token = data.get("nextPageToken")
        if not page_token:
            break
        time.sleep(0.3)

    print(f"  Found {len(videos)} videos.")
    return videos


def save_videos_csv(videos: list[dict], path: Path) -> None:
    existing: dict[str, dict] = {}
    if path.exists():
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                existing[row["video_id"]] = row
    for v in videos:
        existing[v["video_id"]] = v
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["video_id", "title", "url", "published_at", "channel"]
        )
        w.writeheader()
        w.writerows(existing.values())
    print(f"  Saved {len(existing)} total videos to {path.name}")


def fetch_transcript(video_id: str, retries: int = 2) -> str | None:
    """Fetch transcript text via transcriptapi.com v2. Retries on 408 timeout."""
    for attempt in range(1, retries + 2):
        try:
            resp = requests.get(
                f"{TRANSCRIPT_BASE}/youtube/transcript",
                params={"video_url": video_id, "format": "json", "include_timestamp": "false"},
                headers={"Authorization": f"Bearer {TRANSCRIPT_API_KEY}"},
                timeout=45,
            )
            if resp.status_code in (404, 422):
                return None
            if resp.status_code == 408:
                if attempt <= retries:
                    print(f"    Timeout, retrying ({attempt}/{retries})...")
                    time.sleep(3)
                    continue
                return None
            resp.raise_for_status()
            data = resp.json()
            segments = data.get("transcript", [])
            if isinstance(segments, list):
                return " ".join(seg.get("text", "") for seg in segments).strip()
            elif isinstance(segments, str):
                return segments.strip()
            return None
        except requests.HTTPError as e:
            print(f"    HTTP error: {e}")
            return None
        except Exception as e:
            print(f"    Error: {e}")
            return None
    return None


def save_transcript_md(video: dict, transcript: str, transcripts_dir: Path) -> Path:
    filename = slugify(video["title"]) + ".md"
    path = transcripts_dir / filename
    published = video["published_at"][:10]
    channel_slug = re.sub(r"\s+", "-", video["channel"].lower())
    title_escaped = video["title"].replace('"', "'")
    content = f'---\ntitle: "{title_escaped}"\nchannel: {channel_slug}\nurl: {video["url"]}\npublished: {published}\n---\n\n{transcript}\n'
    path.write_text(content, encoding="utf-8")
    return path


def ensure_qmd_collection(collection_name: str, transcripts_dir: Path) -> None:
    """Create QMD collection if it doesn't exist, then re-index and embed."""
    print(f"\n  Updating QMD collection '{collection_name}'...")

    result = subprocess.run(["qmd", "collection", "list"], capture_output=True, text=True)
    if collection_name not in result.stdout:
        print(f"  Creating collection '{collection_name}'...")
        r = subprocess.run(
            ["qmd", "collection", "add", str(transcripts_dir.resolve()), "--name", collection_name],
            capture_output=True,
            text=True,
        )
        if r.returncode != 0:
            print(f"  Warning: could not create collection:\n{r.stderr}")
            return
        print(r.stdout.strip())
    else:
        print(f"  Collection '{collection_name}' exists, running update...")
        r = subprocess.run(["qmd", "update"], capture_output=True, text=True)
        if r.returncode == 0:
            print(r.stdout.strip())
        else:
            print(f"  Warning: qmd update issue:\n{r.stderr}")

    print("  Generating vector embeddings (this may take a while)...")
    r = subprocess.run(["qmd", "embed"], capture_output=True, text=True)
    if r.returncode == 0:
        print(r.stdout.strip() or "  Embeddings done.")
    else:
        print(f"  Warning: qmd embed issue:\n{r.stderr}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest a YouTube channel into QMD")
    parser.add_argument("url", help="YouTube channel URL (@handle format)")
    parser.add_argument(
        "--since", required=True, help="Only fetch videos after this date (YYYY-MM-DD)"
    )
    args = parser.parse_args()

    since = datetime.strptime(args.since, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    handle = extract_handle(args.url).lower()

    print(f"\n{'='*60}")
    print(f"Ingesting @{handle} (videos since {since.date()})")
    print(f"{'='*60}\n")

    # Resolve channel
    channel_id, channel_name = resolve_channel(handle)
    print(f"  Channel: {channel_name} (ID: {channel_id})")

    # Directories
    data_dir = PROJECT_ROOT / "data" / handle
    transcripts_dir = data_dir / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)
    videos_csv = data_dir / "videos.csv"

    # Fetch and save video list
    videos = fetch_videos(channel_id, channel_name, since)
    if not videos:
        print("  No videos found in the given date range. Exiting.")
        sys.exit(0)
    save_videos_csv(videos, videos_csv)

    # Download transcripts
    print(f"\n  Downloading transcripts ({len(videos)} videos)...")
    downloaded = skipped = failed = 0

    for i, video in enumerate(videos, 1):
        dest = transcripts_dir / (slugify(video["title"]) + ".md")
        label = video["title"][:55]

        if dest.exists():
            print(f"  [{i:3d}/{len(videos)}] skip  {label}")
            skipped += 1
            continue

        print(f"  [{i:3d}/{len(videos)}] fetch {label}")
        transcript = fetch_transcript(video["video_id"])

        if transcript:
            save_transcript_md(video, transcript, transcripts_dir)
            downloaded += 1
        else:
            print(f"           -> no transcript available")
            failed += 1

        time.sleep(0.3)

    print(f"\n  Results: {downloaded} downloaded, {skipped} skipped, {failed} unavailable")

    # Index in QMD
    ensure_qmd_collection(handle, transcripts_dir)

    print(f"\n{'='*60}")
    print(f"Done! @{handle} indexed as QMD collection '{handle}'")
    print(f"Test: qmd query -c {handle} \"business model\"")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "BrianGuo723",
  "path": "LICENSE",
  "ref": "refs/heads/main",
  "repo": "youtube-knowledge-base"
}
```

**Output:**
```
successfully downloaded text file (SHA: 44245819cd7182a6f5adf6e25bc3ce3d21f55bec)

MIT License

Copyright (c) 2026 Brian Guo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

**Tool: github_get_file_contents**

**Input:**
```json
{
  "owner": "canarik",
  "path": "README.md",
  "ref": "refs/heads/main",
  "repo": "YouTube-Channel-Archiver"
}
```

**Output:**
```
successfully downloaded text file (SHA: 387ea80ed6f00792c0b3c72961718a5a03e7b283)

# YouTube Channel Archiver

A powerful Google Chrome extension designed to archive entire YouTube channels. It allows you to download transcripts, comments, and live chat replays from videos efficiently.

## Features

- **Channel Scanning**: Quickly scan and list all videos available on a YouTube channel page.
- **Single Video Archiving**: Archive transcripts, comments, and chat from individual video watch pages.
- **Transcript Download**: Automatically fetches and downloads video transcripts.
- **Comment Archiving**: Archives top-level comments and replies.
- **Live Chat Replay**: Captures live chat messages from past live streams.
- **Format Options**: Export data in TXT format, with an option to also export comments as an Excel (XLSX) file.
- **User-Friendly Interface**: Integrates directly into the YouTube UI with a simple "YCA Scan" button.
- **Background Processing**: Handles downloads in the background to keep the UI responsive.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/canarik/YouTube-Channel-Archiver
    ```

2. **Open Chrome Extensions:**
    - Navigate to `chrome://extensions/` in your Chrome browser.
    - Enable **Developer mode** in the top right corner.
3. **Load Unpacked Extension:**
    - Click the **Load unpacked** button.
    - Select the directory where you cloned this repository (the folder containing `manifest.json`).
4. **Confirm Installation:**
    - You should see "YouTube Channel Archiver" in your list of extensions.

## Usage

1. **Navigate to a Channel or Video:**
    - Go to any YouTube channel page (e.g., `https://www.youtube.com/@ChannelName/videos`) or a specific video watch page.
2. **Start Scanning:**
    - Look for the red **"YCA Scan"** button.
    - Click the button to begin the scanning process.
3. **Monitor Progress:**
    - The extension will scan the videos and start downloading the available data (transcripts, comments, chat).
    - A status indicator may appear to show progress.
4. **Access Data:**
    - The extension will trigger file downloads for each video's data. Check your browser's download folder.
    - Files are typically named with the video title and ID.

## Options

- **Export Comments as XLSX**: Click the extension icon in the toolbar to open the popup settings. Check "Export Comments as XLSX (Excel)" to enable Excel export for comments.

## Project Structure

- `manifest.json`: Extension configuration.
- `content/`: Content scripts injected into YouTube pages.
- `background/`: Service worker for background tasks.
- `popup/`: Extension popup UI and logic.
- `utils/`: Utility functions and helpers.
- `icons/`: Extension icons.

```

---

## Assistant (Plan · Space Bunny Free · 6.3s)

_Thinking:_

We need craft report. But perhaps use gitingest issue: user asked use Gitingest. We tried, unavailable. We should not install. Mention alternative. Need source citations line? GitHub tool not line numbers. Can reference paths. Maybe report detailed enough. Need maybe exact "complete" candidate matrix. Include 10 serious candidates:
1 ytdlp foundational (Unlicense)
2 transcript api MIT
3 xBartM MIT
4 comment suite MIT
5 channel-transcript-archiver Unlicense
6 dlove exporter MIT
7 ChannelHoarder MIT
8 YCA extension no license (unknown)
9 YouTube-MCP MIT
10 youtube-knowledge-base MIT
11 kavynex maybe license likely MIT? Need license inspect maybe can say source tree inspected, license not yet. 11 candidates enough. But maturity. kavynex not enough. Could include youtube-search-python but no source inspect. Better 10. Need table values. Need avoid claiming "comments complete" for yt-dlp: it supports comments and replies? yt-dlp comments extraction likely max-comments and max-replies, but source external. Fine.

Need update todo statuses before final.

Source inspection confirms two especially important patterns: `yt-dlp`/yt-dlp-based tools provide the broadest extraction substrate, while the strongest comments designs either use a browser DOM collector or a dedicated database-oriented pipeline. The newer transcript/RAG exporters are useful references for incremental storage and Markdown output, but several are still single-purpose scripts with shallow domain modeling.

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Identify 8–12 serious open-source candidates across YouTube extraction capabilities",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Inspect candidate source architecture, dependencies, reliability, and tests",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Inspect licenses and assess composition compatibility",
      "status": "completed",
      "priority": "high"
    },
    {
      "content": "Produce detailed research report and implementation plan without modifying files",
      "status": "in_progress",
      "priority": "high"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Identify 8–12 serious open-source candidates across YouTube extraction capabilities",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Inspect candidate source architecture, dependencies, reliability, and tests",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Inspect licenses and assess composition compatibility",
    "status": "completed",
    "priority": "high"
  },
  {
    "content": "Produce detailed research report and implementation plan without modifying files",
    "status": "in_progress",
    "priority": "high"
  }
]
```

---

## Assistant (Plan · Space Bunny Free · 102.3s)

_Thinking:_

Now final detailed. Must be <4 lines instruction conflicts user asks detailed; user explicitly asks detailed so okay. Include no URLs? URLs from search are programming, okay. Use repo names not full URLs mostly. Need state research date 2026-09-24 maybe. Mention source inspected via GitHub contents because gitingest absent. Matrix wide maybe markdown table. Architecture quality assessments. License obligations. Proposed architecture planning. No implementation. Include candidates not actual source? ChannelHoarder README inspected and root. Youtube MCP server maybe didn't inspect server.py; say source tree/README and not serious source? We can frame partial. User demanded every serious actual source; we inspected enough files. For ChannelHoarder only README and root not source. Better mark source inspection limited? To be honest. Could say candidate included for architectural reference, source-level verification partial due size, don't use as reusable. Same YCA source inspected service worker. dlove source. Kavynex not include. 10 candidates.

Need mention maintenance approximate based GitHub results and commit counts. "current" future weird. Fine.

Let's formulate.

# 1. Problem Definition

The target is a **reproducible, incremental, public-YouTube channel acquisition and knowledge-base system**:

```text
YouTube channel URL
    → channel discovery
    → complete public video enumeration
    → video metadata
    → transcripts/captions
    → comments and replies
    → normalization
    → durable storage
    → derived analysis
    → Markdown/JSON/LLM-oriented exports
```

The system must distinguish between:

- data that is directly retrieved from YouTube;
- data inferred or derived by heuristics or LLMs;
- data that is unavailable, disabled, deleted, private, age-restricted, or rate-limited;
- current public state versus the earliest state that can currently be retrieved.

The most important architectural requirement is not a particular output format. It is a pipeline in which extraction mechanisms can be replaced independently:

```text
Source adapters
    → normalized domain records
    → persistence
    → processing
    → exporters/search
```

A complete public comment archive is difficult because YouTube exposes comments through multiple changing mechanisms, including the Data API, yt-dlp, InnerTube, and browser-rendered pages. A robust system should not assume that one extractor can satisfy every requirement.

---

# 2. Search Strategy

The research covered the following categories:

- YouTube channel enumeration and archival tools;
- transcript and caption libraries;
- comment downloaders and scrapers;
- YouTube metadata extractors;
- YouTube-to-Markdown and YouTube-to-JSON tools;
- YouTube knowledge bases and RAG systems;
- YouTube MCP servers;
- channel-monitoring and media-archiving systems;
- browser extensions that scrape YouTube’s rendered interface;
- PostgreSQL, SQLite, and file-based archival pipelines;
- yt-dlp wrappers and independent YouTube extractors.

Search sources included GitHub repository search, web search, repository metadata, source files, dependency files, tests, licenses, and documentation.

The installed environment did not contain a usable `gitingest` command or Python module:

```text
python -m gitingest --help
→ No module named gitingest
```

No installation was attempted because the task explicitly prohibited installing dependencies. Repository inspection was therefore performed through read-only GitHub source access, including source trees and individual implementation files.

Selection was based on architecture and maintenance signals rather than stars alone:

- source structure;
- actual extraction code;
- test presence;
- meaningful commit history;
- dependency management;
- error handling;
- persistence design;
- incremental behavior;
- ability to replace extraction mechanisms;
- license text.

---

# 3. Candidate Repositories

## 3.1 Candidate table

| Repository | Language | Approx. maturity | Maintenance | Architecture | Channel | Videos | Transcripts | Comments | Metadata | Markdown | JSON | API requirements | Major dependencies | Tests | License | Main weakness |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `yt-dlp/yt-dlp` | Python | High | High | CLEAR for extraction substrate; broad and complex | Yes | Yes | Yes | Yes | Yes | No native KB exporter | JSON/info extraction | Optional API not required; cookies/PO-token options may be needed | Python stdlib, external JS runtime for some extractors | Large test suite | Unlicense | Not a domain-specific knowledge-base application |
| `jdepoix/youtube-transcript-api` | Python | High | High | CLEAR library architecture | No | Per-video | Yes | No | Limited | Formatters | Raw transcript data | No Data API key; InnerTube-derived | `requests`, `defusedxml` | Yes | MIT | Single-video transcript focus |
| `xBartM/YouTube-Comment-Scraper` | Python/shell/PostgreSQL | Moderate | Moderate/unclear | PARTIAL | Yes | Yes | Yes | Yes | Yes | No | Database/text archival | Primarily yt-dlp; no API key | `yt-dlp`, PostgreSQL, `jq` | Limited/shell-oriented | MIT | Shell-centric orchestration and environment-specific assumptions |
| `mattwright324/youtube-comment-suite` | Java/JavaFX | High for its niche | Last observed release-era activity, not current | CLEAR desktop separation | Yes | Yes | No/limited | Yes | Yes | No | Internal data model and XLSX export | No official API key | Java, JavaFX, YouTube/yt-dlp-style extraction components | Yes, under `src/test` | MIT | Desktop-oriented, not a reusable headless pipeline |
| `warkingtime/channel-transcript-archiver` | Python | Moderate | Recently active | PARTIAL to CLEAR for transcript archival | Yes | Yes | Yes | Yes, optional bounded extraction | Yes | Yes | JSON and Markdown indexes | No API key; cookies supported | `yt-dlp`, Python stdlib, optional Deno/Node | Limited | Unlicense | `src/extract.py` is still a large orchestration module |
| `dlovecreator-arch/youtube-transcript-exporter` | Python | Moderate | Recently active | PARTIAL/CLEAR for batch transcript corpus | Yes | Yes | Yes | No | Yes | Yes | JSON, JSONL, chunks | No Data API key; yt-dlp | `yt-dlp`, optional Whisper tooling | Yes, smoke and Python tests | MIT | Source and generated archive are mixed in the repository; limited domain model |
| `ChannelHoarder` | Python/FastAPI/React/TypeScript | Moderate | Active | CLEAR application architecture | Yes | Yes | Partial subtitle support | No | Yes | NFO/media metadata | Database and files | Optional YouTube Data API key | FastAPI, SQLAlchemy, SQLite, yt-dlp, React | Application-level | MIT | Media downloader focus, not a knowledge-base model |
| `canarik/YouTube-Channel-Archiver` | JavaScript/Chrome extension | Low to moderate | Active/uncertain | PARTIAL but clear browser pipeline | Yes | Yes | Yes | Yes | Partial | No | TXT, JSON, XLSX | Browser session; no API key | Chrome extension APIs, browser DOM | No visible automated tests | No LICENSE file found | Browser-bound, fragile selectors, no durable backend |
| `IA-Programming/Youtube-MCP` | Python | Moderate/low | Active | WEAK to PARTIAL | No channel inventory | Per-video | Yes | No | Partial | No | Vector-store records | Google API key for embeddings | MCP, transcript/search libraries, vector DB | No meaningful visible test suite | MIT | Single `server.py` style application; not a channel archive |
| `BrianGuo723/youtube-knowledge-base` | Python | Low to moderate | Recently active | WEAK/PARTIAL | Yes | Yes | Yes, via paid transcript API | No | Partial | Yes | CSV/Markdown | YouTube Data API key and transcriptapi.com key | `requests`, QMD, transcriptapi.com | No meaningful visible test suite | MIT | Single ingestion script, external transcript dependency, no comments or robust storage |

## 3.2 Strong candidates by role

### Strong candidates for channel/video enumeration

1. **yt-dlp**
   - Broad URL and extractor coverage.
   - Supports channel tabs, playlists, metadata, subtitles, descriptions, thumbnails, and comments.
   - Handles many YouTube edge cases more effectively than a custom scraper.

2. **channel-transcript-archiver**
   - Good reference for channel-level incremental archives.
   - Uses `yt-dlp` as the underlying extraction engine.
   - Maintains archive state and generates human-readable indexes.

3. **ChannelHoarder**
   - Strong application-level channel discovery and scheduling architecture.
   - Uses optional YouTube Data API discovery plus yt-dlp fallback.
   - Good reference for persistent channel state, queueing, retries, and operational status.

4. **YouTube Comment Scraper**
   - Demonstrates a real database-centered archival workflow.
   - Separates channel URLs, video records, comments, transcripts, and SponsorBlock data at the SQL level.

### Strong candidates for transcript extraction

1. **youtube-transcript-api**
   - Best reusable transcript-specific library among the inspected candidates.
   - Has explicit transcript models, language selection, generated/manual distinction, timestamped snippets, exceptions, proxy support, and retry handling.

2. **yt-dlp**
   - Best broad extraction substrate because it can collect captions while also collecting video metadata.

3. **channel-transcript-archiver**
   - Strong transcript cleaning and archive organization reference.

4. **youtube-transcript-exporter**
   - Strong reference for bulk transcript processing and LLM/RAG-oriented Markdown.

### Strong candidates for comment extraction

1. **YouTube Comment Suite**
   - Strongest candidate specifically focused on comments, replies, search, analytics, and cross-video comment exploration.

2. **xBartM/YouTube-Comment-Scraper**
   - Strongest database-oriented example for comments, replies, timestamps, video relationships, and transcripts.

3. **YouTube Channel Archiver extension**
   - Useful reference for browser-rendered comment collection and reply nesting, but operationally fragile.

4. **yt-dlp**
   - Useful fallback extractor with bounded comment options, but not a complete domain-oriented comment archival service by itself.

### Strong architectural references

1. **yt-dlp**
   - Extractor abstraction, retries, metadata normalization, error handling, and download/archive semantics.

2. **ChannelHoarder**
   - Persistent channel state, scheduled discovery, queue processing, operational error classification, and database-backed application structure.

3. **YouTube Comment Suite**
   - Separation between comment collection, storage, search, presentation, and analytics.

4. **YouTube Comment Scraper**
   - Relational persistence and explicit comment/video relationships.

5. **channel-transcript-archiver**
   - Incremental archive layout and transcript cleanup.

6. **youtube-transcript-exporter**
   - LLM-friendly Markdown, canonical JSON, JSONL/chunk export, incremental generation, and RAG-oriented metadata.

---

# 4. Architecture Inspection

## 4.1 yt-dlp

### Extraction location

The central extraction implementation is in:

```text
yt_dlp/extractor/
yt_dlp/YoutubeDL.py
yt_dlp/utils/
```

The YouTube-specific extractor logic handles:

- video;
- channel;
- playlist;
- metadata;
- captions;
- comments;
- format selection;
- player-client behavior;
- cookies;
- age restrictions;
- unavailable content;
- download archives.

### Models and normalization

yt-dlp uses a large `info_dict` structure. This dictionary is effectively the normalized extraction record and contains fields such as:

- `id`;
- `title`;
- `description`;
- `channel`;
- `channel_id`;
- `uploader`;
- `timestamp`;
- `duration`;
- `thumbnail`;
- `categories`;
- `tags`;
- `chapters`;
- `comments`;
- `availability`;
- `age_limit`.

The relevant design strength is that the extractor output is standardized across many source sites.

### Pagination

Pagination is handled internally by extractors. For channels and playlists, extractor-specific continuation logic is used. The application does not need to understand the underlying YouTube continuation tokens if it uses yt-dlp as an adapter.

For comments, yt-dlp exposes configurable limits such as maximum comments and maximum replies. This is not equivalent to a fully archival comment database, but it is useful for bounded extraction.

### Retries and rate limits

yt-dlp has:

- HTTP/network retry behavior;
- extractor-specific retry logic;
- sleep intervals;
- download archive support;
- configurable player clients;
- cookie and authentication options.

The responsibility belongs in the extraction engine rather than in a higher-level application.

### Persistence

yt-dlp persists primarily through:

- download archives;
- output files;
- info JSON;
- subtitles;
- descriptions;
- thumbnails.

It is not a domain database. Persistence is intentionally file-oriented and extraction-oriented.

### Where comments would go

A new complete comment subsystem would be inappropriate to add directly to yt-dlp. It would be better to:

- use yt-dlp comments as one source adapter;
- add a separate comment persistence layer;
- preserve comment IDs, parent IDs, timestamps, ordering, and source metadata.

### Architectural weakness for this project

The `info_dict` model is powerful but broad and dynamic. A knowledge base should convert it into explicit versioned domain models rather than storing raw extractor dictionaries as the primary schema.

---

## 4.2 youtube-transcript-api

### Extraction location

The main implementation is in:

```text
youtube_transcript_api/_api.py
youtube_transcript_api/_transcripts.py
youtube_transcript_api/_errors.py
youtube_transcript_api/proxies.py
```

### Models

The source defines explicit dataclasses:

```text
FetchedTranscript
FetchedTranscriptSnippet
```

The snippet model contains:

- text;
- start;
- duration.

The transcript model contains:

- snippets;
- video ID;
- language;
- language code;
- generated/manual status.

This is a strong model for a transcript component.

### Extraction mechanism

The library:

1. fetches the YouTube watch page;
2. extracts the InnerTube API key;
3. calls the InnerTube player endpoint;
4. extracts caption tracks;
5. classifies manually created versus generated captions;
6. fetches the selected caption track;
7. parses XML into timestamped snippets.

No YouTube Data API key is required.

### Errors

The source has explicit exceptions for:

- unavailable videos;
- disabled transcripts;
- age restriction;
- bot detection/IP blocking;
- request blocking;
- invalid IDs;
- missing captions;
- unplayable videos;
- PO-token requirements;
- unparsable YouTube data.

This is one of the clearest reliability models among the candidates.

### Retries and blocking

The API uses:

- `urllib3.Retry`;
- HTTP 429 handling;
- configurable proxy configuration;
- retry logic for blocked requests.

### Pagination

Not applicable. It handles transcript languages and caption tracks, not video or channel pagination.

### Persistence and export

The library returns Python objects and offers formatting utilities. It does not own channel storage, Markdown export, or a knowledge-base layout.

### Architectural test

A comments extractor would not belong in this library. It would belong in a sibling component sharing the source abstraction.

A Markdown exporter could be added as a separate formatter or downstream package, but it should not be embedded in transcript fetching.

### Reusable components

- `TranscriptList`;
- `FetchedTranscript`;
- transcript exception taxonomy;
- language selection;
- generated/manual caption distinction;
- proxy configuration;
- caption parsing.

---

## 4.3 xBartM/YouTube-Comment-Scraper

### Extraction and orchestration

The repository is organized around:

```text
configs/
database/
scripts/
```

The main enumeration script is:

```text
scripts/update_videos.sh
```

It:

1. selects the least recently scraped channel;
2. invokes yt-dlp to obtain video URLs;
3. invokes yt-dlp to obtain playlist URLs;
4. expands playlists into video URLs;
5. removes Shorts;
6. deduplicates URLs;
7. generates SQL inserts;
8. inserts videos with conflict handling;
9. updates channel scrape timestamps;
10. updates the archive file.

### Domain model

The PostgreSQL schema in:

```text
database/create_schema.sql
```

defines:

```text
ytkp.channel
ytkp.video
ytkp.comment_section
ytkp.video_transcript
ytkp.sponsorblock
```

The comment table includes:

- YouTube comment ID;
- parent comment ID;
- video relationship;
- user name;
- text;
- like count;
- verified status;
- favorited status;
- pinned status;
- comment timestamp;
- insertion timestamp.

This is a good match for the requested comments/VIDEO_ID.json data.

### Shorts handling

The enumeration script explicitly removes URLs containing `shorts`. That is a major mismatch with the target system, which explicitly needs Shorts.

### Pagination

Channel and playlist pagination is delegated to yt-dlp.

Comment pagination is not clearly represented in the inspected orchestration. The database supports replies, but the script architecture is not a robust comment-pagination service.

### Persistence

Persistence is strong relative to the other small projects:

- PostgreSQL;
- explicit relationships;
- unique constraints;
- scrape timestamps;
- conflict handling;
- archival URL files.

### Weaknesses

- shell scripts dominate orchestration;
- SQL is generated with string interpolation;
- environment-specific assumptions;
- no visible comprehensive automated test suite;
- Shorts are removed;
- no clear typed application layer;
- comments and transcripts appear coupled to shell jobs rather than composable services.

### Reusable components

The schema is the strongest reusable idea in this project. It can serve as a relational reference even if the scripts themselves are not reused.

---

## 4.4 YouTube Comment Suite

### Project structure

The repository contains:

```text
src/main/java
src/main/resources
src/test/java
```

It is a Java/JavaFX desktop application with a separate test tree.

### Functional separation

The project is organized around application concerns such as:

- comment retrieval;
- group/channel/playlist/video selection;
- comment search;
- analytics;
- user activity;
- thumbnail/profile archival;
- display.

The repository has releases and a meaningful commit history, making it a mature reference for comment-specific workflows.

### Comment model

The application is designed around:

- videos;
- comments;
- comment authors;
- activity;
- search filters;
- cross-video views.

This is more aligned with the requested audience analysis than generic yt-dlp scripts.

### Pagination and replies

The application’s purpose requires comment-thread handling and reply retrieval. It is more likely to model top-level comments and replies as separate user-facing concepts than a basic `info.json` consumer.

### Persistence and output

It includes:

- local/offline archival behavior;
- search and activity views;
- thumbnail/profile saving;
- XLSX-oriented output.

It is a desktop application rather than a reusable headless library.

### Architectural test

Adding a new source adapter would likely be less obvious than in a pure library. The application is optimized around its existing Java data access and UI model.

A Markdown exporter would probably need to be a separate export service reading the application’s persistence layer. It should not be placed in a UI controller.

### Reuse value

High conceptual value for:

- comment analytics;
- author activity;
- search;
- thread-oriented UX;
- cross-video comment operations.

Lower value as a directly embeddable component for a new local knowledge-base service.

---

## 4.5 channel-transcript-archiver

### Structure

```text
src/
  extract.py
  clean_transcripts.py
  format_and_summarize.py
  get_playlists.py
  list_channels.py
  browser.py
  cli.py
  ...
```

### Extraction

`src/extract.py` orchestrates yt-dlp for:

- channel URLs;
- video URLs;
- metadata;
- descriptions;
- subtitles;
- auto-generated subtitles;
- comments when requested;
- playlist metadata.

It uses:

- `--skip-download`;
- `--write-info-json`;
- `--write-description`;
- `--write-subs`;
- `--write-auto-subs`;
- `--write-comments`;
- `--download-archive`;
- `--sleep-requests`;
- `--sleep-interval`;
- optional cookies;
- optional JS runtime selection.

### Playlist support

`src/get_playlists.py` uses yt-dlp flat playlist extraction to:

1. list playlist IDs;
2. retrieve each playlist’s metadata;
3. write playlist JSON files.

This is a useful two-pass design.

### Persistence

The output layout is file-based:

```text
channels/
  Channel Name/
    data/
      upload-date - title/
        .info.json
        .description.txt
        .en.srt
        .en.txt
    playlists/
    archive.txt
    config.toml
    PLAYLISTS.md
    TRANSCRIPTS.md
```

The archive file provides incremental processing. Deduplication and transcript cleaning occur after extraction.

### Comments

Comments are delegated to yt-dlp with a maximum-comment setting. There is no independent comment domain model, comments JSON exporter, or explicit reply persistence layer.

### Architectural weakness

`src/extract.py` performs orchestration, file setup, yt-dlp invocation, playlist extraction, finalization, and many directory-management tasks. It is understandable but too broad to serve as a clean domain pipeline.

A new comments subsystem should be extracted into a separate module rather than added to the main `sync_channel()` function.

### Reuse value

Useful for:

- archive directory conventions;
- yt-dlp command construction;
- incremental archive state;
- playlist metadata;
- transcript cleanup;
- browser cookie handling.

---

## 4.6 youtube-transcript-exporter

### Structure

```text
src/
  download_resilient.py
  metadata_extractor.py
  enhance_rag_schema.py
  markdown_generator.py
  obsidian_formatter.py
  enhance_markdown_rag.py
  enhance_rag_schema.py
```

It also contains:

```text
db/
markdown/
out/
tests/
```

### Extraction

`src/download_resilient.py` uses yt-dlp with:

- `--skip-download`;
- `--write-info-json`;
- `--write-auto-subs`;
- subtitle language selection;
- socket timeout;
- retry settings;
- sleep intervals;
- user-agent rotation;
- exponential backoff;
- progress counting;
- channel-root retry when a `/videos` URL appears incomplete.

This is a strong practical reference for batch acquisition reliability.

### Normalization

`src/metadata_extractor.py` scans `.info.json` files and creates:

```text
db/canonical.json
```

The canonical record contains:

- ID;
- title;
- channel;
- channel ID;
- uploader;
- date;
- duration;
- views;
- likes;
- URL;
- description;
- category;
- inferred guest;
- inferred topics;
- source paths.

The source also validates video ID shape and excludes channel metadata directories.

### Markdown generation

`src/markdown_generator.py`:

- loads canonical JSON;
- builds an index from video folders;
- cleans VTT transcripts;
- removes duplicate caption fragments;
- writes text files;
- generates YAML frontmatter;
- estimates word count, token count, and reading time;
- creates stable filenames;
- avoids rewriting unchanged Markdown;
- supports incremental generation;
- uses locking to avoid concurrent destructive operations.

This is a strong exporter reference.

### Persistence

Persistence is split across:

- raw yt-dlp output;
- `db/canonical.json`;
- Markdown output;
- archive/download history.

The design is practical for local-first batch processing but not a transactional database.

### Missing components

- no channel-level model;
- no comments;
- no comments JSON;
- no complete public inventory model;
- no explicit extraction provider interface;
- much of the logic is still standalone scripts;
- generated archive content is mixed into the project tree.

### Reuse value

Strong for:

- canonical JSON;
- VTT cleanup;
- stable Markdown;
- incremental regeneration;
- RAG chunks;
- token/readability metadata;
- source traceability.

---

## 4.7 ChannelHoarder

### Structure

```text
backend/
frontend/
docker/
docs/
tools/
```

The documentation describes:

- Python 3.12;
- FastAPI;
- async SQLAlchemy;
- SQLite WAL;
- APScheduler;
- yt-dlp;
- React and TypeScript;
- WebSocket progress reporting.

### Channel discovery

The system supports:

- RSS;
- YouTube Data API;
- yt-dlp fallback.

The API key is optional according to the project documentation, but improves discovery reliability and speed.

### Persistence

SQLite stores application state:

- channels;
- subscriptions;
- videos;
- queue entries;
- download status;
- configuration;
- error state.

The media archive itself is stored on disk with naming templates and NFO metadata.

### Reliability

Documented handling includes:

- rate-limit classification;
- geo-blocked content;
- unavailable/deleted videos;
- format failures;
- PO-token failures;
- yt-dlp staleness;
- ffmpeg errors;
- disk-full errors;
- network errors;
- authentication expiry.

This is a strong operational architecture reference.

### Weaknesses for this use case

- designed for media downloading, not knowledge-base records;
- no comment archival layer;
- no Markdown knowledge-base exporter;
- Shorts are skipped by default;
- output is oriented to Plex/Jellyfin/Emby;
- not focused on transcript semantics or cross-video analysis.

### Reuse value

Use as a reference for:

- scheduler;
- queue;
- database-backed acquisition;
- error classification;
- health status;
- channel state;
- API/UI separation.

It is less suitable as a direct source for transcript, comments, or LLM export code.

---

## 4.8 YouTube Channel Archiver extension

### Extraction

The background service worker:

- opens a tab for each video;
- waits for the YouTube page;
- asks the content script to extract data;
- receives transcript, comments, chat replay, title, duration, and channel information;
- nests replies under parent comments;
- downloads artifacts.

The source includes explicit `nestComments()` logic.

### Persistence/output

It writes:

```text
transcript.txt
comments.json
chat_replay.json
XLSX
```

through browser download APIs.

### Architecture quality

The architecture is clear at a browser-extension level:

```text
content script
    → background coordinator
    → download persistence
```

However:

- it depends on YouTube DOM structure;
- browser lifecycle is part of reliability;
- there is no backend database;
- no canonical channel model;
- no durable crawl state beyond browser storage;
- no visible automated test suite;
- no LICENSE file was found in the repository root.

### Reuse value

Useful as a reference for:

- browser-rendered comment collection;
- comment reply nesting;
- extraction from the YouTube UI;
- handling transcripts and chat replay together.

Not suitable as the primary architecture for a scalable server-side archive without a new persistence and task layer.

---

## 4.9 Youtube-MCP

### Structure

The repository is very small:

```text
server.py
pyproject.toml
README.md
LICENSE
```

### Features

The project provides MCP tools for:

- searching YouTube;
- retrieving transcripts;
- storing video information;
- semantic search over stored transcripts.

### Architecture quality

The application is primarily a single-server integration layer. It is suitable as an MCP adapter but not as a complete channel archival system.

The source-level architecture is too small to provide:

- explicit channel models;
- extraction provider interfaces;
- comments;
- durable acquisition state;
- pagination orchestration;
- storage migrations;
- export separation.

### Reuse value

Useful for:

- MCP tool definitions;
- transcript retrieval tool boundaries;
- vector-store integration;
- semantic search interface design.

It should be treated as a downstream integration reference, not as the core ingestion system.

---

## 4.10 youtube-knowledge-base

### Structure

The project is essentially:

```text
ingest.py
README.md
youtube-knowledge-base.md
requirements.txt
```

### Channel and video ingestion

`ingest.py`:

1. parses an `@handle`;
2. resolves the channel through YouTube Data API;
3. calls the YouTube search endpoint with `channelId`;
4. paginates using `nextPageToken`;
5. saves video records to CSV;
6. calls transcriptapi.com for transcripts;
7. writes Markdown files;
8. creates or updates a QMD collection;
9. generates embeddings.

This is a useful reference for API pagination and QMD integration.

### Weaknesses

- only handles date-bounded video enumeration;
- does not enumerate Shorts separately;
- does not retrieve descriptions, categories, thumbnails, chapters, or playlists;
- transcript acquisition is delegated to a paid external service;
- no comments;
- no explicit database;
- no typed domain models;
- no test suite;
- most orchestration is in one script.

### Reuse value

Useful for:

- YouTube Data API pagination;
- QMD collection setup;
- transcript-to-Markdown flow;
- local search integration.

Not sufficient as the foundation for the requested system.

---

# 5. Capability Matrix

Legend:

- **Strong** = first-class or central feature;
- **Partial** = implemented but incomplete or bounded;
- **No** = not a core feature;
- **Unknown** = not verified sufficiently from source.

| Repository | Channel | Videos | Transcripts | Comments | Replies | Metadata | Playlists | Thumbnails | Markdown | JSON | Storage | Search/RAG | API requirements |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `yt-dlp` | Strong | Strong | Strong | Partial/Strong | Partial | Strong | Strong | Strong | No | Strong | Files/archive | No | Usually no Data API key; cookies may be needed |
| `youtube-transcript-api` | No | Per-video | Strong | No | No | Partial | No | No | Formatters | Raw data | Library return values | No | No Data API key |
| `YouTube-Comment-Scraper` | Strong | Strong | Strong | Strong | Partial/Strong | Strong | Strong | Unknown | No | Database/text | PostgreSQL | No | Mostly yt-dlp |
| `youtube-comment-suite` | Strong | Strong | Limited | Strong | Strong | Strong | Partial | Strong | No | Internal/XLSX | Local application storage | Strong | No official API key |
| `channel-transcript-archiver` | Strong | Strong | Strong | Partial | Partial | Strong | Strong | Partial | Strong | Strong | File archive | No | No Data API key; cookies optional |
| `youtube-transcript-exporter` | Strong | Strong | Strong | No | No | Strong | Partial | Partial | Strong | Strong | Files/canonical JSON | Partial/JSONL | No Data API key; yt-dlp |
| `ChannelHoarder` | Strong | Strong | Partial | No | No | Strong | Partial | Strong | NFO/media metadata | Database/files | SQLite/files | No | Optional Data API key; yt-dlp fallback |
| `YouTube-Channel-Archiver` | Strong | Strong | Strong | Strong | Strong | Partial | Unknown | Partial | No | Strong | Browser downloads | No | Browser session |
| `Youtube-MCP` | No | Per-video | Strong | No | No | Partial | No | No | No | Tool output | Vector store | Strong | Embedding API key |
| `youtube-knowledge-base` | Strong | Strong | Partial/strong | No | No | Partial | No | No | Strong | CSV/Markdown | Files/QMD | Strong | Data API key; transcriptapi.com key |

---

# 6. Architecture Quality

## `yt-dlp`

- Separation of concerns: **CLEAR**
- Modularity: **CLEAR**
- Testability: **CLEAR**
- Extensibility: **CLEAR**
- Maintainability: **CLEAR**, though the codebase is large
- Error handling: **CLEAR**
- Data model quality: **PARTIAL** because `info_dict` is broad and dynamic

## `youtube-transcript-api`

- Separation of concerns: **CLEAR**
- Modularity: **CLEAR**
- Testability: **CLEAR**
- Extensibility: **CLEAR**
- Maintainability: **CLEAR**
- Error handling: **CLEAR**
- Data model quality: **CLEAR** for transcripts, absent for channel/video domain

## `YouTube-Comment-Scraper`

- Separation of concerns: **PARTIAL**
- Modularity: **WEAK**
- Testability: **WEAK**
- Extensibility: **PARTIAL**
- Maintainability: **WEAK**
- Error handling: **PARTIAL**
- Data model quality: **CLEAR** in SQL, weak in application code

## `youtube-comment-suite`

- Separation of concerns: **CLEAR**
- Modularity: **CLEAR**
- Testability: **CLEAR**
- Extensibility: **PARTIAL**
- Maintainability: **CLEAR** for a desktop application
- Error handling: **UNKNOWN/PARTIAL**
- Data model quality: **CLEAR** for comments and activity

## `channel-transcript-archiver`

- Separation of concerns: **PARTIAL**
- Modularity: **PARTIAL**
- Testability: **WEAK**
- Extensibility: **PARTIAL**
- Maintainability: **PARTIAL**
- Error handling: **PARTIAL**
- Data model quality: **WEAK**

## `youtube-transcript-exporter`

- Separation of concerns: **PARTIAL**
- Modularity: **PARTIAL**
- Testability: **PARTIAL**
- Extensibility: **PARTIAL**
- Maintainability: **PARTIAL**
- Error handling: **PARTIAL**
- Data model quality: **PARTIAL**

## `ChannelHoarder`

- Separation of concerns: **CLEAR**
- Modularity: **CLEAR**
- Testability: **UNKNOWN**, not verified in detail
- Extensibility: **CLEAR**
- Maintainability: **CLEAR**
- Error handling: **CLEAR**
- Data model quality: **CLEAR** for download/channel state, weak for knowledge-base content

## `YouTube-Channel-Archiver`

- Separation of concerns: **CLEAR** within a browser extension
- Modularity: **PARTIAL**
- Testability: **WEAK**
- Extensibility: **WEAK**
- Maintainability: **PARTIAL**
- Error handling: **UNKNOWN**
- Data model quality: **PARTIAL**

## `Youtube-MCP`

- Separation of concerns: **WEAK**
- Modularity: **WEAK**
- Testability: **WEAK**
- Extensibility: **PARTIAL**
- Maintainability: **PARTIAL**
- Error handling: **UNKNOWN**
- Data model quality: **WEAK**

## `youtube-knowledge-base`

- Separation of concerns: **WEAK**
- Modularity: **WEAK**
- Testability: **WEAK**
- Extensibility: **WEAK**
- Maintainability: **WEAK**
- Error handling: **PARTIAL**
- Data model quality: **WEAK**

---

# 7. Reusable Components

## Channel/video acquisition

Potential reuse:

- yt-dlp extractor and archive behavior;
- ChannelHoarder channel discovery concepts;
- Data API pagination patterns;
- archive files and resume semantics;
- channel-root versus `/videos` fallback logic.

## Transcript extraction

Strongest reuse candidate:

```text
youtube-transcript-api
```

Useful interfaces:

```text
TranscriptProvider.list(video_id)
TranscriptProvider.fetch(video_id, languages)
```

The implementation can wrap:

- youtube-transcript-api;
- yt-dlp captions;
- optional external transcript service;
- optional future ASR provider.

## Comments

No single candidate is sufficient for a robust server-side archive.

Possible components:

- `youtube-comment-suite` comment/thread model;
- `YouTube-Comment-Scraper` relational schema;
- `YouTube-Channel-Archiver` browser reply nesting;
- yt-dlp bounded comment extraction.

A dedicated comments service should define:

```text
CommentProvider.fetch_top_level(video_id, cursor)
CommentProvider.fetch_replies(comment_id, cursor)
```

## Metadata

Use yt-dlp metadata as the broad source, then normalize into explicit records:

- channel metadata;
- video metadata;
- playlist metadata;
- availability state;
- thumbnails;
- chapters;
- categories;
- tags;
- hashtags;
- source provenance.

## Storage

Potential models:

- SQLite for local-first state and idempotency;
- PostgreSQL if multi-user, concurrent, or high-volume comments are expected;
- raw JSON and JSONL as immutable acquisition artifacts;
- filesystem blobs for thumbnails and transcript source files.

## Markdown and LLM export

Strong reference:

```text
dlovecreator-arch/youtube-transcript-exporter
```

Reusable ideas:

- stable filenames;
- YAML frontmatter;
- explicit source IDs;
- transcript source and confidence;
- token estimates;
- incremental generation;
- content hashes;
- JSONL/chunk exports;
- non-destructive regeneration.

## Search/RAG

Potential references:

- QMD integration from `youtube-knowledge-base`;
- semantic search interface from `Youtube-MCP`;
- cross-video comment search from `youtube-comment-suite`.

A search index should be downstream of normalized storage, not embedded in extraction code.

---

# 8. Architectural Gaps

## Channel-level gaps

Most tools collect one channel but do not maintain a complete channel-level knowledge object containing:

- channel ID;
- canonical URL;
- handle;
- title;
- description;
- creation information;
- external links;
- channel tabs;
- playlists;
- channel-level inventory statistics;
- retrieval timestamps;
- source provenance.

## Video inventory gaps

Several tools either:

- download a page-limited subset;
- only enumerate videos after a date;
- remove Shorts;
- assume standard long-form uploads;
- do not distinguish a video's original publication from capture time.

## Comment gaps

Most projects do not provide a complete archival model covering:

- top-level comments;
- replies;
- pagination cursors;
- source ordering;
- comment ordering as returned;
- earliest currently retrievable comment;
- deleted or hidden comments;
- disabled comments;
- comment fetch timestamps;
- partial failures;
- comment counts versus retrieved counts;
- page-level provenance.

## Normalization gaps

Raw yt-dlp dictionaries are useful but insufficient as a long-term knowledge-base schema.

The system needs explicit records for:

- retrieval state;
- source;
- unavailable state;
- extraction errors;
- normalized values;
- raw values;
- schema version.

## Error and observability gaps

A robust archive needs per-item status:

```text
discovered
metadata_pending
metadata_available
transcript_unavailable
comments_disabled
comments_partial
comments_complete
video_unavailable
rate_limited
requires_authentication
extraction_failed
```

## Storage gaps

File-only systems are simple but weak for:

- querying all comments;
- reply traversal;
- incremental updates;
- duplicate detection;
- pagination state;
- retries;
- concurrency;
- analytics.

## Export gaps

Existing tools generally export only:

- transcript Markdown;
- raw JSON;
- XLSX;
- vector chunks.

They do not provide a complete channel-level LLM package containing:

- channel summary;
- timeline;
- topics;
- audience themes;
- recurring entities;
- format patterns;
- publishing patterns;
- cross-video relationships;
- provenance;
- uncertainty and missing-data notes.

---

# 9. Proposed Architecture

This is a planning proposal, not an implementation decision.

## Components

```text
1. CLI / API
2. Acquisition Orchestrator
3. Channel Resolver
4. Video Inventory Provider
5. Metadata Provider
6. Transcript Provider
7. Comments Provider
8. Normalization Layer
9. Domain Repository
10. Raw Artifact Store
11. Processing Pipeline
12. Derived Analysis Pipeline
13. Markdown Exporter
14. JSON/JSONL Exporter
15. Search/RAG Adapter
16. Observability and Retry Layer
```

## Responsibilities

### CLI/API

Accept:

- channel URL;
- output location;
- date range;
- source selection;
- comment limits;
- transcript languages;
- whether to download thumbnails;
- whether to run derived analysis.

### Acquisition orchestrator

Coordinate stages and persist stage state.

Responsibilities:

- idempotency;
- scheduling;
- retries;
- concurrency limits;
- stage transitions;
- per-item error handling;
- resumability.

### Channel resolver

Produce a canonical channel identity:

```text
input URL
canonical URL
channel ID
handle
display name
resolved channel URL
```

### Video inventory provider

Return a paginated list of video references.

Implementations:

- yt-dlp channel/tab provider;
- YouTube Data API provider;
- RSS provider;
- future browser provider.

The interface should expose:

```text
iter_videos(channel, cursor, include_shorts=True)
```

### Metadata provider

Return a normalized video record containing:

- ID;
- URL;
- title;
- description;
- publication timestamp;
- duration;
- availability;
- channel;
- uploader;
- thumbnails;
- categories;
- tags;
- hashtags;
- chapters;
- playlist relationships;
- source metadata;
- retrieval timestamp.

### Transcript provider

Return:

```text
TranscriptResult
  status
  language
  generated/manual
  snippets
  raw_source
  retrieval_timestamp
  error
```

### Comments provider

Return:

```text
CommentThread
CommentPage
CommentRecord
ReplyPage
```

Must preserve:

- top-level comment ID;
- reply ID;
- parent ID;
- author;
- text;
- timestamp;
- likes;
- pinned state;
- author state;
- ordering;
- source page/cursor;
- retrieval timestamp.

### Normalization layer

Convert provider-specific records into one versioned domain schema.

Normalization should not discard raw values. Store both:

```text
raw record
normalized record
```

### Storage

Recommended initial design:

```text
SQLite
    → acquisition state
    → channel records
    → video records
    → transcript records
    → comment records
    → run records
    → error records
```

Use raw files/JSONL for immutable source artifacts.

PostgreSQL should be considered if requirements expand to:

- multiple concurrent workers;
- multiple users;
- very large comment sets;
- remote operation;
- full-text search;
- complex analytics queries.

### Processing

Process only normalized records.

Examples:

- transcript cleanup;
- chapter extraction;
- topic clustering;
- title pattern analysis;
- publishing cadence;
- comment theme extraction;
- entity extraction;
- cross-video similarity.

### Export

Exporters should read from storage, not directly from providers.

This allows re-export without re-scraping and prevents source failures from destroying downstream artifacts.

### Search/RAG

Treat search as a separate projection:

```text
normalized records
    → chunking
    → embedding/index projection
    → local/full-text/vector search
```

The raw archive remains authoritative.

## Data flow

```text
Channel URL
    ↓
ChannelResolver
    ↓
ChannelRecord
    ↓
VideoInventoryProvider
    ↓
VideoReference[]
    ↓
MetadataProvider
    ↓
Normalized VideoRecord[]
    ↓
TranscriptProvider
    ↓
Normalized TranscriptRecord[]
    ↓
CommentsProvider
    ↓
Normalized CommentThread[]
    ↓
Repository + raw artifact store
    ↓
Processing pipeline
    ↓
Derived records
    ↓
Markdown / JSON / JSONL exporters
    ↓
Search/RAG projection
```

## Proposed output structure

```text
channel.md
timeline.md
topics.md
audience.md
formats.md
entities.md
relationships.md

videos/
    VIDEO_ID.md

comments/
    VIDEO_ID.json

transcripts/
    VIDEO_ID.json
    VIDEO_ID.md

playlists/
    PLAYLIST_ID.md
    PLAYLIST_ID.json

raw/
    channel.json
    videos.json
    comments/
        VIDEO_ID.jsonl
    transcripts/
        VIDEO_ID.jsonl
    metadata/
        VIDEO_ID.json

state/
    acquisition.json
    errors.json
    cursors.json
```

---

# 10. Proposed Repository Structure

```text
youtube-kb/
├── pyproject.toml
├── README.md
├── src/
│   └── youtube_kb/
│       ├── cli/
│       ├── config/
│       ├── domain/
│       │   ├── channel.py
│       │   ├── video.py
│       │   ├── transcript.py
│       │   ├── comment.py
│       │   ├── playlist.py
│       │   └── errors.py
│       ├── providers/
│       │   ├── youtube_data_api/
│       │   ├── ytdlp/
│       │   ├── transcript_api/
│       │   ├── browser/
│       │   └── comments/
│       ├── normalization/
│       ├── acquisition/
│       ├── processing/
│       ├── storage/
│       │   ├── sqlite/
│       │   ├── postgres/
│       │   └── artifacts/
│       ├── exporters/
│       │   ├── markdown/
│       │   ├── json/
│       │   └── jsonl/
│       ├── search/
│       └── observability/
├── tests/
│   ├── unit/
│   ├── provider_contract/
│   ├── normalization/
│   ├── storage/
│   ├── acquisition/
│   └── exporters/
├── fixtures/
│   ├── metadata/
│   ├── transcripts/
│   └── comments/
└── docs/
```

The exact language and framework are not decided. The boundaries are more important than the implementation language.

---

# 11. Implementation Phases

## Phase 1: Domain model and provenance

Define:

- channel;
- video;
- playlist;
- transcript;
- comment;
- reply;
- retrieval run;
- source record;
- availability state;
- error state.

Every record should preserve:

```text
source
retrieved_at
raw_artifact_reference
schema_version
```

## Phase 2: Channel discovery

Implement:

- handle;
- `/channel/UC...`;
- `/user/...`;
- `/c/...`;
- custom URL;
- `/shorts`;
- `/videos`;
- `/streams`;
- `/playlists`.

Store the original URL and canonical resolved identity.

## Phase 3: Video inventory

Implement a provider interface for:

- channel videos;
- Shorts;
- streams;
- playlists;
- tabs.

Do not silently discard Shorts. Treat them as videos with a `content_type`.

## Phase 4: Metadata normalization

Collect and normalize:

- titles;
- descriptions;
- timestamps;
- duration;
- URLs;
- thumbnails;
- categories;
- tags;
- hashtags;
- chapters;
- availability;
- deleted/private/unavailable state.

## Phase 5: Transcript acquisition

Use a provider interface with possible implementations:

1. `youtube-transcript-api`;
2. yt-dlp subtitle extraction;
3. external transcript provider;
4. future ASR fallback.

The system must distinguish:

- no captions;
- captions disabled;
- transcript blocked;
- age restricted;
- video unavailable;
- network failure;
- provider quota failure.

## Phase 6: Comment acquisition

Implement separately from transcript acquisition.

Support:

- top-level pagination;
- reply pagination;
- comment ordering;
- source cursors;
- partial retrieval;
- disabled comments;
- deleted comments;
- unavailable videos;
- earliest currently retrievable comment;
- retrieved count versus reported count.

## Phase 7: Durable storage

Implement:

- SQLite repository;
- transaction boundaries;
- idempotent upserts;
- raw artifact storage;
- acquisition runs;
- item-level status;
- retry metadata.

## Phase 8: Export

Implement:

- channel Markdown;
- timeline;
- video Markdown;
- comments JSON;
- transcript JSON;
- raw JSON;
- JSONL chunks;
- optional XLSX/CSV.

Ensure exports are non-destructive and reproducible.

## Phase 9: Derived analysis

Add processing stages:

- topics;
- topic evolution;
- recurring entities;
- title patterns;
- format patterns;
- publishing patterns;
- audience questions;
- comment themes;
- content clusters;
- video similarity;
- cross-video relationships.

Each derived value should include:

- method;
- model/version;
- confidence;
- source record IDs;
- generated timestamp.

## Phase 10: Search/RAG

Add a downstream index:

- local full-text;
- SQLite FTS;
- QMD;
- vector database;
- MCP tools.

Search should operate on normalized records and exported chunks.

## Phase 11: Reliability and observability

Add:

- bounded concurrency;
- per-provider rate limits;
- exponential backoff;
- jitter;
- circuit breakers;
- error classification;
- retry budgets;
- resumable queues;
- run summaries;
- dead-letter handling.

---

# 12. Risks

## YouTube interface instability

yt-dlp, InnerTube, browser DOM, and comment extraction all change over time. Extraction providers must be isolated so one can be replaced without rewriting the full application.

## Incomplete public inventory

YouTube may expose only recent items, a limited tab view, or a continuation result that is not stable. The system must record enumeration coverage and avoid claiming completeness without evidence.

## Shorts behavior

Shorts may be exposed through different URL forms and extraction behavior. They must be treated as a first-class content type.

## Comments disabled or unavailable

A missing comment result is ambiguous. It may mean:

- comments disabled;
- no comments;
- authentication required;
- video unavailable;
- comments deleted;
- provider blocked;
- pagination incomplete.

These states should not be collapsed into “no comments.”

## Earliest retrievable comment

YouTube generally does not promise a complete historical comment archive. The system should define:

```text
earliest_retrievable_at_observation
```

rather than claiming a definitive historical earliest comment.

## API quotas

The YouTube Data API has quota costs for:

- channel resolution;
- playlist listing;
- video listing;
- video details;
- comment threads;
- replies.

A complete comment archive through the official API can be expensive.

## Transcript coverage

Some videos have:

- no captions;
- manually disabled captions;
- auto-generated captions;
- restricted captions;
- regional or language-specific tracks;
- inaccessible caption URLs.

The system must represent transcript absence explicitly.

## Age-restricted and authenticated content

Cookies and authenticated browser contexts may be required. Cookie handling must be treated as sensitive data and not logged or embedded in output.

## Rate limiting and bot detection

Retry behavior can worsen blocking if not carefully designed. Provider-specific rate limits, jitter, backoff, and circuit breakers are required.

## Deleted/private videos

A previously discovered video can become unavailable. The system should retain the original inventory record and mark current availability separately.

## Duplicate and conflicting metadata

Different providers may disagree on:

- title;
- publication date;
- duration;
- channel identity;
- description;
- thumbnail URL.

A provenance-aware normalized model is necessary.

## LLM-derived information

Derived topics, audience themes, and relationships require:

- source evidence;
- model/version tracking;
- confidence;
- regeneration policy;
- separation from source facts.

## Licensing and redistribution

Most candidates use MIT, Unlicense, or similar permissive terms, but the YouTube extension candidate inspected had no root `LICENSE`. No legal conclusion should be made without reviewing all applicable license and third-party dependency terms.

---

# 13. Questions/Decisions Needed Before Implementation

1. **Primary language/runtime**
   - Python, TypeScript, Go, Rust, or a mixed architecture?

2. **Primary storage target**
   - SQLite local-first;
   - PostgreSQL;
   - filesystem-only;
   - hybrid raw files plus relational database?

3. **Extraction strategy**
   - yt-dlp first;
   - YouTube Data API first;
   - browser extension;
   - multiple interchangeable providers?

4. **Comment policy**
   - official API only;
   - yt-dlp only;
   - browser extraction;
   - multiple providers with reconciliation?

5. **Comment completeness target**
   - bounded extraction;
   - as complete as currently retrievable;
   - all pages until exhaustion;
   - configurable maximum.

6. **Public-content boundary**
   - public unauthenticated content only;
   - optionally user-authorized cookies;
   - age-restricted content with cookies;
   - explicit prohibition on private or account-only content.

7. **Transcript policy**
   - captions only;
   - captions plus external fallback;
   - optional Whisper/ASR fallback;
   - manual upload override.

8. **Shorts policy**
   - include all Shorts;
   - include only Shorts tab;
   - classify Shorts by duration;
   - preserve separate tab relationships.

9. **Playlist scope**
   - channel playlists only;
   - all public playlists associated with the channel;
   - playlist video relationships even when videos are not on the primary uploads tab.

10. **Markdown profile**
    - one LLM-oriented format;
    - separate human-readable and machine-optimized exports;
    - YAML frontmatter schema;
    - token/chunk boundaries;
    - citation/provenance requirements.

11. **Raw data retention**
    - retain all raw provider responses;
    - retain only normalized records;
    - configurable retention by artifact type.

12. **Derived analysis runtime**
    - local models;
    - hosted LLM;
    - provider abstraction;
    - deterministic heuristics first;
    - regeneration policy.

13. **Search/RAG target**
    - SQLite FTS;
    - QMD;
    - LanceDB/Chroma/FAISS;
    - PostgreSQL vector search;
    - external service.

14. **Privacy**
    - whether author names and profile URLs are retained;
    - whether comment text should be redacted;
    - how deletion requests are handled;
    - how personal data is excluded from LLM exports.

15. **Licensing policy**
    - whether dependencies with Unlicense, MIT, GPL, or no-license components may be included;
    - whether the system is internal-only or distributable;
    - whether third-party license notices must be bundled.

---

# Final Assessment

No single inspected project is sufficient for the requested system.

The most practical architectural composition is:

```text
Channel/video enumeration:
    yt-dlp
    optionally YouTube Data API
    ChannelHoarder-style persistent acquisition state

Transcripts:
    youtube-transcript-api
    optionally yt-dlp subtitle extraction

Comments:
    dedicated comments provider
    using relational schema ideas from YouTube-Comment-Scraper
    and thread/analytics ideas from youtube-comment-suite

Storage:
    SQLite for initial local-first implementation
    optional PostgreSQL later

Markdown/RAG:
    canonical JSON and incremental Markdown ideas from
    youtube-transcript-exporter

Search:
    QMD or SQLite FTS initially
    vector projection later

LLM processing:
    separate downstream pipeline, not extraction code
```

The key architectural decision is to treat every source as an **adapter producing normalized, versioned records**, with raw source data retained separately. This makes it possible to replace yt-dlp, the official API, transcript providers, or comment mechanisms without redesigning storage and exports.

---

