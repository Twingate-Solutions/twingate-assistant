---
source: https://help.twingate.com/articles/9841905042-unsupported-regions
type: help
fetched: 2026-10-04
source_version: 33b2719244230fb7e1860cb81f6f7e638a912c106c4f7abc96817fcf2856d354
trust: official
---

# Unsupported Regions

## Page Title
Unsupported Regions

## Summary
Twingate does not explicitly block regions, but some countries block traffic required for Twingate to function. GCP (Twingate's upstream provider) also enforces its own regional blocks. Blockages may occur at DNS, IP, or port level, even if `twingate.com` is reachable in a browser.

## Key Information
- Twingate components affected: Client, Connector, Controller, Relays
- `.twingate.com` browser access may work even when Connector/Relay services are blocked
- China is the most commonly reported issue: the Great Firewall interferes with Connector-to-Relay connectivity, causing instability or full disconnection

## Known Unsupported Regions
| Region | Cause |
|---|---|
| China | Great Firewall blocks Connector↔Relay traffic |
| Crimea, Donetsk & Luhansk (Ukraine) | GCP block |
| Cuba | GCP block |
| Iran | GCP block |
| North Korea | GCP block |
| Syria | GCP block |

*List is not exhaustive — other areas may restrict internet traffic.*

## Workarounds
- **None provided by Twingate** — restrictions stem from legal, security, or geopolitical factors outside Twingate's control
- **Best practice:** Deploy Connectors outside of affected regions when possible

## Gotchas
- Browser access to `.twingate.com` succeeding does **not** confirm full Twingate functionality — Relay and Controller services may still be blocked
- Blocks can occur at multiple layers (DNS, IP, port), making diagnosis inconsistent
- China specifically tends to exhibit partial failures (Connector loses Relay connectivity) rather than complete blocks, which can be harder to diagnose

## Related Docs
- [GCP blocked regions](https://cloud.google.com/terms/restricted-geographies) (referenced but external)
- Twingate Connector deployment documentation