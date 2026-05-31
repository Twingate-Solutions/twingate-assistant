# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out by deploying Machine Keys via MDM. When configured, users cannot quit, sign out, or switch networks on the Client.

## Key Information
- Machine Keys are shared across devices; one key can deploy to all devices
- Up to 10 Machine Keys can be generated simultaneously
- Devices don't appear in Admin Console until a user signs in at least once
- DNS filtering setup is separate from this configuration
- macOS App Store client does **not** support this configuration

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (e.g., Jamf, Intune) for deployment
- Internet Security tab access in Admin Console

## Step-by-Step

### Generate Machine Key
1. Admin Console → **Internet Security** tab → **Client Configuration** sub-tab
2. Click **Generate Key**

### Deploy Machine Key
Deploy file via MDM to platform-specific path, renamed to `machinekey.conf`:

| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

### Keep Client Running (macOS)
1. Create `/Library/LaunchAgents/com.twingate.macos.plist` with `KeepAlive` Launch Agent
2. Optionally set immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`
3. Restart device or load Launch Agent

### Keep Client Running (Windows)
Deploy Intune proactive remediation with detection/remediation scripts that check and restart `Twingate.exe`.

## Configuration Values

**File name (required):** `machinekey.conf`

**macOS plist:**
- Label: `com.twingate.macos`
- Program: `/Applications/Twingate.app/Contents/MacOS/Twingate`
- KeepAlive: `true`
- RunAtLoad: `true`

**Windows process path:** `C:\Program Files\Twingate\Twingate.exe`

## Gotchas
- File **must** be named `machinekey.conf` exactly — wrong filename breaks DNS filtering for signed-out clients
- Machine Key alone doesn't prevent Client from being killed via Task Manager/Activity Monitor; KeepAlive config is required for true persistence
- DNS filtering is configured separately — this config only ensures it runs when signed out
- Signed-out devices show different DNS filtering log entries than signed-in devices

## Related Docs
- [Internet Security / DNS Filtering documentation](https://www.twingate.com/docs/internet-security)
- [DNS Filtering logs for signed-out devices](https://www.twingate.com/docs/dns-filtering)
- [Intune Proactive Remediation](https://learn.microsoft.com/en-us/mem/intune/fundamentals/remediations)