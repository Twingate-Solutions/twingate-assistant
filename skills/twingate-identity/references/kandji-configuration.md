# Kandji (Iru) Configuration

## Page Title
Iru (previously Kandji) Configuration — Twingate Device Integration

## Summary
Twingate integrates with Iru/Kandji to verify macOS devices via MDM, using the Kandji API to pull managed device serial numbers. Verified devices can satisfy Trusted Profile requirements in Security Policies. Available on Business and Enterprise plans only.

## Key Information
- macOS devices only
- Twingate matches device serial numbers against Kandji-managed device list
- Device sync runs periodically; initial sync shows "Waiting to sync" for a few minutes
- Kandji API is polled to maintain current device list

## Prerequisites
- Business or Enterprise Twingate plan
- Kandji tenant with admin access
- API token with specific permissions: **Device details** and **Device list** (under Devices)

## Step-by-Step

### Generate Kandji API Token
1. Kandji web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → Save token
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure Integration in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Kandji URL:
   - US: `<subdomain>.api.kandji.io`
   - EU: `<subdomain>.api.eu.kandji.io`
4. Input API token credentials

### Apply to Security Policies
1. Navigate to Device Security → Trusted Profiles
2. Create/edit a macOS Trusted Profile
3. Set **Iru** as a required Trust Method
4. Incorporate Trusted Profile into Security Policies

## Configuration Values
| Field | Format |
|-------|--------|
| Kandji URL (US) | `<subdomain>.api.kandji.io` |
| Kandji URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API permissions | Device details, Device list |

## Device Verification Requirements (all must be met)
- Serial number present in Kandji
- Reported to Kandji within past **7 days**
- Kandji agent installed
- MDM profile installed
- Not removed from Kandji

## Gotchas
- Initial sync delay: devices may show incorrect state during "Waiting to sync" phase (resolves in a few minutes)
- **Recoverable errors** (API unresponsive): integration pauses, retries automatically, shows last successful sync time
- **Unrecoverable errors** (invalid/deleted credentials, changed permissions): integration stops entirely; admin email notification sent; requires full reconfiguration with new API credentials
- Integration is macOS-only — no support for other platforms

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)