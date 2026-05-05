## Deploying Twingate Clients with Omnissa Workspace ONE

How to distribute the Twingate macOS and iOS Clients via Omnissa Workspace ONE (formerly VMware Workspace ONE).

**macOS:**
- Distribute as a **non-App Store app** (PKG)
- Download the .pkg from the Twingate download page
- Upload via Workspace ONE's standard non-App Store app workflow

**iOS -- Requires Apple Business Manager:**
- Add Twingate Client to **Apple Business Manager** first
- Distribute via Workspace ONE's ABM integration

**Linking Workspace ONE to ABM:**
- **Settings -> Apple (under Devices & Users) -> VPP Managed Distribution**
- Follow the guided setup
- **Uncheck "Automatically Send Invites"**

**Required Workspace ONE Settings After Linking:**

**1. Enable Device Assignment** (avoids requiring users' personal Apple IDs)
- **Applications -> Native -> Purchased**
- Select Twingate iOS app
- **More Actions -> Enable Device Assignment**

**2. Enable Auto Updates** (recommended)
- Same screen, **More Actions -> Enable Auto Updates**

**Pre-Migration Step (Important):**
- Uninstall any manually-installed Twingate Clients via a temporary policy first
- Why: manually-installed versions may differ from MDM-distributed, causing config drift
- Deactivate the cleanup policy before rolling out the MDM-managed Client

**Pre-Configuring the macOS Client:**
- Follow the Twingate **Configuration Profiles** guide (`/docs/macos-and-ios`) to:
  - Auto-enable VPN configuration
  - Auto-allow system extension
  - Pre-populate the Twingate network/tenant name
  - Skip privacy/education screens for silent install
- Same Bundle ID + Team Identifier values as in /docs/jamf-mdm:
  - Bundle ID: `com.twingate.macos`
  - Team Identifier: `6GX8KVTR9H`
  - Tunnel provider: `com.twingate.macos.tunnelprovider`

**Gotchas:**
- "Automatically Send Invites" being **on** during VPP setup will email each user requesting their personal Apple ID -- defeats the device assignment model
- Without the macOS configuration profile, users see prompts for VPN approval and system extension -- not fully silent
- iOS app distribution depends entirely on ABM linkage being correct -- test on a single device before fleet rollout

**Related Docs:**
- /docs/macos-and-ios -- Configuration profile keys
- /docs/jamf-mdm -- Detailed config profile recipe (same keys apply here)
- /docs/kandji-mdm -- Auto App alternative
- /docs/intune-configuration -- Intune for Windows/cross-platform
