# Kandji (Iru) Configuration

## Page Title
Iru (previously Kandji) Configuration for Twingate Device Integration

## Summary
Twingate integrates with Iru/Kandji to verify macOS devices via MDM, pulling managed device lists through the Kandji API and matching serial numbers. Verified devices can be required as a trust method within Security Policies. Available on Business and Enterprise plans only.

## Key Information
- **macOS only** — Iru verification applies exclusively to macOS devices
- Device sync uses serial number matching against Kandji-managed device list
- Initial sync shows "Waiting to sync" status; resolves within a few minutes
- Sync failures from recoverable errors auto-resolve when API becomes available
- Unrecoverable errors trigger admin email notification and require reconfiguration

## Prerequisites
- Twingate Business or Enterprise plan
- Iru/Kandji account with admin access to generate API tokens
- API token permissions: **Device details** + **Device list** (under Devices)

## Step-by-Step

### Generate Kandji API Token
1. Open **Settings** → **Access** in Kandji web app
2. Scroll to **API Token** → click **Add Token**
3. Enter Name and Description → save token value
4. In **Manage API Permissions** modal → click **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL and API token credentials

### Apply to Security Policies
1. Create a Trusted Profile for macOS
2. Set Iru as a required Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API Permissions | Device details, Device list |

## Device Verification Requirements
A device is considered Iru-verified only if **all** conditions are met:
- Serial number present in Iru tenant
- Reported to Iru within the **past 7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Gotchas
- **"Waiting to sync"** after setup is normal — devices may show incorrect state until first sync completes (few minutes)
- Recoverable errors (API unresponsive): integration shows last successful sync time, auto-recovers
- Unrecoverable errors (invalid/deleted credentials, changed permissions): integration stops retrying — requires full reconfiguration with new API credentials
- 7-day check-in requirement means temporarily offline devices will lose verified status

## Related Docs
- Twingate Device Security / Trusted Profiles documentation
- Twingate Security Policies documentation
- [Twingate Pricing](https://www.twingate.com/pricing) (plan requirements)