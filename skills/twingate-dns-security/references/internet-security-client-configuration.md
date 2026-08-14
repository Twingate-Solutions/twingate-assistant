---
source: https://www.twingate.com/docs/internet-security-client-configuration
type: docs
fetched: 2026-08-14
source_version: d0632bfb6a7d6e9b1a33fa0bafa67735bf7a17766d0d4acb6fd8fe84a34f38a2
---

# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM. When configured, users cannot quit, sign out, or switch networks on the Client.

## Key Information
- Machine Keys are shared across devices; one key can deploy to all devices
- Up to 10 keys can be generated simultaneously
- Devices don't appear in Admin Console until a user signs in at least once
- DNS filtering setup is **separate** from this configuration
- macOS App Store client is **not supported**; standalone only

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (e.g., Jamf, Intune)
- Internet Security enabled in Admin Console

## Step-by-Step

### Generate Machine Key
1. Admin Console → **Internet Security** tab → **Client Configuration** sub-tab
2. Click **Generate Key**

### Deploy Machine Key
Place file at platform-specific path (must be named `machinekey.conf`):
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

### Configure KeepAlive (macOS)
1. Create plist file at `/Library/LaunchAgents/com.twingate.macos.plist`
2. Optionally set immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`
3. Restart device or load Launch Agent

### Configure KeepAlive (Windows)
Deploy Intune proactive remediation with detection + remediation scripts that check/restart `Twingate.exe` at `C:\Program Files\Twingate\Twingate.exe`

## Configuration Values
- **macOS plist label**: `com.twingate.macos`
- **macOS binary path**: `/Applications/Twingate.app/Contents/MacOS/Twingate`
- **Windows binary path**: `C:\Program Files\Twingate\Twingate.exe`
- **Machine key filename**: `machinekey.conf` (exact name required)

## Gotchas
- File **must** be named `machinekey.conf` exactly — incorrect filename breaks DNS filtering for signed-out clients
- Machine Key alone is insufficient; users can still kill the process via Task Manager/Activity Monitor — deploy KeepAlive config too
- Signed-out devices show differently in DNS filtering logs
- New devices are invisible in Admin Console until first user sign-in, even with Machine Key deployed

## Related Docs
- [DNS Filtering documentation](https://www.twingate.com/docs/dns-filtering)
- [Internet Security documentation](https://www.twingate.com/docs/internet-security)
- [Intune Proactive Remediation](https://learn.microsoft.com/en-us/mem/intune/fundamentals/remediations)