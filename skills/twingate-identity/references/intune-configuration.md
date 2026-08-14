---
source: https://www.twingate.com/docs/intune-configuration
type: docs
fetched: 2026-08-14
source_version: 0834442d186fb0dd23c9e40f92592dc45a751f0a3819b419a48d39deab95d4ca
---

# Intune Configuration

## Page Title
Twingate Intune Integration Configuration

## Summary
Twingate integrates with Microsoft Intune via API to verify device compliance as part of Device Security policies. Devices are validated by matching serial numbers against Intune-managed devices and checking compliance status. Available on Business and Enterprise plans only.

## Key Information
- Supports **macOS and Windows** devices only
- Device verification requires all three conditions:
  - Managed by Intune
  - Reported to Intune within **last 7 days**
  - Compliance state is **Compliant** or **In-grace period**
- Twingate pulls device list via Intune API; Client matches device serial numbers
- Integration status shows on Device Settings page after configuration

## Prerequisites
- Business or Enterprise Twingate plan
- Azure AD App Registration with:
  - `DeviceManagementManagedDevices.Read.All` (Delegated permissions)
  - `DeviceManagementManagedDevices.Read.All` (Application permissions)
  - Admin consent granted
- Azure credentials: Client ID, Client Secret (Value), Directory (Tenant) ID

## Step-by-Step

### Azure Setup
1. Azure Portal → Azure Active Directory → App registrations → New registration
2. API permissions → Add `Microsoft Graph` > Delegated → `DeviceManagementManagedDevices.Read.All`
3. Add `Microsoft Graph` > Application → `DeviceManagementManagedDevices.Read.All`
4. Grant admin consent
5. App registration Overview → Client credentials → New client secret
6. **Save the secret Value immediately** (not accessible again)
7. Save `Application (client) ID` and `Directory (tenant) ID`

### Twingate Setup
1. Settings → Device Integration → Connect (next to Intune)
2. Input Client ID, Client Secret, Tenant ID
3. Create Trusted Profile requiring Intune as Trust Method
4. Apply Trusted Profile to Security Policies

## Configuration Values
| Parameter | Source |
|-----------|--------|
| Application (client) ID | Azure App Registration Overview |
| Client Secret Value | Azure App Registration → Client credentials |
| Directory (tenant) ID | Azure App Registration Overview |

## Gotchas
- Initial sync shows **"Waiting to sync"** — devices may show incorrect state for a few minutes; wait for sync to complete
- `Intune not verified` reasons: not Intune-managed, non-compliant state, stale (>7 days), serial number unreadable, Intune data unretrievable
- **Recoverable errors** (API unresponsive): integration pauses, retries automatically; last successful sync time displayed
- **Unrecoverable errors** (invalid/deleted credentials, altered permissions): integration stops entirely, admin email notification sent — requires full reconfiguration with new API credentials
- Only serial number matching is used — no other device identifiers

## Related Docs
- Device Security / Trusted Profiles documentation
- Security Policies configuration
- Twingate pricing page (plan eligibility)