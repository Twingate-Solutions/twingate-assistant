---
source: https://github.com/Twingate-Solutions/general-scripts
type: github
fetched: 2026-08-06
source_version: 47dec916d25a6fd71862bce5c604d08ec76267c5
---

# Twingate-Solutions/general-scripts

## Summary
A collection of self-contained operational scripts for Twingate administration covering client deployment, diagnostics, gateway setup, and log parsing. Each subfolder is an independent mini-project with its own README. Scripts are reference examples built with LLM assistance — not a supported product.

## Key Information
- **License:** Apache 2.0 (AS IS, no warranty)
- **Maintainer:** Twingate Solutions Engineering
- **Languages:** Bash, PowerShell, Python
- **Platforms:** macOS, Linux, Windows (varies by script)

| Folder | Purpose | Platform |
|---|---|---|
| `bash-scripts/` | macOS/Linux client diagnostics & admin helpers | macOS/Linux |
| `powershell-scripts/` | Windows client deployment & lifecycle (Intune/MDM) | Windows |
| `powershell-scripts/autopilot-scripting/` | Headless Windows machines, self-promote to user-mode client on first logon | Windows |
| `twingate-headless-client-gateway/` | Linux box as whole-network Twingate gateway + DNS for IoT/unmanaged devices | Linux |
| `filter-network-events-report/` | Filter Network Events CSV to a single user | Cross-platform |
| `unique_ports/` | Extract unique host:port pairs from Network Events report | Cross-platform |
| `remove-users/` | Bulk-remove all users from a Twingate group via CLI | Linux/macOS |
| `internet-security-include-only-group/` | Populate an exclude group from an include group for Internet Security rollout | Linux/macOS |

> Note: `powershell-scripts/hyperv-connector-deployment/` has moved to [Twingate-Solutions/twingate-connector-hyperv](https://github.com/Twingate-Solutions/twingate-connector-hyperv).

## Prerequisites
- Twingate account with API access (token required at runtime)
- Per-script dependencies listed in each subfolder's README
- Twingate CLI installed where Bash scripts call it directly
- Python 3.x for CSV report scripts
- PowerShell for Windows scripts; Bash for Linux/macOS scripts

## Usage
1. Navigate to the relevant subfolder
2. Read the subfolder's README before running anything
3. Test on a non-production/throwaway system first
4. Pass secrets (API tokens, service keys) at runtime via arguments, environment variables, or a local file — **never hardcode**

## Configuration Values
- **Twingate API token:** Pass at runtime (env var or argument); never commit to repo
- **Service keys:** Same — runtime only
- Per-script parameters documented in each subfolder's README

## Gotchas
- Scripts are unsupported reference examples — no warranty, no SLA
- LLM-assisted code: review carefully before use in any critical environment
- Secrets committed to git are a security risk; repo convention explicitly forbids it
- Each script is independent — there is no shared library or install step at the repo root
- HyperV connector deployment has moved repos; the folder in this repo is stale

## Related Docs
- [Individual subfolder READMEs](https://github.com/Twingate-Solutions/general-scripts) (primary usage docs)
- [Twingate-Solutions/twingate-connector-hyperv](https://github.com/Twingate-Solutions/twingate-connector-hyperv) (moved HyperV scripts)
- [CONTRIBUTING.md](https://github.com/Twingate-Solutions/general-scripts/blob/main/CONTRIBUTING.md)
- [Apache 2.0 LICENSE](https://github.com/Twingate-Solutions/general-scripts/blob/main/LICENSE)