<!-- triage: unassigned URL: https://www.twingate.com/docs/iru-configuration -->

# Iru (formerly Kandji) Configuration

## Summary
Twingate integrates with Iru (previously Kandji) to verify macOS devices via MDM management status. The integration uses the Iru API to pull managed device serial numbers and match them against devices connecting through the Twingate Client. Verified devices can be used in Security Policy Trusted Profiles to gate Resource access.

## Key Information
- macOS devices only
- Business & Enterprise plans only
- Device verification checks serial number, last report within 7 days, agent installed, MDM profile present, and not removed from Iru
- Twingate polls Iru API to sync device list; initial sync shows "Waiting to sync" status

## Prerequisites
- Twingate Business or Enterprise plan
- Iru tenant with admin access
- Iru API token with **Device details** and **Device list** permissions under Devices scope

## Step-by-Step

### Generate Iru API Token
1. Iru web app → **Settings** (left panel) → **Access** (top bar)
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → Save token value
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable: `Device details` and `Device list`

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL in format:
   - `<subdomain>.api.kandji.io` (US)
   - `<subdomain>.api.eu.kandji.io` (EU)
4. Enter API token
5. Confirm integration status on Device Settings page

### Apply to Security Policies
1. Navigate to Device Security → Trusted Profiles
2. Create/edit a macOS Trusted Profile
3. Set **Iru** as a Trust Method
4. Incorporate Trusted Profile into Security Policies

## Configuration Values
| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API Permissions | Device details, Device list |

## Gotchas
- **Initial sync delay**: Status shows "Waiting to sync" for a few minutes after setup; device states may be incorrect during this window
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; resolves automatically when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials or changed permissions): Integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials
- Device marked "Iru not verified" if: not Iru-managed, hasn't reported in 7+ days, agent uninstalled, no MDM profile, or removed from Iru

## Related Docs
- Device Security / Trusted Profiles configuration
- Security Policies documentation
- Twingate pricing page (plan eligibility)