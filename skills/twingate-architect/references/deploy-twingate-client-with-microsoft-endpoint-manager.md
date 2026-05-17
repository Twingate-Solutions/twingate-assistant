# Deploy Twingate Client with Microsoft Intune

## Summary
Guide for deploying the Twingate Windows Client via Microsoft Endpoint Manager (Intune) using three methods: Line-of-Business app deployment, Platform Scripts (one-time PowerShell), or Detection and Remediation (scheduled compliance enforcement).

## Key Information
- Requires Windows MSI installer from Twingate's Windows Managed Device page
- Three deployment methods available, each suited to different needs
- Detection and Remediation requires Windows 10/11 Enterprise E3 or E5 licenses
- All script methods require elevated (system) permissions, not user credentials

## Prerequisites
- Microsoft Intune/Endpoint Manager access
- Twingate Windows MSI installer downloaded
- Twingate tenant name available for command-line arguments
- For Detection & Remediation: Windows 10/11 Enterprise E3/E5 licensing
- .NET Desktop Runtime (scripts handle installation if missing)

## Method 1: Line-of-Business App (Endpoint Manager)
1. Download Twingate Windows MSI installer
2. Intune → Apps → Add → Other → **Line-of-business app**
3. Select MSI file via **Select app package file**
4. Fill in Publisher and **command line arguments** (tenant name, update preferences)
5. Configure Assignments → Review → **Create**

## Method 2: Platform Scripts (One-Time)
1. Intune → Devices → Scripts and remediations → Platform scripts → Add → Windows 10 or later
2. Name the script, click Next
3. Script Settings:
   - Upload script file
   - **Run with logged on credentials: No** (requires elevation)
   - **Enforce script signature check: No**
4. Assign to target groups → Review → **Add**

## Method 3: Detection and Remediation (Scheduled)
1. Intune → Devices → Scripts and remediations → **Remediation** tab → + Create
2. Basics: name and description
3. Settings: upload both detection and remediation scripts; set **all options to No** (runs as system user)
4. Assignments: select groups or All Devices; set schedule (hourly minimum, daily recommended)
5. Review → **Create**

**To trigger immediately:** Edit Assignments, set schedule to run **once** at a specific time; reverts to regular schedule afterward.

## Configuration Values
- **Command line arguments**: Tenant name + optional auto-update flag (see Windows Managed Device docs)
- **Script run credentials**: `No` (system, not user)
- **Signature check**: `No`
- **Detection script**: Checks installed version against Twingate Changelog RSS feed
- **Remediation script**: Downloads and installs latest MSI + .NET Desktop Runtime if needed
- **Schedule options**: Hourly (triggers within minutes) or Daily

## Gotchas
- Detection & Remediation requires Enterprise E3/E5 licenses—verify before implementing
- Example scripts from GitHub must be reviewed, modified for your environment, and tested before production use
- Remediation script is identical for both Platform Scripts and Detection & Remediation methods
- Scripts must run as system (not logged-on user) or installation fails due to insufficient permissions
- New devices enrolled in Intune automatically receive script packages once configured

## Related Docs
- [Windows Managed Device page](https://www.twingate.com/docs/windows-managed-device) — MSI details and prerequisites
- [Twingate Windows command line arguments](https://www.twingate.com/docs/windows-managed-device)
- [Example PowerShell scripts (GitHub)](https://github.com/Twingate-Labs)
- [Microsoft Intune Detection & Remediation documentation](https://learn.microsoft.com/en-us/mem/intune/fundamentals/remediations)