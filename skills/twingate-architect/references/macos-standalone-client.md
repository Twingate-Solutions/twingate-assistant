# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client installable without the App Store or Apple ID. It uses a system extension for its VPN adapter, which must be explicitly enabled on first connection. Supports MDM distribution and pre-configuration via mobile config profiles.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/macos-standalone-client) or specific versions from Client changelog
- Requires system extension approval to connect
- Supports automatic updates if user has local administrator permissions
- **Clients older than 12 months cannot connect to Twingate service**
- App must be located at `/Applications/Twingate.app` — system extensions fail from other directories

## Prerequisites
- macOS device
- Local admin permissions (for automatic updates)
- MDM solution (for enterprise distribution)

## Step-by-Step: Enable System Extension
1. Attempt to connect to network — prompt appears to enable system extension
2. Click **"Open System Settings"**
3. Navigate to **Privacy & Security** → **Security** section
4. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
5. Click **Allow**
6. Verify status: Privacy & Security → **Extensions** (bottom of page)

## MDM Distribution
| MDM | Method |
|-----|--------|
| Intune | Custom App |
| Jamf | Distribute as package |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

- Pre-existing network pre-configuration (including disabling auto-updates) works with standalone app
- Use provided `.mobileconfig` example to **pre-enable system extension** via MDM profile before user first launch

## Configuration Values
- **Install path (required):** `/Applications/Twingate.app`
- **Profile type for pre-enabling extension:** `.mobileconfig` (macOS mobile configuration profile)

## Gotchas
- System extension will not load if `Twingate.app` is run from any directory other than `/Applications/`
- No system extension prompt visible? Check **Privacy & Security → Extensions → Others → Networking** section for Twingate entry
- Managed devices need a defined update process — Twingate does not force-update clients; stale clients (12+ months) lose service access
- Automatic updates require local admin rights; managed environments may need to handle updates via MDM

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific PKG downloads)
- Example `.mobileconfig` for system extension pre-approval
- MDM-specific distribution guides (Intune, Jamf, Workspace ONE, Hexnode)