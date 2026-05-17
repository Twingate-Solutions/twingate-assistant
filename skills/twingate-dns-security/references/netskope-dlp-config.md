# Netskope DLP Configuration for Twingate Compatibility

## Summary
Configures Netskope DLP to bypass inspection for Twingate Client processes when both clients are installed on the same device. Requires creating a certificate pinned app definition in Netskope, then adding a steering exception for Twingate processes.

## Key Information
- Both Netskope and Twingate clients can coexist on the same device with proper configuration
- Configuration is done entirely in the Netskope console + client update
- Applies to macOS and Windows platforms

## Prerequisites
- Access to Netskope admin console
- Netskope Steering Configuration exists (or ability to create one)
- Twingate Client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application in Netskope
- Navigate to **Settings → App Definition**
- Create new **Certificate Pinned Application** (recommended name: "Twingate")
- Add platform entries using **Exact** match type:

| Platform | Process Names |
|----------|--------------|
| macOS | `Twingate, Tunnel Provider macos` |
| Windows | `twingate.exe, twingateupdater.exe, twingate.service.exe` |

### 2. Create Steering Exception
- Navigate to **Settings → Steering Configuration**
- Open existing config or create new one
- Under **Exceptions** tab, add new exception:
  - Exception type: **Certificate Pinned Application**
  - Application: Select the Twingate app created in Step 1
  - Custom app domains: `*`
  - Action per OS: **bypass**
- Save the exception

### 3. Apply Configuration to Client
- Click Netskope client icon → **Configuration → Update**
- Restart the Twingate Client

## Configuration Values

| Field | Value |
|-------|-------|
| Exception Type | Certificate Pinned Application |
| Custom App Domains | `*` |
| Action | bypass |
| macOS processes | `Twingate, Tunnel Provider macos` |
| Windows processes | `twingate.exe, twingateupdater.exe, twingate.service.exe` |

## Gotchas
- Must use **Exact** match type (not partial/regex) for process name definitions
- Configuration update must be explicitly pulled via the Netskope client UI — it does not auto-apply
- Twingate Client must be **restarted** after Netskope config update for changes to take effect
- Wildcard (`*`) is required in the custom app domains field

## Related Docs
- Twingate Client installation documentation
- Netskope Steering Configuration documentation (Netskope-side)