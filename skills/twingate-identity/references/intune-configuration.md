# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security policies. Devices must be Intune-managed, reported within 7 days, and classified as Compliant or In-grace period to pass verification. Supports macOS and Windows only.

## Key Information
- Twingate matches device serial numbers against Intune-managed device list
- Verification requires: managed by Intune + reported within last 7 days + status is `Compliant` or `In-grace period`
- Integration syncs periodically; initial sync shows "Waiting to sync" for a few minutes
- Recoverable errors (API unresponsive): auto-retry, last successful sync time displayed
- Unrecoverable errors (invalid credentials/permissions): integration stops, admin email notification sent

## Prerequisites
- Business or Enterprise Twingate plan
- Azure Active Directory access with ability to create App Registrations
- Admin consent rights in Azure AD

## Step-by-Step

### Azure App Registration Setup
1. Azure Portal → **Azure Active Directory** → **App registrations** → New registration
2. **API permissions** → Add **Microsoft Graph** → **Delegated permissions** → `DeviceManagementManagedDevices.Read.All`
3. Add **Microsoft Graph** → **Application permissions** → `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. Go to **Client credentials** → Create new client secret → **Save the Value immediately** (not retrievable later)
6. From Overview page, save **Application (client) ID** and **Directory (tenant) ID**

### Twingate Configuration
1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Intune → Enter credentials
3. Verify sync status on Device Settings page

### Security Policy Integration
- Create a Trusted Profile for macOS/Windows with Intune as required Trust Method
- Attach Trusted Profile to Security Policies

## Configuration Values
| Field | Source |
|-------|--------|
| Client Secret Value | Azure App Registration → Client credentials |
| Application (client) ID | Azure App Registration Overview |
| Directory (tenant) ID | Azure App Registration Overview |

**Required API Permissions:**
- `DeviceManagementManagedDevices.Read.All` (Delegated)
- `DeviceManagementManagedDevices.Read.All` (Application)

## Gotchas
- Serial number must be retrievable from the device — failure to retrieve causes "Intune not verified"
- Initial sync delay: devices show incorrect state until sync completes (few minutes)
- Unrecoverable errors require full reconfiguration with new API credentials
- Client secret value is only shown once at creation time — save immediately
- Platform support is **Mac and Windows only** (no mobile/Linux)

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies documentation
- Twingate pricing page (plan eligibility)