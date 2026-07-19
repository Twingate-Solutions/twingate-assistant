# Deploying Twingate Client with Jamf MDM

## Summary
Guide for deploying Twingate macOS and iOS clients via Jamf Pro MDM. Covers package distribution, silent deployment via Custom Configuration Profiles, and client update procedures.

## Key Information
- macOS deployment uses PKG installer uploaded to Jamf
- iOS deployment requires Apple Business Manager linked to Jamf first
- Configuration Profile enables silent/zero-touch deployment
- Preference domain: `com.twingate.macos`
- Team Identifier: `6GX8KVTR9H`
- System extension bundle ID: `com.twingate.macos.tunnelprovider`

## Prerequisites
- Jamf Pro admin access
- macOS: Twingate `.pkg` from [download page](https://www.twingate.com/download)
- iOS: Apple Business Manager linked to Jamf
- Remove any manually installed Twingate clients before deploying via Jamf

## Configuration Profile Setup (Silent Deployment)

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Add **Application & Custom Settings** → **External Applications** → **Custom Schema**
3. Preference domain: `com.twingate.macos`
4. Upload JSON schema (see below)
5. Add **Managed Login Items** with Team ID `6GX8KVTR9H`
6. Add **Notifications**: App Name `Twingate`, Bundle ID `com.twingate.macos`, Enabled
7. Add **System Extensions**: Allowed + Team ID `6GX8KVTR9H`, extension `com.twingate.macos.tunnelprovider`
8. *(macOS 15+ only)* Add second System Extension entry: Non-removable from UI, same Team ID and extension
9. Add **VPN** configuration (see values below)
10. Set **Scope**, then **Save**

## Configuration Values

### Silent Deployment Schema Properties
| Property | Type | Silent Deploy Value |
|---|---|---|
| `PresentedDataPrivacy` | boolean | `true` |
| `PresentedEducation` | boolean | `true` |
| `automaticallyInstallSystemExtension` | boolean | `true` |
| `network` | string | Your Twingate network name |
| `LaunchApp` | boolean | `false` |
| `SUEnableAutomaticChecks` | boolean | `false` |
| `SUAutomaticallyUpdate` | boolean | `false` |

### VPN Profile Values
| Field | Value |
|---|---|
| Connection Name | `Twingate` |
| VPN Type | `VPN` |
| Connection Type | `Custom SSL` |
| Identifier | `com.twingate.macos` |
| Server | `null` (any non-blank value) |
| Provider Bundle Identifier | `com.twingate.macos.tunnelprovider` |
| Provider Designated Requirement | `anchor apple generic and identifier "com.twingate.macos.tunnelprovider" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /* exists */ or certificate 1[field.1.2.840.113635.100.6.2.6] /* exists */ and certificate leaf[field.1.2.840.113635.100.6.1.13] /* exists */ and certificate leaf[subject.OU] = "6GX8KVTR9H")` |

## Updating the Client
1. Download new `.pkg` from Twingate website
2. Upload to Jamf Pro as new package (same priority as previous)
3. Edit policy: remove old package, add new package
4. Test by flushing policy on test device; policy reruns on trigger

## Gotchas
- **Pre-existing manual installs**: Must be removed before Jamf rollout or version conflicts occur; use a temporary removal policy
- **macOS 15 (Sequoia)**: Requires additional "Non-removable system extensions from UI" entry — configuring it won't break earlier macOS versions
- **LaunchApp**: Set to `false` if deploying with Twingate Launch Agent
- **Server field in VPN**: Cannot be blank; use any placeholder value
- Scope to small test