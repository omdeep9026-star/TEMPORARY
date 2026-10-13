#!/usr/bin/env python3
"""serve.py - minimal backend for the mech-copilot MVP.

Serves:
  /                -> web/index.html
  /api/kb          -> KB listing
  /api/entry?id=   -> one entry (+ preview path)
  /api/agent       -> POST {prompt} -> retrieval + intent match + validation + citations
  /kb-assets/*     -> static KB assets (STEP/STL/GLB/SVG) for the viewer

Intent matching is deterministic regex + the kb_agent calculators. With an
OpenAI-compatible LLM on AMD (llama.cpp server) reachable at $LLM_URL, the
same /api/agent first asks the LLM to emit a JSON tool call; the regex path
is the offline fallback. The LLM NEVER produces numbers: all numbers come
from kb_agent calculators and are labeled.
"""
import json, os, re, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root
sys.path.insert(0, os.path.join(HERE, "tools"))
import kb_agent  # noqa: E402

WEB = os.path.join(HERE, "web")
KB = os.path.join(HERE, "kb")
LLM_URL = os.environ.get("LLM_URL", "")  # e.g. http://127.0.0.1:8080/v1/chat/completions
LLM_MODEL = os.environ.get("LLM_MODEL", "local")

# ---------------------------------------------------------------- intent rules
INTENTS = [
  {
    "name": "slow_down_gear_train",
    "pattern": r"(slow|reduce).*(speed|turn|rotat)|(turn|rotat|spin).*(too fast)|ratio",
    "assembly": "ASM-GEARTRAIN-01",
    "answer": ("To slow the output ~1.5x I propose increasing the driven gear from 30 to 45 teeth "
               "and moving the centre distance from 48 mm to 63 mm (C = m*(z1+z2)/2). "
               "Ratio goes 30/18=1.667 to 45/18=2.500, i.e. 1.50x slower output."),
    "changes": {"spur-gear-30t-m2": {"teeth": 45}, "centre_distance_mm": 63.0},
    "citations": ["PR-GTR-01"],
    "open_items": ["tooth strength at increased torque (CHK-TORQUE-RATING)",
                   "housing slots must move 15 mm or use adjustable centres",
                   "shaft/bore fit unchanged (6 mm)"],
  },
  {
    "name": "fourbar_check",
    "pattern": r"four.?bar|linkage|grashof|bind",
    "assembly": "ASM-FOURBAR-01",
    "answer": ("Checking the four-bar: with ground 150 / crank 60 / coupler 120 / rocker 80 the "
               "Grashof condition s+l <= p+q fails (210 > 200), so the crank cannot fully rotate - "
               "it is a double-rocker. To get full rotation, ground the SHORTEST link (60 mm) instead."),
    "changes": None,
    "citations": ["PR-4BAR-01", "PR-DOF-01"],
    "open_items": ["transmission-angle sweep over the working arc (numeric solve)"],
  },
  {
    "name": "valve_leak",
    "pattern": r"leak|weep|flange|gasket|valve",
    "assembly": "ASM-PIPEVALVE-01",
    "answer": ("Flange weep most often means gasket or bolt-torque problems, not the valve. "
               "Per SC-VALVE-LEAK-01: replace the gasket every time, clean both faces, "
               "finger-tight all bolts then torque in a cross sequence. Torque values must come "
               "from a human-verified table - I will not invent them."),
    "changes": None,
    "citations": ["SC-VALVE-LEAK-01", "PR-FST-01", "PR-TOL-01"],
    "open_items": ["torque values (human-verified table)", "pressure test per site procedure"],
  },
]

