## Internet Security Client Configuration (Always-On)

How to keep Internet Security features (DoH, DNS Filtering) running **even when no user is signed in to Twingate** -- protects shared/multi-user devices and bridges sign-in gaps.

### Why You Need This

By default, DNS filtering and DoH only run when a user is **signed in** to the Twingate Client. Signed-out devices fall back to system DNS -- bypassing all filtering.

With this configuration:
- DNS filtering runs regardless of sign-in state
- Users **cannot quit, sign out of, or switch Networks** on the Client
- Effectively forces Internet Security as a non-optional layer

### Minimum Client Versions

| Platform | Minimum |
|---|---|
| macOS standalone | 2024.17+ |
| Windows | 2024.028+ |
| Linux | 2024.018+ |

**macOS App Store version is NOT supported** -- only the **standalone macOS Client**. Plan accordingly if you distribute via Mac App Store.

### Two-Part Setup

**Part 1: Deploy a Machine Key**

A Machine Key is a shared secret (single key works across all devices, or use multiple for rotation/segmentation).

1. **Generate**: Admin Console -> **Internet Security** -> **Client Configuration** sub-tab -> **Generate Key** (up to 10 keys)
2. **Deploy via MDM** to these paths:

| Platform | Path |
|---|---|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

**Critical: rename the file to exactly `machinekey.conf`** -- the filename is required for the Client to discover it.

**Part 2: Keep the Client Process Alive**

Without this, users can quit Twingate via Task Manager / Activity Monitor -- breaking always-on. Deploy via MDM:

**macOS** -- LaunchAgent at `/Library/LaunchAgents/com.twingate.macos.plist`:
- Set Label = `com.twingate.macos`
- Set Program = `/Applications/Twingate.app/Contents/MacOS/Twingate`
- Set KeepAlive = true
- Set RunAtLoad = true

Optionally lock the file: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`

**Windows** -- Intune Proactive Remediation:

Detection script:
```
$twingate = Get-Process twingate -ErrorAction SilentlyContinue
if ($twingate) { exit 0 } else { exit 1 }
```

Remediation script:
```
Start-Process -FilePath "C:\Program Files\Twingate\Twingate.exe"
```

### FAQ

**Does this setup also enable DNS Filtering?** No -- DNS Filtering is configured separately under /docs/dns-filtering. The Machine Key allows DNS Filtering to keep working when signed out, but you still need to enable Filtering itself.

**Why doesn't my device appear in the Admin Console before sign-in?** Devices appear only after first sign-in. Machine Key enables Filtering pre-sign-in, but device visibility is sign-in-gated.

**Why no device name in signed-out logs?** Signed-out devices use slightly different log fields -- see /docs/dns-filtering for the schema.

### Decision Notes

- Required for any deployment where Internet Security is a compliance/security requirement (vs. optional)
- Machine Keys are **shared secrets** -- treat with appropriate confidentiality; rotate periodically by generating new keys + redeploying via MDM
- Always pair Machine Key + Process-Alive config -- one without the other leaves obvious bypasses

### Gotchas

- macOS App Store Client doesn't support this -- if your fleet uses App Store, switch to the standalone Client
- Filename `machinekey.conf` exactly -- common deployment errors leave the file with the wrong name
- Windows process-alive checking should run on a frequent schedule (e.g., every 15 min) -- otherwise gaps appear

### Related Docs

- /docs/internet-security -- IS overview
- /docs/dns-filtering -- DNS Filtering policies
- /docs/dns-security -- DoH configuration
- /docs/managed-devices, /docs/jamf-mdm, /docs/intune-configuration -- MDM deployment
- /docs/macos-standalone-client -- macOS standalone Client (required)
