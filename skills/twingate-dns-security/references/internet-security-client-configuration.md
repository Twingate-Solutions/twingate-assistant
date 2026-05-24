# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM to target machines. Also restricts users from quitting, signing out, or switching networks on the Client.

## Key Information
- Machine Keys are shared across devices; one key can deploy to all devices
- Up to 10 keys can be generated simultaneously
- Devices don't appear in Admin Console until a user signs in at least once
- DNS filtering setup is **separate** from this configuration
- macOS App Store client does **not** support this — standalone only

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (e.g., Jamf, Intune) for deployment
- Internet Security enabled in Admin Console

## Step-by-Step

1. In Admin Console → **Internet Security** → **Client Configuration** tab
2. Click **Generate Key** to create a Machine Key
3. Rename file to `machinekey.conf`
4. Deploy via MDM to platform-specific path
5. Deploy KeepAlive configuration to ensure Client stays running

## Configuration Values

**Machine Key File Paths:**
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

**macOS KeepAlive Launch Agent:**
- File: `com.twingate.macos.plist`
- Location: `/Library/LaunchAgents/com.twingate.macos.plist`
- Key settings: `KeepAlive=true`, `RunAtLoad=true`
- Program path: `/Applications/Twingate.app/Contents/MacOS/Twingate`

**Windows KeepAlive:** Use Intune proactive remediation
- Detection: checks for `twingate` process
- Remediation: launches `C:\Program Files\Twingate\Twingate.exe`

## Gotchas
- File **must** be named `machinekey.conf` exactly — incorrect filename breaks DNS filtering for signed-out clients
- Without KeepAlive config, users can still kill the process via Task Manager/Activity Monitor
- Optionally set immutable flag on macOS plist: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`
- Signed-out devices show differently in DNS filtering logs than signed-in devices

## Related Docs
- Internet Security documentation (DNS filtering setup)
- DNS filtering documentation (signed-out device logs)
- Intune proactive remediation docs