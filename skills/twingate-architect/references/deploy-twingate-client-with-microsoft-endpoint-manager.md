---
source: https://www.twingate.com/docs/deploy-twingate-client-with-microsoft-endpoint-manager
type: docs
fetched: 2026-08-14
source_version: aec05e0d6cee7f61af6aadb8f2cfe9fc6db4a99b36f1856e5afb117b0d442547
---

# Deploy Twingate Client with Microsoft Intune

## Summary
Guide for deploying the Twingate Windows Client via Microsoft Endpoint Manager (Intune) using three methods: direct MSI package deployment, Platform Scripts (PowerShell), and Detection & Remediation for ongoing compliance enforcement.

## Key Information
- Three deployment methods available: MSI via Endpoint Manager, Platform Scripts (one-time), Detection & Remediation (scheduled/ongoing)
- All methods use the same MSI installer and command line arguments
- Detection & Remediation requires Windows 10/11 Enterprise E3 or E5 licenses
- Scripts must run as system user (not logged-on credentials) with elevated permissions

## Prerequisites
- Microsoft Intune/Endpoint Manager access
- Windows MSI installer downloaded from Twingate
- .NET Desktop Runtime (script handles install check)
- For Detection & Remediation: Windows 10/11 Enterprise E3/E5 license
- Review [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device) page before proceeding

## Method 1: MSI via Endpoint Manager

1. Download Twingate Windows MSI installer
2. Endpoint Manager → **Apps** → **Add**
3. App type: **Other** → **Line-of-business app**
4. Upload MSI file
5. Fill in **Publisher** and **command line arguments** (tenant name, update preferences)
6. Set **Assignments** → **Review** → **Create**

## Method 2: Platform Scripts (PowerShell)

1. Intune → **Devices** → **Scripts and remediations** → **Platform scripts**
2. **Add** → **Windows 10 or later**
3. Upload PowerShell script file
4. Script Settings:
   - `Run this script using logged on credentials`: **No** *(required for elevated permissions)*
   - `Enforce script signature check`: **No**
5. Set Assignments → **Add**

Script requirements:
- Download MSI installer
- Check/install .NET Desktop Runtime
- Install Client using MSI command line arguments

## Method 3: Detection & Remediation (Scheduled)

1. Intune → **Devices** → **Scripts and remediations** → **Remediation** tab
2. **+ Create** new Script Package
3. Upload both detection and remediation scripts
4. Settings: all options set to **No** (runs as system user)
5. Assignments: select devices/groups, set schedule (hourly minimum, daily recommended)
6. **Create**

**Detection script behavior:** Checks installed version against Twingate Client Changelog RSS feed; triggers remediation if not installed or outdated.

## Configuration Values
| Parameter | Notes |
|-----------|-------|
| Command line arguments | Tenant name + auto-update preference |
| Script run credentials | Must be `No` (system, not user) |
| Script signature check | `No` |
| Schedule frequency | Hourly to daily recommended |

## Gotchas
- Detection & Remediation runs on a schedule; to trigger immediately, set a one-time assignment at a specific time, then revert to recurring schedule
- Remediation script is provided as-is — **must be tested before production deployment**
- Platform Scripts run **once only**; use Detection & Remediation for ongoing enforcement
- New devices enrolled in Intune automatically receive assigned script packages

## Related Docs
- [Windows Managed Device](https://www.twingate.com/docs/windows-managed-device)
- [Example PowerShell script (GitHub)](https://github.com/Twingate-Labs)
- [Microsoft Detection/Remediation documentation](https://learn.microsoft.com/en-us/mem/intune/fundamentals/remediations)
- [Intune Platform Scripts](https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension)