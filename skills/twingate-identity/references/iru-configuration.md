# Iru (formerly Kandji) Configuration

## Summary
Twingate integrates with Iru (previously Kandji) to verify macOS devices via MDM for use in Security Policies. The integration pulls managed device lists via the Iru API and matches device serial numbers to determine trust status. Available on Business and Enterprise plans only.

## Key Information
- macOS devices only
- Device verification checks: serial number match, reported within 7 days, Iru agent installed, MDM profile installed, not removed from Iru
- Sync operates on a pull basis; initial sync shows "Waiting to sync" for a few minutes
- Recoverable errors (API unresponsive): retries automatically, shows last successful sync time
- Unrecoverable errors (invalid credentials/permissions): stops retrying, sends admin email alert

## Prerequisites
- Business or Enterprise Twingate plan
- Iru admin access to generate API tokens
- Required API token permissions: **Device details** and **Device list** (under Devices)

## Step-by-Step

### Generate Iru API Key
1. Iru web app → **Settings** → **Access** (top bar)
2. Scroll to **API Token** → **Add Token**
3. Name and describe the token, save it
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure Integration in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Iru
3. Enter Iru URL and API token
4. Verify status on Device Settings page after sync completes

### Apply to Security Policies
1. Create a macOS Trusted Profile in Device Security
2. Set Iru as a required Trust Method
3. Incorporate the Trusted Profile into Security Policies

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |

## Gotchas
- Initial sync delay: devices may show incorrect Iru state during "Waiting to sync" period; wait a few minutes
- Device not verified if it hasn't reported to Iru within **7 days** (strict cutoff)
- Unrecoverable errors require full reconfiguration—integration stops all retry attempts
- Altering API token permissions after setup triggers unrecoverable error state

## Troubleshooting: "Iru not verified" Causes
- Device not managed by Iru
- No check-in within 7 days
- Iru agent uninstalled
- No MDM profile installed
- Device removed from Iru

## Related Docs
- Device Security / Trusted Profiles configuration
- Security Policies configuration
- Twingate pricing (plan eligibility)