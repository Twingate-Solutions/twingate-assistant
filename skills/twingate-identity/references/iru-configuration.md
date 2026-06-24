# Iru (formerly Kandji) Configuration

## Summary
Twingate integrates with Iru (previously Kandji) to verify macOS devices as part of Device Security policies. The integration uses the Iru API to match device serial numbers against managed devices, enforcing MDM-based trust requirements for Resource access.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Platform support**: macOS only
- **Verification checks**: Serial number match, reported within past 7 days, Iru agent installed, MDM profile installed, not removed from Iru
- **Sync mechanism**: Twingate polls Iru API; Client sends device serial number for matching

## Prerequisites
- Business or Enterprise Twingate plan
- Iru tenant with admin access
- API token with specific permissions (Device details + Device list)

## Step-by-Step

### Generate Iru API Token
1. Open Iru web app → **Settings** (left panel)
2. Click **Access** (top bar)
3. Scroll to **API Token** → **Add Token**
4. Enter Name and Description → Save token
5. In **Manage API Permissions** modal → **Configure**
6. Under Devices, enable: **Device details** AND **Device list**

### Configure Integration in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Iru URL and API token
4. Verify status on Device Settings page

### Apply to Security Policies
1. Create a macOS Trusted Profile in Device Security
2. Set Iru as a required Trust Method
3. Incorporate Trusted Profile into Security Policies

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |

**Required API permissions**: `Device details`, `Device list`

## Gotchas
- After initial setup, status shows **"Waiting to sync"** for a few minutes — devices may show incorrect verification state during this window
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials, altered permissions): Integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- Devices report `Iru not verified` if any single verification requirement fails (agent uninstalled, no MDM profile, not reported in 7 days, etc.)

## Related Docs
- Twingate Device Security / Trusted Profiles documentation
- Twingate Security Policies documentation
- [Twingate pricing page](https://www.twingate.com/pricing)