def llm_tool_call(prompt):
    """Ask a local OpenAI-compatible LLM to pick an intent + emit tool args.
    Returns None if no LLM configured or the call fails. Never returns numbers."""
    if not LLM_URL:
        return None
    tools_desc = json.dumps([
        {"intent": i["name"], "assembly": i["assembly"],
         "args": {k: "..." for k in (i.get("changes") or {})}}
        for i in INTENTS])
    sysmsg = ("You are the planner for a mechanical KB agent. Pick ONE intent and reply with ONLY "
              "a JSON object {\"intent\": name}. Do not compute or invent any numbers. Intents: " + tools_desc)
    import urllib.request
    body = json.dumps({"model": LLM_MODEL, "messages": [
        {"role": "system", "content": sysmsg}, {"role": "user", "content": prompt}],
        "max_tokens": 60, "temperature": 0}).encode()
    req = urllib.request.Request(LLM_URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            txt = json.load(r)["choices"][0]["message"]["content"]
        m = re.search(r"\{[^}]*\}", txt, re.S)
        if m:
            return json.loads(m.group(0)).get("intent")
    except Exception:
        return None
    return None


def agent_reply(prompt):
    intent_name = llm_tool_call(prompt)
    intent = None
    if intent_name:
        intent = next((i for i in INTENTS if i["name"] == intent_name), None)
    if intent is None:  # deterministic fallback
        p = prompt.lower()
        best, best_n = None, 0
        for i in INTENTS:
            n = len(re.findall(i["pattern"], p))
            if n > best_n:
                best, best_n = i, n
        intent = best
    if intent is None:
        hits = kb_agent.kb_search(prompt)
        return {"label": "unverified-proposal", "answer": "No rule matched; here is what the KB contains:",
                "hits": hits, "citations": [], "open_items": ["answer is retrieval only"]}
    proposal = kb_agent.propose_change(intent["assembly"], intent["changes"] or {})
    return {"label": proposal["label"], "answer": intent["answer"],
            "changes": intent["changes"], "assembly": intent["assembly"],
            "validation": proposal["validation"], "citations": intent["citations"],
            "open_items": intent["open_items"],
            "planner": ("llm" if intent_name else "regex-fallback")}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _static(self, path, ctype):
        try:
            with open(path, "rb") as f:
                self._send(200, f.read(), ctype)
        except OSError:
            self._send(404, {"error": "not found"})

    def do_GET(self):
        u = urlparse(self.path)
        if u.path in ("/", "/index.html"):
            return self._static(os.path.join(WEB, "index.html"), "text/html")
        if u.path == "/api/kb":
            counts = kb_agent.kb_stats()
            entries = []
            for kind, pool in (("component", kb_agent._COMPONENTS), ("assembly", kb_agent._ASSEMBLIES),
                               ("principle", kb_agent._PRINCIPLES), ("scenario", kb_agent._SCENARIOS)):
                for eid, e in pool.items():
                    entries.append({"id": eid, "kind": kind,
                                    "label": e.get("label") or e.get("title") or eid})
            return self._send(200, {"counts": counts, "entries": entries})
        if u.path == "/api/entry":
            q = parse_qs(u.query)
            eid = q.get("id", [""])[0]
            e = kb_agent.kb_get(eid)
            if not e:
                return self._send(404, {"error": "unknown id"})
            pv = kb_agent.preview_paths(eid)
            preview = None
            if pv and pv.get("glb"):
                preview = "/kb-assets/" + pv["glb"].split("kb/")[-1]
            elif pv and pv.get("svg"):
                preview = "/kb-assets/" + pv["svg"].split("kb/")[-1]
            return self._send(200, {"entry": e, "preview": preview})
        if u.path.startswith("/kb-assets/"):
            rel = u.path[len("/kb-assets/"):]
            target = os.path.realpath(os.path.join(KB, rel))
            if not target.startswith(os.path.realpath(KB)):
                return self._send(403, {"error": "forbidden"})
            ctype = {"glb": "model/gltf-binary", "bin": "application/octet-stream",
                     "svg": "image/svg+xml", "stl": "model/stl", "step": "application/step"}.get(rel.rsplit(".", 1)[-1], "application/octet-stream")
            return self._static(target, ctype)
        self._send(404, {"error": "unknown path"})

    def do_POST(self):
        if self.path == "/api/agent":
            n = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(n) or b"{}")
            prompt = str(payload.get("prompt", ""))[:500]
            return self._send(200, agent_reply(prompt))
        self._send(404, {"error": "unknown path"})


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f"mech-copilot MVP on http://127.0.0.1:{port}  (LLM_URL={LLM_URL or 'not set -> regex planner'})")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
