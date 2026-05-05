# macOS Twingate Client

## Summary
Twingate macOS client can be installed via Mac App Store or as a standalone client. First-time setup requires configuring VPN permissions and a system extension (standalone only). After setup, the client authenticates via your organization's identity provider.

## Key Information
- Native Apple Silicon (ARM) support included
- Two installation paths: Mac App Store or standalone client
- Standalone client requires enabling a system extension in addition to VPN configuration
- Client only intercepts traffic for private Resources; regular internet unaffected
- Notifications required for step-up authentication prompts on sensitive Resources

## Prerequisites
- Apple ID (Mac App Store path only)
- Network name (provided in welcome email)
- Identity provider credentials
- macOS permissions: Notifications, VPN configuration, System Extension (standalone only)

## Step-by-Step

### Installation
1. **Mac App Store**: Search "Twingate" or visit `get.twingate.com`
2. **Standalone**: Follow standalone client setup docs (no Apple ID required)

### First-Time Setup
1. Launch Twingate — onboarding wizard starts automatically
2. Allow notifications (strongly recommended for auth prompts)
3. Allow VPN configuration — **required**
4. Enable system extension (standalone client only) — **required**

### Connecting
1. Enter network name (e.g., `acme`) from welcome email
2. Click **Join Network**
3. Use the drop-down menu → **Connect**
4. Authenticate in the browser window that opens with your IdP credentials
5. Click **Open Twingate.app** when browser prompts — required to activate client
6. Client shows "online" status when complete

## Configuration Values
| Setting | Required | Notes |
|---------|----------|-------|
| VPN Configuration | Yes | Both install methods |
| System Extension | Yes (standalone only) | Mac App Store version does not require this |
| Notifications | Strongly recommended | Needed for MFA/step-up auth prompts |

## Gotchas
- Must click **"Open Twingate.app"** browser prompt after IdP auth — skipping this leaves the client inactive
- System extension setup only required for **standalone** client, not Mac App Store version
- Managed/MDM deployments require additional steps (separate docs)
- Returning users will have network name pre-filled

## Related Docs
- Standalone Client setup
- Managed environment deployment
- `get.twingate.com` (redirect to Mac App Store)