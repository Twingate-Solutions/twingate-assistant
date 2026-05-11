# macOS Twingate Client

## Summary
Installs and configures the Twingate client on macOS via Mac App Store or standalone installer. Requires VPN configuration and system extension setup to function. Operates in background without affecting regular internet traffic.

## Key Information
- Native Apple Silicon (M-series) support included
- Two install paths: Mac App Store (requires Apple ID) or standalone client
- Standalone client requires enabling a system extension (App Store version does not)
- Client only intercepts traffic for defined private Resources, not general browsing
- Notifications required for step-up authentication prompts on sensitive Resources

## Prerequisites
- Apple ID (Mac App Store path only)
- Network name (found in welcome email)
- Identity Provider credentials

## Installation Options

### Mac App Store
- Search "Twingate" in App Store, or visit `get.twingate.com`
- For managed/MDM environments: follow [additional steps](https://www.twingate.com/docs) for enterprise deployment

### Standalone Client
- Use when no Apple ID is available
- Requires additional system extension approval during setup

## Step-by-Step Setup

1. **Launch Twingate** — onboarding wizard starts on first run
2. **Allow notifications** — navigate to macOS notification settings when prompted
3. **Add VPN configuration** — approve in macOS VPN/Network settings *(required)*
4. **Enable system extension** — standalone client only, approve in macOS Security settings *(required)*
5. **Enter network name** — e.g., `autoco` (subdomain of your Twingate network)
6. **Click "Join Network"**
7. **Authenticate via IdP** — browser window opens; use existing SSO credentials
8. **Click "Open Twingate.app"** when browser prompts — activates the client
9. Client shows **Online** status; runs in background

## Configuration Values
| Setting | Location | Required |
|---|---|---|
| VPN Configuration | macOS Network/VPN Settings | Yes |
| System Extension | macOS Security & Privacy | Yes (standalone only) |
| Notifications | macOS Notification Settings | Strongly recommended |

## Gotchas
- Must click **"Open Twingate.app"** in browser after IdP auth — skipping this leaves client inactive
- System extension approval only required for standalone client, not App Store version
- If already authenticated with IdP, browser login step is typically skipped automatically
- Notifications cannot be omitted without losing step-up MFA prompts for sensitive resources

## Related Docs
- [Standalone macOS Client](https://www.twingate.com/docs)
- [Managed/Enterprise macOS Deployment](https://www.twingate.com/docs)
- [Mac App Store — get.twingate.com](https://get.twingate.com)