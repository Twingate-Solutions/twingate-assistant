# macOS & iOS Twingate Client - MDM Distribution & Configuration

## Summary
Twingate clients for macOS and iOS can be distributed and configured via MDM solutions (Jamf, Kandji/Iru, Omnissa Workspace ONE). Configuration is handled through `.mobileconfig` XML profiles with key/value pairs to pre-populate settings and enable silent installs. Standalone App is recommended over App Store version for full feature access.

## Key Information
- macOS: Standalone App (recommended) or Mac App Store
- iOS: App Store only
- Clients older than 12 months are unsupported and cannot connect
- Bundle ID (app): `com.twingate.macos`
- Bundle ID (tunnel provider): `com.twingate.macos.tunnelprovider`
- Team Identifier: `6GX8KVTR9H`
- Profile tools: iMazing Profile Editor, ProfileCreator, or MDM-native tools

## Configuration Key/Value Pairs (Standalone App)

| Key | Type | Description |
|-----|------|-------------|
| `network` | String | Pre-populates Twingate network name |
| `PresentedDataPrivacy` | Boolean | `true` bypasses privacy screen on first launch |
| `PresentedEducation` | Boolean | `true` bypasses education screen on first launch |
| `automaticallyInstallSystemExtension` | Boolean | `true` auto-installs system extension (standalone only) |
| `LaunchApp` | Boolean | `true` launches on login; set `false` if using keep-alive launch daemon |
| `SUEnableAutomaticChecks` | Boolean | `true` enables auto update checks (standalone only) |
| `SUAutomaticallyUpdate` | Boolean | `true` auto-downloads updates and prompts install (standalone only) |

## Profile Payload Types Required for Silent Install
1. `com.apple.vpn.managed` — VPN configuration
2. `com.twingate.macos` — App-specific settings
3. `com.apple.notificationsettings` — Enable notifications
4. `com.apple.servicemanagement` — Background items (TeamID: `6GX8KVTR9H`)
5. `com.apple.system-extension-policy` — Allow system extension

## Apple Business Manager (ABM) Distribution
1. Sign in to Apple Business Manager
2. Search "Twingate" and provision seats (free)
3. Allocated seats appear in MDM for deployment without user Apple ID sign-in

## Gotchas
- **Version expiry**: Clients >12 months old stop working — if disabling auto-updates, implement a manual update process
- **LaunchApp conflict**: Set `LaunchApp: false` when using the keep-alive launch daemon to avoid conflicts
- `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, and `SUAutomaticallyUpdate` are **standalone app only**
- `PayloadRemovalDisallowed: true` in example profile — prevents users from removing the profile
- Must "purchase" free ABM seats before MDM can distribute App Store version

## Related Docs
- Iru (Kandji) MDM guide
- Jamf MDM guide
- Omnissa Workspace ONE guide
- Apple configuration profile tutorial (apple.com)