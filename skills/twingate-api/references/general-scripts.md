# Twingate General Scripts Repository

## Summary
Community repository of operational reference scripts from Twingate Solutions Engineering covering client deployment, log parsing, gateway setup, and diagnostics. Scripts are provided as-is under Apache 2.0 with no official support or warranty. Each subfolder is a self-contained mini-project with its own README.

## Key Information
- All scripts are reference/starting points — not production-ready drop-in tools
- Developed with LLM coding assistance; review and test before use
- Secrets must be passed at runtime (args, env vars, local files) — never hardcoded
- Each folder contains its own README with specific usage instructions

## Folder Index

| Folder | Purpose | Platform | Language |
|--------|---------|----------|----------|
| `bash-scripts/` | macOS/Linux client diagnostics & admin helpers | macOS/Linux | Bash |
| `powershell-scripts/` | Windows client deployment & lifecycle (Intune/MDM) | Windows | PowerShell |
| `powershell-scripts/autopilot-scripting/` | Headless Windows machines → user-mode client on first logon | Windows | PowerShell |
| `twingate-headless-client-gateway/` | Linux box as whole-network gateway + DNS for IoT/unmanaged devices | Linux | Bash |
| `filter-network-events-report/` | Filter Network Events CSV to single user | Cross-platform | Python |
| `unique_ports/` | Extract unique host:port combinations from Network Events report | Cross-platform | Python |
| `remove-users/` | Bulk-remove all users from a Twingate group via CLI | Linux/macOS | Bash |
| `internet-security-include-only-group/` | Populate exclude group from include group for Internet Security rollout | Linux/macOS | Bash |

## Prerequisites
- Twingate CLI required for `remove-users/` and `internet-security-include-only-group/`
- Python required for `filter-network-events-report/` and `unique_ports/`
- Twingate API token (passed at runtime, never committed)
- Each subfolder README specifies additional dependencies

## Configuration Values
- **API tokens**: Pass via CLI arguments, environment variables, or local files excluded from `.gitignore`
- **No hardcoded secrets** — enforce via `.gitignore` for any local config files

## Gotchas
- No official Twingate support attached to any script
- `powershell-scripts/hyperv-connector-deployment/` has been moved to separate repo: `Twingate-Solutions/twingate-connector-hyperv`
- Scripts were LLM-assisted — validate logic independently before production use
- Apache 2.0 "AS IS" terms apply (no warranty, limited liability)

## Related Docs
- Individual folder READMEs (primary usage reference)
- [CONTRIBUTING.md](https://github.com/Twingate-Solutions/general-scripts/blob/main/CONTRIBUTING.md) — pattern for adding new scripts
- [Twingate-Solutions/twingate-connector-hyperv](https://github.com/Twingate-Solutions/twingate-connector-hyperv) — relocated Hyper-V connector scripts
- Twingate CLI documentation (required for bash group management scripts)