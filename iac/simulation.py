"""Prism — Decision Simulation Engine

Runs multi-agent simulations for strategic decisions using persona systems.
Usage: python -m iac.simulation --scenario meeting_reception --variant all_interventions
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Optional

SIM_DIR = Path(__file__).parent.parent.parent.parent / "data" / "simulations"
SIM_DIR.mkdir(parents=True, exist_ok=True)

SCENARIOS = {
    "meeting_reception": {
        "name": "IAC Meeting Reception — Kyle + Leadership",
        "personas": ["kyle", "matthew", "kathleen", "dan", "jeff", "rahul"],
        "rounds": 6,
        "hours": [0, 2, 6, 24, 48, 72],
        "variants": ["control", "pre_brief", "co_ceo_dinner", "all_interventions"],
    },
    "strategic_choice": {
        "name": "IAC Package Selection — A vs B",
        "personas": ["kyle", "matthew", "kathleen", "dan"],
        "rounds": 4,
        "hours": [0, 24, 72, 168],
        "variants": ["package_a", "package_b", "package_c", "practice_build"],
    }
}

def save_simulation(scenario: str, variant: str, results: Dict) -> Path:
    """Save simulation output to vault."""
    from datetime import datetime
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    out_path = SIM_DIR / f"{scenario}_{variant}_{ts}.json"
    out_path.write_text(json.dumps(results, indent=2))
    return out_path

def run_simulation_stub(scenario: str, variant: str) -> Dict:
    """Stub — replace with actual MiroFish integration."""
    cfg = SCENARIOS.get(scenario)
    if not cfg:
        raise ValueError(f"Unknown scenario: {scenario}. Known: {list(SCENARIOS.keys())}")
    return {
        "scenario": scenario,
        "variant": variant,
        "personas": cfg["personas"],
        "rounds": cfg["rounds"],
        "hours": cfg["hours"],
        "result": "STUB — MiroFish engine not wired. Run via ~/Desktop/Startup-Intelligence-OS/MiroFish/",
        "action_required": "Wire to MiroFish Python package when engine API is ready",
        "timestamp": __import__('datetime').datetime.now().isoformat(),
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True, choices=list(SCENARIOS.keys()))
    parser.add_argument("--variant", default="all_interventions")
    parser.add_argument("--save", default="true")
    args = parser.parse_args()

    results = run_simulation_stub(args.scenario, args.variant)
    if args.save.lower() == "true":
        path = save_simulation(args.scenario, args.variant, results)
        print(f"Simulation saved: {path}")
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
