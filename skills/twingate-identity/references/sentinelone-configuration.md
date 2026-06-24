# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne via API to verify device security posture before granting access to private Resources. The integration pulls managed device lists from SentinelOne and matches device serial numbers to enforce access policies. Available on Business and Enterprise plans only; supports macOS and Windows devices.

## Key Information
- Verification uses device serial number matching against SentinelOne's managed device list
- Sync occurs periodically; initial sync shows "Waiting to sync" status for a few minutes
- Only macOS and Windows devices are supported

## Prerequisites
- Twingate Business or Enterprise plan
- SentinelOne Management Console admin access
- SentinelOne Service User API token with **Viewer** access or higher

## Device Verification Requirements (all must be met)
- Serial number present in SentinelOne
- Reported to SentinelOne within the past hour
- Not infected
- Not decommissioned
- No threat reboot required
- Operational state: `na` (agent not disabled or corrupted)

## Step-by-Step

### Generate SentinelOne API Key
1. SentinelOne Console → **Settings** → **Users** → **Service Users**
2. **Actions** → **Create New Service User**
3. Assign name, expiration date, site/account scope
4. Grant **Viewer** access minimum
5. Save the API token

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter **Management URL** as subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/web/api`)
4. Enter API token
5. Confirm status on Device Settings page

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows
2. Set SentinelOne as a required Trust Method
3. Incorporate Trusted Profile into Security Policies

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Management URL | Subdomain only | `abcd` |
| API Token | SentinelOne Service User token | — |
| Access Level | Viewer or higher | — |

## Gotchas
- **Subdomain only** for Management URL — do not enter full URL
- Initial sync delay: devices may show incorrect verification state for a few minutes after setup
- **Recoverable errors** (API unresponsive): integration shows last successful sync time; auto-resolves when API returns
- **Unrecoverable errors** (invalid/deleted credentials, changed permissions): integration stops retrying; admin email notification sent — requires manual reconfiguration with new credentials
- "SentinelOne not verified" can occur if serial number cannot be retrieved from the device (client-side issue)

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)