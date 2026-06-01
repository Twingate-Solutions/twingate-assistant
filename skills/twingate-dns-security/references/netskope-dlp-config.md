# Netskope DLP Configuration for Twingate Compatibility

## Summary
Configures Netskope DLP client to bypass SSL inspection for Twingate Client processes when both are installed on the same device. Requires creating a certificate-pinned app definition in Netskope and adding a steering exception, then pushing the config update to clients.

## Key Information
- Both Netskope and Twingate clients must coexist on the same device
- Netskope intercepts traffic by default; Twingate processes need explicit bypass
- Configuration applies per-platform (macOS and Windows handled separately)
- Changes must be actively pulled to Netskope client after saving

## Prerequisites
- Admin access to Netskope console
- Existing or new Steering Configuration in Netskope
- Netskope client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application
- Navigate: Netskope console → **Settings** → **App Definition**
- Create new **Certificate Pinned Application** (suggested name: "Twingate")
- Add platform entries:

| Platform | Match Type | Definition |
|----------|-----------|------------|
| macOS | Exact | `Twingate, Tunnel Provider macos` |
| Windows | Exact | `twingate.exe, twingate.service.exe, twingateupdater.exe` |

### 2. Create Steering Exception
- Navigate: **Settings** → **Steering Configuration** → open or create config
- Go to **Exceptions** tab → create new exception
- Exception type: **Certificate Pinned Application**
- Select the Twingate app definition created above
- Custom app domains: `*`
- Action for each OS: **bypass**
- Save the exception

### 3. Apply Configuration to Clients
- Click Netskope client icon → **Configuration** → **Update**
- Restart the Twingate Client after Netskope config updates

## Configuration Values

| Field | Value |
|-------|-------|
| macOS process names | `Twingate, Tunnel Provider macos` |
| Windows process names | `twingate.exe, twingate.service.exe, twingateupdater.exe` |
| Custom app domains | `*` |
| Exception action | `bypass` |

## Gotchas
- Must explicitly add entries for **each** applicable platform; missing a platform leaves that OS unprotected from conflicts
- Config changes in Netskope console are **not automatic** — must manually trigger **Update** on each client
- Twingate Client must be **restarted** after Netskope pulls the new config
- Match type must be **Exact** (not partial/regex) for process name definitions

## Related Docs
- Twingate Client installation guides (macOS, Windows)
- Netskope Steering Configuration documentation
- Other Twingate third-party compatibility guides (antivirus, VPN coexistence)