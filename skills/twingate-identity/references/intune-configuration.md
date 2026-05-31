# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security policies. Devices must be Intune-managed, reported within 7 days, and classified as Compliant or In-grace period to pass verification. Supports macOS and Windows only.

## Key Information
- Verification uses device **serial number** matched against Intune-managed device list
- Device must meet **all three** criteria: managed by Intune, reported within last 7 days, compliance state = `Compliant` or `In-grace period`
- After configuring, sync takes a few minutes before device states appear correctly
- Integration status visible at **Settings → Device Integration**

## Prerequisites
- Business or Enterprise Twingate plan
- Azure Active Directory with App Registration access
- Admin consent rights to grant Microsoft Graph API permissions
- macOS or Windows devices (only supported platforms)

## Step-by-Step: Azure App Registration

1. Azure portal → **Azure Active Directory** → **App registrations** → Create new registration
2. Go to **API permissions** → Add permission → **Microsoft Graph** → **Delegated permissions** → select `DeviceManagementManagedDevices.Read.All`
3. Add permission → **Microsoft Graph** → **Application permissions** → select `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. Go to **Client credentials** → Create new client secret → **Save the Value immediately** (not accessible again)
6. From Overview page, save **Application (client) ID** and **Directory (tenant) ID**

## Step-by-Step: Twingate Configuration

1. Twingate Admin Console → **Settings** → **Device Integration**
2. Click **Connect** next to Intune → enter credentials (Client ID, Tenant ID, Client Secret)
3. Verify integration status on Device Settings page

## Configuration Values

| Value | Where to Find |
|-------|--------------|
| Application (client) ID | App Registration → Overview |
| Directory (tenant) ID | App Registration → Overview |
| Client Secret Value | App Registration → Client credentials (save immediately) |

**Required API Permission:** `DeviceManagementManagedDevices.Read.All` (both Delegated and Application)

## Gotchas
- Client secret **Value** cannot be retrieved after initial creation — save immediately
- Initial sync shows "Waiting to sync"; device states may be incorrect for a few minutes
- **Recoverable errors** (API unresponsive): integration shows last successful sync time, auto-resolves when API is reachable
- **Unrecoverable errors** (invalid credentials, altered permissions): sync stops entirely, admin email notification sent — requires full reconfiguration with new credentials
- Serial number retrieval failure causes `Intune not verified` status even if device is otherwise compliant

## Related Docs
- Device Security / Trusted Profiles configuration
- Security Policies documentation
- Twingate pricing page (plan eligibility)