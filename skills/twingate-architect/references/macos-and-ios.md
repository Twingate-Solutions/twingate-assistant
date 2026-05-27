# macOS & iOS Client Distribution via MDM

## Summary
Twingate clients for macOS and iOS can be distributed and configured via MDM solutions (Jamf, Iru/Kandji, Omnissa Workspace ONE) using custom `.mobileconfig` configuration profiles. The Standalone Client is preferred over the App Store version as it supports more configuration options. Silent installation is achievable by deploying a configuration profile alongside the app package.

## Key Information
- macOS: available as Standalone App or Mac App Store
- iOS: available on App Store only
- Clients older than 12 months are unsupported and cannot connect
- Standalone App supports additional keys: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate`
- Profile format: XML `.mobileconfig` file with Apple plist structure

## Prerequisites
- MDM solution (Iru, Jamf, or Omnissa Workspace ONE)
- For App Store distribution: Apple Business Manager account with Twingate seats provisioned (free)
- Tools for profile creation: iMazing Profile Editor or ProfileCreator (optional)

## Configuration Values (Profile Key/Value Pairs)

| Key | Type | Description | Standalone Only |
|-----|------|-------------|-----------------|
| `network` | String | Pre-populates network name (e.g., `acme`) | No |
| `PresentedDataPrivacy` | Boolean | Bypasses Privacy screen on first launch | No |
| `PresentedEducation` | Boolean | Bypasses education screen on first launch | No |
| `automaticallyInstallSystemExtension` | Boolean | Auto-installs system extension | Yes |
| `LaunchApp` | Boolean | Launches app on user login | No |
| `SUEnableAutomaticChecks` | Boolean | Auto-checks for updates | Yes |
| `SUAutomaticallyUpdate` | Boolean | Auto-downloads updates, prompts to install | Yes |

## Critical Identifiers
- **Bundle ID**: `com.twingate.macos`
- **Tunnel Provider Bundle ID**: `com.twingate.macos.tunnelprovider`
- **Team ID**: `6GX8KVTR9H`
- **VPN SubType**: `com.twingate.macos`

## Step-by-Step: Apple Business Manager Distribution
1. Sign in to [Apple Business Manager](https://business.apple.com)
2. Search for "Twingate" and provision desired seat count (free)
3. Seats appear in MDM solution — deploy without requiring personal Apple IDs

## Gotchas
- **Client expiry**: Clients >12 months old stop connecting; if disabling auto-updates, establish a manual update cadence
- **LaunchApp conflict**: Set `LaunchApp: false` if using a Twingate Launch Daemon/keep-alive agent to avoid conflicts
- **Silent install**: Requires deploying the configuration profile *alongside* the Standalone App (not App Store version)
- **PayloadRemovalDisallowed**: Set to `true` in example profile — prevents users from removing the profile
- `SUEnableAutomaticChecks` and `SUAutomaticallyUpdate` only apply to Standalone App, not App Store version

## Related Docs
- Iru (Kandji) MDM Guide
- Jamf MDM Guide
- Omnissa Workspace ONE Guide
- Apple Profile Editor Tutorial