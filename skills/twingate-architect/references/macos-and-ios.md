# macOS & iOS Client Distribution via MDM

## Page Title
macOS & iOS Client Configuration and MDM Distribution

## Summary
Twingate clients for macOS and iOS can be deployed and configured via MDM solutions using custom `.mobileconfig` configuration profiles. The Standalone Client is preferred over the App Store version for full feature availability. Clients older than 12 months are unsupported and cannot connect.

## Key Information
- macOS: Available as Standalone App or Mac App Store; iOS: App Store only
- Supported MDMs: Iru (formerly Kandji), Jamf, Omnissa Workspace ONE
- Configuration profiles are XML `.mobileconfig` files deployed via MDM
- Apple Business Manager (ABM) required for MDM distribution without personal Apple IDs

## Prerequisites
- MDM solution (Iru, Jamf, or Workspace ONE)
- For ABM distribution: company Apple Business Manager account
- For profile creation: iMazing Profile Editor or ProfileCreator (optional tools)

## Configuration Values (Key/Value Pairs)

| Key | Type | Description |
|-----|------|-------------|
| `network` | String | Pre-populates Twingate network name |
| `PresentedDataPrivacy` | Boolean | `true` bypasses Privacy screen on first launch |
| `PresentedEducation` | Boolean | `true` bypasses education screen on first launch |
| `automaticallyInstallSystemExtension` | Boolean | `true` auto-installs system extension *(standalone only)* |
| `LaunchApp` | Boolean | `true` launches app at login |
| `SUEnableAutomaticChecks` | Boolean | `true` enables auto update checks *(standalone only)* |
| `SUAutomaticallyUpdate` | Boolean | `true` auto-downloads updates and prompts install *(standalone only)* |

**Critical identifiers:**
- Bundle ID: `com.twingate.macos`
- Tunnel provider: `com.twingate.macos.tunnelprovider`
- Team ID: `6GX8KVTR9H`

## Step-by-Step: Apple Business Manager Distribution
1. Sign in to [Apple Business Manager](https://business.apple.com) with company Apple ID
2. Search "Twingate" and provision required number of seats (free)
3. Seats appear in MDM solution for deployment without user Apple IDs

## Gotchas
- `SUEnableAutomaticChecks` and `SUAutomaticallyUpdate` are **Standalone App only** — not available for App Store version
- If using the keep-alive launch daemon, set `LaunchApp` to `false` to avoid conflicts
- Clients >12 months old **cannot connect** — establish update process if disabling auto-updates
- `PayloadRemovalDisallowed: true` in the example profile prevents users from removing it
- `automaticallyInstallSystemExtension` is standalone only

## Related Docs
- Iru (Kandji) MDM guide
- Jamf MDM guide
- Omnissa Workspace ONE guide
- Twingate Launch Agent documentation