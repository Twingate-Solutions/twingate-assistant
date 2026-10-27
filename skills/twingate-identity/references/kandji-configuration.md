---
source: https://www.twingate.com/docs/kandji-configuration
type: docs
fetched: 2026-10-25
source_version: 536ee154558f7f5457430fd10682485f0dcc2455befcd53e93b75c50fff41a2c
trust: official
---

# Iru (Kandji) Configuration — Twingate

## Page Title
Iru (previously Kandji) Configuration

## Summary
Twingate integrates with Iru (formerly Kandji) MDM to verify macOS devices as part of Device Security policies. The integration uses the Iru API to match device serial numbers against managed device lists. Only macOS devices meeting all verification criteria can satisfy Trusted Profile requirements.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Platform**: macOS only
- **Client requirement**: Standalone macOS Twingate Client (not Mac App Store version); can be deployed via Iru Auto App or Twingate download page
- **Sync behavior**: After setup, shows "Waiting to sync" briefly; full sync completes within a few minutes
- **API URL formats**: `<subdomain>.api.kandji.io` or `<subdomain>.api.eu.kandji.io`

## Prerequisites
- Business or Enterprise Twingate plan
- Iru admin access to generate API tokens
- Standalone Twingate macOS Client deployed on managed devices

## Device Verification Criteria
A device is considered Iru-verified only if **all** of the following are true:
- Serial number returned by Iru API
- Reported to Iru within the past 7 days
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Step-by-Step

### 1. Generate Iru API Token
1. In Iru web app → **Settings** → **Access** (top bar)
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description; save the token

### 2. Configure API Permissions
1. In the **Manage API Permissions** modal → **Configure**
2. Under **Devices**, enable:
   - `Device details`
   - `Device list`

### 3. Connect Iru in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Iru URL (`<subdomain>.api.kandji.io` or `<subdomain>.api.eu.kandji.io`) and API token

### 4. Apply to Security Policies
1. Create a Device Security **Trusted Profile** for macOS
2. Set Iru as a required **Trust Method**
3. Add the Trusted Profile to relevant **Security Policies**

## Configuration Values
| Field | Format |
|---|---|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API scopes | `Device details`, `Device list` |

## Gotchas
- **Recoverable errors** (e.g., API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): Integration stops retrying; admin email notification sent — requires full reconfiguration with new API credentials
- Mac App Store Twingate Client is **not supported**; must use standalone client
- Initial post-setup sync delay may cause devices to temporarily show incorrect verification state

## Related Docs
- Twingate Device Security / Trusted Profiles documentation
- Twingate Security Policies documentation
- [Twingate download page](https://www.twingate.com/download)
- Twingate pricing page (plan eligibility)