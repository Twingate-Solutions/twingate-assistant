# macOS Twingate Client

## Summary
Installs and configures the Twingate client on macOS via Mac App Store or standalone installer. Requires VPN configuration and system extension setup to function. After setup, client runs in background intercepting only private Resource traffic.

## Key Information
- Native Apple Silicon (ARM) support included
- Two install methods: Mac App Store or standalone client
- Standalone client requires enabling a system extension (App Store version does not)
- Notifications strongly recommended for re-authentication prompts on sensitive Resources
- Client does not affect regular internet traffic — only routes private Resources

## Prerequisites
- Apple ID (for Mac App Store install) or standalone client package
- macOS permissions granted for:
  - Notifications
  - VPN configuration
  - System extension (standalone only)
- Network name (found in welcome email)
- Valid Identity Provider credentials

## Step-by-Step

1. **Install** — Mac App Store: search "Twingate" or visit `get.twingate.com`. Standalone: follow [standalone client docs]
2. **Launch** — Run the Twingate application
3. **Onboarding wizard** — Grant required permissions:
   - Allow notifications (strongly recommended)
   - Add VPN configuration (required)
   - Enable system extension if using standalone (required)
4. **Join network** — Enter network name (e.g., `autoco`); click **Join Network**
5. **Authenticate** — Browser opens to Identity Provider login; use existing credentials
6. **Activate** — Click **Open Twingate.app** when browser prompts after auth completes
7. Client shows **online** status — runs in background

## Configuration Values
| Setting | Requirement | Notes |
|---|---|---|
| Network name | Required | Found in welcome email; pre-filled on return |
| VPN configuration | Required | Configured via macOS system settings |
| System extension | Required (standalone only) | Enabled via macOS system settings |
| Notifications | Strongly recommended | Used for re-auth prompts |

## Gotchas
- Must click **Open Twingate.app** in browser after IdP auth or client won't activate
- System extension requirement applies **only** to standalone client, not App Store version
- Managed/enterprise deployments require additional steps beyond standard App Store install
- If already authenticated with IdP, login step is typically skipped automatically

## Related Docs
- [Standalone macOS Client setup](#)
- [Managed environment deployment](#)
- [get.twingate.com](https://get.twingate.com)