"""Verify script — health check for the Pi IAC repository.

Usage: python3 -m iac.verify
"""

import json
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path(__file__).parent.parent.resolve()
PI_DIR = REPO_ROOT / ".pi"
PROMPTS_DIR = PI_DIR / "prompts"
AGENTS_DIR = PI_DIR / "agents"
CAPS_DIR = PI_DIR / "capabilities"

REQUIRED_FILES = {
    "root": [
        "README.md",
        ".gitignore",
    ],
    ".pi": [
        "README.md",
        "settings.json",
        "workflows.json",
        "orchestration.md",
    ],
    "prompts": [
        "iac-context.md",
        "pitch-prep.md",
        "prism-sim.md",
        "hexis-eval.md",
        "recon.md",
        "website-audit.md",
        "content-create.md",
        "campaign-health.md",
    ],
    "agents": [
        "README.md",
        "strategy.md",
        "content.md",
        "client.md",
        "web.md",
        "campaigns.md",
        "research.md",
    ],
    "capabilities": [
        "browser-use.md",
        "composio.md",
        "gamma.md",
        "apollo.md",
        "prism.md",
    ],
    "python": [
        "iac/__init__.py",
        "iac/client.py",
        "iac/simulation.py",
        "bin/pi-iac",
    ],
}


def check_file(path: Path, label: str) -> Tuple[bool, str]:
    if path.exists():
        size = path.stat().st_size
        return True, f"  OK  {label} ({size} bytes)"
    return False, f"  MISSING {label}"


def check_json(path: Path) -> Tuple[bool, str]:
    ok, msg = check_file(path, str(path.relative_to(REPO_ROOT)))
    if not ok:
        return ok, msg
    try:
        with open(path, "r") as f:
            data = json.load(f)
        return True, f"  OK  {path.name} (valid JSON, {len(json.dumps(data))} chars)"
    except json.JSONDecodeError as e:
        return False, f"  BROKEN JSON {path.name}: {e}"


def verify() -> int:
    print("=" * 60)
    print("π Pi IAC — Repository Health Check")
    print("=" * 60)
    print(f"Repo root: {REPO_ROOT}")
    print()

    all_ok = True

    # Root files
    print("[Root files]")
    for name in REQUIRED_FILES["root"]:
        ok, msg = check_file(REPO_ROOT / name, name)
        print(msg)
        if not ok:
            all_ok = False
    print()

    # .pi files
    print("[.pi/ files]")
    for name in REQUIRED_FILES[".pi"]:
        if name.endswith(".json"):
            ok, msg = check_json(PI_DIR / name)
        else:
            ok, msg = check_file(PI_DIR / name, name)
        print(msg)
        if not ok:
            all_ok = False
    print()

    # Prompts
    print("[Prompts]")
    for name in REQUIRED_FILES["prompts"]:
        ok, msg = check_file(PROMPTS_DIR / name, name)
        print(msg)
        if not ok:
            all_ok = False
    print()

    # Agents
    print("[Agents]")
    for name in REQUIRED_FILES["agents"]:
        ok, msg = check_file(AGENTS_DIR / name, name)
        print(msg)
        if not ok:
            all_ok = False
    print()

    # Capabilities
    print("[Capabilities]")
    for name in REQUIRED_FILES["capabilities"]:
        ok, msg = check_file(CAPS_DIR / name, name)
        print(msg)
        if not ok:
            all_ok = False
    print()

    # Python package
    print("[Python package]")
    for name in REQUIRED_FILES["python"]:
        ok, msg = check_file(REPO_ROOT / name, name)
        print(msg)
        if not ok:
            all_ok = False

    # Check if workflows.json matches prompts
    print()
    print("[Workflow consistency check]")
    workflows_path = PI_DIR / "workflows.json"
    try:
        with open(workflows_path, "r") as f:
            workflows = json.load(f)
        workflow_files = [w["path"] for w in workflows.get("workflows", [])]
        for wf in workflow_files:
            full = REPO_ROOT / wf
            ok, msg = check_file(full, wf)
            print(msg)
            if not ok:
                all_ok = False
    except Exception as e:
        print(f"  BROKEN workflows.json: {e}")
        all_ok = False

    # Check master context length
    print()
    print("[Master context check]")
    ctx_path = PROMPTS_DIR / "iac-context.md"
    ok, msg = check_file(ctx_path, "iac-context.md")
    print(msg)
    if ok:
        lines = len(ctx_path.read_text().splitlines())
        print(f"  Context lines: {lines}")
        if lines < 200:
            print(f"  WARNING: Context seems short (< 200 lines). Was it truncated?")
        else:
            print(f"  Context looks complete.")
    else:
        all_ok = False

    # Summary
    print()
    print("=" * 60)
    if all_ok:
        print("ALL CHECKS PASSED — Repository is complete.")
    else:
        print("SOME CHECKS FAILED — See MISSING / BROKEN lines above.")
    print("=" * 60)

    return 0 if all_ok else 1


if __name__ == "__main__":
    exit(verify())
