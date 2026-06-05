# Agent Modes Reference

Every agent supports a `PLAN` mode as its entry point for when you're unsure what you need. Below is the full list of modes per agent.

---

## Orchestrator (`/agency-run`)

| Mode | Description |
|---|---|
| **FULL** | Full sprint: Think → Plan → Build → Review → Test → Ship → Reflect |
| **QUICK** | Quick sprint: Plan → Build → Test → Ship |
| **HOTFIX** | Hotfix sprint: Investigate → Build → Ship |

---

## Strategist (`/strategist`)

| Mode | Description |
|---|---|
| **PLAN** | Quick triage of an idea — assess clarity and recommend next mode |
| **DIAGNOSE** | Forcing questions mode — ask hard questions one at a time, minimum 5 before any recommendation |
| **REVIEW** | Strategic review of existing plan/product — score across 6 dimensions |
| **CHALLENGE** | Adversarial mode — try to kill the idea. Outputs survival report |

---

## Spec Writer (`/spec-writer`)

| Mode | Description |
|---|---|
| **PLAN** | Assess what spec work is needed — new spec, refinement, or issue decomposition |
| **WRITE** | Interactive spec creation with 7 required sections and acceptance criteria |
| **REFINE** | Ambiguity scanner — find gaps, contradictions, untestable requirements in existing specs |
| **ISSUE** | Generate GitHub issues from spec — one per deliverable with priority and complexity |

---

## Architect (`/architect`)

| Mode | Description |
|---|---|
| **PLAN** | Turn a vague idea into a clear architectural starting point before committing to a full design |
| **DIAGNOSE** | Default entry point — read any request and recommend which agents are needed, in what order |
| **DESIGN** | Full system design: tech stack, data model, API contracts, auth model, security model, caching, scaling |
| **REVIEW-DESIGN** | Audit an existing architecture for structural risks, scalability concerns, and auth gaps |
| **ENG-REVIEW** | Architecture lock-in checkpoint — score 6 dimensions before build starts |

---

## UX (`/ux`)

| Mode | Description |
|---|---|
| **PLAN** | Assess what UX/UI work is needed and map out the design sequence |
| **FLOW** | Map user journeys, personas, navigation architecture, and auth flows before any screens |
| **WIREFRAME** | Low-fidelity layout and hierarchy for every screen including all states |
| **DESIGN** | Full visual design: design tokens, component library, screen designs, accessibility |
| **SPEC** | Developer-ready component specifications for the Full Stack Agent |
| **AUDIT** | Design dimension audit — score existing UI/UX across 8 dimensions (0-10) |

---

## Full Stack (`/fullstack`)

| Mode | Description |
|---|---|
| **PLAN** | Turn an idea into an actionable engineering brief with stack, structure, and build order |
| **BUILD** | Build a feature with complete working code, unit tests, and auth implementation |
| **REFACTOR** | Improve existing code with auth anti-pattern review and updated tests |
| **DEBUG** | Fix a reported issue with root cause, fix, and regression test |
| **REVIEW** | Code audit focused on quality, correctness, and auth security |

---

## Investigator (`/investigator`)

| Mode | Description |
|---|---|
| **PLAN** | Triage a bug report — assess severity, reproducibility, blast radius |
| **INVESTIGATE** | Full root-cause investigation: reproduce → isolate → trace → identify |
| **AUTOPSY** | Post-incident analysis — timeline, contributing factors, prevention measures |
| **TRACE** | Follow a specific code path end-to-end with annotations |

---

## Reviewer (`/reviewer`)

| Mode | Description |
|---|---|
| **PLAN** | Assess review scope and recommend REVIEW vs QUICK mode |
| **REVIEW** | Full review army — 7 parallel specialist checks (security, performance, maintainability, API, data, tests, errors) |
| **QUICK** | Single-pass review covering all areas sequentially |
| **SECURITY** | Security-focused review for auth and data changes |

---

## QA (`/qa`)

| Mode | Description |
|---|---|
| **PLAN** | Assess testing situation and produce a clear testing strategy |
| **TEST-PLAN** | Create a testing plan with unit test checklist, integration cases, and auth test matrix |
| **TEST-RUN** | Execute tests and report findings with severity and reproduction steps |
| **REGRESSION** | Verify fixes didn't break anything, with auth flow re-validation |
| **BROWSER** | Browser-based QA testing via MCP browser tools |
| **REPORT** | Report-only mode — document issues without fixing them |

---

## DevOps (`/devops`)

| Mode | Description |
|---|---|
| **PLAN** | Assess deployment needs and produce a clear infrastructure strategy |
| **PIPELINE** | Build CI/CD pipeline configuration — lint, test, build, deploy |
| **DOCKERIZE** | Containerize the application with multi-stage Dockerfile and docker-compose |
| **DEPLOY** | Deploy to Vercel (frontend) + Cloudflare Workers (backend) — asks user first |
| **INCIDENT** | Deployment failure response — rollback, root cause, fix, hardening |
| **CANARY** | Post-deploy monitoring — health checks, error rates, key flow verification |

---

## Security (`/security`)

| Mode | Description |
|---|---|
| **PLAN** | Assess security risks and produce a strategy before any audit begins |
| **DESIGN-REVIEW** | Review the Architect's auth and security model before build starts |
| **CODE-AUDIT** | Audit delivered code with auth as the primary surface |
| **LAUNCH-AUDIT** | Final security sign-off with pass/fail checklist and launch verdict |
| **INCIDENT** | Security incident response: containment, scope, root cause, remediation |
| **AUDIT** | Full OWASP Top 10 + STRIDE threat model audit |

---

## Shipper (`/shipper`)

| Mode | Description |
|---|---|
| **PLAN** | Pre-ship checklist — verify tests, review, uncommitted changes |
| **SHIP** | Full pipeline: tests → lint → review check → changelog → version bump → PR |
| **CHANGELOG** | Generate changelog from commits since last release |
| **VERSION** | Determine and apply version bump (major/minor/patch) with rationale |

---

## Retro (`/retro`)

| Mode | Description |
|---|---|
| **PLAN** | Assess what retrospective work is needed |
| **RETRO** | Full retrospective: what worked, what didn't, action items. Writes to project memory |
| **LEARN** | Record a single learning from the current session |
| **REVIEW** | Surface past learnings relevant to the current task |

---

## Context Manager (`/context-manager`)

| Mode | Description |
|---|---|
| **PLAN** | Assess what context work is needed |
| **SAVE** | Snapshot current context with 7 required sections to `.claude/memory/context/` |
| **RESTORE** | Load saved context and brief the receiving agent |
| **LIST** | Show all saved contexts with timestamps and summaries |

---

## Installer (`/installer` or auto-dispatched)

| Mode | Description |
|---|---|
| *(no named modes)* | Lists available agents, installs agents globally or per-project, installs starter templates, verifies installation, recommends which agent to start with |

---

## Local Review (invoked by `/agency-run`)

| Mode | Description |
|---|---|
| **REVIEW** | Starts the local dev server, opens the browser, takes a screenshot, and waits for human verdict (LGTM / FEEDBACK / STOP) before the chain continues |
