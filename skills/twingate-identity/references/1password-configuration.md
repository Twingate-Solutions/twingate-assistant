# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Integration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers. Admins configure the integration via API key, then enforce it through Trusted Profiles in Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Supported platforms: macOS, Windows, Linux
- Matching mechanism: device serial numbers returned by Twingate Client vs. 1Password Device Trust records
- Device is considered verified if: serial number exists in 1Password AND device passes 1Password's device checks
- Initial sync shows "Waiting to sync" status; resolves within a few minutes
- Error recovery window: 28 hours before integration stops retrying; admin email notification sent on failure

## Prerequisites
- Twingate Business or Enterprise plan
- Access to 1Password Device Trust Console
- Twingate Admin Console access
- Existing Trusted Profiles configured in Twingate

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right) → **Settings**
3. Left panel → **Developers**
4. Click **Create New Key**
5. Name the key and click **Save** (no write permissions needed)

### Connect Integration in Twingate
1. Navigate to **Settings** → **Device Integrations**
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key

### Enforce via Security Policy
1. Create a Trusted Profile for macOS/Windows/Linux
2. Set **1Password Device Trust** as a required Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
| Parameter | Location | Notes |
|---|---|---|
| 1Password Device Trust API Key | Twingate Device Integrations settings | Read-only permissions sufficient |

## Gotchas
- **"Waiting to sync"** after setup is normal; devices may show incorrect verification state during this window
- Device shows `1Password not verified` if: not managed by 1Password OR device `auth_state` is `blocked`
- Integration halts after **28 hours** of failed sync attempts; requires manual reconfiguration with new API credentials
- After 28-hour failure, admin receives email — resolution requires re-entering API key, not just retrying

## Related Docs
- Twingate Trusted Profiles documentation
- Twingate Security Policies documentation
- [Twingate Pricing Page](https://www.twingate.com/pricing)