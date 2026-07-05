# Deploying Twingate Client with Jamf MDM

## Summary
Guide for distributing Twingate macOS and iOS clients via Jamf Pro using packages, Apple Business Manager, and Configuration Profiles. Covers silent deployment configuration and client update procedures.

## Key Information
- macOS deployment uses PKG package upload to Jamf
- iOS deployment requires Apple Business Manager linked to Jamf first
- Configuration Profile enables silent installation (suppresses prompts, auto-installs system extension)
- Team Identifier for all Jamf settings: `6GX8KVTR9H`
- Preference domain: `com.twingate.macos`
- macOS 15 (Sequoia) requires additional "Non-removable system extensions from UI" configuration

## Prerequisites
- Jamf Pro admin access at `<companyName>.jamfcloud.com`
- macOS: Twingate `.pkg` from [download page](https://www.twingate.com/downloads)
- iOS: Apple Business Manager account linked to Jamf
- Existing manually-installed Twingate clients should be removed first

## Step-by-Step: Create Silent Deployment Configuration Profile

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Set display name (e.g., `Twingate Silent Install`)
3. **Application & Custom Settings** → **External Applications** → **Add**
4. Source: **Custom Schema**, preference domain: `com.twingate.macos`
5. Paste JSON schema (see below), click Save
6. Configure settings for silent deployment
7. Add **Managed Login Items**: Team ID `6GX8KVTR9H`
8. Add **Notifications**: App Name `Twingate`, Bundle ID `com.twingate.macos`, Notifications Enabled
9. Add **System Extensions**: Type = Allowed, Team ID `6GX8KVTR9H`, Extension = `com.twingate.macos.tunnelprovider`
10. *(macOS 15+ only)* Add second System Extension entry: Type = Non-removable from UI, same Team ID and extension
11. Add **VPN** configuration (see values below)
12. Set **Scope**, then **Save**

## Configuration Values

### Silent Deployment Schema Settings
| Property | Value |
|---|---|
| `PresentedDataPrivacy` | `true` |
| `PresentedEducation` | `true` |
| `automaticallyInstallSystemExtension` | `true` |
| `network` | Your Twingate network name |
| `LaunchApp` | `false` |
| `SUEnableAutomaticChecks` | `false` |
| `SUAutomaticallyUpdate` | `false` |

### VPN Configuration
| Field | Value |
|---|---|
| Connection Name | `Twingate` |
| VPN Type | `VPN` |
| Connection Type | `Custom SSL` |
| Identifier | `com.twingate.macos` |
| Server | `null` (any non-blank value) |
| Provider Bundle Identifier | `com.twingate.macos.tunnelprovider` |
| Provider Designated Requirement | `anchor apple generic and identifier "com.twingate.macos.tunnelprovider" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "6GX8KVTR9H")` |

## Gotchas
- Pre-existing manually installed clients must be removed before Jamf deployment to avoid version conflicts
- `LaunchApp` should be `false` if using the Twingate Launch Agent
- macOS 15 Sequoia requires the "Non-removable system extensions from UI" step; configuring it on earlier versions is harmless
- Server field in VPN config cannot be blank; any placeholder value works
- Test scope on a small group before full rollout

## Updating the Client
1. Download new PKG, upload to Jamf Pro as new package (same priority as