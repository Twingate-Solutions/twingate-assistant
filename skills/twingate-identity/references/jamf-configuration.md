# Jamf Configuration

## Page Title
Jamf Configuration (Twingate Device Integration)

## Summary
Twingate integrates with Jamf Pro to verify macOS device management status as a trust requirement for accessing private resources. The integration uses the Jamf API to match device serial numbers against managed devices, requiring check-in within the last 7 days to be considered verified.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Platform support**: macOS only
- **Verification criteria**: Device must be Jamf-managed AND reported to Jamf within the last 7 days
- **Matching method**: Twingate client reads device serial number and compares against Jamf-managed device list
- **Initial sync delay**: Up to 10 minutes after configuration

## Prerequisites
- Business or Enterprise Twingate plan
- Jamf Pro account with **admin-level credentials** that have API access
- Devices must be managed under your Jamf tenant

## Step-by-Step

1. In Jamf, identify or create a user with admin capabilities and API access
2. In Twingate Admin Console → **Settings** → **Device Integration**
3. Click **Connect** next to Jamf and enter Jamf credentials
4. Verify integration status on the Device Settings page
5. Navigate to **Device Security** → **Trusted Profiles** → create/edit a macOS Trusted Profile
6. Set **Jamf** as a required Trust Method
7. Incorporate the Trusted Profile into Security Policies

## Configuration Values
- **Credentials required**: Jamf admin username/password with API access
- **Sync interval**: Jamf device list is polled periodically (no user-configurable interval)
- **Verification window**: 7-day Jamf check-in required

## Gotchas
- **10-minute initial sync delay**: Devices may show incorrect verification state during this window; Device Settings shows "Waiting to sync"
- **Recoverable errors** (e.g., Jamf API unresponsive): Integration shows last successful sync time + failure time; auto-resolves when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops retrying; admin notified via email; requires manual reconfiguration with new API credentials
- Only macOS devices are supported — no mention of iOS/Windows Jamf management
- The Jamf user account used for integration must retain admin + API permissions; any permission changes will break the integration

## Related Docs
- Device Security / Trusted Profiles (Security Policies configuration)
- Twingate pricing page (plan eligibility)
- Device Integration settings