---
source: https://help.twingate.com/articles/9841905042-unsupported-regions
type: help
fetched: 2026-11-08
source_version: 311c3090d2f04a92aaffcd8fbfddef56375589f52d98ac3f10c417064f8bc18a
trust: official
---

# Unsupported Regions

## Page Title
Unsupported Regions

## Summary
Twingate does not explicitly block regions, but some countries block traffic required for Twingate to function, and upstream provider GCP independently blocks certain regions. Connectivity issues may occur at the DNS, IP, or port level, even if `.twingate.com` loads in a browser.

## Key Information
- Twingate itself does not block regions; restrictions come from local governments or GCP
- Browser access to `.twingate.com` may succeed even when Connector/Relay/Controller connectivity fails
- Most common failure mode: Connector loses connectivity to Twingate Relays
- Applies to all Twingate components: Client, Connector, Controller, Relays

## Unsupported/Blocked Regions
| Region | Notes |
|--------|-------|
| China | Great Firewall interferes with Connector↔Relay connectivity; causes instability or full disconnection |
| Crimea, Donetsk & Luhansk (Ukraine) | Blocked via GCP |
| Cuba | Blocked via GCP |
| Iran | Blocked via GCP |
| North Korea | Blocked via GCP |
| Syria | Blocked via GCP |

> **Note:** This list is not exhaustive; other regions with heavy internet filtering may also be affected.

## Workarounds
- **No supported workarounds** from Twingate for end-users in these regions
- **Deploy Connectors outside** of affected regions when possible — this is the only recommended mitigation
- Security and legal constraints may apply beyond technical filtering

## Gotchas
- DNS, IP, or port-level blocking can affect Twingate even when basic HTTPS to `.twingate.com` works — do not use browser access as a connectivity proxy
- GCP-level blocking is outside Twingate's control and cannot be overridden by Twingate configuration
- The list of affected regions can change based on geopolitical developments; treat it as non-exhaustive

## Related Docs
- [GCP blocked regions](https://cloud.google.com/terms/restricted-countries) (referenced upstream provider policy)
- Twingate Connector deployment documentation