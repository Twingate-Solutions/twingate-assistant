# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security policies. Devices must be Intune-managed, compliant (or in grace period), and have reported within the last 7 days to satisfy Trusted Profile requirements. Supports macOS and Windows only.

## Key Information
- Matching is done via **device serial number** against Intune-managed device list
- Device must meet **all three criteria**: managed by Intune + reported within 7 days + status is `Compliant` or `In-grace period`
- Integration syncs periodically; initial state shows "Waiting to sync" for a few minutes
- Recoverable errors (API unresponsive): retries automatically, shows last successful sync time
- Unrecoverable errors (invalid credentials/permissions): stops retrying, sends admin email alert

## Prerequisites
- Business or Enterprise Twingate plan
- Azure Active Directory access with ability to create App Registrations
- Admin consent rights for Microsoft Graph API permissions

## Step-by-Step: Azure App Registration Setup
1. Azure Portal → **Azure Active Directory** → **App registrations** → New registration
2. Go to **API permissions** → Add permission → **Microsoft Graph** → **Delegated permissions** → select `DeviceManagementManagedDevices.Read.All`
3. Add permission → **Microsoft Graph** → **Application permissions** → select `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. Go to **Client credentials** → Create new client secret → **save the Value immediately** (not accessible again)
6. From Overview page, save **Application (client) ID** and **Directory (tenant) ID**

## Step-by-Step: Twingate Configuration
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Intune → enter credentials (Client ID, Tenant ID, Client Secret)
3. Verify integration status on Device Settings page

## Configuration Values
| Value | Source |
|-------|--------|
| Application (client) ID | Azure App Registration Overview |
| Directory (tenant) ID | Azure App Registration Overview |
| Client Secret Value | Azure App Registration → Client credentials (save immediately) |

**Required API Permission:** `DeviceManagementManagedDevices.Read.All` (both Delegated and Application)

## Gotchas
- Client secret **Value** is only shown once at creation — save it immediately
- Both **Delegated** and **Application** permission types are required for the same permission
- Admin consent must be explicitly granted after adding permissions
- Serial number retrieval failure on the client side will cause `Intune not verified` regardless of Intune status
- For unrecoverable errors, must fully reconfigure the integration with new credentials

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)