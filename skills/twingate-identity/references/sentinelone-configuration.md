# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne to verify device security status before granting access to private Resources. The integration uses the SentinelOne API to match device serial numbers against managed devices and validate their health state. Available on Business and Enterprise plans only; supports macOS and Windows devices.

## Key Information
- Twingate pulls device list via SentinelOne API using serial number matching
- Only macOS and Windows devices are supported
- Device sync has an initial delay ("Waiting to sync") of a few minutes after setup
- SentinelOne verification is used within **Trusted Profiles** inside **Security Policies**

## Prerequisites
- Business or Enterprise Twingate plan
- SentinelOne Management Console access
- SentinelOne Service User with **Viewer** access or higher (site or account scope)
- SentinelOne API token

## Step-by-Step

### Generate SentinelOne API Key
1. Open **Settings** → **Users** → **Service Users** in SentinelOne Console
2. Click **Actions** → **Create New Service User**
3. Assign name, expiration date, and site/account scope with **Viewer** access minimum
4. Save the generated **API token**

### Configure Integration in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter Management URL subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/web/api`)
4. Enter API token
5. Verify status on Device Settings page

### Add to Security Policies
1. Create a **Trusted Profile** for macOS/Windows
2. Set **SentinelOne** as a required Trust Method
3. Incorporate the Trusted Profile into a **Security Policy**

## Configuration Values
| Field | Format/Example |
|---|---|
| Management URL | Subdomain only: `abcd` (not full URL) |
| API Token | From SentinelOne Service User |
| Permission Level | Viewer minimum |

## Device Verification Requirements (all must be true)
- Serial number present in SentinelOne
- Reported to SentinelOne **within past hour**
- Not infected
- Not decommissioned
- No threat reboot required
- Operational state: `na` (agent not disabled/corrupted)

## Gotchas
- **Subdomain only** in Management URL field — entering the full URL will break the integration
- Initial sync shows "Waiting to sync"; devices may show incorrect state for a few minutes
- **Recoverable errors** (API unresponsive): integration pauses, auto-resumes when API is reachable
- **Unrecoverable errors** (invalid credentials, deleted user, changed permissions): integration stops entirely; admin email notification sent; requires full reconfiguration with new API credentials
- No serial number retrievable from device = "not verified" even if SentinelOne is healthy

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)