# Team Handoff Chain

The full agent workflow from user request to ship. Three sprint modes are available, each with different agent chains.

---

## FULL Sprint (10 groups)

```
USER ARRIVES (idea, problem, feature request — anything)
    |
STRATEGIST [MODE: DIAGNOSE]
  Forcing questions — validates the idea before any design begins
  Outputs: strategic brief with problem, audience, risks, scope
  Verdict: VALIDATED | NEEDS WORK | PIVOT | KILL
    |
SPEC WRITER [MODE: WRITE]
  Turns strategic brief into precise, buildable specification
  Outputs: 7-section spec with acceptance criteria + edge cases
    |
ARCHITECT [MODE: DESIGN]
  Produces: system design, auth model, security model, testing strategy
  Hands off to all agents with specific briefs
    |
  +---------------------------------------+
  |                                       |
UX [MODE: FLOW -> WIREFRAME -> DESIGN -> SPEC]
  Expects: auth model, system overview    |
  Produces: user flows, wireframes,       |
  component specs, design tokens          |
                                          |
SECURITY [MODE: DESIGN-REVIEW]           |
  Expects: auth model, security model     |
  Produces: numbered auth constraints,    |
  threat model for QA                     |
  |                                       |
  +---------------------------------------+
    | (both complete before build starts)
FULLSTACK [MODE: BUILD]
  Expects: Architect design + UX specs + Security constraints
  Produces: working code, unit tests, auth implementation
    |
LOCAL REVIEW [MODE: REVIEW]
  Starts app locally -> opens browser -> takes screenshot
  Waits for human: LGTM | FEEDBACK | STOP
  Chain pauses here until human responds
    |
REVIEWER [MODE: REVIEW]
  Full review army — 7 parallel specialist checks:
  Security, Performance, Maintainability, API Contracts,
  Data Integrity, Test Coverage, Error Handling
  Verdict: APPROVE | REQUEST CHANGES | BLOCK
    |
  +---------------------------------------+
  |                                       |
QA [MODE: TEST-RUN]                      SECURITY [MODE: CODE-AUDIT]
  Runs test suite, auth test matrix       Audits code, auth implementation
  Reports findings with severity          Reports vulnerabilities with fixes
  |                                       |
  +---------------------------------------+
    |
SHIPPER [MODE: SHIP]
  Tests -> lint -> review check -> changelog -> version bump -> PR
  Outputs: PR URL, ship report
    |
RETRO [MODE: RETRO]
  What worked, what didn't, action items
  Writes learnings to project memory
    |
DONE — Sprint complete, learnings captured
```

---

## QUICK Sprint (6 groups)

```
USER ARRIVES (small feature, UI change, non-breaking addition)
    |
SPEC WRITER [MODE: WRITE] -> ARCHITECT [MODE: DESIGN]
    |
FULLSTACK [MODE: BUILD] -> LOCAL REVIEW [MODE: REVIEW]
    |
QA [MODE: TEST-RUN]
    |
SHIPPER [MODE: SHIP]
    |
DONE
```

---

## HOTFIX Sprint (3 groups)

```
USER ARRIVES (bug, incident, production issue)
    |
INVESTIGATOR [MODE: INVESTIGATE]
  Reproduce -> isolate -> trace -> identify root cause
  Outputs: investigation report + fix strategy
    |
FULLSTACK [MODE: BUILD]
  Targeted fix based on investigation report
    |
SHIPPER [MODE: SHIP]
  Tests -> PR (fast path)
    |
DONE
```

---

## Context Manager (cross-cutting)

The context-manager agent operates outside the sprint chain. It can be invoked at any point to:
- **SAVE** — snapshot current state for later resumption
- **RESTORE** — load a saved context and brief the next agent
- **LIST** — show all saved contexts

This enables multi-session sprints — pause work, come back tomorrow, restore context, continue.

---

## Handoff Artifact Summary

| Agent | Delivers to | Key required sections |
|---|---|---|
| Strategist | Spec Writer, Architect | Strategic brief, forcing questions, risk assessment, scope recommendation |
| Spec Writer | Architect, Fullstack, QA | 7-section spec with acceptance criteria and edge cases |
| Architect | UX, Security, Fullstack | System overview, tech stack, data model, API contracts, auth model, build order |
| UX | Fullstack | User flows, screen inventory, auth UX specs, component specs, design tokens |
| Security | Fullstack, DevOps | Auth constraints (numbered), threat model, vulnerability report, launch verdict |
| Fullstack | Local Review, Reviewer, QA | File manifest, auth notes, unit test results, run instructions |
| Local Review | Orchestrator | Verdict (LGTM/FEEDBACK/STOP), feedback notes |
| Reviewer | Fullstack, Shipper | 7-specialist review, severity-ranked findings, verdict |
| QA | Fullstack, Security | Test results, auth test matrix, bug report |
| Shipper | Retro | PR URL, changelog, ship report |
| Retro | All (via memory) | Learnings, action items, patterns |
| Investigator | Fullstack | Investigation report, root cause, fix strategy |
| Context Manager | Any agent | Context snapshot with decisions, rationale, next steps |
| DevOps | Users | Live URLs, deployment verification, README |
