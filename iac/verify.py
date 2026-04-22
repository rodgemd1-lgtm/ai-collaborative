#!/usr/bin/env python3
"""Verify Pi IA Collaborative installation."""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PASS, FAIL = [], []

def check(name, cond, hint=""):
    (PASS if cond else FAIL).append(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f"  → {hint}" if hint and not cond else ""))

def main():
    print("\n" + "="*60 + "\n  PI IA COLLABORATIVE — VERIFICATION\n" + "="*60 + "\n")

    # Structure
    for d in [".pi", ".pi/agents", ".pi/capabilities", ".pi/prompts", "iac"]:
        check(d, (ROOT / d).is_dir())

    # Config files
    for f in ["settings.json", "workflows.json", "orchestration.md"]:
        check(f, (ROOT / ".pi" / f).is_file())

    # Workflow prompts
    for wf in ["pitch-prep", "prism-sim", "hexis-eval", "recon", "website-audit", "content-create", "campaign-health"]:
        check(f"workflow: {wf}", (ROOT / ".pi" / "prompts" / f"{wf}.md").is_file())

    # Context
    ctx = ROOT / ".pi" / "prompts" / "iac-context.md"
    check("iac-context.md", ctx.is_file())
    if ctx.is_file():
        sz = ctx.stat().st_size
        check("iac-context.md populated", sz > 5000, f"{sz} bytes")

    # Agents + capabilities
    for a in ["strategy", "content", "client", "web", "campaigns", "research"]:
        check(f"agent: {a}", (ROOT / ".pi" / "agents" / f"{a}.md").is_file())
    for c in ["browser-use", "composio", "gamma", "apollo", "prism"]:
        check(f"capability: {c}", (ROOT / ".pi" / "capabilities" / f"{c}.md").is_file())

    # Python package
    for f in ["__init__.py", "client.py", "simulation.py"]:
        check(f"iac/{f}", (ROOT / "iac" / f).is_file())

    # Import test
    try:
        sys.path.insert(0, str(ROOT))
        import iac.client; import iac.simulation
        check("Python import", True)
    except Exception as e:
        check("Python import", False, str(e)[:80])

    print("\n".join(PASS))
    if FAIL:
        print("\n" + "\n".join(FAIL))
    print(f"\n{'='*60}\n  Result: {len(PASS)} passed, {len(FAIL)} failed\n" + "="*60 + "\n")
    return 0 if not FAIL else 1

if __name__ == "__main__":
    sys.exit(main())
