# Jamf Configuration

## Page Title
Jamf Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Jamf to verify macOS device management status as a trust requirement for accessing private resources. The integration uses the Jamf API to match device serial numbers against managed devices. Devices must be Jamf-managed and have reported to Jamf within the last 7 days to be considered verified.

## Key Information
- **Platform support**: macOS only
- **Plan requirement**: Business & Enterprise plans only
- **Verification criteria**: Device must be Jamf-managed AND reported to Jamf within last 7 days
- **Sync mechanism**: Twingate client returns device serial number; matched against Jamf-managed device list
- **Initial sync delay**: Up to 10 minutes after configuration

## Prerequisites
- Business or Enterprise Twingate plan
- Jamf admin user credentials with API access
- macOS devices enrolled in Jamf

## Step-by-Step Configuration

1. In Jamf, identify/create a user with admin capabilities and API access
2. In Twingate Admin Console → **Settings** → **Device Integration**
3. Select **Connect** next to Jamf; enter Jamf credentials
4. Verify integration status on Device Settings page
5. Create a Trusted Profile (macOS) with Jamf as the required Trust Method
6. Incorporate the Trusted Profile into Security Policies

## Configuration Values
| Parameter | Details |
|-----------|---------|
| Jamf credentials | Admin user with API access |
| Trust Method | Jamf (selectable in Device Security Trusted Profiles) |
| Sync frequency | Periodic; device must report to Jamf within 7 days |

## Gotchas
- **10-minute initial sync delay**: Devices show incorrect state during this window; Device Settings shows "Waiting to sync"
- **Recoverable errors** (e.g., Jamf API unresponsive): Integration shows last successful sync time + failure time; auto-resolves when API is reachable again
- **Unrecoverable errors** (e.g., invalid/deleted credentials or altered permissions): Integration stops attempting to connect; admin email notification sent; requires manual reconfiguration with new API credentials
- Jamf verification state is per-device; check individual device details page after sync completes

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (for plan eligibility)