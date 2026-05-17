# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (e.g., DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM. When configured, users cannot quit, sign out, or switch networks on the Client.

## Key Information
- Machine Keys are shared across devices; one key can deploy to all devices
- Up to 10 keys can be generated simultaneously
- Supports key rotation via multiple keys
- Devices don't appear in Admin Console until a user signs in at least once
- DNS filtering setup is **separate** from this configuration

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+ (**App Store version not supported**)
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (e.g., Kandji, Intune)
- Internet Security enabled in Admin Console

## Step-by-Step

1. Navigate to Admin Console → **Internet Security** tab → **Client Configuration** sub-tab
2. Click **Generate Key** to create a Machine Key
3. Rename file to `machinekey.conf` (exact name required)
4. Deploy via MDM to platform-specific path
5. Deploy KeepAlive configuration to prevent users from stopping the client

## Configuration Values

### Machine Key File Paths
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

### macOS KeepAlive Launch Agent
- **File name:** `com.twingate.macos.plist`
- **Deploy path:** `/Library/LaunchAgents/com.twingate.macos.plist`
- **Optional immutable flag:** `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`
- Key plist settings: `KeepAlive: true`, `RunAtLoad: true`, Program: `/Applications/Twingate.app/Contents/MacOS/Twingate`

### Windows KeepAlive
- Use **Intune Proactive Remediation**
- Detection: checks for `twingate` process (exit 0 = running, exit 1 = not running)
- Remediation: `Start-Process -FilePath "C:\Program Files\Twingate\Twingate.exe"`

## Gotchas
- File **must** be named `machinekey.conf` exactly — incorrect name breaks DNS filtering for signed-out clients
- Machine Key alone is insufficient; without KeepAlive config, users can still kill the process via Task Manager/Activity Monitor/CLI
- macOS App Store client does **not** support this feature
- DNS filtering must be configured separately
- Signed-out devices show differently in DNS filtering logs

## Related Docs
- [DNS Filtering Documentation](#)
- [Internet Security Documentation](#)
- [Intune Proactive Remediation](#)