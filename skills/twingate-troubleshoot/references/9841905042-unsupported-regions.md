---
source: https://help.twingate.com/articles/9841905042-unsupported-regions
type: help
fetched: 2026-08-06
source_version: 74ed4be0e7bd1e44e08bb98e0ef6213a0e1b927de3ceb1e10d24e5a018bc2add
---

# Unsupported Regions

## Summary
Twingate does not explicitly block regions, but certain countries block traffic required for Twingate functionality. Restrictions may occur at DNS, IP, or port level, affecting Connector-to-Relay connectivity. GCP (upstream provider) also independently blocks some regions.

## Key Information
- Browsing `.twingate.com` may work even when Twingate services are blocked
- Most common failure mode: Connector loses connectivity to Relays
- Blocks can occur at DNS, IP, or port level
- GCP independently enforces some regional blocks beyond Twingate's control

## Affected Components
All components: Client, Connector, Controller, Relays

## Unsupported/Blocked Regions
| Region | Notes |
|--------|-------|
| China | Great Firewall causes instability or full connection failure; Connector-to-Relay most affected |
| Crimea, Donetsk & Luhansk (Ukraine) | GCP/sanctions-based blocks |
| Cuba | GCP/sanctions-based blocks |
| Iran | GCP/sanctions-based blocks |
| North Korea | GCP/sanctions-based blocks |
| Syria | GCP/sanctions-based blocks |

*List is not exhaustive — other regions with heavy internet filtering may also be affected.*

## Workarounds
- **No direct workarounds available** from Twingate
- Deploy Connectors **outside** of impacted regions when possible
- Restrictions may involve security, legal, or geopolitical factors outside Twingate's control

## Gotchas
- `.twingate.com` web access working does **not** confirm full Twingate functionality — backend services (Relays, Controllers) may still be blocked
- China specifically has documented instability (not always a full block), making it hard to diagnose intermittently
- The list is explicitly non-exhaustive; any country with aggressive internet filtering could cause issues

## Related Docs
- GCP blocked regions: [Google Cloud Platform documentation](https://cloud.google.com/terms/restricted-countries)
- Twingate Connector deployment guidance