"""HandoffContract — parsed representation of agent handoff expectations."""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class HandoffContract:
    """What an agent expects to receive and must deliver."""

    agent_name: str
    receives_from: list[ContractEntry] = field(default_factory=list)
    delivers_to: list[ContractEntry] = field(default_factory=list)
    validation_items: list[str] = field(default_factory=list)

    @classmethod
    def from_content(cls, agent_name: str, content: str) -> HandoffContract:
        """Parse handoff contract from agent markdown content."""
        receives = _parse_contract_table(content, "What I expect to receive")
        delivers = _parse_contract_table(content, "What I must deliver")
        validations = _parse_checklist(content)

        return cls(
            agent_name=agent_name,
            receives_from=receives,
            delivers_to=delivers,
            validation_items=validations,
        )

    def validate_against(self, other: HandoffContract) -> list[str]:
        """Check if this agent's deliverables match what another agent expects.

        Returns a list of mismatches. Empty list = contracts are compatible.
        """
        errors = []

        # Check: does 'other' expect something from me?
        for entry in other.receives_from:
            if self.agent_name.lower() in entry.agent.lower():
                # They expect something from me — do I deliver it?
                matching = [
                    d
                    for d in self.delivers_to
                    if _sections_overlap(d.section, entry.section)
                ]
                if not matching:
                    errors.append(
                        f"{self.agent_name} does not deliver '{entry.section}' "
                        f"that {other.agent_name} expects"
                    )

        return errors


@dataclass
class ContractEntry:
    """A single row in a handoff contract table."""

    section: str
    agent: str  # consumed by / received from
    requirements: str


def _parse_contract_table(content: str, header: str) -> list[ContractEntry]:
    """Parse a markdown table under a specific header."""
    entries = []

    # Find the section
    pattern = rf"###?\s*{re.escape(header)}(.*?)(?=###|\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return entries

    section_text = match.group(1)

    # Parse table rows (skip header and separator)
    rows = re.findall(r"\|(.+?)\|(.+?)\|(.+?)\|", section_text)
    for row in rows:
        cells = [c.strip().strip("*") for c in row]
        # Skip header rows
        if cells[0].startswith("---") or cells[0] in ("Required section", "Source"):
            continue
        entries.append(
            ContractEntry(section=cells[0], agent=cells[1], requirements=cells[2])
        )

    return entries


def _parse_checklist(content: str) -> list[str]:
    """Extract self-validation checklist items."""
    items = []
    in_checklist = False
    for line in content.splitlines():
        if "Self-validation checklist" in line:
            in_checklist = True
            continue
        if in_checklist:
            stripped = line.strip()
            if stripped.startswith("- [ ]"):
                items.append(stripped[5:].strip())
            elif stripped.startswith("- [x]"):
                items.append(stripped[5:].strip())
            elif stripped.startswith("#") or (stripped == "" and items):
                break
    return items


def _sections_overlap(delivered: str, expected: str) -> bool:
    """Check if two section names refer to the same thing."""
    d = delivered.lower().strip()
    e = expected.lower().strip()
    return d == e or d in e or e in d
