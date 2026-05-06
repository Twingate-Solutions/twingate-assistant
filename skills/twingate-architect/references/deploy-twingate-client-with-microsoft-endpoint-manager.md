# Deploy Twingate Client with Microsoft Intune

## Summary
Guide for deploying the Twingate Windows Client via Microsoft Endpoint Manager (Intune) using three methods: Line-of-Business app package, Platform Scripts (PowerShell), or Detection and Remediation for scheduled compliance enforcement.

## Key Information
- Three deployment methods available: Intune LOB app, Platform Scripts (one-time), Detection & Remediation (scheduled)
- All methods use the same Windows MSI installer and command-line arguments
- Detection & Remediation requires Windows 10/11 Enterprise E3 or E5 licensing
- Example scripts hosted in public GitHub repository

## Prerequisites
- Microsoft Intune/Endpoint Manager access
- Windows MSI installer downloaded from Twingate
- Twingate tenant name for command-line arguments
- For Detection & Remediation: Windows 10/11 Enterprise E3/E5 licenses
- Review [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device) page for MSI prerequisites

## Method 1: Line-of-Business App (Endpoint Manager)
1. Download Twingate Windows MSI installer
2. Intune → Apps → Add → Other → **Line-of-business app**
3. Upload MSI file
4. Fill in Publisher and command-line arguments (tenant name, update preferences)
5. Configure Assignments → Review → Create

## Method 2: Platform Scripts (One-Time)
1. Prepare PowerShell script (see GitHub example) that: downloads MSI, checks/installs .NET Desktop Runtime, installs Client
2. Intune → Devices → Scripts and remediations → Platform scripts → Add → Windows 10 or later
3. Script Settings:
   - Upload script file
   - **Run with logged-on credentials: No** (requires elevated permissions)
   - **Enforce script signature check: No**
4. Configure Assignments → Add

## Method 3: Detection and Remediation (Scheduled Compliance)
1. Create detection script (checks installed version vs. Changelog RSS feed)
2. Create remediation script (installs latest Client if missing/outdated)
3. Intune → Devices → Scripts and remediations → Remediation tab → + Create
4. Settings page: assign both scripts; set **all options to No** (runs as system user)
5. Assignments: select groups/All Devices, set schedule (hourly or daily recommended)
6. Review → Create

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Command-line arguments | Twingate tenant name + auto-update preference |
| Run script as logged-on credentials | Must be **No** |
| Enforce script signature check | **No** |
| Detection/Remediation script options | All set to **No** |
| Schedule frequency | Hourly (triggers within minutes) or Daily |

## Gotchas
- Platform Scripts run **once only**; use Detection & Remediation for ongoing compliance
- To trigger Detection & Remediation immediately: edit Assignments, schedule as "run once" at specific time; it reverts to original schedule afterward
- Remediation script is provided as-is — must be reviewed, modified, and tested before production use
- Detection script compares against Twingate Changelog RSS feed for version checking
- New devices enrolled in Intune automatically receive existing script packages

## Related Docs
- [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device)
- [Twingate MSI Command-line Arguments](https://www.twingate.com/docs/windows-managed-device)
- [Microsoft Intune Detection & Remediation Documentation](https://docs.microsoft.com/en-us/mem/intune/)
- [Example Scripts GitHub Repository](https://github.com/Twingate-Labs)