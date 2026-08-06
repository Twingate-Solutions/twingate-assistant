---
source: https://github.com/Twingate-Solutions/twingate-connector-hyperv
type: github
fetched: 2026-08-06
source_version: 9cde89c90d3945379db1c9aaaddf580463f4c9fd
---

<!-- triage: unassigned -->

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
.\Deploy-TwingateConnector.ps1 -Action Remove -TwingateNetwork "acme" -VMName "TG-Connector-Office-1"

# Remove all VMs in a Remote Network
.\Deploy-TwingateConnector.ps1 -Action Remove -TwingateNetwork "acme" -RemoteNetwork "Office"

# Full teardown after failed run (preview first, then force)
.\Reset-TwingateConnectorEnvironment.ps1
.\Reset-TwingateConnectorEnvironment.ps1 -Force
```

## Configuration Values

| Parameter | Default | Notes |
|---|---|---|
| `-Action` | *(required)* | `Deploy`, `Remove`, `UpdateConnector`, `UpdateOS`, `List`, `FixVM` |
| `-TwingateNetwork` | prompted | Network slug (e.g. `acme` for `acme.twingate.com`) |
| `-ApiToken` | prompted | Plain string or SecureString |
| `-RemoteNetwork` | prompted | Display name from Admin Console |
| `-ConnectorCount` | `2` | Deploy only |
| `-VMPath` | `C:\TwingateConnectors` | Root for VM files, images, tools |