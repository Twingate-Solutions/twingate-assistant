---
source: https://help.twingate.com/articles/6706399509-consumer-vpns
type: help
fetched: 2026-09-06
source_version: aef14c776c3b07852250626792a9bb24e42fdec240cf2ffd662b621c3074db3d
---

# Consumer VPNs Compatibility

## Page Title
Consumer VPNs

## Summary
Certain consumer VPN clients are incompatible with the Twingate Client because both attempt to use the same system-level networking functionality. These VPNs often run background processes even when appearing disconnected, blocking Twingate from operating. Full uninstallation (not just disabling) is the recommended fix.

## Key Information
- Incompatibility is caused by VPN software competing for the same OS networking interfaces Twingate requires
- Consumer VPNs frequently run background processes even when the UI shows them as disconnected
- Issue affects the **Twingate Client** component specifically

## Known Incompatible Software
| Product | Vendor |
|---|---|
| TunnelBear | TunnelBear |
| TunnelBlick | Open source |
| NordVPN | Nord Security |
| ExpressVPN | ExpressVPN |
| InfoBlox BloxOne | InfoBlox |
| PIA VPN (Private Internet Access) | Private Internet Access |
| HMA VPN (HideMyAss) | Aura |
| CSC/AnyConnect Umbrella Roaming Security Module | Cisco |

## Resolution Steps
1. Identify if any consumer VPN software is installed on the machine (even if not actively used)
2. Perform a **full uninstall** of the conflicting VPN — do not merely disable or disconnect it
3. Retest Twingate Client connectivity after uninstallation

## Gotchas
- VPNs that *appear* disconnected may still have active background services blocking Twingate
- Simply pausing or toggling off the VPN is insufficient — full removal is required
- Cisco AnyConnect's **Umbrella Roaming Security Module** is listed separately from standard AnyConnect; standard enterprise AnyConnect compatibility is not addressed here

## Related Docs
- Twingate Client troubleshooting (general connectivity issues)
- Enterprise VPN compatibility (separate from consumer VPNs)