# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne via API to verify device security status as a condition for accessing private Resources. The Twingate Client matches device serial numbers against SentinelOne-managed devices and checks multiple health criteria. Available on Business and Enterprise plans only; supports macOS and Windows.

## Key Information
- Integration pulls device list via SentinelOne API using serial number matching
- Verified devices must: be present in SentinelOne, reported within past hour, not infected, not decommissioned, no threat reboot pending, operational state = `na`
- Only macOS and Windows devices are supported
- After setup, expect a brief "Waiting to sync" period before device states are accurate

## Prerequisites
- Twingate Business or Enterprise plan
- SentinelOne Management Console access
- SentinelOne Service User API token with **Viewer** access or higher

## Step-by-Step

### Generate SentinelOne API Key
1. SentinelOne Console → **Settings** → **Users** → **Service Users**
2. **Actions** → **Create New Service User**
3. Set name and expiration date
4. Assign site/account scope with **Viewer** access minimum
5. Save the generated API token

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter Management URL subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/web/api`)
4. Enter API token
5. Verify status on Device Settings page

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows
2. Set SentinelOne as a required Trust Method
3. Incorporate Trusted Profile into Security Policies

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Management URL | Subdomain only | `abcd` (not full URL) |
| API Token | Service User token | From SentinelOne console |
| Permission Level | Viewer or higher | — |

## Gotchas
- **Subdomain only** in Management URL field — do not paste the full URL
- Initial sync shows "Waiting to sync" — device states may be incorrect for a few minutes
- Recoverable errors (API unresponsive): integration shows last successful sync time; auto-resolves when API is reachable
- Unrecoverable errors (invalid/deleted credentials, changed permissions): integration stops retrying; admin email notification sent; requires manual reconfiguration
- `SentinelOne not verified` can occur if serial number cannot be retrieved from the device itself

## Related Docs
- Device Security / Trusted Profiles
- Security Policies
- Twingate Pricing (Business/Enterprise plans)