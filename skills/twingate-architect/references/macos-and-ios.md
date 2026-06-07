# macOS & iOS Twingate Client — MDM Deployment

## Summary
Twingate clients for macOS and iOS can be deployed and configured via MDM solutions using custom `.mobileconfig` configuration profiles. The Standalone Client (macOS) is preferred over the App Store version as it supports more configuration options. Clients older than 12 months are unsupported and cannot connect.

## Key Information
- **macOS**: Available as Standalone App or Mac App Store app
- **iOS**: Available on App Store only
- Supported MDMs: Iru (formerly Kandji), Jamf, Omnissa Workspace ONE
- Standalone App exposes additional keys: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate`
- Profile format: XML `.mobileconfig` file; tools like iMazing Profile Editor or ProfileCreator can assist creation

## Configuration Keys (com.twingate.macos payload)

| Key | Type | Description |
|-----|------|-------------|
| `network` | String | Pre-populates Twingate network name at login |
| `PresentedDataPrivacy` | Boolean | `true` = skip privacy screen on first launch |
| `PresentedEducation` | Boolean | `true` = skip education screen on first launch |
| `automaticallyInstallSystemExtension` | Boolean | `true` = auto-install system extension *(Standalone only)* |
| `LaunchApp` | Boolean | `true` = launch on login; set `false` if using keep-alive launch daemon |
| `SUEnableAutomaticChecks` | Boolean | `true` = auto-check for updates *(Standalone only)* |
| `SUAutomaticallyUpdate` | Boolean | `true` = auto-download updates and prompt to install *(Standalone only)* |

## Bundle Identifiers
- Main app: `com.twingate.macos`
- Tunnel provider: `com.twingate.macos.tunnelprovider`
- Team ID: `6GX8KVTR9H`

## Silent Install Profile Requirements
The example profile includes five payloads:
1. `com.apple.vpn.managed` — VPN configuration
2. `com.twingate.macos` — App settings (network name, extension install, update checks)
3. `com.apple.notificationsettings` — Enable notifications
4. `com.apple.servicemanagement` — Allow background items (TeamID: `6GX8KVTR9H`)
5. `com.apple.system-extension-policy` — Allow system extension

## Apple Business Manager (ABM) Distribution
1. Sign in to Apple Business Manager with company Apple ID
2. Search "Twingate" and provision seats (free)
3. Allocated seats appear in MDM for deployment without user Apple ID sign-in

## Gotchas
- `LaunchApp: true` conflicts with keep-alive launch daemon — set to `false` if using the daemon
- `SUEnableAutomaticChecks` and `SUAutomaticallyUpdate` only apply to Standalone App, not App Store version
- If managing updates manually, disable auto-checks and establish a regular update cadence — clients older than 12 months stop working
- `PayloadRemovalDisallowed: true` in the example profile prevents users from removing the profile

## Related Docs
- Jamf MDM guide
- Iru (Kandji) MDM guide
- Omnissa Workspace ONE guide
- Twingate Launch Agent/Daemon configuration