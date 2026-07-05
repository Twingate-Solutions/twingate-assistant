# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne via API to verify device security status as a trust requirement for accessing private Resources. The Twingate Client matches device serial numbers against SentinelOne's managed device list. Available on Business and Enterprise plans only; supports macOS and Windows devices.

## Key Information
- Integration pulls device list from SentinelOne API using serial number matching
- Verified devices must: exist in SentinelOne, reported within past hour, not infected, not decommissioned, no threat reboot required, operational state = `"na"` (agent not disabled/corrupted)
- After configuration, initial sync shows "Waiting to sync" for a few minutes before devices reflect correct state
- Integrates with Security Policies via Device Security Trusted Profiles

## Prerequisites
- Business or Enterprise Twingate plan
- SentinelOne Management Console access with ability to create Service Users
- SentinelOne Service User with **Viewer** access (minimum) to target site/account

## Step-by-Step

### Generate SentinelOne API Key
1. Open **Settings** → **Users** → **Service Users** in SentinelOne console
2. Click **Actions** → **Create New Service User**
3. Assign name, expiration date, site/account scope, and Viewer role minimum
4. Save the generated API token

### Configure Integration in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter Management URL as subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/web/api`)
4. Enter API token

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows requiring SentinelOne as Trust Method
2. Incorporate Trusted Profile into Security Policies

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Management URL | Subdomain only | `abcd` (from `abcd.sentinelone.net`) |
| API Token | Service User token | Generated in SentinelOne console |

## Gotchas
- **Subdomain only** for Management URL—do not enter the full URL
- Initial sync delay: devices may show incorrect state for a few minutes after setup
- Device shows "SentinelOne not verified" if: not managed by SentinelOne, hasn't reported in >1 hour, infected/decommissioned/reboot required/disabled/corrupted, or serial number unretrievable
- **Recoverable errors** (API unresponsive): integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid credentials, deleted user, changed permissions): integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)