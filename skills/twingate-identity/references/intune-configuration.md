# Intune Configuration

## Page Title
Intune Configuration (Twingate)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security policies. Devices must be Intune-managed, compliant (or in-grace period), and have reported within 7 days to satisfy Trusted Profile requirements. Available on Business and Enterprise plans only.

## Key Information
- Supported platforms: **macOS and Windows only**
- Verification criteria: device managed by Intune + reported within last 7 days + compliance state is `Compliant` or `In-grace period`
- Twingate matches device serial numbers against Intune-managed device list
- Integration pulls data via Intune API (Microsoft Graph)

## Prerequisites
- Twingate Business or Enterprise plan
- Azure AD access with ability to register apps and grant admin consent
- Required Microsoft Graph permissions:
  - `DeviceManagementManagedDevices.Read.All` (Delegated)
  - `DeviceManagementManagedDevices.Read.All` (Application)

## Step-by-Step

### Azure Setup
1. Azure Portal → **Azure Active Directory** → **App registrations** → Create new registration
2. Go to **API permissions** → Add permission → **Microsoft Graph** → **Delegated** → `DeviceManagementManagedDevices.Read.All`
3. Add permission → **Microsoft Graph** → **Application** → `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. Go to **Client credentials** → Create new client secret → **save the Value immediately** (not accessible again)
6. Save **Application (client) ID** and **Directory (tenant) ID** from Overview page

### Twingate Setup
1. Settings → **Device Integration** → **Connect** next to Intune
2. Input credentials (Client ID, Tenant ID, Client Secret)
3. Verify status on Device Settings page

### Policy Integration
- Create a Trusted Profile for macOS/Windows requiring Intune as Trust Method
- Incorporate Trusted Profile into Security Policies

## Configuration Values
| Value | Where to Find |
|-------|--------------|
| Application (client) ID | App registration Overview |
| Directory (tenant) ID | App registration Overview |
| Client Secret Value | Generated once at creation |

## Gotchas
- Client secret **Value** is only shown once — save immediately
- After setup, status shows "Waiting to sync" for a few minutes; devices may show incorrect state during this window
- **Recoverable errors** (e.g., API unresponsive): last successful sync time is preserved; auto-resolves when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): integration stops retrying; admin email notification sent; requires full reconfiguration with new credentials
- `Intune not verified` causes: not managed by Intune, non-compliant state, no report in 7 days, serial number retrieval failure

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)