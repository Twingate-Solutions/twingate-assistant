---
source: https://help.twingate.com/articles/6706399509-consumer-vpns
type: help
fetched: 2026-11-01
source_version: 4d3eccbf545571990b8d420fec858f9ae4390d0fdbcef44e6e2a446469bdec42
trust: official
---

# Consumer VPNs Compatibility

## Page Title
Consumer VPNs

## Summary
Certain consumer VPN clients are incompatible with the Twingate Client because both attempt to use the same system-level networking functionality. These VPNs often run background processes even when appearing disconnected, blocking Twingate from operating. Full uninstallation (not just disabling) is required to resolve conflicts.

## Key Information
- Applies to: **Twingate Client** component only
- Incompatibility cause: competing for the same OS networking/tunnel interfaces
- Consumer VPNs may run background processes even when visually "disconnected"
- Issue manifests as Twingate connectivity failures

## Known Incompatible VPN Clients
- TunnelBear
- TunnelBlick
- NordVPN
- ExpressVPN
- InfoBlox BloxOne
- PIA VPN (Private Internet Access)
- HMA VPN (HideMyAss)
- CSC/AnyConnect Umbrella Roaming Security Module

## Prerequisites
N/A

## Resolution Steps
1. Identify any installed consumer VPN software on the affected machine
2. Perform a **full uninstall** of the conflicting VPN client — do not simply disable or disconnect it
3. Retest Twingate Client connectivity after uninstallation

## Configuration Values
None applicable.

## Gotchas
- A VPN appearing "disconnected" or "off" in its UI does **not** mean its background processes have stopped — uninstall is required, not just toggling off
- If multiple VPN products are installed, uninstall all of them before testing
- CSC/AnyConnect Umbrella Roaming Security Module (a corporate security tool, not just a consumer VPN) is also on the incompatible list — flag this for IT teams deploying Twingate alongside Cisco Umbrella

## Related Docs
- Twingate Client documentation
- Twingate network compatibility / system requirements