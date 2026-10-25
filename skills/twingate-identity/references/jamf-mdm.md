---
source: https://www.twingate.com/docs/jamf-mdm
type: docs
fetched: 2026-10-25
source_version: dbfabf0199806efc8973bb00ac168fc3e5bfd716da5b5399b83ec7e669e95efa
trust: official
---

# Deploying Twingate macOS and iOS Clients with Jamf

## Summary
Covers distributing the Twingate Client via Jamf MDM for macOS (PKG-based) and iOS (App Store via Apple Business Manager). Includes creating a Jamf Configuration Profile for silent deployments with system extension, VPN, and notification settings pre-configured.

## Key Information
- Mac App Store version is **no longer supported**; use the standalone PKG from the Twingate download page
- iOS distribution requires linking Jamf to Apple Business Manager first
- Twingate Team Identifier: `6GX8KVTR9H`
- Main bundle ID: `com.twingate.macos`
- Tunnel provider bundle ID: `com.twingate.macos.tunnelprovider`
- Preference domain: `com.twingate.macos`

## Prerequisites
- macOS: Twingate `.pkg` downloaded from Twingate download page
- iOS: Twingate added to Apple Business Manager; Jamf linked to ABM
- Jamf Pro admin console access

## Configuration Profile – Step-by-Step (Silent Deployment)

1. Jamf Pro → **Computers** → **Configuration Profiles** → **New**
2. Set display name (e.g., `Twingate Silent Install`)
3. **Application & Custom Settings** → **External Applications** → **Add**
4. Source: **Custom Schema**; Preference domain: `com.twingate.macos`
5. Paste JSON schema (see below) → Save

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

6. **Managed Login Items** → Team Identifier: `6GX8KVTR9H`
7. **Notifications** → Add: App Name `Twingate`, Bundle ID `com.twingate.macos`, Notifications **Enabled**
8. **System Extensions** → Configure:
   - Type: `Allowed system extensions`; Team ID: `6GX8KVTR9H`
   - Allowed extension: `com.twingate.macos.tunnelprovider`
   - *(macOS 15+ only)* Add second entry: Type `Non-removable system extensions from UI`, same Team ID and extension
9. **VPN** → Configure:

| Field | Value |
|-------|-------|
| Connection Name | `Twingate` |
| VPN Type | `VPN` |
| Connection Type | `Custom SSL` |
| Identifier | `com.twingate.macos` |
| Server | `null` (any non-blank value) |
| Provider Bundle Identifier | `com.twingate.macos.tunnelprovider` |
| Provider Designated Requirement | *(see full anchor string in source docs)* |

10. Set **Scope** (test group first) → **Save**

## Updating the Client
1. Download latest PKG from Twingate website
2. Upload to Jamf Pro as a new package (match priority of previous)
3. Edit policy: remove old package, add new package
4. Test by flushing policy on specific device(s) via policy logs

## Gotchas
- Remove manually installed clients **before** rolling out Jamf distribution; version mismatches cause issues — use a temporary removal policy
- macOS 15 (Sequoia) requires the additional **Non-removable system extensions** entry; configuring it on earlier versions is harmless
- Set `LaunchApp: false` if using the Twingate Launch Agent instead
- VPN `Server` field cannot be blank; use any placeholder value

## Related Docs
- [macOS & iOS configuration options](https://www.twingate.com/docs/macos-ios) — full list of MDM-manageable keys
- Twingate download page — latest PKG
- Jamf official docs — package