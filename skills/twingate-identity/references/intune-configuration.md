# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security policies. Devices are matched by serial number against Intune-managed devices and must meet specific compliance criteria to access private Resources.

## Key Information
- **Platform support**: macOS and Windows only
- **Verification criteria**: Device must be Intune-managed, reported to Intune within last 7 days, and have Compliance State of `Compliant` or `In-grace period`
- **Matching mechanism**: Twingate Client returns device serial number; matched against Intune tenant device list
- **Use case**: Intune status feeds into Trusted Profiles → Security Policies

## Prerequisites
- Business or Enterprise Twingate plan
- Azure AD App Registration with:
  - `DeviceManagementManagedDevices.Read.All` (Delegated permission)
  - `DeviceManagementManagedDevices.Read.All` (Application permission)
  - Admin consent granted
- Azure credentials: Client ID, Client Secret (Value), Directory (Tenant) ID

## Step-by-Step: Azure Setup
1. Azure Portal → **Azure Active Directory** → **App registrations** → New registration
2. **API permissions** → Add `Microsoft Graph` → Delegated → `DeviceManagementManagedDevices.Read.All`
3. Add `Microsoft Graph` → Application → `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. **Overview** → **Client credentials** → New client secret → save the **Value** immediately
6. Save **Application (client) ID** and **Directory (tenant) ID** from Overview

## Step-by-Step: Twingate Configuration
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Intune → enter credentials
3. Confirm integration status on Device Settings page

## Configuration Values
| Value | Where Found |
|-------|-------------|
| Application (client) ID | Azure App Registration Overview |
| Client Secret Value | Generated in Client credentials (one-time view) |
| Directory (tenant) ID | Azure App Registration Overview |

## Gotchas
- **Client Secret Value is shown only once** — save it immediately after creation
- After setup, status shows "Waiting to sync" for a few minutes — devices may show incorrect state during this period
- **Recoverable errors** (e.g., Intune API unresponsive): integration pauses, resumes automatically when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): integration stops entirely; admin email notification sent; requires full reconfiguration with new API credentials
- `Intune not verified` causes: not managed by Intune, non-compliant state, no check-in within 7 days, serial number retrieval failure

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)