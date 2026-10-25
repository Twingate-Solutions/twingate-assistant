---
source: https://www.twingate.com/docs/macos-and-ios
type: docs
fetched: 2026-10-25
source_version: 4d82aceebf989d2b9d0f51094ac297b1fa256b3b4ed51d139387b870be4d933e
trust: official
---

# macOS & iOS Twingate Client — MDM Distribution & Configuration

## Page Title
macOS & iOS — Distribution & Configuration via MDM

## Summary
Covers deploying the Twingate macOS (standalone PKG) and iOS clients to managed devices via MDM solutions. Includes custom configuration profile (`.mobileconfig`) structure for silent installs and pre-configuration, plus Apple Business Manager guidance for iOS distribution.

## Key Information
- **macOS**: Standalone PKG only — Mac App Store version is **no longer supported**
- **iOS**: Available free on the App Store; distribute via Apple Business Manager (ABM)
- Clients older than **12 months** are unsupported and cannot connect
- If disabling auto-updates on managed devices, establish a manual update cadence
- MDM-specific guides exist for: **Iru (Kandji)**, **Jamf**, **Omnissa Workspace ONE**

## Prerequisites
- MDM solution capable of deploying PKG (macOS) or ABM-linked apps (iOS)
- For iOS ABM distribution: company Apple Business Manager account; "purchase" free Twingate seats before deployment

## Configuration Values — Profile Manifest Keys (`com.twingate.macos`)

| Key | Type | Description |
|-----|------|-------------|
| `PresentedDataPrivacy` | Boolean | `true` = bypass Privacy screen on first launch |
| `PresentedEducation` | Boolean | `true` = bypass Education screen on first launch |
| `automaticallyInstallSystemExtension` | Boolean | `true` = auto-install system extension (standalone only) |
| `network` | String | Pre-populates Twingate network name (e.g., `acme`) |
| `LaunchApp` | Boolean | `true` = launch on login; set `false` if using keep-alive launch daemon |
| `SUEnableAutomaticChecks` | Boolean | `true` = auto-check for updates (standalone only) |
| `SUAutomaticallyUpdate` | Boolean | `true` = auto-download updates and prompt to install (standalone only) |

**Key identifiers:**
- App bundle ID: `com.twingate.macos`
- Tunnel provider bundle ID: `com.twingate.macos.tunnelprovider`
- Team ID: `6GX8KVTR9H`
- VPN subtype: `com.twingate.macos`

## Step-by-Step: Silent Install via Configuration Profile
1. Create a `.mobileconfig` XML file with payloads for: VPN config, app settings, notifications, background items, and system extension policy (see full example in source docs)
2. Set `automaticallyInstallSystemExtension: true`, `PresentedDataPrivacy: true`, `PresentedEducation: true`
3. Set `network` to your Twingate network subdomain
4. Upload and deploy via MDM alongside the standalone PKG

## Step-by-Step: iOS via Apple Business Manager
1. Sign in to [Apple Business Manager](https://business.apple.com)
2. Search "Twingate" and provision desired number of seats (free)
3. Seats appear in your MDM — push app to managed devices without requiring personal Apple IDs

## Gotchas
- Do **not** use the Mac App Store version — it is unsupported; use the standalone PKG
- If using a keep-alive launch daemon, set `LaunchApp: false` to avoid conflicts
- `SUEnableAutomaticChecks` and `SUAutomaticallyUpdate` apply to standalone client only
- Profile tools: [iMazing Profile Editor](https://imazing.com/profile-editor), [ProfileCreator](https://github.com/ProfileCreator/ProfileCreator)

## Related Docs
- Iru (Kandji) MDM guide
- Jamf MDM guide
- Omnissa Workspace ONE guide
- Twingate download page (standalone PKG)