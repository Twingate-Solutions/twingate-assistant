---
source: https://www.twingate.com/docs/netskope-dlp-config
type: docs
fetched: 2026-09-06
source_version: 67c381877de692224e68d08e43386bc8e9bda4fc213bbd54281b29d990c52560
---

# How to Configure Netskope DLP to Work with Twingate

## Summary
Configures Netskope DLP client to coexist with Twingate Client on the same device by creating a certificate-pinned application exception. Only applies when Netskope is configured for **Web Traffic** steering mode.

## Key Information
- Netskope steers traffic via a client app that can conflict with Twingate
- Solution: Create a bypass exception using a certificate-pinned application definition
- Applies to macOS and Windows platforms
- Dynamic Steering users must check steering type for **both** on-premises and remote configurations

## Prerequisites
- Netskope configured for **Web Traffic** or **All Traffic** steering (not Cloud Apps Only)
- Access to Netskope admin console
- Twingate Client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application
- Navigate to **Settings → App Definition**
- Create new **certificate pinned application** (name: `Twingate`)
- Add platform entries with `Exact` match type:

| Platform | Definition |
|----------|-----------|
| macOS | `Twingate, Tunnel Provider macos` |
| Windows | `twingate.exe, twingate.service.exe, twingateupdater.exe` |

### 2. Create Steering Exception
- Navigate to **Settings → Steering Configuration**
- Open existing config or create new one
- Under **Exceptions** tab, create new exception:
  - Exception type: **Certificate Pinned Application**
  - Application: Select the `Twingate` app created above
  - Custom app domains: `*`
  - Action for each OS: **bypass**
- Save the exception

### 3. Apply Configuration
- Click Netskope client icon → **Configuration → Update**
- Restart the Twingate Client

## Configuration Values

| Field | Value |
|-------|-------|
| macOS process names | `Twingate, Tunnel Provider macos` |
| Windows process names | `twingate.exe, twingate.service.exe, twingateupdater.exe` |
| Match type | `Exact` |
| Custom app domains | `*` |
| Exception action | `bypass` |

## Gotchas
- **Dynamic Steering**: Must verify steering type applies for both on-prem and remote profiles — if either uses Web Traffic, this config is needed
- **Cloud Apps Only** steering does not require this configuration
- Must restart Twingate Client after pulling updated Netskope config
- All three Windows executables must be included in the definition

## Related Docs
- Netskope Steering Configuration documentation
- Twingate Client installation guides (macOS/Windows)