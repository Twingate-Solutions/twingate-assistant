# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM and optionally configuring auto-restart. When configured, users cannot quit, sign out, or switch Networks on the Client.

## Key Information
- Machine Keys are shared across devices; one key can deploy to all devices
- Up to 10 keys can be generated simultaneously
- Devices don't appear in Admin Console until a user signs in at least once
- DNS filtering is configured separately from this feature
- macOS App Store client does NOT support this configuration

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
3. Rename downloaded file to `machinekey.conf`
4. Deploy via MDM to platform-specific path
5. (Recommended) Deploy KeepAlive configuration via MDM

## Configuration Values

**Machine Key file paths:**
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

**macOS KeepAlive Launch Agent:**
- File: `com.twingate.macos.plist`
- Location: `/Library/LaunchAgents/com.twingate.macos.plist`
- Key fields: `KeepAlive: true`, `RunAtLoad: true`
- Program path: `/Applications/Twingate.app/Contents/MacOS/Twingate`
- Optional immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`

**Windows KeepAlive:** Use Intune Proactive Remediation
- Detection: checks `Get-Process twingate`
- Remediation: `Start-Process -FilePath "C:\Program Files\Twingate\Twingate.exe"`

## Gotchas
- File **must** be named exactly `machinekey.conf` — incorrect filename breaks DNS filtering for signed-out clients
- Without KeepAlive config, users can manually terminate the Client via Task Manager/Activity Monitor/CLI
- DNS filtering must be configured separately; this config only ensures the Client runs persistently
- Signed-out devices won't appear in Admin Console (no device name in DNS logs)

## Related Docs
- [DNS Filtering documentation](https://www.twingate.com/docs/internet-security)
- Internet Security overview