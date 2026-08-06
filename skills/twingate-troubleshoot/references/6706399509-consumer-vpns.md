---
source: https://help.twingate.com/articles/6706399509-consumer-vpns
type: help
fetched: 2026-08-06
source_version: 70c16fa91305ae865dd8248f36476e297697258bc5b0ce19fb4c0f5e54398c23
---

# Consumer VPNs Compatibility

## Page Title
Consumer VPNs

## Summary
Certain consumer VPN clients are incompatible with the Twingate Client because both products compete for the same OS-level networking functionality. Consumer VPNs often run background processes even when appearing disconnected, preventing Twingate from connecting. Full uninstallation of conflicting VPN software is the recommended resolution.

## Key Information
- Incompatibility occurs at the OS networking layer — both products require exclusive access to the same system functions
- Consumer VPNs may appear disconnected/disabled but still run background processes that block Twingate
- Simply pausing or disabling a VPN client is insufficient; full uninstall is required

## Prerequisites
- Twingate Client installed
- Awareness of any VPN software installed on the endpoint (even inactive ones)

## Known Incompatible Consumer VPN Clients
- TunnelBear
- TunnelBlick
- NordVPN
- ExpressVPN
- InfoBlox BloxOne
- PIA VPN (Private Internet Access)
- HMA VPN (HideMyAss)
- CSC/AnyConnect Umbrella Roaming Security Module

## Step-by-Step Resolution
1. Identify any installed VPN software on the endpoint
2. Fully uninstall the conflicting VPN client (not just disable or disconnect)
3. Retest Twingate Client connectivity

## Gotchas
- VPN software may appear disconnected or inactive in the UI but still runs background services that interfere — do not assume it is safe to leave installed
- This applies even if the user does not actively use the consumer VPN
- AnyConnect Umbrella Roaming Security Module is included — this is commonly deployed as a security tool, not a traditional VPN, so users may not realize it's installed

## Affected Component
- **Twingate Component:** Client

## Related Docs
- Twingate Client troubleshooting documentation
- Enterprise VPN split-tunneling compatibility (separate topic)