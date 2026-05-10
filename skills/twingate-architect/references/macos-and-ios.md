# macOS & iOS – Twingate MDM Distribution & Configuration

## Summary
Twingate Client for macOS and iOS can be distributed and configured via MDM solutions (Kandji, Jamf, Omnissa Workspace ONE) using custom `.mobileconfig` configuration profiles. The Standalone Client is preferred over the App Store version for full feature availability, including system extension auto-install and automatic update controls.

## Key Information
- **macOS**: Available as Standalone App or Mac App Store
- **iOS**: Available on App Store only
- Clients older than 12 months are unsupported and cannot connect
- Profile format: XML `.mobileconfig` file with Apple plist structure
- Bundle IDs: `com.twingate.macos` (app), `com.twingate.macos.tunnelprovider` (tunnel)
- Team Identifier: `6GX8KVTR9H`

## Prerequisites
- MDM solution (Kandji, Jamf, or Workspace ONE)
- For App Store distribution: Apple Business Manager (ABM) account with "purchased" Twingate seats
- Standalone App required for: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate`

## Configuration Values (Profile Key/Value Pairs)

| Key | Type | Description | Standalone Only |
|-----|------|-------------|-----------------|
| `network` | String | Pre-populates network name (e.g., `acme`) | No |
| `PresentedDataPrivacy` | Boolean | `true` bypasses privacy screen on first launch | No |
| `PresentedEducation` | Boolean | `true` bypasses education screen on first launch | No |
| `automaticallyInstallSystemExtension` | Boolean | `true` auto-installs system extension | Yes |
| `LaunchApp` | Boolean | `true` launches app on login | No |
| `SUEnableAutomaticChecks` | Boolean | `true` enables auto update checks | Yes |
| `SUAutomaticallyUpdate` | Boolean | `true` auto-downloads updates, prompts to install | Yes |

## Profile Payload Types Required for Silent Install
1. `com.apple.vpn.managed` – VPN configuration
2. `com.twingate.macos` – App-specific settings
3. `com.apple.notificationsettings` – Enable notifications
4. `com.apple.servicemanagement` – Background items (TeamID: `6GX8KVTR9H`)
5. `com.apple.system-extension-policy` – Allow system extension

## Apple Business Manager Distribution Steps
1. Sign in to Apple Business Manager with company Apple ID
2. Search "Twingate" and provision seats (free)
3. Seats appear in MDM; deploy without requiring user personal Apple IDs

## Gotchas
- **`LaunchApp` conflict**: Set to `false` if using a Twingate Launch Daemon/keep-alive agent to avoid duplicate launch
- **Managed update process**: If disabling `SUEnableAutomaticChecks`, you must maintain a manual update process — clients older than 12 months stop working entirely
- `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, and `SUAutomaticallyUpdate` only apply to the **Standalone App**, not the App Store version
- `PayloadRemovalDisallowed: true` in the example profile prevents users from removing the configuration

## Related Docs
- Kandji MDM Guide
- Jamf MDM Guide
- Omnissa Workspace ONE Guide
- [iMazing Profile Editor](https://imazing.com/profile-editor) / [ProfileCreator](https://github.com/ProfileCreator/ProfileCreator) for building profiles