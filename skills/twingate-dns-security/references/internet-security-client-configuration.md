# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM and optionally configuring auto-restart to ensure continuous operation.

## Key Information
- Without this config, DNS filtering only works when a user is signed in
- When configured, users cannot quit, sign out, or switch Networks in the Client
- Machine Keys are shared across devices; up to 10 keys can be active simultaneously
- Devices don't appear in Admin Console until a user signs in at least once
- macOS App Store client does **not** support this configuration

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (e.g., Jamf, Intune)
- Internet Security enabled in Admin Console

## Step-by-Step

1. Navigate to Admin Console → **Internet Security** → **Client Configuration**
2. Click **Generate Key** to create a Machine Key
3. Rename the file to `machinekey.conf`
4. Deploy via MDM to platform-specific path
5. (Recommended) Deploy KeepAlive/auto-restart configuration via MDM

## Configuration Values

**Machine Key file paths:**
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

**macOS KeepAlive Launch Agent:**
- File: `com.twingate.macos.plist`
- Deploy to: `/Library/LaunchAgents/com.twingate.macos.plist`
- Key settings: `KeepAlive=true`, `RunAtLoad=true`
- Program path: `/Applications/Twingate.app/Contents/MacOS/Twingate`
- Optional immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`

**Windows:** Use Intune Proactive Remediation
- Detection: checks if `twingate` process exists
- Remediation: starts `C:\Program Files\Twingate\Twingate.exe`

## Gotchas
- File **must** be named `machinekey.conf` exactly — incorrect filename breaks DNS filtering for signed-out clients
- Machine Key alone doesn't prevent users from manually killing the process (Task Manager, Activity Monitor, CLI) — deploy KeepAlive config too
- DNS filtering setup is **separate** from this configuration; this does not enable DNS filtering by itself
- Signed-out devices show differently in DNS filtering logs than signed-in devices

## Related Docs
- Internet Security documentation
- DNS Filtering documentation
- Intune Proactive Remediation (Microsoft docs)