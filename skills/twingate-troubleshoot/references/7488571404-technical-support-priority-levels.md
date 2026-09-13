---
source: https://help.twingate.com/articles/7488571404-technical-support-priority-levels
type: help
fetched: 2026-09-13
source_version: d42ca7ff1dadd7dbec379ec430d123b1a48583a681f47b9a6f5a4ef0dcaac3f2
---

# Technical Support Priority Levels

## Page Title
Technical Support Priority Levels

## Summary
Defines four priority levels (P1–P4) for classifying issues when engaging Twingate Technical Support. Proper priority alignment helps route and resolve issues efficiently.

## Priority Level Definitions

| Level | Name | Description | Example |
|-------|------|-------------|---------|
| **P1** | Urgent | Core/mission-critical services not responding; large user impact; no workaround | Most users cannot authenticate or access resources |
| **P2** | High | Services functional but degraded; potentially severe impact for multiple users | Connector or Remote Network issue blocking multiple users |
| **P3** | Normal | Non-critical; minimal performance impact; affects specific users | Some users have issues with Client or a specific Resource |
| **P4** | Low | Non-impacting; informational only | — |

## Key Decision Criteria

- **Scale of impact**: Large number of users (P1/P2) vs. specific users (P3/P4)
- **Service state**: Completely down (P1) vs. degraded (P2) vs. functional (P3/P4)
- **Workaround availability**: No workaround = higher priority (P1)
- **Component affected**: Auth/core services (P1) → Connector/Network (P2) → Client/single Resource (P3)

## Gotchas

- Misaligned priority levels are explicitly discouraged — assess actual impact before selecting
- P2 requires services to still be *responding* but degraded; full outage = P1
- P3 covers individual user issues even if the underlying cause is a shared component

## Related Docs
- Engaging Technical Support (referenced but not linked in source)