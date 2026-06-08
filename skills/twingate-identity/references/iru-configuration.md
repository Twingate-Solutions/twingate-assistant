# Iru (formerly Kandji) Configuration

## Summary
Twingate integrates with Iru (previously Kandji) to verify macOS devices for managed device access control. The integration uses the Iru API to match device serial numbers and validate device health status. Available on Business and Enterprise plans only.

## Key Information
- macOS-only integration
- Twingate polls Iru API for managed device serial numbers
- Device verification checks serial number match, recent check-in, agent presence, MDM profile, and active enrollment
- Verified devices can satisfy Trusted Profiles used in Security Policies

## Prerequisites
- Business or Enterprise Twingate plan
- Iru tenant with admin access
- Iru API token with specific permissions:
  - **Devices → Device details**
  - **Devices → Device list**

## Step-by-Step

### Generate Iru API Token
1. Iru web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → Save token
4. In **Manage API Permissions** modal → **Configure**
5. Enable: **Device details** and **Device list** under Devices

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Iru URL and API token

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL | `<subdomain>.api.kandji.io` or `<subdomain>.api.eu.kandji.io` |
| API Token | Generated from Iru Settings → Access |

## Device Verification Requirements (all must be true)
- Serial number present in Iru tenant
- Reported to Iru within **past 7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Gotchas
- After initial setup, status shows **"Waiting to sync"** — devices may have incorrect verification state for a few minutes
- **Recoverable errors** (e.g., API unresponsive): integration pauses, retries automatically when API is reachable; last successful sync time is preserved
- **Unrecoverable errors** (e.g., invalid/deleted credentials, changed permissions): integration stops entirely, admin email notification sent; requires full reconfiguration with new API credentials
- Only macOS devices are supported — no Windows/Linux equivalent

## Related Docs
- Device Security / Trusted Profiles configuration
- Security Policies
- Twingate pricing page (plan eligibility)