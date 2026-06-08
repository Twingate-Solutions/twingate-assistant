# How to Configure Netskope DLP to Work with Twingate

## Summary
Configures Netskope DLP client to bypass inspection for Twingate Client processes when both applications are installed on the same device. Creates a certificate pinned application exception in Netskope so the two clients don't conflict.

## Key Information
- Applies when Netskope DLP client and Twingate Client are co-installed on the same device
- Solution uses Netskope's "Certificate Pinned Application" exception type
- Covers macOS and Windows platforms
- Configuration is applied via Netskope Steering Configuration

## Prerequisites
- Access to Netskope admin console
- Existing or new Netskope Steering Configuration
- Twingate Client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application in Netskope
- Navigate to **Settings → App Definition**
- Create a new **certificate pinned application** (recommended name: "Twingate")
- Add entries per platform using **Exact** match type:

| Platform | Definition |
|----------|-----------|
| macOS | `Twingate, Tunnel Provider macos` |
| Windows | `twingate.exe, twingate.service.exe, twingateupdater.exe` |

### 2. Create Steering Exception
- Navigate to **Settings → Steering Configuration**
- Open existing config or create new one
- Under **Exceptions** tab, create a new exception:
  - **Exception type:** Certificate Pinned Application
  - **Application:** Select the Twingate app created in Step 1
  - **Custom app domains:** `*`
  - **Action (all OS):** `bypass`
- Save the exception

### 3. Apply Configuration to Clients
- Click Netskope client icon → **Configuration** → **Update** (pulls latest config)
- Restart the Twingate Client

## Configuration Values

| Field | Value |
|-------|-------|
| App type | Certificate Pinned Application |
| macOS processes | `Twingate, Tunnel Provider macos` |
| Windows processes | `twingate.exe, twingate.service.exe, twingateupdater.exe` |
| Custom app domains | `*` |
| Bypass action | `bypass` (all operating systems) |

## Gotchas
- Must restart Twingate Client after pushing updated Netskope config — config update alone is insufficient
- All three Windows process names must be included; omitting any may cause partial conflicts
- The `*` wildcard is required in the custom app domains field

## Related Docs
- Netskope App Definition documentation (Netskope console)
- Netskope Steering Configuration documentation (Netskope console)
- Twingate Client installation guides