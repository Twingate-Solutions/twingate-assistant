---
source: https://www.twingate.com/docs/macos
type: docs
fetched: 2026-08-14
source_version: d03660b2b39d4e882707e05e70243f3ee0631699f0f71eef3fdd91925057467c
---

# macOS Twingate Client

## Page Title
macOS Client Installation and Setup

## Summary
Covers installing the Twingate client on macOS via Mac App Store or standalone installer, and configuring required system permissions. The client supports both Intel and Apple Silicon Macs.

## Key Information
- Two installation methods: Mac App Store (requires Apple ID) or standalone client
- Native Apple Silicon (ARM) support included
- Standalone client requires an additional system extension approval step
- Client only intercepts traffic for configured private Resources; regular browsing is unaffected

## Prerequisites
- Apple ID (Mac App Store method only)
- Network name (found in welcome email)
- Identity Provider credentials
- macOS permissions: VPN configuration, notifications (strongly recommended), system extension (standalone only)

## Step-by-Step

1. **Install** via Mac App Store (search "Twingate" or visit `get.twingate.com`) or use the standalone client
2. **Run** the Twingate application
3. **Grant permissions** via onboarding wizard:
   - Allow notifications (required for MFA/sensitive resource prompts)
   - Add VPN configuration (**required**)
   - Enable system extension — standalone client only (**required**)
4. **Enter network name** (e.g., `acme`) → click **Join Network**
5. **Authenticate** via Identity Provider in browser window that opens
6. **Click "Open Twingate.app"** when browser prompts — required to activate client
7. Client shows **Online** status; runs in background

## Configuration Values
| Setting | Required | Notes |
|---|---|---|
| Network name | Yes | Subdomain portion of your Twingate URL |
| VPN configuration | Yes | Configured via macOS System Settings |
| System extension | Standalone only | Approved via macOS System Settings |
| Notifications | Strongly recommended | Needed for step-up auth prompts |

## Gotchas
- Must click **"Open Twingate.app"** in the browser after IdP auth or the client will not activate
- Standalone client has an extra system extension step not required for App Store version
- Managed/MDM deployments require additional configuration steps (separate doc)
- Notifications are not optional in practice — missing them means missing MFA prompts for sensitive resources

## Related Docs
- Standalone Client setup
- Managed environment deployment
- `get.twingate.com` (redirect to App Store)