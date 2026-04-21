## Windows Client Migration to .NET 8

Documents the November 2024 migration of the Twingate Windows Client from .NET 6 to .NET 8. EXE installer handles the prerequisite automatically; MSI deployments require manual .NET 8 installation on each device.

**Key Information:**
- Migration date: November 2024 (aligned with Microsoft ending .NET 6 support on November 12, 2024)
- EXE installer: automatically installs .NET 8 Desktop Runtime (x64) -- no admin action needed
- MSI installer: .NET 8 Desktop Runtime (x64) must be pre-installed separately on each device
- If .NET 8 is not present, future Windows Client versions will not launch

**Silent Install for MDM:**
```
windowsdesktop-runtime-8.0.10-win-x64.exe /install /quiet /norestart
```

**Verify .NET 8 Installation (PowerShell):**
```
Get-WmiObject -Query "SELECT * FROM Win32_Product WHERE Name LIKE '%.NET%Runtime%8.%.%'"
```
Or: Control Panel > Programs > Programs and Features > look for ".NET 8 Desktop Runtime"

**Gotchas:**
- Only MSI-based deployments require admin action; EXE deployments install the runtime automatically
- Use `/install /quiet /norestart` when deploying the runtime via MDM to avoid prompting users

**Related Docs:**
- /docs/windows -- Windows Client setup
- /docs/clients -- Client download and update policy
- /docs/managed-devices -- MDM deployment guides
