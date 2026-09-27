---
source: https://github.com/Twingate-Solutions/twingate-connector-hyperv
type: github
fetched: 2026-09-27
source_version: 2683b5ab2b76d882bc52d47dce3c81191542b38f
---

# Twingate Connector — Hyper-V Deployment Scripts

## Summary
PowerShell scripts for deploying and managing Twingate Connector VMs on Windows Server via Hyper-V. Each connector runs as an Ubuntu 24.04 Gen2 VM provisioned with cloud-init, with the full lifecycle (create, update, repair, remove) handled through the Twingate API. Provided as an unsupported reference example under Apache 2.0.

## Key Information
- Two primary scripts: `Deploy-TwingateConnector.ps1` (full lifecycle) and `Reset-TwingateConnectorEnvironment.ps1` (teardown)
- Six actions: `Deploy`, `Remove`, `UpdateConnector`, `UpdateOS`, `List`, `FixVM`
- Downloads Ubuntu 24.04 cloud image (~600 MB) and `qemu-img.exe` on first run; cached in `VMPath\images` and `VMPath\tools`
- VMs named `TG-Connector-<RemoteNetwork>-<N>`; connector IDs stored in VM Notes field
- Per-VM ED25519 SSH keypair generated; randomly named admin user (`tgadm` + 4 chars) with 24-char password printed at deploy time
- Default `ubuntu` user is disabled; credentials shown once at deploy — save them
- `FixVM` leaves the old connector record in the Admin Console and flags it — manual cleanup required
- Legacy deployment method retained in `legacy-hyperv-deployment/` (deprecated)
- Every Twingate Admin API call sends a structured `User-Agent` header: `twingate-connector-hyperv/<version> (mode=<action>; op=<operation>) PowerShell/<psversion>`; built by `Get-TwingateUserAgent`, injected via `Invoke-TwingateApi`

## API User-Agent Format

```text
twingate-connector-hyperv/<version> (mode=<action>; op=<operation>) PowerShell/<psversion>
```

- `<version>` — from `$script:ScriptVersion` (default `1.0.0`; overridable via `TWINGATE_DEPLOY_VERSION` env var)
- `mode=` — the `-Action` lowercased (`deploy`, `remove`, `updateconnector`, `updateos`, `list`, `fixvm`)
- `op=` — the API operation: `network-lookup`, `connector-create`, `token-create`, `connector-status`, `connector-delete`, `connector-network`, `network-connectors`, `auth-check`
- Key order (`mode` then `op`) is fixed — reordering breaks downstream log parsing; keys with no value are omitted; if no keys exist the parenthesised comment is dropped entirely

## Prerequisites
- Windows Server 2022 or 2025
- Hyper-V role (script can install it and prompt for reboot)
- PowerShell 5.1+, running as Administrator
- Internet access
- Twingate API token with **Read, Write & Provision** scope
- Remote Network already created in Twingate Admin Console

## Usage / Step-by-Step

```powershell
# Deploy 2 connectors (default)
.\Deploy-TwingateConnector.ps1 -Action Deploy -TwingateNetwork "acme" -RemoteNetwork "Office"

# Deploy 4 connectors with custom resources
.\Deploy-TwingateConnector.ps1 -Action Deploy -TwingateNetwork "acme" -RemoteNetwork "Office" `
    -ConnectorCount 4 -VMPath D:\VMs -VMMemory 4GB

# List all connector VMs (no API token required)
.\Deploy-TwingateConnector.ps1 -Action List

# Update connector package on all VMs
.\Deploy-TwingateConnector.ps1 -Action UpdateConnector -TwingateNetwork "acme"

# Update OS on all VMs
.\Deploy-TwingateConnector.ps1 -Action UpdateOS -TwingateNetwork "acme"

# Repair a single VM
.\Deploy-TwingateConnector.ps1 -Action FixVM -TwingateNetwork "acme" -VMName "TG-Connector-Office-1"

# Remove a single VM