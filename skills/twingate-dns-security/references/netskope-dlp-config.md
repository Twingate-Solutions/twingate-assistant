# Netskope DLP Configuration for Twingate Compatibility

## Summary
Configures Netskope DLP to bypass its SSL inspection for Twingate Client processes, preventing conflicts when both clients run on the same device. Requires creating a certificate-pinned app definition and a steering exception in the Netskope console.

## Key Information
- Both Netskope and Twingate clients use certificate pinning, causing conflicts without this configuration
- Exception bypasses Netskope steering for all Twingate processes across platforms
- Changes require manual config pull via Netskope client UI

## Prerequisites
- Admin access to Netskope console
- Twingate Client installed on target devices
- Netskope Client installed on target devices
- Existing or new Netskope Steering Configuration

## Step-by-Step

### 1. Create Certificate Pinned App Definition
1. Netskope Console → **Settings** → **App Definition**
2. Create new **Certificate Pinned Application** (suggested name: "Twingate")
3. Add platform entries with **Exact** match type:

| Platform | Definition |
|----------|-----------|
| macOS | `Twingate, Tunnel Provider macos` |
| Windows | `twingate.exe, twingateupdater.exe, twingate.service.exe` |

### 2. Create Steering Exception
1. **Settings** → **Steering Configuration** → open or create a configuration
2. Under **Exceptions** tab → create new exception
3. Exception type: **Certificate Pinned Application**
4. Select the Twingate app created in Step 1
5. Custom app domains: `*`
6. Action for each OS: **bypass**
7. Save the exception

### 3. Apply Configuration to Clients
1. Click Netskope client icon → **Configuration** → **Update**
2. Restart the Twingate Client

## Configuration Values

| Field | Value |
|-------|-------|
| App type | Certificate Pinned Application |
| macOS processes | `Twingate, Tunnel Provider macos` |
| Windows processes | `twingate.exe, twingateupdater.exe, twingate.service.exe` |
| Match type | Exact |
| Custom app domains | `*` |
| Exception action | bypass |

## Gotchas
- Must restart Twingate Client after pulling updated Netskope config — clicking "Update" in Netskope alone is insufficient
- All three Windows process names must be included; omitting any may cause partial conflicts
- The `*` wildcard in custom app domains is required to cover all Twingate traffic

## Related Docs
- Twingate Client installation guides
- Netskope Steering Configuration documentation