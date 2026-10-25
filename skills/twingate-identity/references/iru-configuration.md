---
source: https://www.twingate.com/docs/iru-configuration
type: docs
fetched: 2026-10-25
source_version: 536ee154558f7f5457430fd10682485f0dcc2455befcd53e93b75c50fff41a2c
trust: official
---

# Iru (formerly Kandji) Configuration

## Page Title
Iru Configuration — Twingate Device Integration for macOS

## Summary
Twingate integrates with Iru (previously Kandji) MDM to verify macOS devices via the Iru API, matching device serial numbers against managed device lists. Verified devices can satisfy Trusted Profile requirements within Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Verification pulls device list via Iru API; matches Twingate Client-reported serial numbers
- Device considered Iru-verified only if: serial number in Iru, reported within 7 days, Iru agent installed, MDM profile present, not removed from Iru
- **Mac App Store Twingate Client is not supported** — use standalone macOS Client (via Iru Auto App or Twingate download page)
- After initial setup, status shows "Waiting to sync" for a few minutes before verification states populate correctly

## Prerequisites
- Twingate Business or Enterprise plan
- Iru admin access to generate API token
- Standalone Twingate macOS Client deployed on endpoints

## Step-by-Step

### Generate Iru API Token
1. In Iru web app → **Settings** (left panel) → **Access** (top bar)
2. Scroll to **API Token** → click **Add Token**
3. Enter Name and Description → save the token value
4. In **Manage API Permissions** modal → click **Configure**
5. Under Devices, enable: **Device details** and **Device list**

### Configure Integration in Twingate
1. Navigate to **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL and API token

## Configuration Values

| Parameter | Format |
|-----------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API permissions | Device details, Device list |

## Gotchas
- **Recoverable errors** (API unresponsive): Integration shows last successful sync time; auto-resolves when API is reachable again
- **Unrecoverable errors** (invalid/deleted credentials or altered permissions): Integration stops connecting; admin email notification sent; requires manual reconfiguration with new API credentials
- Devices show "Iru not verified" if any verification condition is unmet (agent uninstalled, no MDM profile, not reporting, removed from Iru)
- Initial sync delay — do not assume failure if verification states are missing immediately after setup

## Related Docs
- Twingate Device Security / Trusted Profiles
- Twingate Security Policies
- [Twingate download page](https://www.twingate.com/download)
- Twingate pricing page (for plan eligibility)