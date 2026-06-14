# macOS & iOS Client Distribution via MDM

## Summary
Twingate clients for macOS and iOS can be distributed and configured via MDM solutions (Jamf, Iru, Omnissa Workspace ONE) using custom `.mobileconfig` configuration profiles. The Standalone Client is preferred over the App Store version as it supports more configuration options. Clients older than 12 months cannot connect and must be kept updated.

## Key Information
- macOS: Available as Standalone App or Mac App Store
- iOS: Available on App Store only
- Supported MDMs: Iru (formerly Kandji), Jamf, Omnissa Workspace ONE
- Configuration profiles are XML `.mobileconfig` files
- Profile tools: iMazing Profile Editor, ProfileCreator
- Standalone App required for: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate`

## Configuration Values (Profile Key/Value Pairs)

| Key | Type | Description |
|-----|------|-------------|
| `PresentedDataPrivacy` | Boolean | `true` bypasses privacy screen on first launch |
| `PresentedEducation` | Boolean | `true` bypasses education screen on first launch |
| `automaticallyInstallSystemExtension` | Boolean | `true` auto-installs system extension *(Standalone only)* |
| `network` | String | Pre-populates Twingate network name (e.g., `acme`) |
| `LaunchApp` | Boolean | `true` launches app at login; set `false` if using launch daemon |
| `SUEnableAutomaticChecks` | Boolean | `true` enables auto update checks *(Standalone only)* |
| `SUAutomaticallyUpdate` | Boolean | `true` auto-downloads updates and prompts install *(Standalone only)* |

## Critical Identifiers (for profile construction)
- **App Bundle ID**: `com.twingate.macos`
- **Tunnel Provider Bundle ID**: `com.twingate.macos.tunnelprovider`
- **Team Identifier**: `6GX8KVTR9H`
- **VPN SubType**: `com.twingate.macos`

## Apple Business Manager (ABM) Distribution
1. Sign in to Apple Business Manager with company Apple ID
2. Search "Twingate" and provision seats (free, no cost)
3. Allocated seats appear in MDM for push-install without user Apple ID

## Gotchas
- **Client expiry**: Clients >12 months old lose connectivity — if disabling auto-updates, implement a manual update process
- **LaunchApp conflict**: Set `LaunchApp: false` if deploying with a keep-alive launch daemon to avoid conflicts
- **Silent install**: Requires deploying the Standalone App alongside the `.mobileconfig` profile with `automaticallyInstallSystemExtension: true`, `PresentedDataPrivacy: true`, `PresentedEducation: true`
- **ABM required**: App Store version requires "purchasing" free seats in ABM before MDM distribution; users won't need personal Apple IDs
- **`SUEnableAutomaticChecks: false`** recommended for fully managed devices (pair with manual update process)

## Related Docs
- Iru (Kandji) MDM Guide
- Jamf MDM Guide
- Omnissa Workspace ONE Guide
- Twingate Launch Agent (keep-alive daemon)