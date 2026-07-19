# Deploy Twingate Client with Microsoft Intune

## Summary
Guide for deploying the Twingate Windows Client via Microsoft Endpoint Manager (Intune) using three methods: Line-of-business app deployment, Platform Scripts (one-time PowerShell), or Detection and Remediation (scheduled, compliance-based). Detection and Remediation is the most robust option for ongoing compliance enforcement.

## Key Information
- All methods use the Windows MSI installer with command line arguments for tenant configuration
- Detection and Remediation requires Windows 10/11 Enterprise E3 or E5 licenses
- PowerShell scripts must run as SYSTEM (not logged-on user) to have elevated permissions
- Example scripts available in a public Twingate GitHub repository
- Detection script compares installed version against Twingate Client Changelog RSS feed

## Prerequisites
- Microsoft Intune / Endpoint Manager access
- Downloaded Twingate Windows MSI installer
- Review [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device) page for MSI details and deployment options
- For Detection and Remediation: Windows 10/11 Enterprise E3/E5 licenses

## Method 1: Line-of-Business App (Endpoint Manager)
1. Download Twingate Windows MSI installer
2. Intune → Apps → Add → Other → **Line-of-business app**
3. Upload MSI file
4. Fill in Publisher and command line arguments (tenant name, update settings)
5. Configure Assignments → Review → Create

## Method 2: Platform Scripts (One-Time)
1. Intune → Devices → Scripts and remediations → Platform scripts → Add → Windows 10 or later
2. Upload PowerShell script, set name/description
3. Script Settings:
   - **Run with logged-on credentials: No** (required for elevation)
   - **Enforce script signature check: No**
4. Configure Assignments → Add

## Method 3: Detection and Remediation (Scheduled/Compliance)
1. Intune → Devices → Scripts and remediations → Remediation tab → + Create
2. Basics: name and description
3. Settings: upload detection script + remediation script; set **all options to No** (runs as SYSTEM)
4. Assignments: select groups or All Devices; set schedule (hourly minimum, daily recommended)
5. Review → Create

**To trigger immediate run:** Edit Assignments, schedule as "once" at a specific time; reverts to original schedule after.

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| MSI command line arguments | Tenant name + auto-update preferences (see Windows Managed Device docs) |
| Run script as logged-on credentials | Must be `No` for elevated execution |
| Enforce script signature check | `No` |
| Detection/Remediation script options | All set to `No` |
| Schedule | Hourly (triggers within minutes) or Daily |

## Script Requirements (Custom Scripts)
Any deployment script must:
1. Download Twingate Client MSI installer
2. Check for / install required .NET Desktop Runtime
3. Install MSI with appropriate command line arguments

## Gotchas
- Example scripts from GitHub are provided as-is — **review and test before production use**
- Detection and Remediation requires specific Microsoft licenses; verify before implementing
- Remediation script is the same as Platform Scripts example — must be modified for your environment
- Platform Scripts run once; use Detection and Remediation if ongoing compliance enforcement is needed
- Script signature check must be disabled for the deployment scripts to run

## Related Docs
- [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device) — MSI details, prerequisites, deployment options
- Microsoft Intune Scripts and Remediations documentation
- Microsoft Detection and Remediation documentation (licensing requirements)
- Twingate example scripts: [detection](https://github.com) / [remediation](https://github.com) (GitHub)