# Deploy Twingate Client with Microsoft Intune/Endpoint Manager

## Summary
Three methods to deploy the Twingate Windows Client via Microsoft Intune: Line-of-business app package, Platform Scripts (PowerShell one-time), and Detection & Remediation (scheduled compliance). Each method supports MSI command-line arguments for tenant configuration.

## Key Information
- All methods use the Twingate Windows MSI installer
- MSI command-line arguments configure tenant name and auto-update behavior
- Detection & Remediation requires Windows 10/11 Enterprise E3 or E5 licenses
- Example scripts available in Twingate's public GitHub repository
- Scripts must run as system user (not logged-on credentials)

## Prerequisites
- Microsoft Intune/Endpoint Manager access
- Twingate Windows MSI installer downloaded
- Tenant name available for command-line arguments
- For Detection & Remediation: Windows 10/11 Enterprise E3/E5 licenses
- Review [Windows Managed Device page](https://www.twingate.com/docs/windows-managed-device) before proceeding

## Method 1: Line-of-Business App (Endpoint Manager)

1. Download Twingate Windows MSI installer
2. Intune → **Apps** → **Add**
3. Select app type: **Other** → **Line-of-business app**
4. Upload MSI file
5. Fill in Publisher and **command-line arguments** (tenant name, update options)
6. Configure Assignments → Review → **Create**

## Method 2: Platform Scripts (One-Time)

1. Obtain/modify example PowerShell script from GitHub
2. Intune → **Devices** → **Scripts and remediations** → **Platform scripts**
3. **Add** → **Windows 10 or later**
4. Script Settings:
   - Upload script file
   - **Run with logged-on credentials**: `No` ← critical
   - **Enforce script signature check**: `No`
5. Set Assignments → **Add**

## Method 3: Detection & Remediation (Scheduled)

1. Prepare two scripts: detection script + remediation script (from GitHub)
2. Intune → **Devices** → **Scripts and remediations** → **Remediation** tab
3. **+ Create** → Fill Basics
4. Settings page:
   - Upload detection script and remediation script
   - All options set to `No` (runs as system user)
5. Assignments: select groups or **All Devices**
6. Set schedule (daily recommended, hourly minimum) → **Create**

> To trigger immediately: edit Assignments and schedule as **once** at a specific time; reverts to regular schedule afterward.

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| MSI command-line args | Tenant name + optional auto-update flag |
| Script credential setting | `No` (requires elevated/system permissions) |
| Script signature check | `No` |
| Recommended run frequency | Daily (supports hourly) |

## Gotchas
- **Do not** run scripts with logged-on credentials—script requires system/elevated permissions
- Detection & Remediation requires specific Intune licenses (E3/E5)—verify before implementing
- Example scripts are provided as-is; review and test before production deployment
- Detection script compares installed version against Twingate Changelog RSS feed
- New devices enrolled after deployment automatically receive the script package

## Related Docs
- [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device)
- [MSI Command Line Arguments](https://www.twingate.com/docs/windows-managed-device#command-line-arguments)
- [Microsoft Intune Platform Scripts documentation](https://learn.microsoft.com/en-us/intune/intune-service/apps/intune-management-extension)
- [Microsoft Detection & Remediation documentation](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/remediations)