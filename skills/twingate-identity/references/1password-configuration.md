# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Integration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers. Admins configure this as a Trust Method within Trusted Profiles, which feed into Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Integration matches device serial numbers between Twingate Client and 1Password Device Trust
- Supported platforms: macOS, Windows, Linux
- Device considered verified if: serial number exists in 1Password AND device passes 1Password's device checks
- Initial sync shows "Waiting to sync" status; resolves within a few minutes
- On API errors, Twingate retries for 28 hours before stopping; admin email notification sent if unresolved

## Prerequisites
- Twingate Business or Enterprise plan
- 1Password Device Trust Console admin access
- Existing Trusted Profiles setup in Twingate

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right)
3. Go to **Settings → Developers**
4. Click **Create New Key**
5. Name the key, click **Save** (no special write permissions needed)

### Configure in Twingate
1. Navigate to **Settings → Device Integrations**
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows/Linux
2. Set **1Password Device Trust** as a Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
| Parameter | Details |
|-----------|---------|
| API Key permissions | Read-only (no write permissions required) |
| Retry window on error | 28 hours |
| Supported OS | macOS, Windows, Linux |

## Gotchas
- **"Waiting to sync"** state after initial setup is normal; devices may show incorrect verification state during this window
- Device marked **"1Password not verified"** if: not managed by 1Password OR `auth_state` is `blocked`
- If 28-hour retry window expires without reconnecting, integration stops entirely — requires manual reconfiguration with new API credentials
- Admins receive email notification when integration needs attention after retry window expires

## Related Docs
- Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (for plan eligibility)