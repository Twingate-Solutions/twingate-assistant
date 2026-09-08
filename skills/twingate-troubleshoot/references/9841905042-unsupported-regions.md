---
source: https://help.twingate.com/articles/9841905042-unsupported-regions
type: help
fetched: 2026-09-06
source_version: 87f605c7db8a68843a378f9046501c380ec54efe12dd0d97f84a1e5bc67018cb
---

# Unsupported Regions

## Summary
Twingate does not explicitly block regions, but some countries block traffic required for Twingate to function. Restrictions may occur at DNS, IP, or port level, affecting Connectors and Relays even when `twingate.com` is browser-accessible. GCP (upstream provider) also independently blocks certain regions.

## Key Information
- Browser access to `.twingate.com` may work while Connector/Relay services remain blocked
- China's Great Firewall most commonly causes Connector→Relay connectivity loss (instability or full outage)
- GCP independently enforces its own regional blocks regardless of Twingate policy
- Affects all Twingate components: Client, Connector, Controller, Relays

## Known Unsupported Regions
| Region | Notes |
|--------|-------|
| China | Great Firewall interferes with Connector↔Relay connectivity |
| Crimea, Donetsk & Luhansk (Ukraine) | GCP/geopolitical restrictions |
| Cuba | GCP/sanctions |
| Iran | GCP/sanctions |
| North Korea | GCP/sanctions |
| Syria | GCP/sanctions |

> List is not exhaustive — other regions with heavy internet filtering may also experience issues.

## Workarounds
- **No official workarounds** are provided by Twingate
- Deploy Connectors outside affected regions when possible
- Security and legal barriers may prevent Twingate from offering solutions

## Gotchas
- Connectivity issues in these regions may appear as intermittent instability rather than a clean failure, making diagnosis harder
- The Connector losing Relay connectivity is the most common failure mode in China — not a full block of all services
- This list is not exhaustive; any country with aggressive internet filtering is a potential risk

## Related Docs
- Twingate Connector documentation
- Twingate Relay architecture
- GCP blocked regions: [cloud.google.com](https://cloud.google.com/terms/restricted-service-terms)