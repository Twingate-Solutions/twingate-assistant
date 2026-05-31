# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Configuration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers. Admins configure the integration via API key and incorporate it into Trusted Profiles within Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Matches device serial numbers from Twingate Client against 1Password Device Trust managed devices
- Supported platforms: macOS, Windows, Linux
- Device is "1Password-verified" if: serial number exists in 1Password Device Trust AND device passes 1Password's device checks
- Integration status visible on Device Integrations page
- Initial sync shows "Waiting to sync" for a few minutes before first state resolution

## Prerequisites
- Twingate Business or Enterprise plan
- Access to 1Password Device Trust Console
- Twingate Admin Console access
- 1Password Device Trust API key (no special write permissions required)

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right)
3. Navigate to **Settings → Developers**
4. Click **Create New Key**
5. Name the key, click **Save**

### Configure in Twingate
1. Navigate to **Settings → Device Integrations**
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key

### Apply to Security Policies
1. Create a Trusted Profile for macOS, Windows, or Linux
2. Set **1Password Device Trust** as a required Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
| Parameter | Value |
|-----------|-------|
| API Key permissions | Read-only (no write permissions needed) |
| Supported OS | macOS, Windows, Linux |

## Gotchas
- **Initial sync delay**: After setup, status shows "Waiting to sync" — devices may show incorrect verification state during this window (resolves within minutes)
- **"1Password not verified" causes**: Device not managed by 1Password, OR device `auth_state` is `blocked`
- **Error recovery window**: Twingate retries failed connections for **28 hours**; after 28 hours, integration stops retrying and admin receives email notification
- **Recovery action**: If integration fails beyond 28 hours, reconfigure the integration with new API client credentials
- Last successful sync time is displayed during error states

## Related Docs
- Trusted Profiles documentation
- Device Security policies
- Twingate pricing page (Business/Enterprise plan details)
- Device Integrations settings