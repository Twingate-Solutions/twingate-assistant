# Jamf Configuration

## Page Title
Jamf Configuration (Twingate Device Integration)

## Summary
Twingate integrates with Jamf to verify Mac device management status as part of Device Security policies. The integration uses the Jamf API to match device serial numbers against managed devices, granting "Jamf verified" status to devices managed by Jamf that have reported within the last 7 days.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Supported platforms**: macOS only
- **Verification logic**: Device serial number matched against Jamf-managed device list; device must have reported to Jamf within last 7 days
- **Sync timing**: Initial sync takes up to 10 minutes after configuration
- **Integration status visible**: Settings → Device Integration page shows last sync time and current status

## Prerequisites
- Business or Enterprise Twingate plan
- Jamf admin user credentials with API access permissions
- macOS devices enrolled in Jamf

## Step-by-Step Configuration

1. In Jamf, identify or create a user with admin capabilities and API access
2. In Twingate Admin Console: **Settings → Device Integration**
3. Click **Connect** next to Jamf and enter Jamf credentials
4. Wait up to 10 minutes for initial sync; status shows "Waiting to sync" during this period
5. Create a Trusted Profile in Device Security (macOS) with Jamf as a required Trust Method
6. Incorporate the Trusted Profile into Security Policies

## Configuration Values
- **Jamf credentials required**: Admin username/password with API access
- **Sync interval**: Implied periodic sync (7-day device reporting window enforced)
- **Initial sync delay**: Up to 10 minutes

## Gotchas
- **macOS only** — Jamf trust method applies only to Mac devices
- **7-day reporting window**: Devices not checking into Jamf within 7 days lose verified status
- **Recoverable errors** (e.g., Jamf API unresponsive): Integration auto-retries; shows last successful sync time
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops retrying; admin receives email alert requiring manual reconfiguration with new API credentials
- Devices may show incorrect Jamf verification state during the initial 10-minute sync window

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)