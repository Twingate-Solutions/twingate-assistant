# macOS Twingate Client

## Summary
Twingate client for macOS available via Mac App Store or standalone installer. Requires VPN configuration and system extension (standalone only) to function. Supports Apple Silicon natively.

## Key Information
- Two installation methods: Mac App Store or standalone client
- Native Apple Silicon (M-series) support included
- System extension required only for standalone client (not App Store version)
- Client operates transparently — only intercepts traffic for private Resources, not general internet traffic
- Notifications are strongly recommended for step-up authentication prompts

## Prerequisites
- Apple ID (Mac App Store method only)
- Network name (found in welcome email)
- Identity provider credentials

## Step-by-Step Setup

1. **Install** via Mac App Store (search "Twingate" or visit `get.twingate.com`) or install standalone client
2. **Run** the Twingate application
3. **Complete onboarding wizard** — grant the following permissions:
   - Allow notifications (strongly recommended)
   - Add VPN configuration (**required**)
   - Enable system extension — standalone client only (**required**)
4. **Enter network name** (e.g., `autoco`) → click **Join Network**
5. **Authenticate** via identity provider in the browser window that opens
6. **Click "Open Twingate.app"** when browser prompts — this activates the client
7. Client shows **online** status; runs in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Network name | Yes | Subdomain format (e.g., `autoco`); pre-filled on return |
| VPN configuration | Yes | Configured via macOS System Settings |
| System extension | Standalone only | Configured via macOS System Settings |
| Notifications | Recommended | Required for step-up auth prompts |

## Gotchas
- Must click **"Open Twingate.app"** in browser after IdP authentication or client won't activate
- System extension prompt only appears for standalone client, not App Store version
- Managed/enterprise deployments require additional steps (separate documentation)
- If already authenticated with IdP, browser login step may be skipped automatically

## Related Docs
- [Standalone Client setup](https://www.twingate.com/docs/standalone-client)
- [Managed environment deployment](https://www.twingate.com/docs/macos) (linked as "few additional steps")
- `get.twingate.com` — auto-redirects to Mac App Store