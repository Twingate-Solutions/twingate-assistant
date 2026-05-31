# macOS Twingate Client

## Summary
Twingate client for macOS is available via Mac App Store or as a standalone installer. Initial setup requires configuring VPN permissions and a system extension (standalone only). Once authenticated via identity provider, the client runs in the background intercepting only private resource traffic.

## Key Information
- Native Apple Silicon (M-series) support included
- Two install paths: Mac App Store or standalone client
- Standalone client requires enabling a system extension (App Store version does not)
- Client only intercepts traffic for defined private Resources, not general internet traffic
- Notifications should be enabled — used for step-up/re-authentication prompts

## Prerequisites
- Mac App Store install: Apple ID required
- Standalone install: No Apple ID needed
- Network name (found in welcome email)
- Identity provider credentials
- macOS permissions: VPN configuration + notifications (system extension for standalone)

## Step-by-Step

1. **Install** via [Mac App Store](https://get.twingate.com) or [standalone client](https://www.twingate.com/docs/standalone-client)
2. **Launch** Twingate — onboarding wizard starts on first run
3. **Grant permissions** when prompted:
   - Allow notifications
   - Allow VPN configuration
   - Enable system extension *(standalone only)*
4. **Enter network name** (e.g., `autoco`) → click **Join Network**
5. **Authenticate** via identity provider in the browser window that opens
6. **Click "Open Twingate.app"** when browser prompts — required to activate the client
7. Client shows **Online** status; runs in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Network name | Yes | Subdomain from welcome email |
| VPN configuration | Yes | Must approve in macOS System Settings |
| System extension | Standalone only | Must approve in macOS System Settings |
| Notifications | Strongly recommended | Required for MFA/step-up auth prompts |

## Gotchas
- **Must click "Open Twingate.app"** in browser after IdP auth — skipping this leaves the client inactive
- System extension requirement applies **only to standalone client**, not App Store version
- Managed/enterprise deployments require [additional MDM steps](https://www.twingate.com/docs/managed-environments)
- Network name field is pre-filled on subsequent logins

## Related Docs
- [Standalone Client setup](https://www.twingate.com/docs/standalone-client)
- [Managed environment deployment](https://www.twingate.com/docs/managed-environments)
- [get.twingate.com](https://get.twingate.com) — App Store redirect