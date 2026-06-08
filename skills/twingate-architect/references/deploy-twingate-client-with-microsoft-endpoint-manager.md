# Deploy Twingate Client with Microsoft Intune

## Summary
Three methods for deploying the Twingate Windows Client via Microsoft Intune/Endpoint Manager: Line-of-Business app package, Platform Scripts (PowerShell), and Detection & Remediation scripts. Detection & Remediation provides ongoing compliance enforcement on a schedule.

## Key Information
- All methods use the same Windows MSI installer and command-line arguments
- MSI requires .NET Desktop Runtime (scripts should check/install this)
- Detection & Remediation requires Windows 10/11 Enterprise E3 or E5 licenses
- Example scripts available in Twingate's public GitHub repository

## Prerequisites
- Microsoft Intune/Endpoint Manager access
- Downloaded Twingate Windows MSI installer
- Review [Windows Managed Device page](https://www.twingate.com/docs/windows-managed-device) for MSI details and deployment options
- For Detection & Remediation: Windows 10/11 Enterprise E3/E5 license

## Method 1: Endpoint Manager (Line-of-Business App)
1. Download Twingate Windows MSI installer
2. Open Endpoint Manager → **Apps** → **Add**
3. Select app type: **Other → Line-of-business app**
4. Upload MSI file
5. Fill in Publisher and command-line arguments (tenant name, update settings)
6. Configure Assignments → Review → **Create**

## Method 2: Platform Scripts (One-Time)
1. Open Intune → **Devices → Scripts and remediations → Platform scripts**
2. **Add → Windows 10 or later**
3. Upload PowerShell script
4. Script Settings:
   - `Run with logged on credentials`: **No** (requires elevated permissions)
   - `Enforce script signature check`: **No**
5. Set Assignments → Review → **Add**

## Method 3: Detection & Remediation (Scheduled/Ongoing)
1. Open Intune → **Devices → Scripts and remediations → Remediation**
2. **+ Create** new Script Package
3. Upload both detection script and remediation script
4. Settings: all options set to **No** (runs as system user)
5. Assign to groups/All Devices; set schedule (hourly minimum, daily recommended)
6. **Create**

### Detection & Remediation Logic
- Detection script checks installed Client version against Twingate Changelog RSS feed
- If not installed or version outdated → triggers remediation script
- Remediation script = same as Platform Scripts installer

## Configuration Values
- **Command-line arguments**: tenant name, auto-update preference (see Windows Managed Device docs)
- **Script run schedule**: hourly (triggers within minutes) or daily
- **Run as**: System (not logged-on user)

## Gotchas
- Detection & Remediation requires specific enterprise licenses — verify before implementing
- Example scripts from GitHub must be reviewed, modified, and tested before production use
- To trigger Detection & Remediation immediately: edit Assignments, schedule as **once** at specific time; it reverts to original schedule afterward
- Remediation script must handle .NET Desktop Runtime installation

## Related Docs
- [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device)
- [MSI Command Line Arguments](https://www.twingate.com/docs/windows-managed-device)
- [Microsoft Intune Scripts and Remediations documentation](https://learn.microsoft.com/en-us/intune/)
- GitHub: Detection script, Remediation script (linked from Twingate docs)