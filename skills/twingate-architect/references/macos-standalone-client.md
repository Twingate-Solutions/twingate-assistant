---
source: https://www.twingate.com/docs/macos-standalone-client
type: docs
fetched: 2026-10-25
source_version: 1ea362846ac83d670439a2379905f92c38cef671fcd601986a9344f8d2b674ac
trust: official
---

# macOS Standalone Client

## Summary
The standalone macOS Client is installed via PKG installer (not the Mac App Store, which is no longer supported). It requires a system extension to be enabled for VPN functionality. Supports automatic updates when the user has local administrator permissions.

## Key Information
- PKG installer available from the [Twingate download page](https://www.twingate.com/docs/download)
- Specific versions available in the Client changelog
- Clients older than 12 months cannot connect to the Twingate service
- Automatic updates require local administrator permissions on the device
- App must be installed at `/Applications/Twingate.app` — system extensions will not work from other directories

## Prerequisites
- macOS device
- No Apple ID required
- Local admin permissions (for automatic updates)

## Step-by-Step: Installation

1. Download PKG from the Twingate download page
2. Double-click PKG file and complete onboarding
3. Follow the general macOS onboarding guide
4. On first network connection, enable the system extension when prompted

## Step-by-Step: Enabling System Extension

1. Click **"Open System Settings"** when prompted on first connect
2. Navigate to **Privacy & Security** in sidebar
3. Scroll to **Security** section
4. Click **Allow** next to "System software from application 'Twingate.app' was blocked from loading"
5. Verify extension status at bottom of Privacy & Security page under **Extensions**

## MDM Distribution

| MDM Platform | Method |
|---|---|
| Intune | Custom App |
| Jamf | Distribute as package |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

- Existing pre-configuration (e.g., network pre-configuration, disabling auto-updates) remains compatible
- Use the provided `.mobileconfig` example to **pre-enable the system extension** via MDM profile before deployment

## Gotchas
- App must be at exactly `/Applications/Twingate.app` — system extension fails from any other path
- System extension must be explicitly enabled; Twingate cannot connect without it
- Mac App Store version is deprecated and unsupported
- Clients >12 months old are blocked from connecting; ensure update cadence is managed for fully managed devices

## Troubleshooting: Won't Connect
1. Verify system extension is enabled via Privacy & Security → Extensions
2. If no prompt appeared, check **Extensions → Others → Networking** section for Twingate toggle
3. Confirm app location is `/Applications/Twingate.app`

## Related Docs
- Twingate download page
- General macOS onboarding guide
- Client changelog (version-specific PKGs)
- Example `.mobileconfig` for MDM system extension pre-enablement