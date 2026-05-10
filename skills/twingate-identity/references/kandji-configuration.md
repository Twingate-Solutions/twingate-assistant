# Kandji Configuration

## Page Title
Kandji Device Integration Configuration for Twingate

## Summary
Twingate integrates with Kandji MDM to verify macOS device compliance as part of Device Security policies. The integration uses the Kandji API to match device serial numbers and validate management status. Verified devices can be required as a trust method in Security Policy Trusted Profiles.

## Key Information
- **Plan requirement**: Business and Enterprise only
- **Platform support**: macOS devices only
- **Sync behavior**: Twingate pulls device list via Kandji API; matches by serial number
- **Sync interval**: Initial sync shows "Waiting to sync" for a few minutes; subsequent syncs show last sync time

## Prerequisites
- Twingate Business or Enterprise plan
- Kandji admin access to generate API token
- Kandji API permissions: **Device details** and **Device list** (under Devices)

## Step-by-Step

### Generate Kandji API Key
1. Kandji web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → Save token
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure Integration in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Kandji
3. Enter Kandji URL: `<subdomain>.api.kandji.io` or `<subdomain>.api.eu.kandji.io`
4. Enter API token

### Apply to Security Policies
1. Navigate to Device Security → Trusted Profiles
2. Create/edit a macOS Trusted Profile
3. Add **Kandji** as a required Trust Method
4. Incorporate the Trusted Profile into Security Policies

## Configuration Values
| Parameter | Format |
|-----------|--------|
| Kandji URL (US) | `<subdomain>.api.kandji.io` |
| Kandji URL (EU) | `<subdomain>.api.eu.kandji.io` |

## Device Verification Requirements
A device is considered Kandji-verified only if **all** are true:
- Serial number exists in Kandji
- Reported to Kandji within the past **7 days**
- Kandji agent installed
- MDM profile installed
- Not removed from Kandji

## Gotchas
- Initial sync has a delay ("Waiting to sync"); devices may show incorrect state during this window
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid credentials, deleted token, altered permissions): Integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- Altering Kandji API token permissions after setup causes unrecoverable error

## Related Docs
- Twingate Device Security / Trusted Profiles documentation
- Twingate Security Policies documentation
- [Twingate Pricing](https://www.twingate.com/pricing)