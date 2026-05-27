# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client that installs without the App Store or Apple ID. It uses a system extension for its VPN adapter, which must be explicitly enabled on first use. Supports MDM distribution and pre-configuration via profiles.

## Key Information
- Download from [Twingate download page](https://www.twingate.com/docs/macos-standalone-client) or specific versions from Client changelog
- Requires system extension to be enabled before connecting
- Auto-updates supported if user has local admin permissions
- **Clients older than 12 months cannot connect** to Twingate service
- App must be installed at `/Applications/Twingate.app` — system extensions fail from other locations

## Prerequisites
- macOS device with admin access (for system extension approval)
- For MDM distribution: MDM platform (Intune, Jamf, Workspace ONE, Hexnode)
- Local admin rights required for automatic updates

## Step-by-Step: Initial Setup
1. Download PKG from Twingate download page
2. Double-click PKG and complete onboarding
3. On first network connection, click **"Open System Settings"** when prompted
4. Navigate to **System Settings → Privacy & Security → Security**
5. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
6. Click **Allow**

## MDM Distribution
| Platform | Method |
|----------|--------|
| Intune | Distribute as Custom App |
| Jamf | Distribute as a package |
| Omnissa Workspace ONE | Distribute as non-App Store app |
| Hexnode UEM | Distribute as enterprise app |

- Pre-existing network pre-configuration (including disabling auto-updates) works with standalone app
- Use provided `.mobileconfig` example to **pre-enable the system extension** via MDM profile before deployment

## Gotchas
- System extension will **not function** if `Twingate.app` is run outside `/Applications/`
- No system extension prompt visible? Check **Privacy & Security → Extensions → Others → Networking** for Twingate toggle
- Without local admin rights, auto-updates won't work — managed devices need a manual update process
- 12-month client expiry means unmanaged/neglected devices will lose connectivity silently

## Troubleshooting: Won't Connect
1. Confirm system extension is enabled via Privacy & Security settings
2. Verify app location is exactly `/Applications/Twingate.app`
3. If no security prompt appears, check **Extensions → Added Extensions → Networking**

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific PKG downloads)
- Example `.mobileconfig` for MDM system extension pre-enablement
- Pre-configuration guide (network pre-config, disabling auto-updates)