---
source: https://www.twingate.com/docs/1password-configuration
type: docs
fetched: 2026-08-14
source_version: 9874218f2220dd0c1f46b002379bd87d273c202373566813bc6aacf92024890e
---

# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Integration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers between Twingate clients and 1Password-managed devices. Admins configure this via Trusted Profiles on macOS, Windows, and Linux. Available on Business and Enterprise plans only.

## Key Information
- Verification matches **device serial numbers** from Twingate Client against 1Password Device Trust inventory
- Device is considered verified if: serial number exists in 1Password AND device passes 1Password's device checks
- Integration status visible on Device Integrations page
- Initial sync shows "Waiting to sync" — resolves within a few minutes
- Error recovery window: **28 hours** before integration stops retrying
- Admins receive email notification if integration fails after 28 hours

## Prerequisites
- Business or Enterprise Twingate plan
- Access to 1Password Device Trust Console
- Twingate Admin Console access
- Supported platforms: macOS, Windows, Linux

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right) → **Settings**
3. Left panel → **Developers**
4. Click **Create New Key**
5. Name the key → **Save** (no special write permissions needed)

### Configure in Twingate
1. Navigate to **Settings** → **Device Integrations**
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key

### Apply to Security Policies
1. Create a **Trusted Profile** (macOS/Windows/Linux)
2. Set **1Password Device Trust** as the Trust Method
3. Incorporate the Trusted Profile into a **Security Policy**

## Configuration Values
| Parameter | Value/Location |
|-----------|---------------|
| API Key | Generated in 1Password Device Trust Console → Developers |
| Integration location | Twingate Admin → Settings → Device Integrations |
| Required permissions | None (read-only sufficient) |

## Gotchas
- **"Waiting to sync"** is normal on initial setup — wait a few minutes before troubleshooting
- Devices show `1Password not verified` if: not managed by 1Password OR device `auth_state` is `blocked`
- After errors, integration shows **last successful sync time**, not current status
- If unreachable for **28 hours**, integration stops retrying — must be manually reconfigured with new API credentials
- Resolution for persistent errors: reconfigure integration and input new API client information

## Related Docs
- Twingate Trusted Profiles documentation
- Twingate Security Policies documentation
- [Pricing page](https://www.twingate.com/pricing) (Business/Enterprise plan comparison)