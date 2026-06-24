# Intune Configuration

## Page Title
Intune Configuration (Business & Enterprise only)

## Summary
Twingate integrates with Microsoft Intune via the Intune API to verify device compliance as part of Device Security Trusted Profiles. Devices must be Intune-managed, reported within 7 days, and classified as Compliant or In-grace period to pass verification. Supports macOS and Windows only.

## Key Information
- Verification logic: device serial number matched against Intune-managed device list
- Device passes if: managed by Intune + reported within last 7 days + status is **Compliant** or **In-grace period**
- Platform support: **Mac and Windows only**
- Integration pulls data via Microsoft Graph API using Azure App Registration credentials

## Prerequisites
- Twingate Business or Enterprise plan
- Azure Active Directory access with ability to create App Registrations
- Admin consent rights for Microsoft Graph API permissions

## Step-by-Step: Azure App Registration Setup

1. Azure Portal → **Azure Active Directory** → **App registrations** → New registration
2. **API permissions** → Add permission → **Microsoft Graph** → **Delegated** → `DeviceManagementManagedDevices.Read.All`
3. Add permission → **Microsoft Graph** → **Application** → `DeviceManagementManagedDevices.Read.All`
4. Click **Grant admin consent**
5. Overview → **Client credentials** → New client secret → **Save the Value immediately** (not retrievable later)
6. Save **Application (client) ID** and **Directory (tenant) ID** from Overview

## Step-by-Step: Twingate Configuration

1. Twingate Admin → **Settings** → **Device Integration**
2. Click **Connect** next to Intune → enter credentials (Client ID, Tenant ID, Client Secret)
3. Verify status on Device Settings page (initial state: "Waiting to sync" — resolves in a few minutes)
4. Create a **Trusted Profile** requiring Intune as Trust Method → incorporate into Security Policies

## Configuration Values

| Value | Source |
|---|---|
| Application (client) ID | Azure App Registration Overview |
| Directory (tenant) ID | Azure App Registration Overview |
| Client Secret Value | Generated under Client Credentials (save immediately) |

**Required API Permissions:**
- `DeviceManagementManagedDevices.Read.All` (Delegated)
- `DeviceManagementManagedDevices.Read.All` (Application)

## Gotchas
- Client secret **Value** is only shown once — save it immediately
- Initial sync shows "Waiting to sync"; devices may show incorrect state for a few minutes
- **Recoverable errors** (e.g., API unresponsive): integration pauses, auto-resumes when API is reachable
- **Unrecoverable errors** (e.g., invalid/deleted credentials, altered permissions): integration stops entirely, admin email notification sent — requires full reconfiguration
- `Intune not verified` can occur if serial number cannot be retrieved from device

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)