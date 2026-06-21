# macOS Twingate Client

## Summary
Twingate macOS client can be installed via Mac App Store or as a standalone client. Setup requires configuring VPN permissions and (for standalone) a system extension. Once authenticated via identity provider, the client runs in background intercepting only private Resource traffic.

## Key Information
- Native Apple Silicon (M-series) support included
- Two installation methods: Mac App Store or standalone client
- VPN configuration is **required** for operation
- System extension required for **standalone client only** (not App Store version)
- Notifications strongly recommended for step-up authentication prompts
- Client only intercepts traffic to private Resources, not general internet traffic

## Prerequisites
- Apple ID (Mac App Store method only)
- Network name (found in welcome email)
- Identity provider credentials
- macOS permissions: VPN configuration, notifications, system extension (standalone)

## Step-by-Step

1. **Install** via Mac App Store (search "Twingate" or visit `get.twingate.com`) or install standalone client
2. **Launch** Twingate app — onboarding wizard starts on first run
3. **Grant permissions** when prompted:
   - Allow notifications (strongly recommended)
   - Add VPN configuration (**required**)
   - Enable system extension (**required** for standalone only)
4. **Enter network name** (e.g., `autoco`) → click **Join Network**
5. **Authenticate** via identity provider in the browser window that opens
6. **Click "Open Twingate.app"** when browser prompts — this activates the client
7. Client shows **online** status; runs in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Network name | Yes | Found in welcome email; pre-filled on return visits |
| VPN configuration | Yes | Set in macOS System Settings |
| System extension | Standalone only | Set in macOS System Settings |
| Notifications | Recommended | Required for re-authentication prompts |

## Gotchas
- Must click **"Open Twingate.app"** in browser after IdP auth — skipping this leaves client inactive
- System extension prompt only appears for standalone client, not App Store version
- Managed/enterprise deployments require additional steps beyond standard App Store install
- If already authenticated with IdP, browser login step may be skipped automatically

## Related Docs
- Standalone Client setup
- Managed environment deployment (enterprise/MDM)
- Mac App Store managed install guide