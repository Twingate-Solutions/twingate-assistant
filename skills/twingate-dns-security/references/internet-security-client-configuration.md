# Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (DNS filtering) even when users are signed out. Requires deploying a Machine Key via MDM and optionally configuring process keep-alive to prevent users from stopping the client.

## Key Information
- Without this config, DNS filtering only works when users are signed in
- When configured, users **cannot** quit, sign out, or switch Networks on the Client
- Machine Keys are shared across devices; one key can deploy to all machines
- Up to 10 keys can be generated simultaneously (useful for rotation)
- Devices don't appear in Admin Console until a user signs in at least once
- DNS filtering setup is **separate** — this config only enables the always-on behavior

## Prerequisites
- Minimum Client versions:
  - macOS standalone: 2024.17+ (**App Store version NOT supported**)
  - Windows: 2024.028+
  - Linux: 2024.018+
- MDM solution (e.g., Jamf, Intune) for deployment
- Internet Security enabled in Admin Console

## Step-by-Step

1. Navigate to Admin Console → **Internet Security** → **Client Configuration**
2. Click **Generate Key** to create a Machine Key
3. Rename the file to exactly `machinekey.conf`
4. Deploy via MDM to the correct path per OS
5. (Recommended) Deploy keep-alive configuration via MDM

## Configuration Values

**Machine Key file paths:**
| OS | Path |
|----|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

**macOS Keep-Alive (LaunchAgent):**
- File: `com.twingate.macos.plist`
- Path: `/Library/LaunchAgents/com.twingate.macos.plist`
- Binary: `/Applications/Twingate.app/Contents/MacOS/Twingate`
- Optional immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`

**Windows Keep-Alive:**
- Use Intune Proactive Remediation
- Detection: checks if `twingate` process exists
- Remediation: `Start-Process -FilePath "C:\Program Files\Twingate\Twingate.exe"`

## Gotchas
- File **must** be named `machinekey.conf` — incorrect filename breaks DNS filtering for signed-out users
- macOS App Store client does **not** support this configuration
- Without keep-alive config, users can still kill the process via Task Manager/Activity Monitor/CLI
- DNS filtering and Client Configuration are configured independently
- Signed-out devices show differently in DNS filtering logs

## Related Docs
- [DNS Filtering documentation](https://www.twingate.com/docs/dns-filtering)
- [Internet Security documentation](https://www.twingate.com/docs/internet-security)