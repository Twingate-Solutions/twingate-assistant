# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne via API to verify device health before granting access to private Resources. Devices are matched by serial number against the SentinelOne tenant and must pass health checks. Only macOS and Windows devices are supported.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Supported OS**: macOS and Windows
- **Sync mechanism**: Twingate polls SentinelOne API; Client returns device serial number for matching
- **Sync interval**: Near real-time; initial sync shows "Waiting to sync" for a few minutes

## Prerequisites
- SentinelOne Management Console access
- SentinelOne Service User API token with **Viewer** access or higher
- Business or Enterprise Twingate plan

## Step-by-Step

### Generate SentinelOne API Key
1. SentinelOne Console → **Settings** → **Users** → **Service Users**
2. **Actions** → **Create New Service User**
3. Assign name, expiration date, site/account scope, and **Viewer** role (minimum)
4. Save the generated API token

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter **Management URL** as subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/web/api`)
4. Enter API token
5. Confirm integration status on Device Settings page

### Apply to Security Policy
1. Create a Trusted Profile for macOS/Windows
2. Set SentinelOne as a required Trust Method
3. Add Trusted Profile to a Security Policy

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Management URL | Subdomain only | `abcd` (not full URL) |
| API Token | Service User token | From SentinelOne console |
| Permission level | Viewer or higher | Viewer |

## Device Verification Requirements (all must be true)
- Serial number present in SentinelOne
- Reported to SentinelOne within past **1 hour**
- Not infected
- Not decommissioned
- No threat reboot required
- Operational state: `na` (agent active and uncorrupted)

## Gotchas
- **Subdomain only** in Management URL field — entering the full URL will break the integration
- Initial sync delay: devices may show incorrect state for a few minutes after setup
- `SentinelOne not verified` can occur if serial number cannot be retrieved from the device (client-side issue)
- **Recoverable errors** (API unresponsive): integration pauses, auto-resumes when API is reachable; last successful sync time is preserved
- **Unrecoverable errors** (invalid/deleted credentials, changed permissions): integration stops entirely, admin email notification sent — requires manual reconfiguration with new API credentials

## Related Docs
- Twingate Device Security / Trusted Profiles
- Twingate Security Policies
- [Twingate Pricing](https://www.twingate.com/pricing)