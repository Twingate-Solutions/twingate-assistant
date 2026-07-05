# Twingate General Scripts Repository

## Summary
Community repository maintained by Twingate Solutions Engineering containing utility scripts for deployment, log parsing, and administration tasks. Each subdirectory contains its own README with usage instructions. Licensed under Apache-2.0.

## Key Information
- **Repository**: `Twingate-Solutions/general-scripts`
- **Languages**: PowerShell (78.3%), Shell (16.6%), Python (5.1%)
- **126 commits**, 6 forks, 4 stars

## Script Categories / Directories

| Directory | Purpose |
|-----------|---------|
| `bash-scripts/` | General bash utilities |
| `filter-network-events-report/` | Parse/filter network event logs |
| `internet-security-include-only-group/` | Internet security group filtering |
| `powershell-scripts/` | Windows PowerShell utilities |
| `remove-users/` | User removal automation |
| `twingate-headless-client-gateway/` | Headless client/gateway deployment |
| `unique_ports/` | Port enumeration utilities |

## Prerequisites
- Each script has its own dependencies — check the README in each subdirectory
- PowerShell scripts require Windows or PowerShell Core
- Shell scripts require bash-compatible environment
- Twingate API credentials likely required for admin scripts (user removal, group management)

## Usage Pattern
```bash
# Navigate to specific script directory
cd <script-folder>/

# Read per-script documentation
cat README.md

# Execute per script-specific instructions
```

## Notable Scripts

- **`twingate-headless-client-gateway/`** — Deployment automation for headless Twingate clients/gateways; includes Ubuntu Hyper-V image release (Sep 2024)
- **`remove-users/`** — Automates user removal, likely via Twingate API
- **`filter-network-events-report/`** — Post-processing of Twingate network event exports
- **`internet-security-include-only-group/`** — Restricts internet security policies to specific groups

## Gotchas
- No centralized configuration — each script is independently configured
- Repository is community/solutions-team maintained, not official product support
- Must read per-directory READMEs; top-level README provides no implementation details
- Scripts may require Twingate API tokens with appropriate scopes (admin-level for user/group management)

## Related Docs
- [Twingate API Documentation](https://docs.twingate.com/docs/api-overview)
- [Twingate Headless Client](https://docs.twingate.com/docs/linux-headless-client)
- [Network Events / Logs](https://docs.twingate.com/docs/network-events)
- Individual script READMEs within each subdirectory