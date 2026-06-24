# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM to each device. Without this, Internet Security only activates when a user is signed in.

## Key Information
- Machine Keys are shared across devices; one key can deploy to all devices
- Up to 10 keys can be generated simultaneously
- Users cannot quit, sign out, or switch networks when Client is configured this way
- Devices don't appear in Admin Console until a user signs in at least once
- DNS filtering setup is separate from this configuration

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+ (App Store version **not supported**)
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (Jamf, Intune, etc.) for deployment

## Step-by-Step

1. Navigate to Admin Console → **Internet Security** → **Client Configuration**
2. Click **Generate Key** to create a Machine Key
3. Rename file to `machinekey.conf`
4. Deploy via MDM to platform-specific path
5. Deploy KeepAlive configuration via MDM (recommended)

## Configuration Values

### Machine Key File Paths
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

### macOS KeepAlive (Launch Agent)
- File: `com.twingate.macos.plist`
- Path: `/Library/LaunchAgents/com.twingate.macos.plist`
- Binary: `/Applications/Twingate.app/Contents/MacOS/Twingate`
- Set immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`

### Windows KeepAlive (Intune Proactive Remediation)
- Detection: checks `Get-Process twingate`; exits 0 if running, 1 if not
- Remediation: `Start-Process -FilePath "C:\Program Files\Twingate\Twingate.exe"`

## Gotchas
- File **must** be named `machinekey.conf` exactly — wrong filename breaks DNS filtering for signed-out clients
- Machine Key alone doesn't prevent Client from being killed (Task Manager, Activity Monitor, CLI) — deploy KeepAlive config too
- macOS App Store client does **not** support this configuration
- DNS filtering requires separate configuration; this setup alone does not enable it
- Signed-out devices have different DNS filtering log format

## Related Docs
- Internet Security documentation
- DNS Filtering documentation
- Intune Proactive Remediation setup