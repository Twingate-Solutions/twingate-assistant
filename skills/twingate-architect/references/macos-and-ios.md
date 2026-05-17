# macOS & iOS Twingate Client — MDM Deployment

## Summary
Twingate clients for macOS and iOS can be distributed and configured via MDM solutions (Kandji, Jamf, Omnissa Workspace ONE) using custom `.mobileconfig` configuration profiles. The Standalone App is preferred over the App Store version as it supports more configuration options. Clients older than 12 months cannot connect to the service.

## Key Information
- **macOS**: Available as Standalone App or Mac App Store
- **iOS**: Available on App Store only
- Standalone App supports additional keys: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate`
- Profile format: XML `.mobileconfig` file
- Tools for building profiles: iMazing Profile Editor, ProfileCreator

## Configuration Values (Profile Key/Value Pairs)

| Key | Type | Description | Standalone Only |
|-----|------|-------------|-----------------|
| `PresentedDataPrivacy` | Boolean | Bypass privacy screen on first launch | No |
| `PresentedEducation` | Boolean | Bypass education screen on first launch | No |
| `automaticallyInstallSystemExtension` | Boolean | Auto-install system extension | Yes |
| `network` | String | Pre-populate Twingate network name | No |
| `LaunchApp` | Boolean | Launch app on login | No |
| `SUEnableAutomaticChecks` | Boolean | Auto-check for updates | Yes |
| `SUAutomaticallyUpdate` | Boolean | Auto-download updates and prompt install | Yes |

## Critical Identifiers
- **Bundle ID**: `com.twingate.macos`
- **Tunnel Provider Bundle ID**: `com.twingate.macos.tunnelprovider`
- **Team ID**: `6GX8KVTR9H`
- **VPN Subtype**: `com.twingate.macos`

## Apple Business Manager (ABM) Distribution Steps
1. Sign into Apple Business Manager with company Apple ID
2. Search "Twingate" and provision seats (free, no cost)
3. Seats appear in MDM solution for distribution without personal Apple IDs

## Gotchas
- **`LaunchApp` conflict**: Set to `false` if deploying with Twingate Launch Agent/keep-alive launch daemon to avoid conflict
- **Managed update process required**: If disabling `SUEnableAutomaticChecks`, ensure a manual update process exists — clients >12 months old stop working
- **ABM required for App Store MDM distribution**: Even though Twingate is free, seats must be "purchased" via ABM before MDM can distribute it
- **`PayloadRemovalDisallowed: true`** in example profile prevents users from removing the profile

## Related Docs
- Kandji MDM Guide
- Jamf MDM Guide
- Omnissa Workspace ONE Guide
- Apple configuration profile tutorial (developer.apple.com)