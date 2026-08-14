---
source: https://www.twingate.com/docs/netskope-dlp-config
type: docs
fetched: 2026-08-14
source_version: dfdd4e9acd0d3eef63b5b5484854fc99251963e270952a5695ed20b77ebe25fd
---

# How to Configure Netskope DLP to Work with Twingate

## Summary
Configures Netskope DLP client to bypass inspection for Twingate Client processes when both are installed on the same device. Creates a certificate pinned application definition and steering exception so Netskope doesn't interfere with Twingate's traffic.

## Key Information
- Both Netskope and Twingate clients can coexist on the same device with proper configuration
- Configuration is done in Netskope console (not Twingate)
- Applies to macOS and Windows platforms
- Exception uses wildcard domain bypass (`*`)

## Prerequisites
- Access to Netskope admin console
- Netskope Steering Configuration (existing or new)
- Twingate Client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application
- Navigate: Netskope Console → **Settings** → **App Definition**
- Create new **certificate pinned application** (suggested name: "Twingate")
- Add entries per platform with **Exact** match type:

| Platform | Process Names |
|----------|--------------|
| macOS | `Twingate, Tunnel Provider macos` |
| Windows | `twingate.exe, twingateupdater.exe` |

> Windows processes: `twingate.exe`, `twingate.service.exe`, `twingateupdater.exe`

### 2. Create Steering Exception
- Navigate: **Settings** → **Steering Configuration** → open/create configuration
- Go to **Exceptions** tab → create new exception
- Exception type: **Certificate Pinned Application**
- Select the Twingate app definition created in Step 1
- Custom app domains: `*`
- Per OS action: **bypass**
- Save the exception

### 3. Apply Configuration to Clients
- Click Netskope client icon → **Configuration** → **Update**
- Restart the Twingate Client

## Configuration Values

| Field | Value |
|-------|-------|
| App type | Certificate Pinned Application |
| macOS definition (match type) | Exact |
| macOS definition | `Twingate, Tunnel Provider macos` |
| Windows definition (match type) | Exact |
| Windows definition | `twingate.exe, twingate.service.exe, twingateupdater.exe` |
| Custom app domains | `*` |
| Exception action | bypass |

## Gotchas
- Must restart Twingate Client after pulling updated Netskope config — updating Netskope config alone is not sufficient
- All three Windows process names must be included; omitting any may cause partial interference
- If no Steering Configuration exists, one must be created before adding exceptions

## Related Docs
- Twingate Client installation guides
- Netskope Steering Configuration documentation (Netskope-side)