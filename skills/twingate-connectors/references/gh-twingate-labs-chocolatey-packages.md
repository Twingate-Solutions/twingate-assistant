---
source: https://github.com/Twingate-Labs/chocolatey-packages
type: github
fetched: 2026-08-06
source_version: 012eb5f14ca539989cd1857d7db175985e9463fb
---

<!-- triage: unassigned -->

# Twingate Chocolatey Packages

## Summary
This repository contains Chocolatey package definitions for installing the Twingate client on Windows. It provides automated package management for deploying Twingate via the Chocolatey Windows package manager.

## Key Information
- Hosts Chocolatey packaging scripts for the Twingate Windows client
- Enables silent/automated installation of Twingate on Windows systems
- Maintained by Twingate Labs as the official Chocolatey distribution channel
- Packages likely follow standard Chocolatey `.nuspec` + `chocolateyInstall.ps1` structure

## Prerequisites
- Windows OS
- [Chocolatey](https://chocolatey.org/install) package manager installed
- Administrator privileges for installation
- PowerShell execution policy allowing script execution

## Usage / Step-by-Step

**Install via Chocolatey:**
```powershell
choco install twingate
```

**Upgrade existing installation:**
```powershell
choco upgrade twingate
```

**Uninstall:**
```powershell
choco uninstall twingate
```

**Install specific version:**
```powershell
choco install twingate --version <version>
```

## Configuration Values
| Parameter | Description |
|-----------|-------------|
| `--version` | Pin a specific package version |
| `--yes` / `-y` | Auto-confirm prompts |
| `--force` | Force reinstall |
| `--ignore-checksums` | Skip checksum validation (not recommended) |

Post-install configuration (network/tenant setup) is handled through the Twingate client UI or via the Twingate admin console, not through Chocolatey parameters.

## Gotchas
- Chocolatey packages may lag behind the latest Twingate client release; check [Chocolatey Community Repository](https://community.chocolatey.org/packages/twingate) for current version
- Admin rights are required; run from an elevated PowerShell or cmd prompt
- Twingate client requires a valid tenant network address to connect after installation — package install alone does not configure the client
- Package checksums are tied to specific release binaries; using `--ignore-checksums` introduces security risk
- Windows Defender or other AV tools may flag the installer during execution; allowlisting may be needed in managed environments

## Related Docs
- [Twingate Documentation](https://docs.twingate.com)
- [Twingate Client Downloads](https://www.twingate.com/download)
- [Chocolatey Package Page](https://community.chocolatey.org/packages/twingate)
- [Chocolatey Documentation](https://docs.chocolatey.org)
- [Twingate Labs GitHub Org](https://github.com/Twingate-Labs)