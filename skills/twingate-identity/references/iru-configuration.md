# Iru (Kandji) Configuration

## Summary
Twingate integrates with Iru (formerly Kandji) to verify macOS devices for managed device access enforcement. The integration uses the Iru API to match device serial numbers against managed device lists. Available on Business and Enterprise plans only.

## Key Information
- **macOS only** — only macOS devices can be verified through this integration
- Device verification pulls serial numbers via Iru API and matches against Twingate Client-reported serial numbers
- Sync delay expected after initial setup ("Waiting to sync" state lasts a few minutes)
- Recoverable errors (API unresponsive): auto-resolves when API is reachable again
- Unrecoverable errors (invalid credentials/permissions): triggers admin email notification, requires manual reconfiguration

## Prerequisites
- Business or Enterprise Twingate plan
- Iru account with admin access to generate API tokens
- Iru API token with permissions: **Device details** + **Device list** (under Devices)

## Device Verification Requirements (all must be true)
- Serial number present in Iru
- Reported to Iru within past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Step-by-Step

### Generate Iru API Token
1. Iru web app → **Settings** → **Access** (top bar)
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → save token value
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Iru URL and API token

### Incorporate into Security Policies
1. Navigate to Device Security → Trusted Profiles
2. Create/edit a macOS Trusted Profile
3. Set Iru as a **Trust Method**
4. Apply Trusted Profile to Security Policies

## Configuration Values

| Parameter | Format |
|-----------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |

## Gotchas
- Initial sync shows "Waiting to sync" — devices may show incorrect verification state during this window
- Unrecoverable errors **stop retry attempts** entirely; must reconfigure manually
- Altering API token permissions after setup causes unrecoverable error
- 7-day reporting window is strict — inactive devices fail verification automatically

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)