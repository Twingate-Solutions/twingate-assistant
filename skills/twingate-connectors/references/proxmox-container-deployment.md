# Deploy Twingate Connector in Proxmox Container

## Summary
Guide for deploying a Twingate Connector inside a Proxmox LXC container. Uses Ubuntu 22.04 LTS template as the base image. Process covers container creation, configuration, and Connector installation via the standard Linux deployment script.

## Key Information
- Minimum requirements: 1 vCPU, 512MB RAM
- Uses LXC containers (not full VMs)
- Tested on Proxmox 7.4-3 with Ubuntu 22.04
- Connectors do **not** auto-update — must be managed manually

## Prerequisites
- Proxmox VE installed with a node accessible
- Container template downloaded (Ubuntu 22.04 LTS or other [supported distro](https://www.twingate.com/docs/supported-platforms))
- Access to Twingate Admin Console with a configured Remote Network

## Step-by-Step

### 1. Download Container Template
```bash
pveam update
pveam list
pveam download <storageLocation> <templateName>
```

### 2. Create Container (via Proxmox UI → "Create CT")
| Tab | Setting |
|-----|---------|
| General | Set hostname, password; leave **Nesting** checked |
| General | Uncheck **Unprivileged container** to allow pings to Resources |
| Template | Select storage ID and Ubuntu 22.04 image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge; DHCP or static IP |
| DNS | Default or custom |

### 3. Prepare Container
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
5. Copy the generated deployment command
6. Paste and run in container console

## Configuration Values
- **Storage location**: Proxmox storage ID that supports container templates as content type
- **Container user**: `root` (login via Proxmox VNC/Console tab)
- **Deployment script**: Auto-includes tokens; sourced from Admin Console

## Gotchas
- **Unprivileged containers block ICMP**: Uncheck "Unprivileged container" if you need to ping Resources through the Connector
- **Static IP recommended**: Required if Resources use IP allowlists or if you need consistent network logging
- **cURL is not pre-installed**: Must install before running the deployment script
- **No auto-updates**: Connector updates must be manually triggered or automated via cron job; stagger updates across multiple Connectors on the same Remote Network to avoid downtime
- **Peer-to-peer connections**: Should be configured to avoid Fair Use Policy bandwidth limits

## Related Docs
- [Supported Distros](https://www.twingate.com/docs/supported-platforms)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Automate Updates via Cron Job](https://www.twingate.com/docs/connector-updates)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)