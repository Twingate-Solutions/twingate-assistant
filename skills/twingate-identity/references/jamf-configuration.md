---
source: https://www.twingate.com/docs/jamf-configuration
type: docs
fetched: 2026-08-14
source_version: 85c953a7b28909619c71a2193e7941b5ee673feb6043ff8b929656eb3967e4ed
---

# Jamf Configuration

## Page Title
Jamf Configuration (Twingate Device Integration)

## Summary
Twingate integrates with Jamf to verify macOS device management status as part of Device Security policies. The integration uses the Jamf API to sync managed device serial numbers, and devices must have reported to Jamf within the last 7 days to be considered verified. Available on Business and Enterprise plans only.

## Key Information
- Only **macOS** devices are supported for Jamf verification
- Device verification requires matching serial numbers between Twingate client and Jamf-managed device list
- Device must have **reported to Jamf within last 7 days** to be considered verified
- Jamf verification integrates with **Trusted Profiles** → **Security Policies**
- Initial sync takes **up to 10 minutes** after configuration

## Prerequisites
- Business or Enterprise Twingate plan
- Jamf admin credentials with API access
- macOS devices enrolled in Jamf

## Step-by-Step Configuration

1. In Jamf, identify/create a user with **admin capabilities and API access**
2. In Twingate Admin Console → **Settings** → **Device Integration**
3. Click **Connect** next to Jamf, enter Jamf credentials
4. Verify integration status on the **Device Settings** page
5. Navigate to **Device Security** → create/edit a **Trusted Profile** for macOS
6. Set **Jamf** as a required Trust Method in the Trusted Profile
7. Incorporate the Trusted Profile into a **Security Policy**

## Configuration Values
- **Credentials required**: Jamf admin username/password (API access required)
- **Sync frequency**: Periodic (post-setup delay up to 10 minutes for initial sync)
- **Verification window**: Device must report to Jamf within **7 days**

## Gotchas
- **Initial sync delay**: Devices show incorrect state for up to 10 minutes after setup; status displays as "Waiting to sync"
- **Recoverable errors** (Jamf API unresponsive): Integration shows last successful sync time + failure time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials or altered permissions): Integration stops retrying; admin email notification sent — requires manual reconfiguration with new API credentials
- Serial number matching is the verification mechanism — devices not reporting their serial number correctly will fail verification

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)