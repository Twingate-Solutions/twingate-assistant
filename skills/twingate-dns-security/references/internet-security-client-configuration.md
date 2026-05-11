# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM to target machines. Without this, DNS filtering only works when a user is actively signed in.

## Key Information
- Users cannot quit, sign out, or switch Networks when Client is configured for Internet Security
- Machine Keys are shared across devices; one key can deploy to all devices
- Up to 10 keys can be generated simultaneously
- Devices won't appear in Admin Console until first user sign-in, even with Machine Key deployed
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
3. Deploy key file via MDM — rename file to `machinekey.conf` before deployment
4. Deploy KeepAlive configuration via MDM (see below)

## Configuration Values

**Machine Key file paths:**
| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

**macOS KeepAlive Launch Agent:**
- File name: `com.twingate.macos.plist`
- Deploy to: `/Library/LaunchAgents/com.twingate.macos.plist`
- Optional immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`
- Key plist settings: `KeepAlive: true`, `RunAtLoad: true`, Program: `/Applications/Twingate.app/Contents/MacOS/Twingate`

**Windows:** Use Intune Proactive Remediation to detect/restart `Twingate.exe` at `C:\Program Files\Twingate\Twingate.exe`

## Gotchas
- File **must** be named `machinekey.conf` exactly — incorrect filename breaks DNS filtering for signed-out users
- Machine Key alone doesn't prevent the Client from being stopped manually; KeepAlive config is required for full enforcement
- macOS App Store client is **not supported**
- Signed-out devices show differently in DNS filtering logs
- Devices only appear in Admin Console after first user sign-in

## Related Docs
- Internet Security / DNS Filtering documentation
- DNS filtering logs for signed-out devices
- Kandji / Intune MDM configuration guides