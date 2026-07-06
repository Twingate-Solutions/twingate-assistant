# Jamf Configuration

## Summary
Twingate integrates with Jamf to enforce device trust in Security Policies. The integration uses the Jamf API to verify Mac devices by matching serial numbers against managed devices in a Jamf tenant. Devices must be Jamf-managed and have reported to Jamf within the last 7 days to be considered verified.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Supported platform**: macOS only
- **Verification criteria**: Device must be Jamf-managed AND reported to Jamf within last 7 days
- **Sync mechanism**: Twingate client returns device serial number; matched against Jamf API pull
- **Integration surfaces**: Device Security → Trusted Profiles → Security Policies

## Prerequisites
- Business or Enterprise Twingate plan
- Jamf admin user credentials with API access permissions
- Jamf tenant/instance accessible via API

## Step-by-Step

1. **In Jamf**: Identify or create a user with admin capabilities and API access
2. **In Twingate**: Navigate to **Settings → Device Integration**
3. Select **Connect** next to Jamf; input Jamf credentials
4. Verify integration status on the Device Settings page
5. **Create Trusted Profile**: Settings → Device Security → create macOS Trusted Profile with Jamf as Trust Method
6. Incorporate Trusted Profile into Security Policies

## Configuration Values
- **Credentials required**: Jamf admin username/password with API access
- **Sync interval**: Initial sync takes up to 10 minutes; subsequent syncs show timestamp on Device Integration page
- **Verification window**: Device must have reported to Jamf within last **7 days**

## Gotchas
- **Initial sync delay**: Up to 10 minutes before devices show correct Jamf verification state; status shows "Waiting to sync" during this period
- **Recoverable errors** (e.g., Jamf API unresponsive): Integration shows last successful sync time + failure time; auto-resolves when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops attempting to connect; admin email notification sent — requires manual reconfiguration with new API credentials
- Only Macs verified through Jamf satisfy the Trusted Profile; non-Jamf devices will fail the trust check

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)