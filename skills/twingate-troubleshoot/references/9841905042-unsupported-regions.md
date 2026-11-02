---
source: https://help.twingate.com/articles/9841905042-unsupported-regions
type: help
fetched: 2026-11-01
source_version: 2c4694ea259c5b5b2e76bbfa02bfe93f021319c200013290739de1d20505a95a
trust: official
---

# Unsupported Regions

## Page Title
Unsupported Regions

## Summary
Twingate does not explicitly block regions, but certain countries block traffic required for Twingate to function. GCP (Twingate's upstream provider) also enforces its own regional blocks. These restrictions can affect DNS, IP, or port-level connectivity for Connectors, Controllers, and Relays.

## Key Information
- Twingate access via browser to `.twingate.com` may still work in restricted regions, but Connector/Relay/Controller services may be blocked
- Blockages can occur at DNS, IP, or port level
- China's Great Firewall specifically causes Connector-to-Relay connectivity instability or full failure
- GCP independently enforces sanctions-based regional blocks

## Affected Components
All Twingate components: Client, Connector, Controller, Relays

## Unsupported/Blocked Regions
| Region | Notes |
|---|---|
| China | Great Firewall interferes with Connector↔Relay connectivity; instability or full failure |
| Crimea, Donetsk & Luhansk (Ukraine) | GCP/sanctions-based block |
| Cuba | GCP/sanctions-based block |
| Iran | GCP/sanctions-based block |
| North Korea | GCP/sanctions-based block |
| Syria | GCP/sanctions-based block |

> List is not exhaustive — other regions with heavy internet filtering may also be affected.

## Workarounds
- **No official workarounds available** from Twingate
- **Best practice:** Deploy Connectors outside of affected regions when possible
- Security and legal barriers are beyond Twingate's control

## Gotchas
- Browser access to `.twingate.com` succeeding does **not** mean Twingate is functional — Relay/Controller services may still be blocked
- The most common failure mode in China is the Connector losing connectivity to Relays specifically
- The blocked region list is not exhaustive; any country with heavy internet filtering may have partial or full Twingate failure

## Related Docs
- Twingate Connector documentation
- Twingate Relay documentation
- [GCP regional restrictions](https://cloud.google.com/terms/restricted-countries)