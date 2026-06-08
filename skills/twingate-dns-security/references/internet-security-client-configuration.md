# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) persistently, even when users are signed out. Requires deploying a Machine Key via MDM to end-user machines. Also restricts users from quitting, signing out, or switching networks on the Client.

## Key Information
- Machine Keys are shared across devices; up to 10 keys can be generated simultaneously
- Machine Key alone doesn't prevent users from killing the process—additional MDM config needed for true persistence
- Devices don't appear in Admin Console until a user signs in for the first time
- macOS App Store client is **not supported**; only macOS standalone app

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (e.g., Jamf, Intune) for deployment
- Internet Security enabled in Admin Console

## Step-by-Step

### 1. Generate Machine Key
Admin Console → **Internet Security** tab → **Client Configuration** sub-tab → **Generate Key**

### 2. Deploy Machine Key via MDM
Rename file to `machinekey.conf` and deploy to:
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

### 3. Configure Client Keep-Alive

**macOS** — Create Launch Agent plist:
- File: `com.twingate.macos.plist`
- Location: `/Library/LaunchAgents/com.twingate.macos.plist`
- Set immutable flag (optional): `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`
- Key settings: `KeepAlive: true`, `RunAtLoad: true`, Program: `/Applications/Twingate.app/Contents/MacOS/Twingate`

**Windows** — Deploy Intune Proactive Remediation:
- Detection: checks if `twingate` process exists (`Get-Process twingate`)
- Remediation: `Start-Process -FilePath "C:\Program Files\Twingate\Twingate.exe"`

## Configuration Values
| Item | Value |
|------|-------|
| macOS plist label | `com.twingate.macos` |
| macOS binary path | `/Applications/Twingate.app/Contents/MacOS/Twingate` |
| Windows binary path | `C:\Program Files\Twingate\Twingate.exe` |
| Machine Key filename | `machinekey.conf` (exact name required) |
| Max concurrent keys | 10 |

## Gotchas
- File **must** be named `machinekey.conf` exactly—wrong filename breaks DNS filtering for signed-out clients
- DNS filtering must be configured separately; this setup does not enable it automatically
- Signed-out devices show differently in DNS filtering logs
- Without keep-alive config, users can kill the Client via Task Manager/Activity Monitor/CLI

## Related Docs
- [DNS Filtering / Internet Security documentation](https://www.twingate.com/docs/internet-security)
- Intune Proactive Remediation (Microsoft docs)