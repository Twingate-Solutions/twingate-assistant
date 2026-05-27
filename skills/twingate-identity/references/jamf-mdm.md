# Deploying Twingate Clients with Jamf MDM

## Summary
Instructions for distributing Twingate macOS and iOS clients via Jamf Pro MDM. Covers package deployment, silent installation via Custom Configuration Profiles, and client update procedures.

## Key Information
- macOS: Deploy via PKG package uploaded to Jamf
- iOS: Requires Apple Business Manager linked to Jamf first
- Configuration Profile preference domain: `com.twingate.macos`
- Team Identifier: `6GX8KVTR9H`
- Bundle IDs: `com.twingate.macos` (app), `com.twingate.macos.tunnelprovider` (system extension)

## Prerequisites
- Jamf Pro admin access
- macOS: PKG from [Twingate download page](https://www.twingate.com/download)
- iOS: Apple Business Manager account linked to Jamf
- Remove any manually installed Twingate clients before MDM rollout

## Silent Deployment Configuration Profile Settings

| Property Key | Value | Purpose |
|---|---|---|
| `PresentedDataPrivacy` | `true` | Suppress data privacy screen |
| `PresentedEducation` | `true` | Suppress education screen |
| `automaticallyInstallSystemExtension` | `true` | Auto-install system extension |
| `network` | `<your-network-name>` | Pre-populate network name |
| `LaunchApp` | `false` | Disable if using Launch Agent |
| `SUEnableAutomaticChecks` | `false` | Jamf manages updates |
| `SUAutomaticallyUpdate` | `false` | Jamf manages updates |

## Step-by-Step: Create Configuration Profile

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Set display name (e.g., `Twingate Silent Install`)
3. **Application & Custom Settings** → **External Applications** → **Add**
4. Source: **Custom Schema**; Preference domain: `com.twingate.macos`
5. **Add Schema** → paste JSON schema → Save; configure boolean/string values
6. **Managed Login Items**: Team ID `6GX8KVTR9H`
7. **Notifications**: App Name `Twingate`, Bundle ID `com.twingate.macos`, enable Notifications
8. **System Extensions** → Allowed system extensions, Team ID `6GX8KVTR9H`, add `com.twingate.macos.tunnelprovider`
9. *(macOS 15+ only)* Add second System Extensions entry: Non-removable from UI, same Team ID and extension ID
10. **VPN** → Configure:
    - Type: `VPN`, Connection Type: `Custom SSL`
    - Identifier: `com.twingate.macos`
    - Server: `null` (required, any non-blank value)
    - Provider Bundle ID: `com.twingate.macos.tunnelprovider`
    - Provider Designated Requirement: `anchor apple generic and identifier "com.twingate.macos.tunnelprovider"...` (full cert chain string)
11. **Scope** tab: test on small group first → Save

## Updating the Client
1. Download new PKG; upload to Jamf Pro (match priority of old package)
2. Edit policy: remove old package, add new package
3. Test by flushing policy on test device via policy logs
4. Policy reruns per triggers and updates client

## Gotchas
- **macOS 15 (Sequoia)**: Must add separate "Non-removable system extensions from UI" entry; won't apply retroactively on upgrade
- Manually installed clients must be removed first or version conflicts may occur; use a temporary removal policy
- `LaunchApp` must be `false` if deploying with Twingate Launch Agent
- VPN Server field cannot be blank—enter any placeholder value (e.g., `null`)

## Related Docs
- [macOS & iOS Client configuration options](https://www.twingate.com/docs/macos-ios)
- Jamf official package deployment documentation
- Apple Business Manager linking guide (Jamf docs)