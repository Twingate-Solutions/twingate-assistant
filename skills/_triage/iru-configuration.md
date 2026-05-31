<!-- triage: unassigned URL: https://www.twingate.com/docs/iru-configuration -->

# Iru (formerly Kandji) Configuration

## Summary
Twingate integrates with Iru (previously Kandji) to verify macOS devices against an MDM-managed device list. The integration pulls device serial numbers via the Iru API and matches them against Twingate Client-reported serials. Verified devices can satisfy Trusted Profiles used in Security Policies.

## Key Information
- macOS only
- Business & Enterprise plans only
- Sync uses Iru API; device serial number is the matching identifier
- Device verification checks occur against a periodically synced list (not real-time)

## Prerequisites
- Iru (Kandji) tenant with API access
- Twingate Business or Enterprise plan
- Admin access to both Iru and Twingate

## Device Verification Requirements
A device is considered Iru-verified only if **all** conditions are met:
- Serial number exists in Iru
- Reported to Iru within the past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Step-by-Step

### Generate Iru API Token
1. Iru web app → **Settings** → **Access** (top bar)
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description; save the token
4. In **Manage API Permissions** → **Configure**
5. Under Devices, enable: **Device details** + **Device list**

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL and API token

### Apply to Security Policy
1. Create a macOS **Trusted Profile** in Device Security
2. Set **Iru** as a required Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API permissions | Device details, Device list |

## Gotchas
- After initial setup, status shows **"Waiting to sync"** — devices may temporarily show incorrect verification state; allow a few minutes
- **Recoverable errors** (API unresponsive): integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials, altered permissions): integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials
- No Windows/Linux support — Iru verification is macOS-only

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)