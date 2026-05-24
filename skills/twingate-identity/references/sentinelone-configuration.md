# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne via API to verify device health before granting access to private Resources. The Twingate Client matches device serial numbers against SentinelOne-managed devices. Available on Business and Enterprise plans only; supports macOS and Windows devices.

## Key Information
- Integration pulls device list from SentinelOne API using serial number matching
- Verified devices must: appear in SentinelOne, reported within past hour, not infected, not decommissioned, no threat reboot required, operational state = `"na"` (agent enabled and uncorrupted)
- Once configured, SentinelOne can be used as a Trust Method in Device Security Trusted Profiles, which feed into Security Policies
- Initial sync shows "Waiting to sync" status — allow a few minutes before device states are accurate

## Prerequisites
- Business or Enterprise Twingate plan
- SentinelOne Management Console access
- SentinelOne Service User API token with **Viewer** access or higher

## Step-by-Step

### Generate SentinelOne API Key
1. Open **Settings** → **Users** → **Service Users** in SentinelOne console
2. Under **Actions**, click **Create New Service User**
3. Set name, expiration date, and scope (site or account)
4. Grant **Viewer** access minimum
5. Save the API token

### Configure Integration in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter API token and Management URL subdomain (e.g., for `https://abcd.sentinelone.net/...` enter `abcd`)
4. Verify integration status on Device Settings page

### Add to Security Policies
1. Create a Trusted Profile for macOS/Windows
2. Set SentinelOne as a required Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
| Field | Format/Example |
|-------|---------------|
| Management URL | Subdomain only: `abcd` (from `https://abcd.sentinelone.net`) |
| API Token | Generated SentinelOne Service User token |
| Permission Level | Viewer (minimum) |

## Gotchas
- **Subdomain only** in Management URL field — do not paste full URL
- Devices show "SentinelOne not verified" if: not managed by SentinelOne, haven't reported in >1 hour, infected/decommissioned/reboot-required/disabled/corrupted, or serial number is unretreivable
- **Recoverable errors** (API unresponsive): integration shows last successful sync time, auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials, changed permissions): integration stops retrying, admin email notification sent — requires full reconfiguration with new API credentials

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)