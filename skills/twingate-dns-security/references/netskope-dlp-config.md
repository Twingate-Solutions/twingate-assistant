# Netskope DLP Configuration for Twingate Compatibility

## Summary
Configures Netskope DLP to bypass inspection for Twingate Client processes when both applications are installed on the same device. Creates a certificate pinned application exception so Netskope does not interfere with Twingate's traffic tunneling.

## Key Information
- Both Netskope and Twingate clients can coexist on the same device with proper configuration
- Solution uses Netskope's "Certificate Pinned Application" exception type
- Applies to macOS and Windows platforms
- Configuration must be pushed to the Netskope client after changes

## Prerequisites
- Access to Netskope admin console with Settings permissions
- Existing or new Steering Configuration in Netskope
- Twingate Client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application
- Navigate to **Settings → App Definition** in Netskope console
- Create new **certificate pinned application** (recommended name: "Twingate")
- Add entries per platform using **Exact** match type

### 2. Create Steering Exception
- Navigate to **Settings → Steering Configuration**
- Open existing or create new configuration
- Under **Exceptions** tab, add new exception:
  - Type: **Certificate Pinned Application**
  - App: Select "Twingate" (created above)
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
| Windows | Exact | `twingate.exe, twingateupdater.exe, twingate.service.exe` |

**Exception settings:**
- Exception Type: `Certificate Pinned Application`
- Custom App Domains: `*`
- Action: `bypass`

## Gotchas
- Must restart the Twingate Client after pushing updated Netskope configuration — Update alone is insufficient
- All Twingate process names must be included for Windows; missing any may cause partial interference
- The domain wildcard `*` is required in the custom app domains field for the bypass to apply broadly

## Related Docs
- Netskope Steering Configuration documentation (Netskope console)
- Twingate Client installation guides