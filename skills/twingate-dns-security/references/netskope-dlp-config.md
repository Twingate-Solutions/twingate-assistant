# Netskope DLP Configuration for Twingate Compatibility

## Summary
Configures Netskope DLP to bypass inspection for Twingate Client processes, preventing conflicts when both clients run on the same device. Requires creating a certificate pinned app definition and a steering exception in the Netskope console.

## Key Information
- Both Netskope and Twingate clients can conflict when installed on the same device
- Solution uses Netskope's "Certificate Pinned Application" exception type to bypass Twingate traffic
- Applies to macOS and Windows platforms

## Prerequisites
- Access to Netskope admin console
- Existing or new Netskope Steering Configuration
- Twingate Client installed on end-user devices

## Step-by-Step

### 1. Create Certificate Pinned Application
- Navigate to **Settings → App Definition** in Netskope console
- Create new **Certificate Pinned Application** (recommended name: "Twingate")
- Add entries per platform using **Exact** match type

### 2. Create Steering Exception
- Navigate to **Settings → Steering Configuration**
- Open existing config or create new one
- Under **Exceptions** tab, add new exception:
  - Type: **Certificate Pinned Application**
  - App: Select the Twingate app created in Step 1
  - Custom app domains: `*`
  - Action per OS: **bypass**
- Save the exception

### 3. Apply Configuration
- Click Netskope client icon → **Configuration → Update**
- Restart the Twingate Client

## Configuration Values

| Platform | Match Type | Process Definitions |
|----------|------------|---------------------|
| macOS | Exact | `Twingate, Tunnel Provider macos` |
| Windows | Exact | `twingate.exe, twingate.service.exe, twingateupdater.exe` |

| Exception Field | Value |
|----------------|-------|
| Exception Type | Certificate Pinned Application |
| Custom App Domains | `*` |
| Action | bypass |

## Gotchas
- Must add entries for **all applicable platform types** in the app definition — omitting a platform leaves that OS unprotected from conflicts
- After saving console changes, the Netskope client requires a manual **Update** pull before changes take effect
- Twingate Client must be **restarted** after Netskope configuration is updated
- Windows requires three separate process names; missing any may cause incomplete bypass

## Related Docs
- Netskope App Definition documentation (Netskope console)
- Netskope Steering Configuration documentation (Netskope console)
- Twingate Client installation guides