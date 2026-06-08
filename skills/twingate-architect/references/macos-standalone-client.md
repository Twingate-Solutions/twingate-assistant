# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client installable without the App Store or Apple ID. It uses a system extension for VPN functionality that must be explicitly enabled on first use. Supports MDM distribution with pre-configuration options including pre-enabling the system extension via `.mobileconfig`.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/download) or specific versions via Client changelog
- Requires system extension enabled to connect — without it, Twingate cannot function
- Auto-updates supported if user has local administrator permissions
- Clients older than 12 months are unsupported and cannot connect
- Existing pre-configuration options (network pre-config, disabling auto-updates) work with standalone app

## Prerequisites
- macOS device
- Local admin rights (for automatic updates)
- MDM solution (for enterprise distribution)
- App must be installed at `/Applications/Twingate.app` (required for system extension)

## Step-by-Step: First-Time Setup
1. Download PKG from Twingate download page
2. Double-click PKG and complete onboarding
3. On first network connection, click **"Open System Settings"** when prompted
4. Navigate to **System Settings → Privacy & Security → Security**
5. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
6. Click **Allow**

## MDM Distribution
| MDM | Method |
|-----|--------|
| Intune | Distribute as Custom App |
| Jamf | Distribute as a package |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

**Pre-enabling system extension via MDM:** Use the provided [example `.mobileconfig`](https://www.twingate.com/docs/macos-standalone-client) when deploying to skip manual user approval.

## Gotchas
- **App location is mandatory:** System extension will not work if `Twingate.app` is run from any directory other than `/Applications/Twingate.app`
- **12-month client expiry:** Unsupported clients lose ability to connect entirely — establish an update cadence for managed devices
- **System extension must be manually allowed** on first connect unless pre-enabled via MDM profile
- If no security prompt appears, check **Privacy & Security → Extensions → Others → Networking** to verify Twingate extension state

## Troubleshooting: Won't Connect
1. Verify system extension is enabled (Privacy & Security → Security section)
2. If no prompt visible, check Privacy & Security → Extensions → Added extensions → Networking
3. Confirm app is located at `/Applications/Twingate.app`

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific PKG downloads)
- MDM pre-configuration guide
- Example `.mobileconfig` for system extension pre-approval