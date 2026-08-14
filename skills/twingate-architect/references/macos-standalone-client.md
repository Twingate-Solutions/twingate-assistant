---
source: https://www.twingate.com/docs/macos-standalone-client
type: docs
fetched: 2026-08-14
source_version: a013788ea8b13edd9645cced9b3931b2cf912e379ea330aaae61193f83d356fe
---

# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client installable without the App Store or Apple ID. It requires a system extension to be enabled for VPN functionality. Supports MDM distribution and pre-configuration via mobile config profiles.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/download) or specific versions from Client changelog
- Requires system extension approval on first connection
- Clients older than 12 months cannot connect to Twingate service
- Automatic updates supported if user has local administrator permissions
- Pre-configuration options (including disabling auto-updates) work with standalone app

## Prerequisites
- macOS device with local admin rights (for auto-updates)
- App must be installed at `/Applications/Twingate.app` (system extension requirement)
- For MDM distribution: appropriate MDM platform access

## Step-by-Step

### Manual Installation
1. Download PKG from Twingate download page
2. Double-click PKG and complete onboarding
3. On first network connection, click **Open System Settings** when prompted
4. Navigate to **System Settings → Privacy & Security → Security**
5. Find "System software from application 'Twingate.app' was blocked from loading"
6. Click **Allow**

### Verify System Extension
- Bottom of Privacy & Security page under **Extensions**
- If no message: scroll to **Others → Extensions** → confirm Twingate enabled under **Added Extensions → Networking**

## MDM Distribution

| Platform | Method |
|----------|--------|
| Intune | Custom App (PKG) |
| Jamf | Distribute as package |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

**Pre-enable system extension via MDM:** Deploy the provided [example `.mobileconfig`](https://www.twingate.com/docs/macos-standalone-client) to automatically approve the system extension without user interaction.

## Configuration Values
- Install path (required): `/Applications/Twingate.app`
- System extension profile: `.mobileconfig` (available from Twingate docs)

## Gotchas
- System extension **will not work** if app runs from any directory other than `/Applications/Twingate.app`
- Clients >12 months old are blocked from connecting — maintain an update process for managed devices
- Users without local admin cannot auto-update; manual or MDM-based updates required
- Must explicitly click **Allow** in Privacy & Security; dismissing the initial prompt requires navigating manually to Settings

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific downloads)
- Twingate pre-configuration guide (network pre-config + disabling auto-updates)
- Example `.mobileconfig` for system extension pre-approval