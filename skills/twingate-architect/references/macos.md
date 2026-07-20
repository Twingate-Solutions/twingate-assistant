# macOS Twingate Client

## Page Title
macOS Client Installation and Setup

## Summary
Covers installing the Twingate client on macOS via the Mac App Store or standalone installer, and completing initial setup including VPN configuration and system extension enablement. The client runs in the background and only intercepts traffic destined for private Resources.

## Key Information
- Two install methods: Mac App Store or standalone client
- Native Apple Silicon (M-series) support included
- Standalone client requires enabling a system extension; App Store version does not
- Notifications must be enabled to receive MFA/re-authentication prompts for sensitive Resources
- Client does not affect general internet traffic — only routes private Resource traffic

## Prerequisites
- Apple ID (Mac App Store method only)
- Network name (found in welcome email)
- Identity Provider credentials

## Step-by-Step

1. **Install** — Search "Twingate" in Mac App Store, visit `get.twingate.com`, or install standalone client
2. **Run the app** — Onboarding wizard launches on first run
3. **Allow notifications** — Required for auth prompts on sensitive Resources
4. **Add VPN configuration** — Required; wizard directs to macOS system settings
5. **Enable system extension** — Required for standalone client only; wizard directs to macOS system settings
6. **Enter network name** — e.g., `acme` (subdomain portion of your Twingate network)
7. **Click "Join Network"**
8. **Authenticate via IdP** — Browser window opens; complete login with existing credentials
9. **Click "Open Twingate.app"** when browser prompts — activates the client
10. **Client shows Online** — Setup complete; runs in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Network name | Yes | Subdomain, found in welcome email |
| VPN configuration | Yes | Set via macOS system settings |
| System extension | Standalone only | Set via macOS system settings |
| Notifications | Strongly encouraged | Needed for re-auth prompts |

## Gotchas
- After IdP authentication in browser, you **must** click "Open Twingate.app" — skipping this leaves the client inactive
- System extension prompt only appears for the **standalone client**, not the App Store version
- Managed environment deployments require additional steps (linked separately)
- If returning user, network name field is pre-filled

## Related Docs
- [Standalone macOS Client](https://www.twingate.com/docs/standalone-client)
- [Managed environment deployment](https://www.twingate.com/docs/macos) (additional steps referenced in page)
- `get.twingate.com` — redirects to Mac App Store listing