# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne via API to verify device health before granting access to private Resources. Devices are matched by serial number against the SentinelOne tenant and must pass health checks. Available on Business and Enterprise plans only; supports macOS and Windows.

## Key Information
- Verification pulls device list via SentinelOne API, matching serial numbers from Twingate Client
- Only macOS and Windows devices are supported
- Integration feeds into Device Security Trusted Profiles → Security Policies

## Prerequisites
- Business or Enterprise Twingate plan
- SentinelOne Management Console access with ability to create Service Users
- SentinelOne Service User with **Viewer** access or higher

## Step-by-Step

### Generate SentinelOne API Key
1. SentinelOne Console → **Settings** → **Users** → **Service Users**
2. **Actions** → **Create New Service User**
3. Set name, expiration date, site/account scope, minimum **Viewer** access
4. Save the generated API token

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter **Management URL** as subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/web/api`)
4. Enter API token
5. Verify status on Device Settings page

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows
2. Set SentinelOne as required Trust Method
3. Attach Trusted Profile to a Security Policy

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Management URL | Subdomain only | `abcd` (not full URL) |
| API Token | From Service User creation | — |
| Access Level | Viewer minimum | — |

## Device Verification Requirements (all must pass)
- Serial number present in SentinelOne
- Reported to SentinelOne **within past hour**
- Not infected
- Not decommissioned
- No threat reboot required
- Operational state = `na` (agent not disabled/corrupted)

## Gotchas
- **Initial sync delay**: Status shows "Waiting to sync" after setup; devices may have incorrect state for a few minutes
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API returns
- **Unrecoverable errors** (invalid credentials, deleted user, changed permissions): Integration stops retrying; admin email notification sent → must reconfigure with new API credentials
- Serial number retrieval failure from the Twingate Client side also causes "not verified" status

## Related Docs
- Twingate Device Security / Trusted Profiles documentation
- Twingate Security Policies documentation
- [Twingate Pricing](https://www.twingate.com/pricing)