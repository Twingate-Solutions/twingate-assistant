---
source: https://www.twingate.com/docs/iru-configuration
type: docs
fetched: 2026-08-14
source_version: 432065d46f17cc57860e73020ee78518669f83fb9750f99e15bc3609135f24d0
---

# Iru (Kandji) Configuration

## Summary
Twingate integrates with Iru (formerly Kandji) to verify macOS devices via the Iru API, matching device serial numbers against managed device lists. Verified devices can be used as trust requirements in Security Policies. Available on Business and Enterprise plans only.

## Key Information
- **macOS only** — Iru verification applies exclusively to macOS devices
- Twingate pulls managed device list via Iru API; matches on device serial number
- Sync shows "Waiting to sync" initially; resolves within a few minutes
- Recoverable errors (API unresponsive): auto-resolves when API is reachable again
- Unrecoverable errors (invalid credentials/permissions): admin email notification sent; requires manual reconfiguration

## Prerequisites
- Business or Enterprise Twingate plan
- Iru tenant with admin access to generate API tokens
- API token permissions: **Device details** + **Device list** (under Devices)

## Device Verification Requirements
A device is considered Iru-verified only if **all** conditions are met:
- Serial number present in Iru
- Reported to Iru within the past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Step-by-Step

### Generate Iru API Key
1. Iru web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → save the token
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL and API token

### Incorporate into Security Policies
1. Navigate to Device Security → Trusted Profiles
2. Create/edit a macOS Trusted Profile
3. Set Iru as a required Trust Method
4. Attach Trusted Profile to Security Policies

## Configuration Values

| Parameter | Format |
|-----------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |

## Gotchas
- Initial sync shows "Waiting to sync" — devices may have incorrect verification state during this window
- Altering API token permissions after setup causes unrecoverable error requiring full reconfiguration
- Devices not reporting to Iru for >7 days will lose verified status even if otherwise managed
- Unrecoverable errors halt all sync attempts until admin manually reconfigures

## Related Docs
- Device Security / Trusted Profiles configuration
- Security Policies documentation
- Twingate pricing page (plan eligibility)