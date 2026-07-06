# Iru (formerly Kandji) Configuration

## Summary
Twingate integrates with Iru (previously Kandji) to verify macOS devices against MDM-managed device lists. Device verification uses serial number matching via the Iru API. Verified devices can satisfy Trusted Profile requirements within Security Policies.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Platform support**: macOS only
- **Sync timing**: Initial sync shows "Waiting to sync" — allow a few minutes before device states are accurate
- **Verification check interval**: Devices must have reported to Iru within past 7 days

## Prerequisites
- Iru (Kandji) tenant with admin access
- Iru API token with specific permissions (Device details + Device list)
- Twingate Business or Enterprise plan

## Step-by-Step

### Generate Iru API Token
1. Iru web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → save token value
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable: **Device details** and **Device list**

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Iru URL and API token

## Configuration Values

| Parameter | Format |
|-----------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API permissions | `Device details`, `Device list` |

## Device Verification Requirements (all must be true)
- Serial number present in Iru device list
- Reported to Iru within past 7 days
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Gotchas
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable again
- **Unrecoverable errors** (invalid/deleted credentials or altered permissions): Integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- During initial "Waiting to sync" period, device verification states may be incorrect — wait a few minutes
- `Iru not verified` status does not distinguish between the five failure reasons without checking device details individually

## Related Docs
- [Device Security / Trusted Profiles](https://www.twingate.com/docs/device-security)
- [Security Policies](https://www.twingate.com/docs/security-policies)
- [Twingate Pricing](https://www.twingate.com/pricing)