# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security policies. Devices are verified by matching serial numbers against Intune-managed device lists. Only Mac and Windows devices classified as Compliant or In-grace period that have reported within 7 days qualify.

## Key Information
- Supported platforms: **macOS and Windows only**
- Device verification criteria (all three must be true):
  - Managed by Intune
  - Reported to Intune within the **last 7 days**
  - Intune compliance state is **Compliant** or **In-grace period**
- Twingate pulls device list via Intune API and matches by **serial number**
- Integration status shows "Waiting to sync" initially; full sync takes a few minutes

## Prerequisites
- Twingate Business or Enterprise plan
- Azure Active Directory access with permissions to create App registrations
- Ability to grant admin consent in Azure AD

## Step-by-Step: Azure App Registration

1. Azure Portal → **Azure Active Directory** → **App registrations** → Create new registration
2. Go to **API permissions** → Add permission → **Microsoft Graph** → **Delegated permissions** → select `DeviceManagementManagedDevices.Read.All`
3. Add another permission → **Microsoft Graph** → **Application permissions** → select `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. Go to **Client credentials** → Create new client secret → **save the Value immediately** (not retrievable later)
6. From Overview page, save **Application (client) ID** and **Directory (tenant) ID**

## Step-by-Step: Twingate Configuration

1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Intune → enter credentials (Client ID, Tenant ID, Client Secret)
3. Verify integration status on Device Settings page
4. Create a **Trusted Profile** requiring Intune as Trust Method
5. Incorporate Trusted Profile into **Security Policies**

## Configuration Values
| Value | Source |
|-------|--------|
| Application (client) ID | Azure App Registration Overview |
| Directory (tenant) ID | Azure App Registration Overview |
| Client Secret Value | Azure App Registration → Client credentials |

## Gotchas
- Client secret **Value** is only shown once—save it immediately
- Both Delegated **and** Application permissions for `DeviceManagementManagedDevices.Read.All` are required
- Initial sync shows "Waiting to sync"—devices may show incorrect state for a few minutes
- **Recoverable errors** (API unresponsive): integration auto-retries, shows last successful sync time
- **Unrecoverable errors** (invalid/deleted credentials, altered permissions): integration stops, admin email notification sent—requires full reconfiguration with new credentials
- `Intune not verified` can also occur if Twingate cannot retrieve the device serial number

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)