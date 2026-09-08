---
source: https://help.twingate.com/articles/3201241878-vpn-profile-fails-to-deploy-for-macos-using-jamf-pro
type: help
fetched: 2026-09-06
source_version: 1d1aeb7da6829a85f96b010ce8b582b4c7ab85d89043ad851df1bd041a6951d1
---

# VPN Profile Fails to Deploy for macOS Using Jamf Pro

## Summary
Jamf Pro version 11.11 has a bug (PI122416) preventing Twingate VPN Custom Configuration Profiles from installing on macOS devices. A workaround exists involving building and signing the profile outside of Jamf Pro before uploading.

## Key Information
- **Affected version**: Jamf Pro 11.11
- **Fixed in**: Jamf Pro 11.12.1
- **Jamf bug ID**: PI122416 (critical severity)
- **Impact**: Twingate VPN Custom Configuration Profile fails to install on any macOS device managed by affected Jamf Pro versions

## Workaround: Build and Sign Profile Externally

### Prerequisites
- [iMazing Profile Editor](https://imazing.com/profile-editor) (or equivalent profile signing tool)
- A valid signing certificate
- Access to Jamf Pro admin console

### Step-by-Step
1. Open **iMazing Profile Editor** (or similar tool)
2. Build the VPN Custom Configuration Profile outside of Jamf Pro
3. Export the profile and **sign it** with a signing certificate during export
4. Upload the signed profile to Jamf Pro
5. Verify upload success — Jamf Pro will display that the profile is signed and **signature removal is required to make changes**
6. **Do not remove the signature**
7. Deploy the profile as normal through Jamf Pro

## Gotchas
- Signing prevents Jamf Pro from modifying the profile on upload, which is the intentional bypass for this bug
- If you remove the signature after upload, the workaround will not function correctly
- Any future edits to the profile must be done externally, re-signed, and re-uploaded — you cannot edit a signed profile directly in Jamf Pro
- Upgrade to Jamf Pro 11.12.1+ to eliminate the need for this workaround

## Related Docs
- Twingate macOS Jamf Pro deployment documentation
- [iMazing Profile Editor](https://imazing.com/profile-editor)