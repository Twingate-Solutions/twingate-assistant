---
source: https://www.twingate.com/docs/proxmox-container-deployment
type: docs
fetched: 2026-08-14
source_version: 1798ee83b85d94ae70498f02e54d5f7cf03c19fe39e3b9e6be0bca22d874e8ff
---

# How to Deploy a Connector in a Proxmox Container

## Summary
Deploys a Twingate Connector inside a Proxmox LXC container. Uses an Ubuntu 22.04 template with minimal resource requirements. Connector is installed via the standard Linux deployment script from the Admin Console.

## Key Information
- Proxmox uses LXC containers (lightweight, no dedicated kernel)
- Minimum resources: 1 vCPU, 512MB RAM
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 template
- Connectors do **not** auto-update; must be managed manually or via cron

## Prerequisites
- Proxmox VE host with shell access
- Container template downloaded (Ubuntu 22.04 LTS recommended)
- Twingate Admin Console access with a configured Remote Network
- `curl` installed in container

## Step-by-Step

### 1. Download Container Template
```bash
pveam update
pveam list
pveam download <storageLocation> <templateName>
```

### 2. Create LXC Container (via Proxmox UI → "Create CT")
| Tab | Setting |
|-----|---------|
| General | Set hostname, password; keep **Nesting** checked; uncheck **Unprivileged container** to allow pings |
| Template | Select storage + downloaded template image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge + DHCP or static IP (static recommended for Resources with IP allowlists) |
| DNS | Host defaults or custom |

### 3. Prepare Container
```bash
apt update
apt upgrade -y
apt install curl -y
```

### 4. Deploy Connector
1. Go to Admin Console → Remote Network → select Linux deployment
2. Click **Generate Tokens** (tokens auto-embed in script)
3. Copy and paste the generated deploy command into the container console
4. Verify Connector shows connected in Admin Console

## Configuration Values
- **storageLocation**: Proxmox storage ID that allows container template content type
- **templateName**: Exact name from `pveam list` output
- **Network**: DHCP or static IP; static recommended for logging/allowlisting

## Gotchas
- **Unprivileged container**: Must be **unchecked** if you need ping support from Connector to Resources
- **Nesting**: Must remain **checked**
- **Static IP**: Recommended if Resources require Connector IP allowlisting or network logging is in use
- **No auto-updates**: Stagger updates across multiple Connectors on the same Remote Network to avoid downtime
- Peer-to-peer connections should be enabled to stay within Fair Use Policy bandwidth limits

## Related Docs
- [Supported Linux distros](https://www.twingate.com/docs/supported-distros)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Automate updates via cron job](https://www.twingate.com/docs/connector-updates)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)