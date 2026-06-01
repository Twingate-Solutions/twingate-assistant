# macOS Standalone Client

## Summary
Twingate offers a PKG-based macOS client installable without the App Store or Apple ID. It requires a system extension to enable its VPN adapter. Supports MDM distribution with pre-configuration options.

## Key Information
- Downloaded from [Twingate download page](https://www.twingate.com/docs/download) or specific versions from Client changelog
- Uses a **system extension** for VPN adapter — must be enabled to connect
- Auto-updates supported if user has local administrator permissions
- Clients older than 12 months are unsupported and cannot connect

## Prerequisites
- macOS device with ability to allow system extensions
- Local admin permissions (for auto-updates)
- App must reside at `/Applications/Twingate.app` (system extensions won't work otherwise)

## Step-by-Step: Installation

1. Download PKG from the Twingate download page
2. Double-click PKG and complete onboarding
3. On first network connection, click **"Open System Settings"** when prompted
4. In System Settings → **Privacy & Security** → scroll to **Security** section
5. Find panel: *"System software from application 'Twingate.app' was blocked from loading"*
6. Click **"Allow"**
7. Verify extension status: Privacy & Security → **Extensions** (bottom of page)

## MDM Distribution

| MDM Platform | Method |
|---|---|
| Intune | Custom App |
| Jamf | Distribute as package |
| Omnissa Workspace ONE | Non-App Store app |
| Hexnode UEM | Enterprise app |

**Pre-enabling system extension via MDM:**
- Use a `.mobileconfig` profile to auto-approve the system extension at deploy time
- Twingate provides an [example .mobileconfig](https://www.twingate.com/docs/macos-standalone-client) for this purpose
- Existing pre-configuration (e.g., network pre-selection, disabling auto-updates) works with standalone app

## Gotchas
- System extension **will not work** if app is run outside `/Applications/Twingate.app`
- If no security prompt appears, check: Privacy & Security → Extensions → **Others** → verify Twingate is enabled under **Added Extensions / Networking**
- Managed devices need a regular update process — Twingate does not force updates, and expired clients lose access entirely
- Auto-updates require local admin rights; without them, updates must be managed externally

## Troubleshooting: Won't Connect
1. Confirm system extension is enabled (Privacy & Security → Security section)
2. If no prompt visible: Privacy & Security → Extensions → Others → Twingate enabled?
3. Confirm app location is exactly `/Applications/Twingate.app`

## Related Docs
- General macOS onboarding guide
- Client changelog (version-specific downloads)
- Example `.mobileconfig` for MDM system extension pre-approval
- Twingate download page