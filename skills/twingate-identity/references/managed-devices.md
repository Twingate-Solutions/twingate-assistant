## Managed Devices Overview

Twingate Client deployment across MDM solutions -- index page pointing to platform-specific guides.

### Supported MDMs

Twingate Client works with most MDM solutions:
- **AirWatch / Workspace ONE** (Omnissa)
- **Microsoft Intune / Endpoint Manager**
- **Jamf** (macOS/iOS)
- **Kandji** (macOS/iOS)
- **Other MDMs** that support PKG/EXE/MSI deployment

### Platform-Specific Guides

| Platform | Format | Notes |
|---|---|---|
| **Windows** | EXE (preferred) or MSI | EXE bundles .NET 8 Runtime; see /docs/windows-managed-devices |
| **macOS** | App Store app or standalone PKG | MDMs use Apple Business Manager for App Store distribution |
| **iOS** | App Store app | Requires Apple Business Manager linkage in the MDM |

### Permissions / Privileges

The Twingate Client does **not** require special device privileges, **but** it must create a **VPN profile** to operate.

**Important**: the Twingate Client uses a local VPN profile -- the VPN server address is `127.0.0.1`. **No VPN traffic actually leaves the device** via traditional VPN means; the VPN profile is just the OS hook for the Twingate tunnel infrastructure.

This is relevant for:
- MDM compliance reviews flagging "VPN configuration" as a concern
- Documentation for security/privacy stakeholders -- Twingate is not a traditional VPN despite the OS-level VPN hook

### Decision Notes

- For mixed fleets (Windows + Mac + iOS): use Intune for Windows + Jamf/Kandji for macOS+iOS, OR Workspace ONE for cross-platform
- For Apple-only orgs: Kandji (with the Twingate Auto App) is fastest to deploy
- For Microsoft-only orgs: Intune handles all three platforms reasonably
- Always pre-configure the Twingate Network and silent-install flags to minimize end-user friction

### Gotchas

- The "VPN profile" terminology can confuse users and security reviewers -- proactively document that no traditional VPN traffic is involved
- iOS distribution **always** requires Apple Business Manager -- plan ABM linkage before MDM rollout
- macOS configuration profiles for VPN/system extension are required for silent UX -- without them, users still see system prompts

### Related Docs

- /docs/windows-managed-devices -- Windows MDM details
- /docs/jamf-mdm -- Jamf for macOS/iOS
- /docs/kandji-mdm -- Kandji for macOS/iOS
- /docs/intune-configuration -- Microsoft Intune
- /docs/omnissa-workspace-one-mdm -- Omnissa Workspace ONE
