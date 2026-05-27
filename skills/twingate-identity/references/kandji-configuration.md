# Kandji (Iru) Configuration

## Page Title
Iru (Kandji) Configuration – Device Integration for macOS Trust Verification

## Summary
Twingate integrates with Iru (formerly Kandji) to verify macOS devices via MDM enrollment status. Device serial numbers are matched against Iru's managed device list to satisfy Trusted Profile requirements in Security Policies. Requires Business or Enterprise plan.

## Key Information
- **macOS only** – Iru verification applies exclusively to macOS devices
- Twingate pulls device list via Iru API; matches by serial number
- Sync shows "Waiting to sync" initially; allow a few minutes before device states are accurate
- Integration status and last sync time visible on Device Settings page

## Prerequisites
- Twingate Business or Enterprise plan
- Iru (Kandji) tenant with admin access
- API token with specific permissions (see below)

## Step-by-Step

### Generate Iru API Token
1. In Iru web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description; save the token
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable: **Device details** + **Device list**

### Configure in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL and API token

### Incorporate into Security Policy
1. Create a Trusted Profile for macOS
2. Set Iru as a required Trust Method
3. Attach Trusted Profile to a Security Policy

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API permissions | Device details, Device list |

## Device Verification Requirements
A device is considered Iru-verified only if **all** are true:
- Serial number present in Iru
- Reported to Iru within the past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Gotchas
- **Recoverable errors** (e.g., API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops retrying; admin email notification sent; must reconfigure integration with new API credentials
- During initial sync ("Waiting to sync"), device verification states may be incorrect — wait a few minutes
- Devices removed from Iru or with uninstalled agents will fail verification immediately

## Related Docs
- Device Security / Trusted Profiles configuration
- Security Policies
- Twingate pricing (plan eligibility)