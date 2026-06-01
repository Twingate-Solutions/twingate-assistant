# macOS & iOS — Twingate MDM Deployment

## Summary
Twingate clients for macOS and iOS can be distributed and configured via MDM solutions (Jamf, Kandji/Iru, Omnissa Workspace ONE). Configuration profiles (`.mobileconfig` XML) enable silent installs, pre-populated network names, and suppressed onboarding screens. Standalone App is preferred over Mac App Store version for full feature support.

## Key Information
- macOS: Standalone App or Mac App Store; iOS: App Store only
- Clients older than 12 months are unsupported and cannot connect
- Standalone App supports more config options (`automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate`)
- Apple Business Manager (ABM) required to distribute App Store version via MDM without personal Apple IDs

## Configuration Values (Profile Manifest Keys)

| Key | Type | Description |
|-----|------|-------------|
| `network` | String | Pre-populate network name |
| `PresentedDataPrivacy` | Boolean | Skip privacy screen on first launch |
| `PresentedEducation` | Boolean | Skip education screen on first launch |
| `automaticallyInstallSystemExtension` | Boolean | Auto-install system extension *(standalone only)* |
| `LaunchApp` | Boolean | Launch on login (set `false` if using keep-alive daemon) |
| `SUEnableAutomaticChecks` | Boolean | Auto-check for updates *(standalone only)* |
| `SUAutomaticallyUpdate` | Boolean | Auto-download updates and prompt install *(standalone only)* |

**Key identifiers:**
- Bundle ID: `com.twingate.macos`
- Tunnel provider: `com.twingate.macos.tunnelprovider`
- Team ID: `6GX8KVTR9H`
- PayloadType for app config: `com.twingate.macos`

## Prerequisites
- MDM solution (Jamf, Iru/Kandji, or Omnissa Workspace ONE)
- For App Store distribution: Apple Business Manager account with provisioned (free) seats
- Supervised/managed devices

## Step-by-Step: ABM Distribution
1. Sign in to Apple Business Manager with company Apple ID
2. Search "Twingate" and provision required number of seats (free)
3. Seats appear in MDM solution for deployment without user Apple ID

## Gotchas
- **`LaunchApp` conflict**: Set to `false` if deploying with a keep-alive launch daemon to avoid duplicate launch behavior
- **Managed update responsibility**: If disabling `SUEnableAutomaticChecks`, you must maintain a manual update process — clients >12 months old stop working
- **Standalone-only keys**: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate` do not apply to App Store version
- `PayloadRemovalDisallowed: true` in example profile prevents users from removing the config

## Related Docs
- Jamf MDM guide
- Iru (Kandji) MDM guide
- Omnissa Workspace ONE guide
- [iMazing Profile Editor](https://imazing.com/profile-editor) / [ProfileCreator](https://github.com/ProfileCreator/ProfileCreator) for building `.mobileconfig` files