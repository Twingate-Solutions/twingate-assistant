# Kandji (Iru) Configuration

## Page Title
Iru (previously Kandji) Configuration for Twingate Device Integration

## Summary
Twingate integrates with Iru/Kandji to verify macOS devices via MDM enrollment status. The integration uses the Kandji API to match device serial numbers and enforce managed device requirements within Security Policies. Only macOS devices passing all verification checks satisfy the Trusted Profile condition.

## Key Information
- **macOS only** — no support for other platforms
- Device sync has an initial delay ("Waiting to sync"); allow a few minutes before verification states appear
- Verification checks device serial number, last check-in (≤7 days), agent presence, MDM profile, and active enrollment
- Integration pulls device list via Kandji API; Twingate Client reports serial number for matching

## Prerequisites
- **Business or Enterprise** Twingate plan required
- Iru/Kandji tenant with admin access to generate API tokens
- API token with specific permissions: **Device details** and **Device list** (under Devices scope)

## Step-by-Step

### Generate Kandji API Key
1. Open Iru web app → **Settings** (left panel)
2. Click **Access** (top bar)
3. Scroll to **API Token** → **Add Token**
4. Enter Name and Description → save token value
5. In **Manage API Permissions** modal → **Configure**
6. Under Devices, enable: **Device details** + **Device list**

### Configure in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL and API token
4. Verify status on Device Settings page after sync completes

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API Permissions | Device details, Device list |

## Device Verification Criteria (ALL must be true)
- Serial number present in Iru
- Reported to Iru within past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Gotchas
- Initial sync shows "Waiting to sync" — devices won't show correct state until first sync completes (few minutes)
- **Recoverable errors** (API unresponsive): integration shows last successful sync time; auto-recovers when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials or changed permissions): integration stops retrying; admin email notification sent; requires manual reconfiguration with new API credentials
- Altering API token permissions after setup causes unrecoverable error

## Related Docs
- Twingate Device Security / Trusted Profiles documentation
- Twingate Security Policies configuration
- [Twingate Pricing](https://www.twingate.com/pricing)