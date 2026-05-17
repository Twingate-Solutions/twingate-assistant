# Kandji Configuration

## Page Title
Kandji Device Integration Configuration for Twingate

## Summary
Twingate integrates with Kandji MDM to verify macOS devices via the Kandji API, matching device serial numbers against managed devices. Verified devices can be used as a trust method in Security Policies. Available on Business and Enterprise plans only.

## Key Information
- **macOS only** — Kandji verification applies exclusively to macOS devices
- Twingate polls Kandji API to retrieve managed device list by serial number
- Sync status visible on Device Settings page; initial sync shows "Waiting to sync" for a few minutes
- Integration supports EU tenants via separate API subdomain format

## Prerequisites
- Twingate Business or Enterprise plan
- Kandji admin access to generate API token
- API token permissions: **Device details** + **Device list** (under Devices)

## Step-by-Step

### Generate Kandji API Key
1. Kandji web app → **Settings** → **Access** tab
2. Scroll to **API Token** → **Add Token**
3. Name and describe the token, save it
4. In **Manage API Permissions** modal → **Configure**
5. Enable: **Device details** and **Device list**

### Configure in Twingate
1. Twingate → **Settings** → **Device Integration**
2. Click **Connect** next to Kandji
3. Enter Kandji URL and API token
4. Incorporate into a macOS **Trusted Profile** via Device Security settings

## Configuration Values

| Parameter | Format |
|-----------|--------|
| Kandji URL (US) | `<subdomain>.api.kandji.io` |
| Kandji URL (EU) | `<subdomain>.api.eu.kandji.io` |
| Required API Permissions | `Device details`, `Device list` |

## Device Verification Requirements
A device is considered Kandji-verified only if ALL conditions are met:
- Serial number present in Kandji
- Reported to Kandji within the **past 7 days**
- Kandji agent installed
- MDM profile installed
- Not removed from Kandji

## Gotchas
- Initial sync delay: devices may show incorrect state for a few minutes after setup
- **Recoverable errors** (API unresponsive): integration shows last successful sync time; auto-resolves when API is reachable
- **Unrecoverable errors** (invalid/deleted credentials, altered permissions): sync stops entirely, admin email notification sent — requires full reconfiguration with new API credentials
- Devices inactive >7 days in Kandji will fail verification even if otherwise managed

## Related Docs
- Twingate Device Security / Trusted Profiles
- Twingate Security Policies
- [Twingate Pricing](https://www.twingate.com/pricing)