---
source: https://www.twingate.com/docs/kandji-configuration
type: docs
fetched: 2026-08-14
source_version: 432065d46f17cc57860e73020ee78518669f83fb9750f99e15bc3609135f24d0
---

# Kandji (Iru) Configuration

## Page Title
Iru (Kandji) Configuration - Twingate Device Integration

## Summary
Twingate integrates with Iru (formerly Kandji) to verify macOS devices against MDM-managed device lists. The integration uses the Iru API to pull managed device serial numbers and match them against connecting devices. Verified devices can be required for Resource access via Security Policies.

## Key Information
- **Plan requirement**: Business & Enterprise only
- **Platform support**: macOS only
- **Verification method**: Serial number matching against Iru-managed device list
- **Sync polling**: Twingate pulls device list via Iru API periodically

## Prerequisites
- Iru (Kandji) account with admin access
- Iru API token with specific permissions (Device details + Device list)
- Twingate Business or Enterprise plan

## Step-by-Step

### Generate Iru API Token
1. Iru web app → Settings → Access → API Token → Add Token
2. Name and describe the token, save it
3. In **Manage API Permissions** modal → Configure
4. Under Devices, enable: **Device details** and **Device list**

### Configure in Twingate
1. Twingate Admin → Settings → Device Integration
2. Select **Connect** next to Iru
3. Enter Iru URL and API token

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API Permissions | Device details, Device list |

## Device Verification Requirements
A device is considered **Iru-verified** only if ALL conditions are met:
- Serial number exists in Iru tenant
- Reported to Iru within past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Gotchas
- After initial setup, status shows "Waiting to sync" — devices may show incorrect state for a few minutes
- **Recoverable errors** (API unresponsive): Integration retries automatically, last successful sync time preserved
- **Unrecoverable errors** (invalid/deleted credentials, changed permissions): Integration stops retrying; admin email notification sent; requires full reconfiguration with new API credentials
- Only macOS devices are supported — no Windows/Linux verification via this integration

## Related Docs
- Device Security / Trusted Profiles (Security Policies configuration)
- Twingate pricing page (plan eligibility)