# Jamf Configuration

## Page Title
Jamf Configuration (Twingate Device Integration)

## Summary
Twingate integrates with Jamf Pro to verify Mac device management status as part of Device Security policies. The integration uses the Jamf API to match device serial numbers against managed devices, requiring devices to have reported to Jamf within the last 7 days to be considered verified.

## Key Information
- **Plan requirement**: Business and Enterprise only
- **Platform support**: macOS only
- **Verification logic**: Device serial number matched against Jamf-managed device list; device must have reported to Jamf within last 7 days
- **Sync cadence**: Initial sync takes up to 10 minutes after setup
- **Integration use**: Jamf verification is incorporated into Trusted Profiles → Security Policies

## Prerequisites
- Twingate Business or Enterprise plan
- Jamf admin user credentials with API access permissions
- macOS devices enrolled in Jamf

## Step-by-Step Configuration

1. In Jamf, identify or create a user with admin capabilities and API access
2. In Twingate Admin Console → **Settings** → **Device Integration**
3. Click **Connect** next to Jamf; enter Jamf credentials
4. Verify integration status on the Device Settings page
5. Create a Trusted Profile (macOS) requiring **Jamf** as a Trust Method
6. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
| Field | Notes |
|-------|-------|
| Jamf username | Must have admin + API access |
| Jamf password | Admin credentials |
| Jamf tenant URL | Entered during Connect flow |

## Gotchas
- **Initial sync delay**: Up to 10 minutes before devices show correct Jamf state; status shows "Waiting to sync" during this period
- **Recoverable errors** (e.g., Jamf API unresponsive): Integration shows last successful sync time + failure time; auto-resolves when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops retrying; admin notified via email; requires full reconfiguration with new API credentials
- Only Macs verified by Jamf satisfy the Trusted Profile — non-Jamf devices are blocked if policy requires it

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)