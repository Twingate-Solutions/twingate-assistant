# macOS Standalone Client

## Summary
Twingate provides a PKG-based macOS client that installs without the App Store or Apple ID. It uses a macOS system extension for its VPN adapter, which must be explicitly enabled on first connection. Supports MDM distribution and pre-configuration via mobile config profiles.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/download) or specific versions from Client changelog
- Requires system extension approval on first run
- Auto-updates supported if user has local admin permissions
- Clients older than 12 months cannot connect to Twingate service
- App **must** reside at `/Applications/Twingate.app` for system extension to function

## Prerequisites
- macOS device with local admin rights (for auto-updates and system extension approval)
- MDM profile with system extension pre-approval (for managed deployments)

## Step-by-Step: Installation
1. Download PKG from Twingate download page
2. Double-click PKG and complete onboarding
3. On first network connection, click **Open System Settings** when prompted
4. Navigate to **Privacy & Security → Security**
5. Find "System software from application 'Twingate.app' was blocked from loading"
6. Click **Allow**

## Step-by-Step: Verify System Extension
- Go to **Privacy & Security → Extensions → Others → Networking**
- Confirm Twingate is listed and enabled under "Added extensions"

## MDM Distribution
| MDM Platform | Method |
|---|---|
| Kandji | Custom App |
| Jamf | Package distribution |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

## Configuration Values
- **Pre-enable system extension**: Deploy example `.mobileconfig` profile before rollout
- **Pre-configuration**: Existing network pre-config options (including disabling auto-updates) work with standalone app

## Gotchas
- System extension **will not work** if app runs from any path other than `/Applications/Twingate.app`
- If no security prompt appears, check manually under **Privacy & Security → Extensions → Networking**
- Clients >12 months old are blocked from connecting — establish a managed update process for fully managed devices
- Users without local admin cannot auto-update; manual or MDM-pushed updates required

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific downloads)
- Example `.mobileconfig` for system extension pre-approval
- MDM-specific guides: Kandji, Jamf, Omnissa Workspace ONE, Hexnode UEM