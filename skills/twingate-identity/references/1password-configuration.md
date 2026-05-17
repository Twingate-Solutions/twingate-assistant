# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Integration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers between Twingate Clients and 1Password-managed devices. Admins configure this as a Trust Method within Trusted Profiles, which are then applied to Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Matches device serial numbers from Twingate Client against 1Password Device Trust inventory
- Supports macOS, Windows, and Linux platforms
- Device is considered verified only if: (1) serial number exists in 1Password Device Trust AND (2) device passes 1Password's device checks
- Initial sync shows "Waiting to sync" status — allow a few minutes before full verification state is available

## Prerequisites
- Twingate Business or Enterprise plan
- Access to 1Password Device Trust Console
- Admin access to Twingate Admin Console

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right) → **Settings**
3. Left panel → **Developers**
4. Click **Create New Key**
5. Name it, click **Save** (no special write permissions needed)

### Configure in Twingate
1. Navigate to **Settings** → **Device Integrations**
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows/Linux
2. Add **1Password Device Trust** as a required Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
- **API Key**: No special write permissions required
- **Integration location**: Settings → Device Integrations in Twingate Admin Console

## Gotchas
- **Initial sync delay**: Status shows "Waiting to sync" after setup; devices may have incorrect verification state until sync completes (a few minutes)
- **Device "not verified" causes**: Device not managed by 1Password, OR device `auth_state` is `blocked`
- **Error recovery window**: Twingate retries connecting to 1Password API for **28 hours** after an error; resolves automatically when API is reachable
- **After 28 hours**: Integration stops retrying; admin receives email notification; fix requires reconfiguring the integration with new API credentials
- **Last successful sync time**: Displayed on Device Integrations page during error states

## Related Docs
- Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)