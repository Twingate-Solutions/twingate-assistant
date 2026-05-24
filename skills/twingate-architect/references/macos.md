# macOS Twingate Client

## Summary
Twingate client for macOS can be installed via Mac App Store or as a standalone client. Setup requires configuring VPN permissions and a system extension (standalone only). Once authenticated via identity provider, the client runs in the background intercepting only private Resource traffic.

## Key Information
- Native Apple Silicon (M-series) support included
- Two install methods: Mac App Store or standalone client
- Standalone client requires enabling a system extension; App Store version does not
- Client only intercepts traffic to configured private Resources, not general internet traffic
- Notifications are strongly recommended for MFA/step-up auth prompts

## Prerequisites
- Mac App Store install: Apple ID required
- Standalone install: No Apple ID needed
- Network name (found in welcome email)
- Identity provider credentials

## Step-by-Step

1. **Install** via [Mac App Store](https://get.twingate.com) or standalone client
2. **Launch** Twingate — onboarding wizard starts on first run
3. **Grant permissions** when prompted:
   - Allow notifications (strongly recommended)
   - Add VPN configuration (required)
   - Enable system extension — **standalone client only** (required)
4. **Enter network name** (e.g., `yourcompany`) → click **Join Network**
5. **Authenticate** via identity provider in the browser window that opens
6. **Click "Open Twingate.app"** when browser prompts — required to activate the client
7. Client shows **Online** status; runs in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Network name | Yes | Subdomain only (e.g., `autoco`) |
| VPN configuration | Yes | Set in macOS System Settings |
| System extension | Standalone only | Set in macOS System Settings |
| Notifications | Recommended | Required for step-up auth prompts |

## Gotchas
- Must click **"Open Twingate.app"** in browser after authentication or the client won't activate
- System extension prompt only appears for **standalone client**, not App Store version
- Network name field pre-fills on subsequent logins
- Managed/MDM deployments require [additional configuration steps](https://www.twingate.com/docs) beyond standard install

## Related Docs
- [Standalone macOS Client setup](https://www.twingate.com/docs)
- [Managed environment deployment](https://www.twingate.com/docs)
- [get.twingate.com](https://get.twingate.com) — App Store redirect