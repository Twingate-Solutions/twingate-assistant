# Jamf Configuration

## Page Title
Jamf Configuration (Business & Enterprise Only)

## Summary
Twingate integrates with Jamf to verify macOS device management status as a trust requirement for accessing private resources. The integration uses the Jamf API to match device serial numbers and validates devices have reported to Jamf within the last 7 days. Verified devices can satisfy Trusted Profile requirements in Security Policies.

## Key Information
- **Platform scope**: macOS only
- **Plan requirement**: Business & Enterprise plans only
- **Verification criteria**: Device must be Jamf-managed AND reported to Jamf within the last 7 days
- **Sync timing**: Initial sync takes up to 10 minutes after configuration
- **Matching method**: Twingate client returns device serial number; matched against Jamf-managed device list

## Prerequisites
- Twingate Business or Enterprise plan
- Jamf admin user credentials with API access permissions
- macOS devices enrolled in Jamf

## Step-by-Step

1. In Jamf, identify/create a user with admin capabilities and API access
2. In Twingate Admin Console, navigate to **Settings → Device Integration**
3. Click **Connect** next to Jamf and enter Jamf credentials
4. Verify integration status on the Device Settings page
5. Navigate to Device Security and create a **Trusted Profile** for macOS
6. Set **Jamf** as a required Trust Method in the Trusted Profile
7. Incorporate the Trusted Profile into Security Policies

## Configuration Values
- No explicit env vars or CLI flags
- Inputs required: Jamf tenant credentials (admin username/password with API access)

## Gotchas
- **10-minute delay**: Initial sync shows "Waiting to sync" status — devices may show incorrect verification state during this window
- **Recoverable errors** (e.g., Jamf API unresponsive): Integration shows last successful sync time and failure time; auto-resolves when API becomes reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- Only devices that have **both** Jamf management AND recent check-in (≤7 days) are considered verified

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)