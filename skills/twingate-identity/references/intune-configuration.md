# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security Trusted Profiles. Devices must be Intune-managed, compliant (or in grace period), and have reported to Intune within 7 days to pass verification. Supports macOS and Windows only.

## Key Information
- Verification checks: device is Intune-managed + compliance state is `Compliant` or `In-grace period` + reported to Intune within last 7 days
- Twingate matches device serial numbers against Intune-managed device list
- After setup, initial sync shows "Waiting to sync" status for a few minutes
- Integration visible at: **Settings → Device Integration**

## Prerequisites
- Business or Enterprise Twingate plan
- Azure AD App Registration with:
  - `DeviceManagementManagedDevices.Read.All` (Delegated permission)
  - `DeviceManagementManagedDevices.Read.All` (Application permission)
  - Admin consent granted
- Client Secret, Application (Client) ID, and Directory (Tenant) ID

## Step-by-Step

### Azure Setup
1. Azure Portal → **Azure Active Directory → App registrations** → New registration
2. **API permissions** → Add `Microsoft Graph` → Delegated → `DeviceManagementManagedDevices.Read.All`
3. Add `Microsoft Graph` → Application → `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. **Overview → Client credentials** → New client secret → **save the Value immediately**
6. Save **Application (client) ID** and **Directory (tenant) ID** from Overview

### Twingate Setup
1. Navigate to **Settings → Device Integration**
2. Click **Connect** next to Intune, input credentials
3. Confirm sync status on Device Settings page

### Policy Setup
1. Create a Trusted Profile for macOS/Windows requiring Intune as Trust Method
2. Incorporate Trusted Profile into Security Policies

## Configuration Values
| Field | Source |
|---|---|
| Client Secret Value | Azure App Registration → Client credentials |
| Application (Client) ID | Azure App Registration → Overview |
| Directory (Tenant) ID | Azure App Registration → Overview |

## Gotchas
- Client secret Value is only shown once—save it immediately
- Both Delegated **and** Application permissions required for `DeviceManagementManagedDevices.Read.All`
- Serial number must be retrievable from the device; failure to retrieve = `Intune not verified`
- **Recoverable errors** (API unresponsive): integration shows last successful sync, auto-resolves when API is reachable
- **Unrecoverable errors** (invalid credentials, altered permissions): integration stops retrying; admin email notification sent; requires full reconfiguration with new credentials
- iOS/Android devices not supported—macOS and Windows only

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)