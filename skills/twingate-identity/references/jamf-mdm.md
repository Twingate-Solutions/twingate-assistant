# Deploying Twingate Client with Jamf MDM

## Summary
Covers deploying Twingate macOS and iOS clients via Jamf Pro using packages, App Store distribution, and Configuration Profiles. Includes silent deployment configuration via custom JSON schema and VPN/system extension profile setup.

## Key Information
- macOS: Deploy via PKG uploaded to Jamf; download from Twingate download page
- iOS: Requires Apple Business Manager linked to Jamf first; distribute via ABM
- Configuration Profile enables silent install by suppressing onboarding screens and pre-filling network name
- Preference domain: `com.twingate.macos`
- Team Identifier: `6GX8KVTR9H`
- Bundle ID: `com.twingate.macos`
- Tunnel provider bundle: `com.twingate.macos.tunnelprovider`
- macOS 15+ requires additional "Non-removable system extensions from UI" configuration

## Prerequisites
- Jamf Pro admin access
- For iOS: Apple Business Manager account linked to Jamf
- Twingate PKG installer (from download page)
- Existing devices manually uninstalled before MDM rollout

## Configuration Values (Silent Deployment Profile)

| Key | Type | Recommended Value |
|-----|------|-------------------|
| `PresentedDataPrivacy` | boolean | `true` |
| `PresentedEducation` | boolean | `true` |
| `automaticallyInstallSystemExtension` | boolean | `true` |
| `network` | string | Your Twingate network name |
| `LaunchApp` | boolean | `false` |
| `SUEnableAutomaticChecks` | boolean | `false` |
| `SUAutomaticallyUpdate` | boolean | `false` |

## Step-by-Step: Create Configuration Profile

1. Navigate to **Computers → Configuration Profiles → New**
2. Set display name (e.g., "Twingate Silent Install")
3. Select **Application & Custom Settings → External Applications → Add**
4. Choose **Custom Schema**, enter domain `com.twingate.macos`
5. Click **Add Schema**, paste JSON schema, save
6. Configure silent deployment values (table above)
7. Add **Managed Login Items** → Team ID: `6GX8KVTR9H`
8. Add **Notifications** → App Name: `Twingate`, Bundle ID: `com.twingate.macos`, enable Notifications
9. Add **System Extensions** → Type: `Allowed system extensions`, Team ID: `6GX8KVTR9H`, add `com.twingate.macos.tunnelprovider`
10. *(macOS 15+ only)* Add second System Extensions entry → Type: `Non-removable system extensions from UI`, same Team ID and bundle
11. Add **VPN** profile:
    - VPN Type: `VPN`, Connection Type: `Custom SSL`
    - Identifier: `com.twingate.macos`
    - Server: `null` (required field, any value)
    - Provider Bundle Identifier: `com.twingate.macos.tunnelprovider`
    - Provider Designated Requirement: *(full certificate string from docs)*
12. Set **Scope**, then **Save**

## Updating the Client
1. Download new PKG from Twingate website
2. Upload to Jamf as new package (match priority of old package)
3. Edit policy: remove old package, add new package
4. Flush policy on test device(s) to validate
5. Policy runs on trigger and updates client

## Gotchas
- Remove manually installed clients **before** MDM rollout to avoid version conflicts
- `LaunchApp: false` required if using Twingate Launch Agent
- macOS 15 non-removable extension config won't break earlier macOS versions but won't retroactively apply post-upgrade
- VPN Server field cannot be blank; use any placeholder value
- Scope to test group first before org-wide deployment

## Related Docs
- macOS & iOS Client configuration options (full options list)
- Twingate Launch Agent deployment
- Jamf official package deployment documentation
- Apple Business Manager + Jamf integration guide