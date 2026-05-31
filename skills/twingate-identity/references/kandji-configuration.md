# Kandji (Iru) Configuration

## Page Title
Iru (previously Kandji) Configuration for Twingate Device Integration

## Summary
Twingate integrates with Iru/Kandji to verify macOS devices via MDM, using the Kandji API to match device serial numbers against managed device lists. Verified devices can satisfy Trusted Profile requirements within Security Policies. Available on Business and Enterprise plans only.

## Key Information
- macOS devices only
- Twingate pulls device list via Kandji API and matches serial numbers from the Twingate Client
- Sync has an initial delay ("Waiting to sync") of a few minutes before device states are accurate
- Device list refreshes periodically; last successful sync time is displayed in Device Settings

## Prerequisites
- Twingate Business or Enterprise plan
- Iru/Kandji tenant with admin access
- Kandji API token with specific permissions: **Device details** and **Device list** (under Devices)

## Step-by-Step

### Generate Kandji API Token
1. Kandji web app → **Settings** → **Access** (top bar)
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → save token value
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable: `Device details` + `Device list`

### Configure Integration in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Kandji URL and API token

### Incorporate into Security Policies
1. Create a Device Security **Trusted Profile** for macOS
2. Set Iru as a required **Trust Method**
3. Add Trusted Profile to desired Security Policy

## Configuration Values

| Field | Format |
|-------|--------|
| Kandji URL (US) | `<subdomain>.api.kandji.io` |
| Kandji URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API permissions | `Device details`, `Device list` |

## Device Verification Requirements (all must be met)
- Serial number present in Kandji
- Reported to Kandji within **past 7 days**
- Kandji agent installed
- MDM profile installed
- Not removed from Kandji

## Gotchas
- **Initial sync delay**: After setup, status shows "Waiting to sync"—device states may be incorrect for a few minutes
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials or changed permissions): Integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials
- Only macOS devices are supported—no iOS/Windows coverage via this integration

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)