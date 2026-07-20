# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Integration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers. Admins configure the integration via API key and incorporate it into Trusted Profiles within Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Matches device serial numbers from Twingate Client against 1Password Device Trust managed devices
- Supports macOS, Windows, and Linux platforms
- Device is considered verified if: serial number exists in 1Password AND device passes 1Password's device checks
- Integration status visible on Device Integrations page after setup
- Error retry window: 28 hours before integration stops attempting reconnection
- Admin email notification sent if 28-hour reconnection window expires

## Prerequisites
- Twingate Business or Enterprise plan
- Access to 1Password Device Trust Console
- 1Password Device Trust API key (no special write permissions required)
- Twingate Admin Console access

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right)
3. Navigate to **Settings → Developers**
4. Click **Create New Key**
5. Name the key, click **Save** (no write permissions needed)

### Configure in Twingate
1. Go to **Settings → Device Integrations**
2. Click **Connect** next to 1Password
3. Enter the 1Password Device Trust API Key

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows/Linux
2. Set **1Password Device Trust** as a Trust Method
3. Incorporate the Trusted Profile into Security Policies

## Configuration Values
| Parameter | Value/Location |
|---|---|
| API Key source | 1Password Device Trust Console → Settings → Developers |
| Integration location | Twingate Admin → Settings → Device Integrations |
| Supported OS | macOS, Windows, Linux |

## Gotchas
- **Initial sync delay**: Status shows "Waiting to sync" after setup; device states may be incorrect for several minutes
- **"1Password not verified" causes**: Device not managed by 1Password, OR device `auth_state` is `blocked`
- **28-hour retry limit**: If 1Password API is unreachable for 28 hours, integration stops retrying and requires manual reconfiguration with new API credentials
- **Error recovery**: After 28-hour failure, reconfigure integration with fresh API key—errors do not auto-resolve after the window expires

## Related Docs
- Trusted Profiles documentation
- Device Security / Security Policies
- Twingate pricing page (plan eligibility)
- Device Integrations settings