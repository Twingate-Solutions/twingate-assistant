# Twingate macOS Client

## Summary
Twingate macOS client can be installed via Mac App Store or as a standalone client. Setup requires configuring VPN permissions and a system extension (standalone only). Once authenticated via identity provider, the client runs in the background intercepting only private Resource traffic.

## Key Information
- Native Apple Silicon (ARM) support included
- Two installation methods: Mac App Store or standalone client
- Standalone client requires enabling a system extension (App Store version does not)
- Client only intercepts traffic for defined private Resources, not general internet traffic
- Notifications required for step-up authentication prompts on sensitive Resources

## Prerequisites
- Apple ID (Mac App Store install only)
- Network name (found in welcome email)
- Identity provider credentials
- macOS permissions: Notifications, VPN configuration, System Extension (standalone only)

## Step-by-Step

1. **Install** via Mac App Store (search "Twingate" or visit `get.twingate.com`) or install the standalone client
2. **Launch** Twingate application
3. **Complete onboarding wizard**:
   - Allow notifications (strongly recommended)
   - Add VPN configuration (required)
   - Enable system extension — standalone client only (required)
4. **Enter network name** (e.g., `autoco`) and click **Join Network**
5. **Authenticate** via identity provider in the browser window that opens
6. **Click "Open Twingate.app"** when prompted by browser to activate the client
7. Client shows "online" — leave connected in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Notifications | Strongly recommended | Used for re-authentication prompts |
| VPN Configuration | Required | All install types |
| System Extension | Required | Standalone client only |

## Gotchas
- After browser-based IdP authentication completes, you **must click "Open Twingate.app"** in the browser prompt — skipping this step leaves the client inactive
- System extension requirement applies **only** to standalone client, not App Store version
- Managed/enterprise deployments require additional steps (separate documentation)
- Network name field is pre-filled for returning users

## Related Docs
- [Standalone macOS Client setup](https://www.twingate.com/docs/standalone-client)
- [Managed environment deployment](https://www.twingate.com/docs/macos-managed)
- `get.twingate.com` — redirects to Mac App Store