# macOS & iOS Client Distribution via MDM

## Summary
Twingate clients for macOS and iOS can be deployed and configured via MDM solutions (Iru/Kandji, Jamf, Omnissa Workspace ONE) using custom `.mobileconfig` configuration profiles. The Standalone Client is preferred over the App Store version as it supports more features. Silent install is achievable by deploying a configuration profile alongside the app.

## Key Information
- macOS: Available as Standalone App or Mac App Store
- iOS: Available on App Store only
- Clients older than 12 months are unsupported and cannot connect
- Standalone App supports additional config keys: `automaticallyInstallSystemExtension`, `SUEnableAutomaticChecks`, `SUAutomaticallyUpdate`
- Profile manifest (JSON schema) available for Jamf integration
- Apple Business Manager (ABM) required to distribute App Store version via MDM without personal Apple IDs

## Prerequisites
- MDM solution (Iru, Jamf, or Omnissa Workspace ONE)
- For App Store distribution: Apple Business Manager account with "purchased" (free) Twingate seats
- Tools for profile creation: iMazing Profile Editor or ProfileCreator (optional)

## Configuration Values (Profile Key/Value Pairs)

| Key | Type | Description | Standalone Only |
|-----|------|-------------|----------------|
| `network` | String | Pre-populates Twingate network name | No |
| `PresentedDataPrivacy` | Boolean | `true` bypasses privacy screen on first launch | No |
| `PresentedEducation` | Boolean | `true` bypasses education screen on first launch | No |
| `automaticallyInstallSystemExtension` | Boolean | `true` auto-installs system extension | Yes |
| `LaunchApp` | Boolean | `true` launches app on login | No |
| `SUEnableAutomaticChecks` | Boolean | `true` enables automatic update checks | Yes |
| `SUAutomaticallyUpdate` | Boolean | `true` auto-downloads updates and prompts install | Yes |

**Key identifiers:**
- App bundle ID: `com.twingate.macos`
- Tunnel provider: `com.twingate.macos.tunnelprovider`
- Team ID: `6GX8KVTR9H`

## Step-by-Step: Apple Business Manager Distribution
1. Sign in to Apple Business Manager with company Apple ID
2. Search for "Twingate" and provision seats (free)
3. Seats appear in MDM solution for deployment without user Apple IDs

## Gotchas
- `LaunchApp: true` conflicts with the Twingate Launch Agent/keep-alive daemon — set to `false` if using the daemon
- Disable `SUEnableAutomaticChecks` on fully managed devices and implement a manual update process to avoid clients aging past 12 months
- `automaticallyInstallSystemExtension` is Standalone App only; not applicable to App Store version
- Must generate unique UUIDs for `PayloadUUID` and `PayloadIdentifier` fields in custom profiles
- App Store version requires ABM seat "purchase" before MDM distribution is possible

## Related Docs
- Iru (Kandji) MDM Guide
- Jamf MDM Guide
- Omnissa Workspace ONE Guide
- Apple Business Manager User Guide