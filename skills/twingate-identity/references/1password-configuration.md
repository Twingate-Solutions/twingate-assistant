# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Configuration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers. Admins configure the integration via API key and enforce it through Trusted Profiles in Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Matches device serial numbers between Twingate Client and 1Password Device Trust
- Supports macOS, Windows, and Linux platforms
- Device considered verified if: serial number exists in 1Password AND device passes 1Password's device checks
- Integration status visible on Device Integrations page after setup

## Prerequisites
- Business or Enterprise Twingate plan
- Access to 1Password Device Trust Console
- Twingate Admin Console access
- No special write permissions needed for the API key

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right) → Settings
3. Left panel → Developers → Create New Key
4. Name the key → Save

### Configure in Twingate
1. Twingate Admin Console → Settings → Device Integrations
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows/Linux
2. Add 1Password Device Trust as a required Trust Method
3. Incorporate Trusted Profile into Security Policies

## Configuration Values
| Parameter | Value |
|-----------|-------|
| API Key | Generated from 1Password Device Trust Console → Developers |
| Platforms supported | macOS, Windows, Linux |

## Gotchas
- After setup, status shows **"Waiting to sync"** for a few minutes — devices may show incorrect verification state during this window
- Device shows `1Password not verified` if: not managed by 1Password, OR `auth_state` is `blocked`
- On API errors, Twingate retries for **28 hours maximum**; if unresolved, integration stops attempting and admin receives email notification
- Recovery from 28-hour timeout requires **reconfiguring the integration with new API credentials**
- Last successful sync time is displayed when errors occur

## Related Docs
- Trusted Profiles documentation
- Device Security / Security Policies
- Twingate pricing page (plan eligibility)