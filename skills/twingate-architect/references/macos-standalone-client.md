## macOS Standalone Client

The standalone macOS Client installs without the App Store or an Apple ID via a PKG installer. It requires a system extension to be enabled for VPN connectivity; the extension can be pre-approved via MDM profile.

**Key Information:**
- PKG installer available from Twingate download page; specific versions from the Client changelog
- System extension is required for Twingate to connect -- must be enabled in Privacy & Security
- Auto-updates supported if the user has local admin permissions
- Must be installed at `/Applications/Twingate.app` -- system extensions fail from any other path

**Setup:**
1. Download PKG and run installer
2. On first network connection, click "Open System Settings" when prompted for system extension
3. System Settings → Privacy & Security → Security: click "Allow" for Twingate

**MDM Distribution:**
- Kandji: distribute as Custom App
- Jamf: distribute as package
- Omnissa Workspace ONE: distribute as non-App Store app
- Hexnode UEM: distribute as enterprise app

**Pre-enabling System Extension (MDM):**
Deploy the Twingate-provided example `.mobileconfig` to auto-approve the system extension at deployment time.

**Troubleshooting:**
- Won't connect: check System Settings → Privacy & Security → Extensions (or Others → Added extensions → Networking)
- Confirm app location is `/Applications/Twingate.app` -- any other path breaks the system extension

**Related Docs:**
- /docs/macos -- macOS Client setup and general usage
- /docs/macos-and-ios -- MDM deployment with config profiles
