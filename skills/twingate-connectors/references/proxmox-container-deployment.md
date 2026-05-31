# Deploy Twingate Connector in a Proxmox Container

## Summary
Guide for deploying a Twingate Connector inside a Proxmox LXC container. Uses Ubuntu 22.04 template with minimal resource requirements. Installation follows standard Linux Connector deployment via script from the Admin Console.

## Key Information
- Proxmox uses LXC containers (lightweight, no separate kernel)
- Minimum specs: 1 vCPU, 512MB RAM
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 template
- Connectors do **not** auto-update — must be managed manually or via cron

## Prerequisites
- Proxmox VE installed with shell access
- LXC container template downloaded (Ubuntu 22.04 recommended)
- Access to Twingate Admin Console with a configured Remote Network

## Step-by-Step

### 1. Download Container Template
```bash
pveam update
pveam list
pveam download <storageLocation> <templateName>
```

### 2. Create LXC Container (via Proxmox UI)
| Tab | Setting |
|-----|---------|
| General | Set hostname, password; leave **Nesting** checked |
| General | Uncheck **Unprivileged container** to allow pings to Resources |
| Template | Select storage + downloaded image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge interface; DHCP or static IP |
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
4. Click **Generate Tokens** (tokens auto-included in script)
5. Copy deployment command and run in container console

## Configuration Values
- **storageLocation**: Proxmox storage ID that supports container templates
- **templateName**: Copied from `pveam list` output

## Gotchas
- **Unprivileged container**: Must be **unchecked** if ICMP (ping) to Resources is required
- **Static IP recommended**: Required if Resources have IP allowlists or if network logging is in use
- **No auto-updates**: Stagger updates across multiple Connectors on the same Remote Network to avoid downtime
- `curl` must be installed before running the deployment script
- Peer-to-peer connections should be configured to avoid Fair Use Policy bandwidth limits

## Related Docs
- [Supported Linux distros](https://www.twingate.com/docs/supported-platforms)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Automate updates with cron](https://www.twingate.com/docs/connector-cron-updates)