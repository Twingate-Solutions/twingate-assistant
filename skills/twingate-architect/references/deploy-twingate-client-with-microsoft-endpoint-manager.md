# Deploy Twingate Client with Microsoft Intune/Endpoint Manager

## Summary
Three methods to deploy the Twingate Windows Client via Microsoft Intune: Line-of-business app package, Platform Scripts (PowerShell), and Detection & Remediation (scheduled compliance). Each method supports the same MSI command-line arguments for tenant configuration.

## Key Information
- All methods use the same Windows MSI installer with identical command-line arguments
- Scripts require elevated permissions (run as system, not logged-on user)
- Detection & Remediation requires Windows 10/11 Enterprise E3 or E5 licensing
- Example scripts available in public GitHub repository

## Prerequisites
- Microsoft Intune/Endpoint Manager access
- Twingate Windows MSI installer downloaded
- .NET Desktop Runtime (scripts handle installation if missing)
- For Detection & Remediation: Windows 10/11 Enterprise E3/E5 license

## Method 1: Endpoint Manager (Line-of-Business App)

1. Download latest Twingate Windows MSI from Twingate site
2. Intune → Apps → Add → Other → **Line-of-business app**
3. Upload MSI file
4. Fill in **Publisher** and **command line arguments** (tenant name, update preferences)
5. Configure Assignments → Review → Create

## Method 2: Platform Scripts (PowerShell)

1. Intune → Devices → Scripts and remediations → Platform scripts → Add → Windows 10 or later
2. Upload PowerShell script (downloads MSI + installs .NET Runtime if needed)
3. Script Settings:
   - Run with logged-on credentials: **No** (requires elevated permissions)
   - Enforce script signature check: **No**
4. Set Assignments → Review → Add
- Runs **once** per device; good for initial deployment

## Method 3: Detection & Remediation (Scheduled Compliance)

**Two scripts required:**
- **Detection script**: Checks installed version against Twingate Changelog RSS feed
- **Remediation script**: Installs latest Client if not present or outdated

**Steps:**
1. Intune → Devices → Scripts and remediations → Remediation tab → + Create
2. Basics: name/description
3. Settings: upload both scripts; set all options to **No** (runs as system user)
4. Assignments: select groups or All Devices; set schedule (hourly or daily recommended)
5. Review → Create

**To trigger immediately:** Edit Assignments, schedule as "once" at a specific time; reverts to regular schedule afterward.

## Configuration Values

| Parameter | Notes |
|-----------|-------|
| Command-line arguments | Tenant name + auto-update preference (see Windows Managed Device docs) |
| Script run as | System (not logged-on user) |
| Signature check | Disabled |
| Recommended schedule | Daily (minimum: hourly) |

## Gotchas
- **Platform Scripts run once only**; use Detection & Remediation for ongoing compliance enforcement
- Detection & Remediation compares against RSS changelog feed — version mismatch triggers remediation
- Example scripts are provided as-is; must be reviewed, modified for your environment, and tested before production use
- Enterprise E3/E5 license required for Detection & Remediation — verify before implementation
- New devices enrolled in Intune automatically receive script packages

## Related Docs
- [Windows Managed Device page](https://www.twingate.com/docs/windows-managed-device) — MSI details and deployment options
- [Twingate Client Changelog RSS feed](https://www.twingate.com/docs/changelog) — used by detection script
- [Microsoft Detection & Remediation documentation](https://docs.microsoft.com/en-us/mem/intune/fundamentals/remediations)
- Example scripts: [GitHub repository](https://github.com/Twingate-Labs) (detection + remediation)