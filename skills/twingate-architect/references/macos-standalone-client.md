# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client that doesn't require the App Store or Apple ID. It uses a system extension for its VPN adapter that must be explicitly enabled on first use. Supports MDM distribution and pre-configuration via `.mobileconfig` profiles.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/macos-standalone-client) or specific versions from Client changelog
- Requires system extension enabled to connect — without it, Twingate cannot function
- Auto-updates supported if user has local administrator permissions
- Clients older than 12 months are unsupported and cannot connect
- App **must** reside at `/Applications/Twingate.app` — system extension fails from other directories

## Prerequisites
- macOS device with local admin rights (for system extension approval and auto-updates)
- Or MDM with capability to push `.mobileconfig` profiles (for pre-enabling extension)

## Step-by-Step: Initial Setup
1. Download PKG from Twingate download page
2. Double-click PKG and complete onboarding
3. On first network connection, click **"Open System Settings"** when prompted
4. Navigate to **System Settings → Privacy & Security → Security**
5. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
6. Click **Allow**

## Step-by-Step: MDM Distribution
1. Use MDM-specific PKG distribution method:
   - **Kandji**: Custom App
   - **Jamf**: Package distribution
   - **Omnissa Workspace ONE**: Non-App Store app
   - **Hexnode UEM**: Enterprise app
2. Deploy provided `.mobileconfig` to pre-enable system extension (avoids end-user prompt)
3. Apply any existing pre-configuration (network pre-config, disabling auto-updates) — compatible with standalone app

## Configuration Values
| Item | Value |
|------|-------|
| Installer format | `.pkg` |
| Required install path | `/Applications/Twingate.app` |
| MDM profile type | `.mobileconfig` (system extension pre-approval) |

## Gotchas
- System extension **silently fails** if app runs outside `/Applications/Twingate.app`
- No system extension prompt visible? Check **Privacy & Security → Extensions → Others → Networking** section
- Clients >12 months old are blocked from service — establish update cadence for managed devices
- Auto-updates require local admin; managed environments should handle updates via MDM

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific downloads)
- Example `.mobileconfig` for system extension pre-approval
- MDM-specific guides: Kandji, Jamf, Omnissa Workspace ONE, Hexnode UEM