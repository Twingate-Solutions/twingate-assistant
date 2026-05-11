# Jamf Configuration

## Page Title
Jamf Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Jamf to verify device management status as a trust requirement for accessing private resources. The integration uses the Jamf API to match device serial numbers against managed devices. Devices must be Jamf-managed and have reported to Jamf within the last 7 days to be considered verified.

## Key Information
- macOS only for Jamf-based device verification
- Verification criteria: device is Jamf-managed AND reported to Jamf within last 7 days
- Jamf status integrates into Device Security Trusted Profiles → Security Policies
- Initial sync takes up to 10 minutes after setup

## Prerequisites
- Business or Enterprise Twingate plan
- Jamf admin credentials with API access
- Twingate admin access to Settings → Device Integration

## Step-by-Step

1. In Jamf: identify/create a user with admin capabilities and API access
2. In Twingate: navigate to **Settings → Device Integration**
3. Click **Connect** next to Jamf and enter Jamf credentials
4. Verify integration status on the Device Settings page
5. Create a macOS **Trusted Profile** under Device Security, set Jamf as the Trust Method
6. Incorporate the Trusted Profile into Security Policies

## Configuration Values
- **Jamf user requirement**: admin role + API access permissions
- **Sync check window**: 7 days (device must have reported to Jamf within this period)
- **Initial sync delay**: up to 10 minutes

## Gotchas
- During initial 10-minute sync window, devices may show incorrect Jamf verification state; Device Settings shows "Waiting to sync"
- **Recoverable errors** (Jamf API unresponsive): integration shows last successful sync time + failure time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials, altered permissions): integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- Only macOS devices can satisfy Jamf-based Trusted Profiles

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)