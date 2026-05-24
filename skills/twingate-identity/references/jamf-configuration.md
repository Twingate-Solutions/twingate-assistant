# Jamf Configuration

## Page Title
Jamf Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Jamf Pro to verify device management status as a trust method within Device Security policies. The integration uses the Jamf API to match device serial numbers against managed devices, marking compliant devices as "Jamf verified." Only macOS devices are supported for this trust method.

## Key Information
- Jamf verification requires the device to be managed by Jamf **and** have reported to Jamf within the **last 7 days**
- Integration pulls device serial numbers via Jamf API and matches them against the Twingate client-reported serial number
- Only available on **Business and Enterprise** plans
- Initial sync takes **up to 10 minutes** after configuration
- Only macOS is mentioned as supported for Trusted Profile enforcement

## Prerequisites
- Twingate Business or Enterprise plan
- Jamf admin user credentials with **API access permissions**
- Jamf tenant/instance accessible via API

## Step-by-Step Configuration

1. In Jamf, identify or create a user with admin capabilities and API access
2. In Twingate Admin Console → **Settings** → **Device Integration**
3. Click **Connect** next to Jamf; enter Jamf credentials
4. Verify integration status on the Device Settings page
5. Navigate to Device Security → Trusted Profiles → create/edit a macOS Trusted Profile
6. Set **Jamf** as a required Trust Method
7. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
| Field | Notes |
|-------|-------|
| Jamf credentials | Admin user with API access |
| Jamf tenant URL | Your organization's Jamf instance |

## Gotchas
- **10-minute delay** on initial sync; devices show incorrect state and status displays "Waiting to sync" during this window
- Devices must have checked in to Jamf within **7 days** or they fail verification even if managed
- **Recoverable errors** (Jamf API unresponsive): integration shows last successful sync time and retries automatically
- **Unrecoverable errors** (invalid/deleted credentials or altered permissions): integration stops retrying; admin email notification sent — requires manual reconfiguration with new API credentials
- Changing Jamf API user permissions after setup will trigger an unrecoverable error state

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)