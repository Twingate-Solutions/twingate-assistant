# Jamf Configuration

## Page Title
Jamf Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Jamf to verify macOS device management status as part of Device Security policies. The integration uses the Jamf API to match device serial numbers against managed devices in a Jamf tenant. Devices must be Jamf-managed and have reported to Jamf within the last 7 days to be considered verified.

## Key Information
- **Platform support**: macOS only
- **Verification criteria**: Device must be Jamf-managed AND reported to Jamf within last 7 days
- **Plan requirement**: Business & Enterprise plans only
- **Sync timing**: Initial sync takes up to 10 minutes after configuration

## Prerequisites
- Twingate Business or Enterprise plan
- Jamf admin user credentials with API access
- macOS devices enrolled in Jamf

## Step-by-Step Configuration

1. In Jamf, identify/create a user with admin capabilities and API access
2. In Twingate Admin Console: **Settings → Device Integration**
3. Click **Connect** next to Jamf and enter Jamf credentials
4. Verify integration status on the Device Settings page
5. Create a macOS Trusted Profile in Device Security, selecting **Jamf** as a Trust Method
6. Incorporate the Trusted Profile into Security Policies

## Configuration Values
- **Credentials required**: Jamf admin username/password with API permissions
- **Sync interval**: Not specified (automatic)
- **Verification window**: 7 days (device must have reported to Jamf within this period)

## Gotchas
- **Initial sync delay**: Up to 10 minutes before devices show correct verification state; status shows "Waiting to sync" during this period
- **Recoverable errors** (e.g., Jamf API unresponsive): Integration shows last successful sync time + failure time; auto-resolves when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops attempting to connect; admin email notification sent; requires manual reconfiguration with new API credentials
- Device serial number is used for matching — devices must expose serial number to Twingate client

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)