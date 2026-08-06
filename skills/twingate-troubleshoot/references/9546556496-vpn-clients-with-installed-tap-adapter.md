---
source: https://help.twingate.com/articles/9546556496-vpn-clients-with-installed-tap-adapter
type: help
fetched: 2026-08-06
source_version: c42f7d26446adf55f87cab3ad2d232504c73f84423de1b06c2cfa66504014826
---

# VPN Clients With Installed TAP Adapter

## Summary
Certain Windows VPN clients that use TAP adapters can interfere with the Twingate TAP adapter, causing connectivity issues. This applies to the Twingate Windows client and affects specific VPN software even when not actively running.

## Key Information
- Conflict occurs because both Twingate and some VPN clients attempt to use the same Windows system functionality (TAP adapter)
- VPN software can interfere even when not actively connected or running
- Issue is Windows-specific

## Known Incompatible Software

**OpenVPN:**
- TAP-Windows Adapter V9 for OpenVPN Connect
- TAP-Windows Provider V9 for OpenVPN Connect

**Fortinet:**
- TAP-Windows Adapter V9 ftsvnic
- Fortinet SSL VPN Virtual Ethernet Adapter

## Resolution Steps
1. Identify if any of the above VPN clients are installed (even if not in use)
2. Perform a **full uninstall** of the conflicting VPN software
3. Test Twingate connectivity after uninstall

## Gotchas
- Software does **not** need to be actively running to cause interference — installation alone is sufficient to trigger conflicts
- Partial uninstalls or simply disabling the VPN may not resolve the issue; full uninstall is required

## Related Docs
- Known Incompatibility Overview
- Joining a Twingate network fails with "Unable to join network"