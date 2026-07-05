# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client installable without the App Store or Apple ID. It uses a system extension for VPN functionality that must be explicitly enabled on first connection. Supports MDM distribution and pre-configuration via mobile config profiles.

## Key Information
- PKG installer available at Twingate download page; specific versions in Client changelog
- Requires system extension enabled — without it, Twingate cannot connect
- Auto-updates supported if user has local administrator permissions
- Clients older than 12 months cannot connect to Twingate service
- Pre-configuration (network, disabling auto-updates) works with standalone app

## Prerequisites
- macOS device
- Local admin permissions (for auto-updates)
- App must reside at `/Applications/Twingate.app` (system extension requirement)

## Step-by-Step: Enable System Extension
1. Attempt first connection — prompted to enable system extension
2. Click **Open System Settings**
3. Navigate to **Privacy & Security** → **Security** section
4. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
5. Click **Allow**
6. Verify status: bottom of Privacy & Security page under **Extensions**

## MDM Distribution
| MDM Platform | Method |
|---|---|
| Intune | Distribute as Custom App |
| Jamf | Distribute as a package |
| Omnissa Workspace ONE | Distribute as non-App Store app |
| Hexnode UEM | Distribute as enterprise app |

**Pre-enabling system extension via MDM:** Deploy provided `.mobileconfig` profile to automatically enable the system extension for end users before first launch.

## Configuration Values
- **Install path (required):** `/Applications/Twingate.app`
- **Pre-config profile:** `.mobileconfig` (example provided by Twingate)

## Gotchas
- System extension **will not work** if app is run outside `/Applications/Twingate.app`
- Must actively manage update cadence if fully managing devices — no auto-update without local admin rights
- Clients >12 months old are blocked from connecting; establish regular update process for managed fleets
- If no security prompt appears, check **Privacy & Security → Extensions → Others → Networking** for Twingate toggle

## Related Docs
- Twingate download page
- Client changelog (version-specific PKG downloads)
- General macOS onboarding guide
- Example `.mobileconfig` for system extension pre-enablement
- MDM-specific distribution guides (Intune, Jamf, Workspace ONE, Hexnode)