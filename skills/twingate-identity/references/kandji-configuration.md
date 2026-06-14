# Kandji (Iru) Configuration

## Summary
Twingate integrates with Iru (formerly Kandji) to verify macOS devices as managed and compliant before granting access to private Resources. The integration uses the Iru API to match device serial numbers against managed device lists. Available on Business and Enterprise plans only.

## Key Information
- macOS devices only
- Twingate pulls managed device list via Iru API using serial number matching
- Sync delay expected after initial setup ("Waiting to sync" state for a few minutes)
- Verified devices are incorporated into Security Policies via Trusted Profiles

## Prerequisites
- Twingate Business or Enterprise plan
- Iru tenant with admin access
- Iru API token with specific permissions: **Device details** and **Device list** (under Devices)

## Device Verification Requirements
A device is considered Iru-verified only if ALL conditions are met:
- Serial number exists in Iru
- Reported to Iru within the past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Step-by-Step

### Generate Iru API Key
1. Iru web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → save token value
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure in Twingate
1. Twingate → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Iru URL and API token

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |

## Gotchas
- **Initial sync delay**: Status shows "Waiting to sync" after setup; devices won't show correct state until sync completes (allow a few minutes)
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials or changed permissions): Integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- Changing API token permissions after setup causes unrecoverable error

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan requirements)