---
source: https://www.twingate.com/docs/internet-security-client-configuration
type: docs
fetched: 2026-10-25
source_version: 8c1aed3c26c1f9b667e78a26b4182ae68a6a0645c70131b6a72aafa0b6c5e51d
trust: official
---

# Internet Security Client Configuration

## Page Title
Internet Security Client Configuration

## Summary
Configures Twingate Clients to run Internet Security features (e.g., DNS filtering) even when users are signed out, via MDM-deployed Machine Keys. Without this configuration, Internet Security only activates when a user is signed in. Also prevents users from quitting, signing out, or switching networks.

## Key Information
- Machine Keys are shared across devices; one key can cover all devices
- Up to 10 Machine Keys can be generated simultaneously
- Supports key rotation via multiple keys
- macOS: **standalone app only** — App Store client does NOT support this
- Devices won't appear in Admin Console until a user signs in at least once
- Signed-out devices have different DNS filtering log format

## Prerequisites
- Internet Security enabled on the Twingate account
- MDM solution (e.g., Jamf, Intune) for deployment
- Machine Key generated from Admin Console → Internet Security → Client Configuration tab

## Step-by-Step

### 1. Generate Machine Key
Admin Console → **Internet Security** tab → **Client Configuration** sub-tab → **Generate Key**

### 2. Deploy Machine Key via MDM
File must be named exactly `machinekey.conf` and placed at:

| Platform | Path |
|----------|------|
| macOS | `/Library/Application Support/Twingate/machinekey.conf` |
| Windows | `%ProgramData%/Twingate/machinekey.conf` |
| Linux | `/etc/twingate/machinekey.conf` |

### 3. Keep Client Running (Recommended)

**macOS** — Deploy Launch Agent via MDM:
- File: `com.twingate.macos.plist`
- Location: `/Library/LaunchAgents/com.twingate.macos.plist`
- Optionally set immutable flag: `sudo chflags schg /Library/LaunchAgents/com.twingate.macos.plist`
- Reload or restart device to activate

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.twingate.macos</string>
  <key>Program</key><string>/Applications/Twingate.app/Contents/MacOS/Twingate</string>
  <key>KeepAlive</key><true/>
  <key>RunAtLoad</key><true/>
</dict>
</plist>
```

**Windows** — Use Intune Proactive Remediation with detection/remediation scripts checking/starting `C:\Program Files\Twingate\Twingate.exe`.

## Configuration Values
| Item | Value |
|------|-------|
| macOS binary path | `/Applications/Twingate.app/Contents/MacOS/Twingate` |
| Windows binary path | `C:\Program Files\Twingate\Twingate.exe` |
| Machine key filename | `machinekey.conf` (exact name required) |
| Max simultaneous keys | 10 |

## Gotchas
- DNS filtering is **configured separately** — this setup alone does not enable DNS filtering
- Machine Key file **must** be named `machinekey.conf` exactly
- Without the KeepAlive configuration, users can manually kill the Client process (Task Manager, Activity Monitor, CLI), disabling Internet Security
- New devices won't appear in Admin Console until first user sign-in, even if Machine Key is deployed

## Related Docs
- [Internet Security documentation](https://www.twingate.com/docs/internet-security)
- [DNS Filtering documentation](https://www.twingate.com/docs/dns-filtering)
- macOS standalone app setup
- Intune Proactive Remediation (Microsoft docs)