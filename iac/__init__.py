"""Pi — IA Collaborative Strategic Engagement Agent

Multi-agent system for winning, delivering, and scaling the IAC partnership.
"""

__version__ = "1.0.0"
__author__ = "Mike Rodgers (RIG)"

from iac.client import ClientIntel, Deal, Meeting, Persona, Stance
from iac.simulation import SCENARIOS, run_simulation_stub

__all__ = [
    "ClientIntel",
    "Deal",
    "Meeting",
    "Persona",
    "Stance",
    "SCENARIOS",
    "run_simulation_stub",
]
