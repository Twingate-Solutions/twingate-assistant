# Twingate General Scripts Repository

## Summary
Community repository maintained by Twingate Solutions Engineering containing utility scripts for deployment, log parsing, and administration tasks. Each script is organized in its own folder with individual README documentation. Licensed under Apache-2.0.

## Key Information
- **Repository**: `Twingate-Solutions/general-scripts` (public)
- **Languages**: PowerShell (78.3%), Shell (16.6%), Python (5.1%)
- **Script categories available**:
  - `bash-scripts/` — General bash utilities
  - `filter-network-events-report/` — Parse/filter network event logs
  - `internet-security-include-only-group/` — Internet security group filtering
  - `powershell-scripts/` — Windows PowerShell utilities
  - `remove-users/` — User removal automation
  - `twingate-headless-client-gateway/` — Headless client/gateway deployment
  - `unique_ports/` — Port enumeration utilities

## Prerequisites
- Each script has its own dependencies; check individual folder READMEs
- PowerShell scripts require Windows or PowerShell Core
- Shell scripts require bash-compatible environment
- Python scripts require Python 3.x (implied by content)

## Usage Pattern
1. Navigate to the specific script folder matching your use case
2. Read the folder-level `README.md` for that script
3. Follow folder-specific setup and execution instructions

## Releases
- `Ubuntu Hyper-V Image` (Latest — Sep 27, 2024) available under Releases

## Gotchas
- No monolithic setup — each subdirectory is an independent script/project
- Must read per-folder README before use; no unified CLI or configuration
- Scripts are community/solutions-engineering maintained, not official product — verify before production use
- Repository is sparse on top-level documentation; all detail is in subdirectory READMEs not visible from the index page

## Related Docs
- Individual folder READMEs (e.g., `twingate-headless-client-gateway/README.md`)
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- Twingate official deployment guides for context on headless client/gateway scripts