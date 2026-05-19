# Deploying Twingate Client with Jamf MDM

## Summary
Covers distributing the Twingate macOS and iOS clients via Jamf Pro, including package deployment, configuration profiles for silent installs, and client update procedures.

## Key Information
- macOS: Deploy via PKG uploaded to Jamf; download from Twingate download page
- iOS: Requires linking Jamf to Apple Business Manager first, then distribute via Jamf
- Team Identifier: `6GX8KVTR9H`
- Bundle ID: `com.twingate.macos`
- Tunnel Provider: `com.twingate.macos.tunnelprovider`
- Preference domain: `com.twingate.macos`

## Prerequisites
- Jamf Pro admin access
- macOS: PKG installer from Twingate download page
- iOS: Apple Business Manager linked to Jamf Pro

## Configuration Profile Setup (Silent Deployment)

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Set display name (e.g., `Twingate Silent Install`)
3. **Application & Custom Settings** → **External Applications** → **Add**
4. Source: **Custom Schema**; Preference domain: `com.twingate.macos`
5. Paste JSON schema (see below); configure values
6. Add **Managed Login Items**: Team ID `6GX8KVTR9H`
7. Add **Notifications**: App Name `Twingate`, Bundle ID `com.twingate.macos`, Notifications Enabled
8. Add **System Extensions**: Type = Allowed, Team ID `6GX8KVTR9H`, Extension = `com.twingate.macos.tunnelprovider`
9. *(macOS 15+ only)* Add second System Extensions entry: Type = **Non-removable from UI**, same Team ID and extension
10. Add **VPN** configuration (see values below)
11. Set **Scope**, then **Save**

## Configuration Values

### Silent Deployment Settings
| Key | Value |
|-----|-------|
| `PresentedDataPrivacy` | `true` |
| `PresentedEducation` | `true` |
| `automaticallyInstallSystemExtension` | `true` |
| `network` | Your Twingate network name |
| `LaunchApp` | `false` |
| `SUEnableAutomaticChecks` | `false` |
| `SUAutomaticallyUpdate` | `false` |

### VPN Configuration
| Field | Value |
|-------|-------|
| Connection Name | `Twingate` |
| VPN Type | `VPN` |
| Connection Type | `Custom SSL` |
| Identifier | `com.twingate.macos` |
| Server | `null` (any non-blank value) |
| Provider Bundle Identifier | `com.twingate.macos.tunnelprovider` |
| Provider Designated Requirement | `anchor apple generic and identifier "com.twingate.macos.tunnelprovider" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "6GX8KVTR9H")` |

## Updating the Client
1. Download latest PKG from Twingate website
2. Upload to Jamf Pro as new package (match priority of previous package)
3. Edit policy: remove old package, add new package
4. Test by flushing policy on specific device(s) via policy logs
5. Policy runs on next trigger and updates client

## Gotchas
- **Pre-existing manual installs**: Must uninstall manually-installed clients before Jamf rollout to avoid version conflicts; use a temporary removal policy
- **macOS 15 Sequoia**: Requires additional "Non-removable system extensions from UI" entry; safe to configure on earlier versions (ignored if macOS 15 not yet installed)
- **LaunchApp**: Set to `false` if deploying with Twingate Launch