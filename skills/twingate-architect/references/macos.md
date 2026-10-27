---
source: https://www.twingate.com/docs/macos
type: docs
fetched: 2026-10-25
source_version: a7870a33094872f67c3599d54d5004046d710305fb9ede395c94c1702ff742f5
trust: official
---

# macOS Twingate Client

## Page Title
macOS Client Installation and Setup

## Summary
Guide for installing and configuring the Twingate client on macOS. The Mac App Store version is deprecated; use the standalone PKG installer instead. Setup requires VPN configuration and a system extension to be enabled.

## Key Information
- Mac App Store version is **no longer supported** — use standalone PKG
- Native Apple Silicon (ARM) support included
- Required permissions: VPN configuration + system extension
- Strongly recommended: notifications (used for step-up auth prompts)
- Client only intercepts traffic for defined private Resources; general browsing is unaffected

## Prerequisites
- macOS device (Intel or Apple Silicon)
- Admin rights to install system extension and configure VPN
- Network name (found in welcome email)
- Identity Provider credentials

## Step-by-Step

1. Download PKG installer from [twingate.com download page](https://www.twingate.com/docs/macos)
2. Run the PKG and follow installer prompts
3. Launch Twingate — onboarding wizard starts on first run
4. Grant required permissions when prompted:
   - **Notifications**: System Settings → Notifications → Twingate
   - **VPN configuration**: System Settings → VPN
   - **System extension**: System Settings → Privacy & Security → allow extension
5. Enter your network name (e.g., `acme`) → click **Join Network**
6. Authenticate via Identity Provider in the browser window that opens
7. Click **Open Twingate.app** when browser prompts to return to the client
8. Client shows "online" — leave running in background

## Configuration Values
None (no CLI flags or env vars for standard user setup; managed/enterprise deployments see separate documentation linked below)

## Gotchas
- Must click **Open Twingate.app** in browser after IdP auth or the client won't activate
- Skipping system extension or VPN config setup will prevent Twingate from functioning
- Skipping notifications may cause silent failures on resources requiring step-up authentication
- Managed environment deployments require additional steps beyond standard install

## Related Docs
- [Twingate Download Page](https://www.twingate.com/download)
- Standalone Client setup guide
- Managed/enterprise macOS deployment guide