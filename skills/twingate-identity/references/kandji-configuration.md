# Kandji (Iru) Configuration

## Page Title
Iru (Kandji) Configuration — Twingate Device Integration

## Summary
Twingate integrates with Iru (formerly Kandji) to verify macOS devices against an MDM-managed device list. Verified devices can satisfy Trusted Profile requirements within Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Verification uses Iru API to pull managed device serial numbers; Twingate Client matches device serial number against this list
- **macOS only**
- Sync runs periodically; initial status shows "Waiting to sync" for a few minutes before device states populate
- Recoverable errors (API unresponsive): integration pauses, auto-resumes when API is reachable
- Unrecoverable errors (invalid/deleted credentials, changed permissions): integration stops, admin notified by email; requires manual reconfiguration

## Prerequisites
- Business or Enterprise Twingate plan
- Access to Iru web app with permission to create API tokens
- Required API token permissions: **Device details** and **Device list** (under Devices)

## Step-by-Step

### Generate Iru API Key
1. Iru web app → **Settings** (left panel) → **Access** (top bar)
2. Scroll to **API Token** → **Add Token**
3. Enter Name and Description → save the token
4. In **Manage API Permissions** modal → **Configure**
5. Under Devices, enable **Device details** and **Device list**

### Configure in Twingate
1. Twingate Admin → **Settings** → **Device Integration**
2. Select **Connect** next to Iru
3. Enter Iru URL and API token
4. Verify status on Device Settings page

### Incorporate into Security Policies
1. Create a Trusted Profile for macOS
2. Set Iru as a required Trust Method
3. Add Trusted Profile to Security Policies

## Configuration Values

| Field | Format |
|-------|--------|
| Iru URL (US) | `<subdomain>.api.kandji.io` |
| Iru URL (EU) | `<subdomain>.api.eu.kandji.io` |

## Device Verification Requirements (all must be met)
- Serial number present in Iru tenant
- Reported to Iru within past **7 days**
- Iru agent installed
- MDM profile installed
- Not removed from Iru

## Gotchas
- Initial sync delay: devices may show incorrect verification state for a few minutes after setup
- Changing API token permissions after setup causes an unrecoverable error requiring full reconfiguration
- Integration only verifies macOS devices; no other OS supported
- "Iru not verified" is expected if device hasn't checked in within 7 days, even if otherwise healthy

## Related Docs
- Device Security / Trusted Profiles configuration
- Security Policies configuration
- Twingate pricing page (plan eligibility)