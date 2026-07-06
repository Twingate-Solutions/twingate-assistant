# How to Configure Netskope DLP to Work with Twingate

## Summary
Configures Netskope DLP to bypass inspection for Twingate Client processes when both applications are installed on the same device. Creates a certificate pinned application exception in Netskope Steering Configuration to prevent conflicts between the two clients.

## Key Information
- Applies when Netskope DLP client and Twingate Client are co-installed on the same device
- Solution uses Netskope's "Certificate Pinned Application" exception mechanism
- Supports macOS and Windows platforms
- Changes require manual config pull and Twingate Client restart to take effect

## Prerequisites
- Access to Netskope admin console
- Existing or new Netskope Steering Configuration
- Twingate Client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application in Netskope
- Navigate to **Settings → App Definition**
- Create a new **certificate pinned application** (recommended name: "Twingate")
- Add platform entries with **Exact** match type:

| Platform | Definition |
|----------|------------|
| macOS | `Twingate, Tunnel Provider macos` |
| Windows | `twingate.exe, twingate.service.exe, twingateupdater.exe` |

### 2. Create Steering Exception
- Navigate to **Settings → Steering Configuration**
- Open existing config or create new one
- Under **Exceptions** tab, create a new exception:
  - Exception type: **Certificate Pinned Application**
  - Application: Select the "Twingate" app created above
  - Custom app domains: `*`
  - Action for each OS: **bypass**
- Save the exception

### 3. Apply Configuration to Clients
- Click Netskope client icon → **Configuration → Update** (pulls latest config)
- Restart the Twingate Client

## Configuration Values

| Field | Value |
|-------|-------|
| macOS process names | `Twingate, Tunnel Provider macos` |
| Windows process names | `twingate.exe, twingate.service.exe, twingateupdater.exe` |
| Match type | `Exact` |
| Exception type | `Certificate Pinned Application` |
| Custom app domains | `*` |
| Bypass action | `bypass` (all OS) |

## Gotchas
- Must restart Twingate Client after pulling Netskope config update — config pull alone is insufficient
- Use wildcard `*` for custom app domains field in the exception
- All three Windows executables must be included; omitting any may cause partial conflicts
- Exception must be set to **bypass** per operating system, not just globally

## Related Docs
- Netskope Steering Configuration documentation (Netskope console)
- Twingate Client installation guides (platform-specific)