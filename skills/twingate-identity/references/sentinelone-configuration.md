# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne via API to verify device trust status for macOS and Windows devices. Verified devices can be required as a condition in Security Policies via Trusted Profiles. Device verification is based on serial number matching against the SentinelOne tenant's managed device list.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Supported OS**: macOS and Windows only
- **Sync mechanism**: Twingate polls SentinelOne API for managed device serial numbers; Client matches local serial number against list
- **Sync interval**: Near real-time; initial sync shows "Waiting to sync" for a few minutes

## Prerequisites
- SentinelOne Management Console access
- SentinelOne Service User API token with **Viewer** access or higher
- Twingate Business or Enterprise plan

## Step-by-Step

### Generate SentinelOne API Key
1. SentinelOne Console → **Settings** → **Users** → **Service Users**
2. **Actions** → **Create New Service User**
3. Set name and expiration date
4. Assign site/account scope; grant **Viewer** access minimum
5. Save the generated API token

### Configure Integration in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter **Management URL** as subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/...`)
4. Enter API token
5. Confirm integration status on Device Settings page

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows
2. Add SentinelOne as a required **Trust Method**
3. Attach Trusted Profile to a Security Policy

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Management URL | Subdomain only | `abcd` (from `https://abcd.sentinelone.net`) |
| API Token | SentinelOne Service User token | — |

## Device Verification Requirements (all must pass)
- Serial number present in SentinelOne
- Reported to SentinelOne within **past hour**
- Not infected
- Not decommissioned
- No threat reboot required
- Operational state = `na` (agent active and uncorrupted)

## Gotchas
- Initial sync shows "Waiting to sync"—device states may be incorrect for a few minutes post-setup
- **Recoverable errors** (API unresponsive): integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials, changed permissions): integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- Missing serial number on the Twingate Client side also causes "not verified" status

## Related Docs
- Twingate Device Security / Trusted Profiles documentation
- Twingate Security Policies documentation
- [Twingate Pricing](https://www.twingate.com/pricing)