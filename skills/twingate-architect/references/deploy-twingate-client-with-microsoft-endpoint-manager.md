# Deploy Twingate Client with Microsoft Intune/Endpoint Manager

## Summary
Three methods to deploy the Twingate Windows Client via Microsoft Intune: Line-of-Business app package, Platform Scripts (one-time PowerShell), and Detection & Remediation (scheduled compliance enforcement). Each method uses the same MSI installer and command-line arguments.

## Key Information
- All methods use the Twingate Windows MSI installer
- Command-line arguments configure tenant name and auto-update behavior
- Detection & Remediation requires Windows 10/11 Enterprise E3/E5 licenses
- Example scripts available in Twingate's public GitHub repository
- Scripts must run as SYSTEM (not logged-on user credentials)

## Prerequisites
- Twingate Windows MSI installer downloaded
- Microsoft Intune/Endpoint Manager access
- Review [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device) page for MSI details and deployment options
- For Detection & Remediation: Windows 10/11 Enterprise E3/E5 license

## Method 1: Endpoint Manager (Line-of-Business App)

1. Download Twingate Windows MSI installer
2. Intune → **Apps** → **Add** → **Other** → **Line-of-business app**
3. Upload MSI file
4. Fill in Publisher and command-line arguments (tenant name, update preferences)
5. Configure Assignments → Review → **Create**

## Method 2: Platform Scripts (One-Time Deployment)

1. Obtain/modify PowerShell script from GitHub example
2. Intune → **Devices** → **Scripts and remediations** → **Platform scripts** → **Add** → **Windows 10 or later**
3. Configure Script Settings:
   - Upload script file
   - **Run with logged-on credentials**: `No` (requires elevated permissions)
   - **Enforce script signature check**: `No`
4. Set Assignments → **Add**

**Script must:**
- Download MSI installer
- Check/install required .NET Desktop Runtime
- Install Client with MSI command-line arguments

## Method 3: Detection & Remediation (Scheduled Compliance)

1. Prepare two scripts (examples on GitHub):
   - **Detection script**: Checks installed version against Twingate Changelog RSS feed
   - **Remediation script**: Installs latest Client if missing or outdated
2. Intune → **Devices** → **Scripts and remediations** → **Remediation** → **+ Create**
3. **Settings page**: Select both scripts; set all options to `No` (runs as SYSTEM)
4. **Assignments**: Select target groups/All Devices; set schedule (hourly minimum, daily recommended)
5. Review → **Create**

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| MSI command-line args | Tenant name + auto-update preference |
| Run as logged-on credentials | `No` |
| Enforce script signature check | `No` |
| Recommended schedule | Daily (hourly minimum) |

## Gotchas
- Scripts **must** run as SYSTEM, not logged-on user — deployment fails otherwise
- Detection & Remediation requires Enterprise E3/E5 licensing — verify before implementing
- To trigger immediate run: edit Assignments, schedule as **once** at specific time; it reverts to original schedule afterward
- Example scripts are provided as-is — review and test before production use
- New devices enrolled in Intune automatically receive existing script packages

## Related Docs
- [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device)
- [Intune Platform Scripts](https://learn.microsoft.com/en-us/intune/intune-service/apps/intune-management-extension)
- [Intune Detection & Remediation](https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/remediations)
- Twingate GitHub: Detection script, Remediation script examples