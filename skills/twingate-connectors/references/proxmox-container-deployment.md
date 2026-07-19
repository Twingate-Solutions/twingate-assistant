# Deploy Twingate Connector in Proxmox LXC Container

## Summary
Guide for deploying a Twingate Connector inside a Proxmox VE Linux Container (LXC). Uses Ubuntu 22.04 LTS template as the base OS. Installation uses the standard Linux deployment script from the Twingate Admin Console.

## Key Information
- Proxmox uses LXC containers (lightweight, not full VMs)
- Minimum specs: 1 vCPU, 512MB RAM
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 template
- Connectors do **not** auto-update — must be managed manually or via cron

## Prerequisites
- Proxmox VE host with shell access
- Container template downloaded (Ubuntu 22.04 LTS or other [supported distro](https://www.twingate.com/docs/connector-supported-os))
- Access to Twingate Admin Console
- Remote Network already configured in Twingate

## Step-by-Step

### 1. Download Container Template (Proxmox Shell)
```bash
pveam update
pveam list
pveam download <storageLocation> <templateName>
```

### 2. Create Container (Proxmox UI → "Create CT")
| Tab | Setting |
|-----|---------|
| General | Set hostname, password; leave **Nesting** checked |
| General | Uncheck **Unprivileged container** to allow pings from Connector |
| Template | Select storage ID and downloaded template image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge interface; DHCP or static IP recommended |
| DNS | Default (host settings) or custom |

### 3. Prepare Container OS
```bash
apt update
apt upgrade -y
apt install curl -y
```

### 4. Deploy Connector
1. Log into Twingate Admin Console
2. Navigate to target Remote Network
3. Select **Linux** deployment method
4. Click **Generate Tokens**
5. Copy the deployment command (tokens auto-included)
6. Paste and run in container console

## Configuration Values
- **Storage location**: Must have "container templates" enabled as content type
- **Container user**: `root` (use password set during creation)
- **Network**: Static IP recommended if Resources need to allowlist Connector IP or for logging purposes

## Gotchas
- **Unprivileged container**: Must be **unchecked** if you need ICMP/ping support to Resources
- **Nesting**: Must remain **checked** for proper operation
- **No auto-updates**: Stagger updates across multiple Connectors on same Remote Network to avoid downtime; use cron to automate
- `curl` must be installed before running the deployment script
- Peer-to-peer connections should be configured to avoid Fair Use Policy bandwidth limits

## Related Docs
- [Supported Distros](https://www.twingate.com/docs/connector-supported-os)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Automate Updates with Cron](https://www.twingate.com/docs/connector-update)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)