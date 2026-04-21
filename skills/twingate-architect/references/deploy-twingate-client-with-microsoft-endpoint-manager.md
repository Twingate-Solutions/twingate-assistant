## Deploy Twingate Client with Microsoft Intune / Endpoint Manager

Three methods to deploy the Twingate Windows Client via Microsoft Intune: MSI via Endpoint Manager, PowerShell via Platform Scripts (one-time run), and Detection and Remediation (scheduled compliance enforcement). All methods use the same MSI installer with command line arguments for tenant name and auto-update settings.

**Key Information**
- MSI installer: download from Twingate Windows Managed Device page; deploy as Line-of-business app in Endpoint Manager
- Command line arguments: specify Twingate tenant name and optional auto-update settings
- Platform Scripts: PowerShell script downloads MSI and installs; must run as SYSTEM (not logged-on credentials)
- Detection and Remediation: requires Windows 10/11 Enterprise E3 or E5 license; runs on schedule (hourly minimum)
- Detection script checks installed version against Twingate Client Changelog RSS feed; runs remediation if outdated or missing
- Example scripts hosted in Twingate Community GitHub repository

**Prerequisites**
- Microsoft Intune (Endpoint Manager) subscription
- For Detection and Remediation: Windows 10/11 Enterprise E3 or E5 device licenses
- Twingate MSI installer downloaded from Twingate Windows Managed Device page

**Step-by-Step (Endpoint Manager MSI)**
1. Download Twingate Windows MSI installer
2. Open Endpoint Manager -> Apps -> Add -> Other -> Line-of-business app
3. Select MSI file; fill in Publisher and command line arguments (tenant name, auto-update options)
4. Set assignments (target devices/groups) -> Review -> Create

**Step-by-Step (Platform Scripts)**
1. Get/modify PowerShell example script from Twingate Community GitHub
2. Intune -> Devices -> Scripts and remediations -> Platform scripts -> Add -> Windows 10 or later
3. Select script file; set "Run this script using the logged on credentials" to No; disable signature check
4. Set assignments -> Add

**Step-by-Step (Detection and Remediation)**
1. Create/modify detection script (checks installed version vs RSS feed) and remediation script
2. Intune -> Devices -> Scripts and remediations -> Remediation -> Create
3. Select both scripts; set all options to No (run as SYSTEM)
4. Set assignments and schedule (daily recommended, hourly minimum)

**Gotchas**
- Platform Scripts must run as SYSTEM (not logged-on user) -- "Run using logged on credentials" must be set to No
- Detection and Remediation requires E3/E5 license -- not available on all Intune SKUs
- To trigger a Detection and Remediation script immediately, set schedule to "once" at a specific time, then revert

**Related Docs**
- /docs/windows-client
- /docs/windows-managed-device
- /docs/mdm-deployment
