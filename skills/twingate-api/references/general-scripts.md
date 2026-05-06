# Twingate General Scripts Repository

## Summary
Community repository maintained by Twingate Solutions Engineering containing general-purpose scripts for deploying Twingate services, parsing logs, and automating administrative tasks. Each script is organized in its own subdirectory with its own README. Licensed under Apache-2.0.

## Key Information
- **Repository**: `Twingate-Solutions/general-scripts` (public)
- **Languages**: PowerShell (73.4%), Shell (20.3%), Python (6.3%)
- **Script categories available**:
  - `bash-scripts/` — General bash utilities
  - `filter-network-events-report/` — Log/report parsing
  - `internet-security-include-only-group/` — Internet security policy management
  - `powershell-scripts/` — Windows/PowerShell utilities
  - `remove-users/` — User removal automation
  - `twingate-headless-client-gateway/` — Headless client/gateway deployment
  - `unique_ports/` — Port enumeration utilities

## Prerequisites
- Varies per script — check individual subdirectory READMEs
- PowerShell scripts likely require Windows or PowerShell Core
- Shell scripts require bash-compatible environment
- Python scripts require Python 3.x (implied by usage)

## Usage Pattern
Each script folder contains its own README with specific instructions:
```
cd <script-folder>/
cat README.md
```

## Notable Scripts

### twingate-headless-client-gateway
- Deployment automation for headless Twingate client or gateway
- Includes Ubuntu Hyper-V Image release (Sept 2024)

### remove-users
- Automates bulk user removal from Twingate

### internet-security-include-only-group
- Manages Internet Security policies to restrict to specific groups

### filter-network-events-report
- Parses and filters Twingate network event logs/reports

### unique_ports
- Extracts or enumerates unique ports (likely from logs or resource configs)

## Gotchas
- No centralized configuration — each script is independent; always read the subdirectory README before use
- Scripts are community/solutions-engineering maintained, not official product — validate before production use
- 121 commits of history; check last commit date per folder to assess maintenance status
- Releases section only contains Ubuntu Hyper-V Image asset; other scripts have no versioned releases

## Related Docs
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- [Twingate Connector Deployment](https://docs.twingate.com/docs/connectors)
- Individual `README.md` files within each subdirectory (primary reference for each script)