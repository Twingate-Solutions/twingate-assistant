---
source: https://help.twingate.com/articles/6706399509-consumer-vpns
type: help
fetched: 2026-10-04
source_version: db6de5683abac452e61918d182fb6e1040b6a3032ad61b38dbb64568f9003a2d
trust: official
---

# Consumer VPNs Compatibility

## Page Title
Consumer VPNs

## Summary
Certain consumer VPN clients are incompatible with the Twingate Client because both products compete for the same OS-level networking functionality. Even when a consumer VPN appears disconnected, background processes can block Twingate from connecting. Full uninstallation (not just disabling) is required to resolve conflicts.

## Key Information
- Incompatibility is caused by VPN software occupying the same system networking layer Twingate requires
- Consumer VPNs often run background processes even when visually "disconnected"
- Issue affects the **Twingate Client** component specifically

## Known Incompatible Software
| Product | Vendor |
|---|---|
| TunnelBear | TunnelBear LLC |
| TunnelBlick | Open source |
| NordVPN | Nord Security |
| ExpressVPN | ExpressVPN |
| InfoBlox BloxOne | Infoblox |
| PIA VPN (Private Internet Access) | Private Internet Access |
| HMA VPN (HideMyAss) | Avast |
| CSC/AnyConnect Umbrella Roaming Security Module | Cisco |

## Prerequisites
N/A — this is a compatibility/troubleshooting reference.

## Resolution Steps
1. Identify any consumer VPN software installed on the machine (including software not actively in use)
2. Perform a **full uninstall** of the conflicting VPN client — disabling or pausing is insufficient
3. Retest Twingate Client connectivity after uninstallation

## Gotchas
- A VPN that **appears** disconnected or inactive may still have background services running that block Twingate
- Simply disabling the VPN is not a reliable fix; full removal is required
- Cisco AnyConnect's **Umbrella Roaming Security Module** is specifically called out — note this is distinct from standard AnyConnect usage in enterprise environments

## Related Docs
- Twingate Client troubleshooting (general connectivity issues)
- Enterprise VPN coexistence (separate topic — consumer VPNs are distinct from corporate VPN compatibility)