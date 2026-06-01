# Deploying Twingate Clients with Jamf MDM

## Summary
Guide for distributing Twingate macOS and iOS clients via Jamf Pro MDM. Covers package deployment, configuration profiles for silent installation, and client update procedures.

## Key Information
- macOS deployment uses `.pkg` installer uploaded to Jamf
- iOS deployment requires Apple Business Manager linked to Jamf
- Configuration profiles enable silent deployment by suppressing onboarding screens
- Team Identifier for Twingate: `6GX8KVTR9H`
- System extension bundle ID: `com.twingate.macos.tunnelprovider`
- App bundle ID: `com.twingate.macos`
- Preference domain: `com.twingate.macos`

## Prerequisites
- Jamf Pro admin access
- macOS: Twingate `.pkg` from [download page](https://www.twingate.com/download)
- iOS: Apple Business Manager account linked to Jamf

## Configuration Profile Setup (Silent Deployment)

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Name profile (e.g., `Twingate Silent Install`)
3. **Application & Custom Settings** → **External Applications** → **Add**
4. Source: **Custom Schema**, domain: `com.twingate.macos`
5. Paste JSON schema → configure values below
6. Add **Managed Login Items**: Team ID `6GX8KVTR9H`
7. Add **Notifications**: App Name `Twingate`, Bundle ID `com.twingate.macos`, Enabled
8. Add **System Extensions**: Allowed + Non-removable (macOS 15+), Team ID `6GX8KVTR9H`, extension `com.twingate.macos.tunnelprovider`
9. Add **VPN** configuration (see values below)
10. Set **Scope**, then **Save**

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
| Provider Designated Requirement | `anchor apple generic and identifier "com.twingate.macos.tunnelprovider"...` (full string in docs) |

## Updating the Client
1. Download new `.pkg` from Twingate website
2. Upload to Jamf Pro as new package (same priority as previous)
3. Edit policy: remove old package, add new package
4. Flush policy on test device(s) to verify
5. Policy runs on trigger and updates clients

## Gotchas
- **Pre-existing manual installs**: Remove manually installed clients before Jamf rollout; version conflicts cause issues. Use a temporary removal policy, then deactivate it.
- **macOS 15 (Sequoia)**: Must add `Non-removable system extensions from UI` entry separately; configuring it on earlier versions is harmless but won't apply retroactively after upgrade.
- **LaunchApp**: Set to `false` if deploying with the Twingate Launch Agent.
- **Server field in VPN**: Cannot be blank—use any placeholder value (e.g., `null`).

## Related Docs
- [macOS & iOS client configuration options](https://www.twingate.com/docs/macos-ios)
- Jamf official package deployment documentation
- Apple Business Manager + Jamf linking documentation