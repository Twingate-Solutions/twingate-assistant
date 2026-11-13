---
source: https://www.twingate.com/docs/internet-security-client-configuration
type: docs
fetched: 2026-11-13
source_version: 18ea1a9b5f1b2cb491c7c7276b79eb2f86b5b6e3d32c0d148dc8376aa3767102
trust: official
---

# Internet Security Client Configuration

## Summary
Keeps Twingate Internet Security features (e.g., DNS filtering) running on Clients even when no user is signed in. Done by deploying a Machine Key via MDM and optionally a keep-alive mechanism so the Client restarts if quit. When configured, users cannot quit, sign out, or switch Networks on the Client.

## Key Information
- Without this configuration, Internet Security features run only while a user is signed in.
- macOS: only the standalone app is supported; the App Store Client is not.
- Machine Keys are shared across devices; one key can be deployed to all devices. Each device uses a single key.
- Use multiple keys for rotation or per-group assignment. Up to 10 keys can be generated at once.
- This configuration does not set up DNS filtering. DNS filtering is configured separately under Internet Security.

## Prerequisites
- Internet Security enabled
- Admin Console access
- MDM (e.g., Iru, Intune) for deployment
- macOS standalone Client (if on macOS)

## Step-by-Step
1. In Admin Console, go to **Internet Security > Client Configuration** and click **Generate Key**.
2. Rename the downloaded file to `machinekey.conf`.
3. Deploy it via MDM to the OS-specific path (below).
4. Deploy keep-alive configuration so Twingate restarts if closed.

**macOS keep-alive (Launch Agent):**
1. Create `com.twingate.macos.plist` with keys: `Label` = `com.twingate.macos`, `Program` = `/Applications/Twingate.app/Contents/MacOS/Twingate`, `KeepAlive` = true, `RunAtLoad` = true.
2. Save to `/Library/LaunchAgents/com.twingate.macos.plist`.
3. Optional: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist` (system immutable flag).
4. Restart the device or load the Launch Agent.

**Windows keep-alive (Intune proactive remediation):**
- Detection script: `Get-Process twingate -ErrorAction SilentlyContinue`; exit 0 if running, exit 1 if not.
- Remediation script: `Start-Process -FilePath "C:\Program Files\Twingate\Twingate.exe"`.

## Configuration Values
| OS | Machine Key path |
|---|---|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%\Twingate\machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

- Launch Agent label: `com.twingate.macos`
- Windows executable: `C:\Program Files\Twingate\Twingate.exe`

## Gotchas
- The file must be named exactly `machinekey.conf`; otherwise DNS filtering won't run on signed-out Clients.
- A Machine Key alone doesn't prevent the Client from stopping (e.g., via Task Manager, Activity Monitor, or command line); add the keep-alive config.
- Devices don't appear in the Admin Console until a user signs in for the first time, even though DNS filtering works beforehand.
- Signed-out devices show no device name; their DNS filtering logs differ (see Filtering Analytics).
- Linux has a Machine Key path, but no keep-alive guidance is given on this page.

## Related Docs
- Internet Security documentation (DNS filtering, Secure DNS options)
- Filtering Analytics