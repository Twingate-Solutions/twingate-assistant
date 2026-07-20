# Netskope DLP Configuration for Twingate Compatibility

## Summary
Configures Netskope DLP to bypass inspection for Twingate Client processes, preventing conflicts when both clients run on the same device. Requires creating a certificate pinned app definition in Netskope and adding a steering exception for Twingate.

## Key Information
- Both Netskope and Twingate clients can coexist on the same device with proper configuration
- Solution uses Netskope's "Certificate Pinned Application" exception type
- Applies to macOS and Windows platforms
- Configuration must be pushed to the Netskope client after changes

## Prerequisites
- Admin access to Netskope console
- Existing Netskope Steering Configuration (or create new)
- Twingate Client installed on target devices

## Step-by-Step

### 1. Create Certificate Pinned Application
1. Netskope Console → **Settings** → **App Definition**
2. Create new **Certificate Pinned Application** (suggested name: "Twingate")
3. Add entries per platform using **Exact** match type

### 2. Create Steering Exception
1. Go to **Settings** → **Steering Configuration**
2. Open existing config or create new
3. Under **Exceptions** tab → create new exception
4. Exception type: **Certificate Pinned Application**
5. Select the Twingate app created in Step 1
6. Custom app domains: `*`
7. Per OS action: set to **bypass**
8. Save the exception

### 3. Apply Configuration
1. Click Netskope client icon → **Configuration** → **Update**
2. Restart the Twingate Client

## Configuration Values

### macOS Process Names (Exact match)
```
Twingate, Tunnel Provider macos
```

### Windows Process Names (Exact match)
```
twingate.exe, twingate.service.exe, twingateupdater.exe
```

### Exception Settings
| Field | Value |
|---|---|
| Exception Type | Certificate Pinned Application |
| Custom App Domains | `*` |
| OS Action | bypass |

## Gotchas
- Must add entries for **all applicable platform types** — incomplete platform coverage will leave conflicts on unconfigured OSes
- After saving Netskope config changes, you must manually trigger **Update** in the Netskope client; changes are not automatic
- Twingate Client must be **restarted** after the Netskope config update is applied
- Only macOS and Windows process names are documented; other platforms not covered

## Related Docs
- Twingate Client installation guides
- Netskope Steering Configuration documentation (Netskope-side)