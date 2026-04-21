"""IAC Client Intelligence Agent

Manages BD pipeline, meeting prep, CRM, follow-ups, and client relationships.
"""

import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import List, Optional, Dict

DATA_DIR = Path(__file__).parent.parent.parent / "data"
CLIENT_DIR = DATA_DIR / "clients"
CLIENT_DIR.mkdir(parents=True, exist_ok=True)

class Persona(Enum):
    KYLE = "kyle"
    MATTHEW = "matthew"
    KATHLEEN = "kathleen"
    DAN = "dan"
    JEFF = "jeff"
    RAHUL = "rahul"
    DAVID = "david"

class Stance(Enum):
    OPPOSE = 0.0
    SKEPTICAL = 0.25
    NEUTRAL = 0.5
    ENGAGED = 0.75
    CHAMPION = 1.0

@dataclass
class Meeting:
    date: str
    attendees: List[str]
    type: str  # "pitch", "follow_up", "internal_", "stakeholder"
    summary: Optional[str] = None
    outcomes: Optional[str] = None
    next_action: Optional[str] = None
    follow_up_sent: bool = False

@dataclass
class Stakeholder:
    persona: Persona
    stance: Stance = Stance.NEUTRAL
    motivation_triggers: List[str] = field(default_factory=list)
    barriers: List[str] = field(default_factory=list)
    notes: Optional[str] = None
    last_updated: str = field(default_factory=lambda: datetime.now().isoformat())

@dataclass
class Deal:
    id: str
    package: str  # "a", "b", "c", "practice_build"
    price: float
    stage: str  # "discovered", "qualified", "pitched", "negotiating", "closed_won", "closed_lost"
    stakeholders: Dict[str, Stakeholder] = field(default_factory=dict)
    meetings: List[Meeting] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        return {
            "id": self.id,
            "package": self.package,
            "price": self.price,
            "stage": self.stage,
            "stakeholders": {k: {"stance": v.stance.value, "triggers": v.motivation_triggers} for k, v in self.stakeholders.items()},
            "meetings": [{"date": m.date, "type": m.type, "next_action": m.next_action} for m in self.meetings],
            "created_at": self.created_at,
        }

    def save(self):
        path = CLIENT_DIR / f"{self.id}.json"
        path.write_text(json.dumps(self.to_dict(), indent=2))
        return path

class ClientIntel:
    """Manages all IAC client intelligence."""

    def __init__(self):
        self.deals: Dict[str, Deal] = {}
        self.load_all()

    def load_all(self):
        for f in CLIENT_DIR.glob("*.json"):
            data = json.loads(f.read_text())
            deal = Deal(
                id=data["id"],
                package=data["package"],
                price=data["price"],
                stage=data["stage"],
            )
            self.deals[deal.id] = deal

    def new_deal(self, package: str, price: float) -> Deal:
        deal_id = f"iac_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        deal = Deal(id=deal_id, package=package, price=price)
        self.deals[deal_id] = deal
        deal.save()
        return deal

    def get_status(self) -> str:
        """Print current engagement status."""
        lines = ["=== IA COLLABORATIVE ENGAGEMENT STATUS ==="]
        lines.append(f"Total deals: {len(self.deals)}")
        for deal_id, deal in self.deals.items():
            lines.append(f"\nDeal: {deal_id}")
            lines.append(f"  Package: {deal.package.upper()}")
            lines.append(f"  Price: ${deal.price:,.0f}")
            lines.append(f"  Stage: {deal.stage}")
            if deal.meetings:
                last = deal.meetings[-1]
                lines.append(f"  Last meeting: {last.date} ({last.type})")
                if last.next_action:
                    lines.append(f"  Next action: {last.next_action}")
            else:
                lines.append("  No meetings yet")
        if not self.deals:
            lines.append("  No active deals. Run: new_deal('a', 125000)")
        return "\n".join(lines)

def main():
    intel = ClientIntel()
    print(intel.get_status())

if __name__ == "__main__":
    main()
