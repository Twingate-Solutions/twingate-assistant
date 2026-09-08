---
source: https://help.twingate.com/articles/9546556496-vpn-clients-with-installed-tap-adapter
type: help
fetched: 2026-09-06
source_version: a5f42c9344f5526b98fd1c8e07ecde3b4714417d0a7428d805dd5fd035a87638
---

# VPN Clients With Installed TAP Adapter

## Summary
Some Windows VPN clients using TAP Adapters conflict with Twingate's TAP Adapter, causing connectivity issues. This affects OpenVPN and Fortinet products specifically. The conflict can occur even when the third-party VPN is not actively running.

## Key Information
- **Platform**: Windows only
- **Affected component**: Twingate Client
- Conflict arises because both Twingate and certain VPNs compete for the same system-level TAP Adapter functionality
- Interference can be intermittent, not always consistent

## Known Incompatible Software

| Vendor | Conflicting Adapter/Component |
|--------|-------------------------------|
| OpenVPN | TAP-Windows Adapter V9 for OpenVPN Connect |
| OpenVPN | TAP-Windows Provider V9 for OpenVPN Connect |
| Fortinet | TAP-Windows Adapter V9 ftsvnic |
| Fortinet | Fortinet SSL VPN Virtual Ethernet Adapter |

## Resolution

**Full uninstall of conflicting VPN software** is the recommended fix:
1. Identify if any of the listed VPN clients are installed (even if unused or not running)
2. Perform a **complete uninstall** of the conflicting VPN software
3. Retest Twingate Client connectivity

## Gotchas
- The VPN does **not** need to be actively running to cause interference — installed-only state is sufficient to trigger the conflict
- Interference is described as "occasional," meaning it may not reproduce consistently, making diagnosis harder
- No workaround short of full uninstall is documented

## Related Docs
- Known Incompatibility Overview
- "Joining a Twingate network fails with 'Unable to join network'"