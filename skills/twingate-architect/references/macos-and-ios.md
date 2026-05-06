# macOS & iOS — Twingate MDM Deployment

## Summary
Twingate clients for macOS and iOS can be deployed and configured via MDM solutions using custom `.mobileconfig` configuration profiles. The Standalone Client (macOS) is preferred over the App Store version as it supports more configuration options. Clients older than 12 months will not connect to the service.

## Key Information
- **macOS**: Standalone App (recommended) or Mac App Store
- **iOS**: App Store only
- Supported MDMs: Kandji, Jamf, Omnissa Workspace ONE
- Config profiles are XML files with `.mobileconfig` extension
- App Store distribution requires Apple Business Manager (ABM) seat provisioning — free but required

## Configuration Values (Profile Keys)

| Key | Type | Description |
|-----|------|-------------|
| `network` | String | Pre-populates Twingate network name at login |
| `PresentedDataPrivacy` | Boolean | Skip privacy screen on first launch |
| `PresentedEducation` | Boolean | Skip education screen on first launch |
| `automaticallyInstallSystemExtension` | Boolean | Auto-install system extension (Standalone only) |
| `LaunchApp` | Boolean | Launch app at login |
| `SUEnableAutomaticChecks` | Boolean | Enable update checks (Standalone only) |
| `SUAutomaticallyUpdate` | Boolean | Auto-download updates and prompt to install (Standalone only) |

**Bundle identifiers:**
- App: `com.twingate.macos`
- Tunnel provider: `com.twingate.macos.tunnelprovider`
- Team ID: `6GX8KVTR9H`
- PayloadType for app config: `com.twingate.macos`

## Prerequisites
- MDM solution enrolled with managed devices
- For App Store distribution: Apple Business Manager account with Twingate seats "purchased"
- Profile creation tool (MDM built-in, iMazing Profile Editor, or ProfileCreator)

## Step-by-Step: Silent Install via MDM
1. Build `.mobileconfig` XML with required payloads (VPN, app config, notifications, background items, system extension policy)
2. Set `automaticallyInstallSystemExtension: true`, `PresentedDataPrivacy: true`, `PresentedEducation: true`
3. Set `network` to your Twingate network name (e.g., `acme`)
4. Upload profile to MDM and deploy alongside Standalone App package

## Gotchas
- **Client expiry**: Clients >12 months old cannot connect — if disabling auto-updates, establish a manual update process
- **LaunchApp conflict**: Set `LaunchApp: false` if using a Twingate Launch Daemon (keep-alive) to avoid conflicts
- **Standalone-only keys**: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate` do not apply to App Store version
- **ABM requirement**: Even though Twingate is free, MDM distribution of App Store version requires ABM seat allocation
- `PayloadRemovalDisallowed: true` in example profile prevents users from removing the config

## Related Docs
- Kandji deployment guide
- Jamf deployment guide
- Omnissa Workspace ONE guide
- Apple Business Manager user guide