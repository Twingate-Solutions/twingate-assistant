# macOS Twingate Client

## Summary
Installs and configures the Twingate client on macOS via Mac App Store or standalone installer. Requires VPN configuration and system extension setup to function. Client runs in background and only intercepts traffic for private Resources.

## Key Information
- Native Apple Silicon (M-series) support included
- Two installation methods: Mac App Store or standalone client
- Standalone client requires system extension enablement (App Store version does not)
- Client only intercepts traffic for configured private Resources, not general internet traffic
- Notifications required for MFA/re-authentication prompts on sensitive Resources

## Prerequisites
- Apple ID (Mac App Store method only)
- Network name (found in Twingate welcome email)
- Identity Provider credentials
- macOS permissions for: notifications, VPN configuration, system extension (standalone only)

## Step-by-Step

1. **Install** via [Mac App Store](https://get.twingate.com) or standalone client
2. **Launch** Twingate — onboarding wizard starts on first run
3. **Grant permissions** in macOS System Settings:
   - Allow notifications
   - Allow VPN configuration *(required)*
   - Enable system extension *(required for standalone only)*
4. **Enter network name** (e.g., `acme`) → click **Join Network**
5. **Authenticate** via browser with Identity Provider credentials
6. **Click "Open Twingate.app"** when browser prompts — activates the client
7. Client shows **Online** status; runs in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Network name | Yes | Subdomain prefix, found in welcome email |
| VPN configuration | Yes | Set in macOS System Settings |
| System extension | Yes (standalone only) | Set in macOS System Settings |
| Notifications | Strongly recommended | Needed for auth prompts |

## Gotchas
- Must click **"Open Twingate.app"** in browser after IdP auth or client won't activate
- System extension permission only required for standalone client, not App Store version
- Managed/MDM deployments need [additional configuration steps](https://www.twingate.com/docs) beyond standard install
- If returning user, network name field is pre-filled

## Related Docs
- [Standalone macOS Client setup](https://www.twingate.com/docs)
- [Managed environment deployment](https://www.twingate.com/docs)
- [get.twingate.com](https://get.twingate.com) — App Store redirect