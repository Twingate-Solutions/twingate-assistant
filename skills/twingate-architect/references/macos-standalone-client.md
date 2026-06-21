# macOS Standalone Client

## Summary
Twingate provides a PKG-based macOS client that installs without the App Store or Apple ID. It requires a system extension for VPN functionality. Supports MDM distribution and pre-configuration via mobile config profiles.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/download) or specific versions via Client changelog
- Requires system extension enabled for VPN adapter to function
- Auto-updates supported if user has local administrator permissions
- Clients older than 12 months cannot connect to Twingate service
- Pre-configuration (network pre-selection, disabling auto-updates) works with standalone app

## Prerequisites
- macOS device
- Local admin permissions (for auto-updates)
- System extension approval (user or MDM-pushed)

## Step-by-Step: Installation
1. Download PKG from download page
2. Double-click PKG and complete onboarding
3. On first connection, click **Open System Settings** when prompted
4. Navigate to **System Settings → Privacy & Security → Security**
5. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
6. Click **Allow**

## MDM Distribution
| MDM | Method |
|-----|--------|
| Intune | Custom App |
| Jamf | Package distribution |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

**Pre-enabling system extension via MDM:** Use provided [example `.mobileconfig`](https://www.twingate.com/docs/macos-standalone-client) to push system extension approval silently.

## Configuration Values
- App must reside at: `/Applications/Twingate.app`
- System extension status: **System Settings → Privacy & Security → Extensions**

## Gotchas
- System extension **will not work** if `Twingate.app` is run from any directory other than `/Applications/Twingate.app`
- No system extension prompt visible? Check **Privacy & Security → Extensions → Others → Networking** section for Twingate toggle
- Clients >12 months old are blocked from connecting — establish a regular update process for managed devices
- Users without local admin cannot auto-update; MDM admins must handle updates manually

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific downloads)
- Example `.mobileconfig` for system extension pre-approval
- MDM-specific distribution guides (Intune, Jamf, Workspace ONE, Hexnode)