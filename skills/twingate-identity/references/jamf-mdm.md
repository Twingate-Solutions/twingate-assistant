---
source: https://www.twingate.com/docs/jamf-mdm
type: docs
fetched: 2026-08-14
source_version: b5057abce219d20b56da1da896167a66ec947319303a416598f2ae1ff47219d5
---

# Deploying Twingate Client with Jamf MDM

## Summary
Guide for distributing Twingate macOS and iOS clients via Jamf Pro. Covers package deployment, configuration profiles for silent installation, and client update procedures.

## Key Information
- macOS: Deploy via PKG package upload to Jamf
- iOS: Requires Apple Business Manager linked to Jamf first
- Configuration Profile preference domain: `com.twingate.macos`
- Team Identifier: `6GX8KVTR9H`
- Bundle ID: `com.twingate.macos`
- Tunnel provider: `com.twingate.macos.tunnelprovider`
- macOS 15+ requires additional "Non-removable system extensions from UI" configuration

## Prerequisites
- Jamf Pro admin access
- macOS: Download `.pkg` from Twingate download page
- iOS: Apple Business Manager account linked to Jamf
- Existing manually-installed Twingate clients removed before rollout

## Step-by-Step: Silent Deployment Configuration Profile

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Set display name (e.g., `Twingate Silent Install`)
3. **Application & Custom Settings** → **External Applications** → **Add**
4. Source: **Custom Schema**, preference domain: `com.twingate.macos`
5. Paste JSON schema (see Configuration Values)
6. Set silent deployment values (see below)
7. Add **Managed Login Items**: Team ID `6GX8KVTR9H`
8. Add **Notifications**: App Name `Twingate`, Bundle ID `com.twingate.macos`, Notifications Enabled
9. Add **System Extensions**: Type = Allowed, Team ID `6GX8KVTR9H`, Extension `com.twingate.macos.tunnelprovider`
10. *(macOS 15+ only)* Add second System Extensions entry: Type = Non-removable from UI, same Team ID and extension
11. Add **VPN** configuration (see Configuration Values)
12. Set **Scope**, then **Save**

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

### VPN Profile Settings
| Field | Value |
|-------|-------|
| Connection Name | `Twingate` |
| VPN Type | `VPN` |
| Connection Type | `Custom SSL` |
| Identifier | `com.twingate.macos` |
| Server | `null` (any non-blank value) |
| Provider Bundle Identifier | `com.twingate.macos.tunnelprovider` |
| Provider Designated Requirement | *(full certificate chain string in doc)* |

## Gotchas
- Remove manually installed clients before Jamf rollout to avoid version conflicts
- `Server` field in VPN config cannot be blank—use any placeholder value
- macOS 15 (Sequoia) requires the additional Non-removable system extensions entry; safe to configure on earlier versions (ignored if macOS 15 not present at config time)
- Set `LaunchApp: false` if using Twingate Launch Agent instead
- Scope to test group before organization-wide deployment

## Updating the Client
1. Download new `.pkg` from Twingate website
2. Upload to Jamf Pro as new package (same priority as previous)
3. Edit policy: remove old package, add new package
4. Flush policy on test device(s) to verify
5. Policy runs on trigger schedule to update remaining devices

## Related Docs
- [macOS & iOS Client configuration options](https://www.twingate.com/docs/macos-ios)
- Jamf official package deployment documentation
- Apple Business Manager → Jamf integration guide