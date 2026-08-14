---
source: https://www.twingate.com/docs/macos-and-ios
type: docs
fetched: 2026-08-14
source_version: f21b9524372ee6ba750147da325dc6890c50f93c295fd427064da7d6836e95eb
---

# macOS & iOS Client Distribution via MDM

## Summary
Twingate clients for macOS and iOS can be distributed and configured via MDM solutions (Iru, Jamf, Omnissa Workspace ONE) using custom `.mobileconfig` configuration profiles. The Standalone Client is preferred over App Store version for full feature availability. Clients older than 12 months are unsupported and cannot connect.

## Key Information
- macOS: Available as Standalone App or Mac App Store; iOS: App Store only
- Standalone Client recommended—enables system extension auto-install, auto-update controls
- Configuration profiles are XML `.mobileconfig` files deployed via MDM
- Tools for building profiles: iMazing Profile Editor, ProfileCreator, or MDM-native tools
- Apple Business Manager (ABM) required to distribute App Store version without personal Apple IDs

## Prerequisites
- MDM solution (Iru, Jamf, or Omnissa Workspace ONE)
- For ABM distribution: company Apple Business Manager account
- For Standalone: direct download/deployment outside App Store

## Configuration Values (Profile Key/Value Pairs)

| Key | Type | Description | Standalone Only |
|-----|------|-------------|-----------------|
| `network` | String | Pre-populates Twingate network name (e.g., `acme`) | No |
| `PresentedDataPrivacy` | Boolean | `true` = bypass Privacy screen on first launch | No |
| `PresentedEducation` | Boolean | `true` = bypass education screen on first launch | No |
| `automaticallyInstallSystemExtension` | Boolean | `true` = auto-install system extension | Yes |
| `LaunchApp` | Boolean | `true` = launch on login | No |
| `SUEnableAutomaticChecks` | Boolean | `true` = auto-check for updates | Yes |
| `SUAutomaticallyUpdate` | Boolean | `true` = auto-download updates, prompt to install | Yes |

**Key identifiers:**
- App Bundle ID: `com.twingate.macos`
- Tunnel Provider: `com.twingate.macos.tunnelprovider`
- Team ID: `6GX8KVTR9H`

## Apple Business Manager Distribution Steps
1. Sign in to Apple Business Manager with company Apple ID
2. Search "Twingate" and provision required seats (free)
3. Allocated seats appear in MDM for device deployment—no personal Apple ID required from users

## Gotchas
- **`LaunchApp` conflict**: Set to `false` if using a keep-alive launch daemon to avoid conflicts
- **`SUEnableAutomaticChecks`/`SUAutomaticallyUpdate`**: Standalone only—not available for App Store version
- **`automaticallyInstallSystemExtension`**: Standalone only
- **Client expiry**: Clients >12 months old stop working; if disabling auto-updates, establish a manual update process
- UUIDs in example profile must be replaced with unique values per deployment (use `uuidgen`)

## Related Docs
- [Iru (Kandji) MDM Guide]
- [Jamf MDM Guide]
- [Omnissa Workspace ONE Guide]
- [Apple Configuration Profile Tutorial](https://developer.apple.com)