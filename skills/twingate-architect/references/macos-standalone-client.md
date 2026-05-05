# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client that installs without the App Store or Apple ID. It uses a system extension for VPN functionality that must be explicitly enabled on first connection. Supports MDM distribution and automatic updates for local admin users.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/download) or specific versions via Client changelog
- Requires system extension approval on first use
- Auto-updates supported only if user has local administrator permissions
- Clients older than 12 months cannot connect to the service
- Pre-configuration (network pre-config, disabling auto-updates) works with standalone app

## Prerequisites
- macOS device with administrator access (for system extension approval)
- App must be located at `/Applications/Twingate.app` (system extensions fail from other directories)

## Step-by-Step

### Installation
1. Download PKG from Twingate download page
2. Double-click PKG and complete onboarding
3. Follow general macOS onboarding guide

### Enabling System Extension (First Connection)
1. Attempt to connect — prompt appears to enable system extension
2. Click **Open System Settings**
3. Navigate to **Privacy & Security** → **Security** section
4. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
5. Click **Allow**

### MDM Distribution
| MDM Platform | Method |
|---|---|
| Kandji | Custom App |
| Jamf | Package distribution |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

## Configuration Values
- **MDM pre-enable**: Use provided `.mobileconfig` profile to pre-approve system extension
- **Install path** (required): `/Applications/Twingate.app`

## Gotchas
- System extension will **not** work if app runs from any path other than `/Applications/Twingate.app`
- System extension must be enabled — Twingate cannot connect without it
- Clients >12 months old are blocked from connecting; ensure MDM update processes are in place
- If no blocked-software message appears, check **Privacy & Security → Extensions → Others → Networking** section for Twingate toggle

## Troubleshooting
- **Won't connect**: Verify system extension is enabled in Privacy & Security
- **Extension not visible in blocked panel**: Check **Extensions → Added Extensions → Networking** for Twingate entry
- **Wrong install path**: Move app to `/Applications/Twingate.app`

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific downloads)
- Example `.mobileconfig` for MDM system extension pre-approval
- Twingate download page