# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security Trusted Profiles. Devices must be Intune-managed, reported within 7 days, and classified as **Compliant** or **In-grace period** to pass verification. Supports macOS and Windows only.

## Key Information
- Verification uses device **serial number** matched against Intune-managed device list
- Intune status is pulled via Microsoft Graph API
- Integration syncs periodically; initial sync shows "Waiting to sync" for a few minutes
- Verified devices can be required in Security Policies via Trusted Profiles

## Prerequisites
- Business or Enterprise Twingate plan
- Azure Active Directory access with ability to create App Registrations
- Admin consent rights for Microsoft Graph API permissions

## Step-by-Step: Azure App Registration Setup

1. Azure Portal → **Azure Active Directory** → **App registrations** → Create new registration
2. Go to **API permissions** → Add permission → **Microsoft Graph** → **Delegated permissions** → `DeviceManagementManagedDevices.Read.All`
3. Add another permission → **Microsoft Graph** → **Application permissions** → `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. Go to **Client credentials** → Create new client secret → **Save the Value immediately** (not accessible again)
6. Save **Application (client) ID** and **Directory (tenant) ID** from Overview page

## Step-by-Step: Twingate Configuration

1. Twingate → **Settings** → **Device Integration**
2. Select **Connect** next to Intune → input credentials (Client ID, Tenant ID, Client Secret)
3. Verify integration status on Device Settings page

## Configuration Values
| Value | Where to Find |
|---|---|
| Application (client) ID | App Registration → Overview |
| Directory (tenant) ID | App Registration → Overview |
| Client Secret Value | App Registration → Client credentials (save at creation) |

## Gotchas
- Initial sync shows **"Waiting to sync"** — devices may show incorrect state for a few minutes
- `Intune not verified` causes: device not managed by Intune, non-compliant status, no check-in within 7 days, serial number retrieval failure
- **Recoverable errors** (API unresponsive): integration pauses, auto-recovers when API is reachable; last successful sync time is preserved
- **Unrecoverable errors** (invalid credentials, altered permissions): integration stops completely, admin email notification sent → must reconfigure with new credentials
- Only **Mac and Windows** devices supported

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)