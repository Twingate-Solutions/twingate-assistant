---
source: https://www.twingate.com/docs/sentinelone-configuration
type: docs
fetched: 2026-08-14
source_version: 1b95649619b042cb946591585b9c6684cf85c5261e39d856397781cdb3235026
---

# SentinelOne Configuration

## Page Title
SentinelOne Configuration (Twingate Device Security Integration)

## Summary
Twingate integrates with SentinelOne to enforce device trust requirements for accessing private Resources. The integration pulls managed device lists via the SentinelOne API and matches serial numbers from the Twingate Client. Supports macOS and Windows only; requires Business or Enterprise plan.

## Key Information
- Verification matches device serial numbers against SentinelOne-managed device list
- Sync occurs periodically; initial sync shows "Waiting to sync" status for a few minutes
- Device verification state visible on Device Details page after sync completes
- Integration can be used as a Trust Method within Device Security Trusted Profiles and Security Policies

## Prerequisites
- Business or Enterprise Twingate plan
- SentinelOne Management Console admin access
- SentinelOne Service User API token with **Viewer** access or higher
- macOS or Windows devices only (other OSes not supported)

## Step-by-Step

### Generate SentinelOne API Key
1. Open **Settings** → **Users** → **Service Users** in SentinelOne console
2. Under **Actions**, click **Create New Service User**
3. Set name, expiration date, and scope (site or account)
4. Grant **Viewer** access minimum
5. Save the generated **API token**

### Configure in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to SentinelOne
3. Enter **Management URL** as subdomain only (e.g., `abcd` from `https://abcd.sentinelone.net/web/api`)
4. Enter API token
5. Verify status on Device Settings page

### Add to Security Policy
1. Create a Trusted Profile for macOS/Windows
2. Set SentinelOne as a required **Trust Method**
3. Incorporate Trusted Profile into a Security Policy

## Configuration Values
| Field | Format | Example |
|-------|--------|---------|
| Management URL | Subdomain only | `abcd` (not full URL) |
| API Token | SentinelOne Service User token | — |
| Access Level | Viewer or higher | — |

## Device Verification Requirements (all must be true)
- Serial number present in SentinelOne
- Reported to SentinelOne within past **1 hour**
- Not infected
- Not decommissioned
- No threat reboot required
- Operational state = `na` (agent not disabled/corrupted)

## Gotchas
- **Management URL must be subdomain only** — do not paste full URL
- Initial sync delay: devices may show incorrect state for a few minutes post-configuration
- Recoverable errors (API unresponsive): integration pauses but auto-recovers; last successful sync time is displayed
- Unrecoverable errors (invalid credentials, deleted user, altered permissions): integration stops entirely, admin email notification sent — requires full reconfiguration with new API credentials
- Devices not reporting within 1 hour will fail verification even if managed by SentinelOne

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- [Twingate Pricing](https://www.twingate.com/pricing)