# Deploy Twingate Connector in Proxmox Container

## Summary
Deploys a Twingate Connector inside a Proxmox LXC container using an Ubuntu 22.04 template. The process involves creating the container via Proxmox UI, then running the Twingate deployment script from the Admin Console.

## Key Information
- Proxmox uses LXC containers (lightweight, no dedicated kernel)
- Minimum resources: 1 vCPU, 512MB RAM
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 template
- Connectors do **not** auto-update; requires manual update strategy

## Prerequisites
- Proxmox VE installed with a node accessible
- Container template downloaded (Ubuntu 22.04 LTS recommended)
- Access to Twingate Admin Console with a Remote Network configured
- `curl` available in container (installed during setup)

## Step-by-Step

### 1. Download Container Template
```bash
pveam update
pveam list
pveam download <storageLocation> <templateName>
```

### 2. Create Container (Proxmox UI → "Create CT")
| Tab | Setting |
|-----|---------|
| General | Set hostname, password; leave **Nesting** checked; uncheck **Unprivileged container** to allow pings |
| Template | Select storage ID + Ubuntu 22.04 image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge interface; DHCP or static IP |
| DNS | Default (host settings) or custom |

### 3. Prepare Container
```bash
apt update
apt upgrade -y
apt install curl -y
```

### 4. Deploy Connector
1. Go to Twingate Admin Console → Remote Network → Linux deployment
2. Click **Generate Tokens**
3. Copy the deployment command (tokens auto-included)
4. Paste and run in container console

## Configuration Values
- **storageLocation**: Proxmox storage ID that allows container template content type
- **templateName**: Copied from `pveam list` output
- **Container login**: `root` + password set during creation

## Gotchas
- **Unprivileged container**: Must be **unchecked** if you want ICMP/ping to work from this Connector to Resources
- **Static IP recommended**: Required if Resources need to allowlist Connector IP, or for network logging purposes
- **No auto-updates**: Stagger updates across multiple Connectors on the same Remote Network to avoid downtime; use cron jobs to automate
- Peer-to-peer connections should be configured to stay within Fair Use Policy bandwidth limits

## Related Docs
- [Supported Linux distros](https://www.twingate.com/docs/supported-distros)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Automate updates with cron job](https://www.twingate.com/docs/connector-update)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)