# 1Password XAM Configuration

## Page Title
1Password Extended Access Management (XAM) Device Trust Integration

## Summary
Twingate integrates with 1Password Device Trust to restrict resource access to verified devices by matching device serial numbers between Twingate Client and 1Password's managed device list. Admins configure this as a Trust Method within Trusted Profiles, which are then applied to Security Policies. Available on Business and Enterprise plans only.

## Key Information
- Matches device serial numbers from Twingate Client against 1Password Device Trust inventory
- Supports macOS, Windows, and Linux platforms
- Device considered verified if: serial number is in 1Password AND device passes 1Password's own device checks
- Integration syncs automatically; status visible on Device Integrations page
- Error retry window: 28 hours before integration stops attempting; admin email notification sent on failure

## Prerequisites
- Twingate Business or Enterprise plan
- Access to 1Password Device Trust Console
- Twingate Admin Console access

## Step-by-Step

### Generate 1Password API Key
1. Log into 1Password Device Trust Console
2. Click user account (upper right)
3. Go to **Settings** → **Developers** (left panel)
4. Click **Create New Key**
5. Name the key, click **Save** (no special write permissions needed)

### Configure in Twingate
1. Navigate to **Settings** → **Device Integrations**
2. Click **Connect** next to 1Password
3. Input the 1Password Device Trust API Key

### Apply to Security Policies
1. Create a Trusted Profile for macOS/Windows/Linux
2. Set **1Password Device Trust** as the required Trust Method
3. Incorporate the Trusted Profile into a Security Policy

## Configuration Values
- **API Key**: Read-only key from 1Password Device Trust (no write permissions required)
- **Integration location**: Twingate Admin Console → Settings → Device Integrations

## Gotchas
- Initial sync shows status **"Waiting to sync"** — devices may show incorrect verification state for a few minutes
- Device shows `1Password not verified` if:
  - Device not managed by 1Password
  - Device `auth_state` is `blocked`
- If 1Password API is unreachable for **>28 hours**, integration stops retrying and requires manual reconfiguration with new API credentials
- On reconnect after errors, resolution is automatic — no manual device state correction needed

## Troubleshooting Reference
| Status | Meaning |
|--------|---------|
| Waiting to sync | Initial setup, sync pending |
| Shows last sync time | Integration healthy |
| Error + last successful sync time | API connectivity issue; retrying up to 28hrs |
| Integration stopped | 28hr window exceeded; reconfigure required |

## Related Docs
- Trusted Profiles configuration
- Security Policies
- Twingate pricing page (plan eligibility)
- Device Integrations overview