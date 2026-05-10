# Deploying Twingate Client with Jamf MDM

## Summary
Guide for distributing the Twingate macOS and iOS clients via Jamf Pro MDM. Covers package deployment, silent installation via Custom Configuration Profiles, and client update procedures.

## Key Information
- macOS deployment uses a PKG file uploaded to Jamf
- iOS deployment requires Apple Business Manager linked to Jamf
- Configuration Profile preference domain: `com.twingate.macos`
- Team Identifier: `6GX8KVTR9H`
- System extension bundle ID: `com.twingate.macos.tunnelprovider`
- macOS 15 (Sequoia)+ requires additional "Non-removable system extensions from UI" configuration

## Prerequisites
- Jamf Pro admin access
- macOS: Twingate `.pkg` from [download page](https://www.twingate.com/docs/downloads)
- iOS: Apple Business Manager linked to Jamf
- Remove any manually installed Twingate clients before MDM rollout

## Configuration Profile Values

| Property Key | Type | Silent Deploy Value |
|---|---|---|
| `PresentedDataPrivacy` | boolean | `true` |
| `PresentedEducation` | boolean | `true` |
| `automaticallyInstallSystemExtension` | boolean | `true` |
| `network` | string | Your network name |
| `LaunchApp` | boolean | `false` |
| `SUEnableAutomaticChecks` | boolean | `false` |
| `SUAutomaticallyUpdate` | boolean | `false` |

## Step-by-Step: Silent Deployment Profile

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Set display name (e.g., `Twingate Silent Install`)
3. **Application & Custom Settings** → **External Applications** → **Add**
4. Source: **Custom Schema**; Preference domain: `com.twingate.macos`
5. Paste provided JSON schema; configure boolean/string values per table above
6. Add **Managed Login Items** → Team ID: `6GX8KVTR9H`
7. Add **Notifications**: App Name `Twingate`, Bundle ID `com.twingate.macos`, Notifications Enabled
8. Add **System Extensions** → Allowed system extensions, Team ID `6GX8KVTR9H`, extension: `com.twingate.macos.tunnelprovider`
9. *(macOS 15+ only)* Add second System Extensions entry → **Non-removable system extensions from UI**, same Team ID and extension
10. Add **VPN** configuration:
    - VPN Type: `VPN`, Connection Type: `Custom SSL`
    - Identifier: `com.twingate.macos`
    - Provider Bundle ID: `com.twingate.macos.tunnelprovider`
    - Server: any non-blank value (e.g., `null`)
    - Provider Designated Requirement: (full certificate anchor string per docs)
11. Set **Scope** to test group first, then **Save**

## Updating the Client

1. Download new PKG from Twingate website
2. Upload to Jamf Pro as new package (same priority as previous)
3. Edit existing policy: remove old package, add new package
4. Test by flushing policy on specific device; policy re-runs on trigger

## Gotchas
- Manually installed clients must be removed before Jamf rollout to avoid version conflicts — use a temporary removal policy
- macOS 15 Sequoia requires the "Non-removable system extensions" entry; configuring it on pre-15 devices is harmless
- `LaunchApp` should be `false` if using a Twingate Launch Agent
- VPN Server field cannot be blank — use any placeholder value

## Related Docs
- [macOS & iOS Client configuration options](https://www.twingate.com/docs/macos-ios)
- Jamf official package deployment documentation
- Apple Business Manager + Jamf linking guide