# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client that installs without the App Store or Apple ID. It uses a system extension for its VPN adapter, which must be manually enabled on first connection. MDM distribution is supported with options to pre-enable the system extension via configuration profile.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/download) or specific versions from Client changelog
- Requires system extension enabled to connect — Twingate will not function without it
- Automatic updates supported if user has local administrator permissions
- Clients older than 12 months are unsupported and cannot connect to the service
- Existing pre-configuration (network pre-config, disabling auto-updates) works with standalone app

## Prerequisites
- macOS device
- Local admin permissions (for automatic updates)
- App must reside at `/Applications/Twingate.app` — system extension will not work from other directories

## Step-by-Step: Initial Setup
1. Download PKG from Twingate download page
2. Double-click PKG and complete onboarding
3. On first network connection, click **Open System Settings** when prompted
4. Navigate to **Privacy & Security → Security**
5. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
6. Click **Allow** to enable system extension

## Step-by-Step: MDM Distribution
1. Distribute PKG via your MDM platform:
   - **Intune**: distribute as Custom App
   - **Jamf**: distribute as a package
   - **Omnissa Workspace ONE**: distribute as non-App Store app
   - **Hexnode UEM**: distribute as enterprise app
2. Deploy the example `.mobileconfig` profile to pre-enable the system extension (avoids end-user prompt)

## Configuration Values
| Item | Value |
|------|-------|
| Required install path | `/Applications/Twingate.app` |
| System extension config profile | Example `.mobileconfig` available from Twingate docs |
| Settings location (macOS) | System Settings → Privacy & Security → Extensions → Networking |

## Gotchas
- System extension **will not load** if app is run from any directory other than `/Applications/Twingate.app`
- If user dismisses the system extension prompt, must manually navigate to **Privacy & Security → Security** to allow it
- If no blocked message appears, check **Privacy & Security → Extensions → Others → Networking** for Twingate toggle
- Devices without local admin cannot auto-update — managed deployments need a defined update process to stay within the 12-month support window

## Troubleshooting
- **Won't connect**: Verify system extension is enabled under Privacy & Security → Extensions
- **Extension not visible**: Check under "Added extensions" in the Networking section
- **Blocked extension missing**: May already be approved or need to scroll to "Others" section

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific downloads)
- Example `.mobileconfig` for MDM pre-enablement
- Pre-configuration guide (network pre-config, disabling auto-updates)