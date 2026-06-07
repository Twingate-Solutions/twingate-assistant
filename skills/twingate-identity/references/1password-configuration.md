# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Integration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers. Admins configure the integration via API key and apply it through Trusted Profiles in Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Matches device serial numbers between Twingate Client and 1Password Device Trust
- Supports macOS, Windows, and Linux platforms
- Device verified if: serial number exists in 1Password AND device passes 1Password's device checks
- Initial sync shows "Waiting to sync" status for a few minutes before devices show correct state
- Error retry window: 28 hours before integration stops attempting; admin email notification sent on failure

## Prerequisites
- Twingate Business or Enterprise plan
- Access to 1Password Device Trust Console
- 1Password Device Trust API key (read-only; no special write permissions needed)
- Existing Trusted Profiles setup in Twingate

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right) → **Settings**
3. Left panel → **Developers**
4. Click **Create New Key**
5. Name the key → **Save** (no write permissions required)

### Configure in Twingate
1. Navigate to **Settings** → **Device Integrations**
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key
4. Verify status shows on Device Integrations page

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows/Linux
2. Set 1Password Device Trust as a **Trust Method**
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
| Parameter | Value/Location |
|-----------|---------------|
| API Key source | 1Password Device Trust Console → Settings → Developers |
| Integration location | Twingate Admin → Settings → Device Integrations |
| Required permissions | Read-only (no write permissions needed) |

## Gotchas
- **Sync delay**: After setup, devices may show incorrect verification state during initial "Waiting to sync" period (resolves within minutes)
- **"Not verified" causes**: Device not managed by 1Password, OR device `auth_state` is `blocked`
- **Error recovery**: Auto-retries for 28 hours; after that, manual reconfiguration with new API credentials required
- **Serial number matching**: Integration depends entirely on serial number matching — devices without reported serial numbers will not verify correctly

## Related Docs
- Trusted Profiles configuration
- Device Security Policies
- Twingate pricing page (plan eligibility)