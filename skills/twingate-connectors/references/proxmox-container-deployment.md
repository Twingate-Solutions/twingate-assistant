# Deploy Twingate Connector in a Proxmox LXC Container

## Summary
Deploys a Twingate Connector inside a Proxmox LXC container using an Ubuntu 22.04 template. The process covers container creation, configuration, and running the Twingate deployment script. Connectors do not auto-update and require manual update management.

## Key Information
- Minimum resources: 1 vCPU, 512MB RAM
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 LTS template
- LXC containers are preferred over full VMs for single-service deployments
- Static IP recommended if Resources need to allowlist the Connector IP or for logging purposes
- Connectors do **not** auto-update; stagger updates across Connectors to avoid downtime

## Prerequisites
- Proxmox VE host with shell access
- Container template downloaded (Ubuntu 22.04 LTS recommended)
- Supported Linux distro template
- Twingate Admin Console access with a configured Remote Network

## Step-by-Step

### 1. Download Container Template
```bash
pveam update
pveam list
pveam download <storageLocation> <templateName>
```

### 2. Create Container (`Create CT` button)
| Tab | Setting |
|-----|---------|
| General | Set hostname, password; keep **Nesting** checked; uncheck **Unprivileged container** to allow pings |
| Template | Select storage ID and downloaded template image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge interface; DHCP or static IP (static recommended) |
| DNS | Default or custom |

### 3. Prepare Container
```bash
apt update
apt upgrade -y
apt install curl -y
```

### 4. Deploy Connector
1. Log in to Twingate Admin Console
2. Navigate to target Remote Network
3. Select **Linux** deployment method
4. Click **Generate Tokens** (tokens are auto-embedded in script)
5. Optionally enable local connection logs (for SIEM)
6. Copy and paste the generated deployment command into the container console

## Configuration Values
- **Login user**: `root`
- **Console access**: Proxmox VNC console tab
- **cURL**: Required dependency for deployment script

## Gotchas
- **Unprivileged container**: Must be **unchecked** to allow ICMP/pings from the Connector to Resources
- **Nesting**: Must remain **checked**
- Auto-updates are not supported — build into existing update strategy
- `curl` must be installed before running the deployment script or it will fail
- `storageLocation` must have container templates enabled as a content type

## Related Docs
- [Supported Linux distros](https://www.twingate.com/docs)
- [Peer-to-peer connections setup](https://www.twingate.com/docs)
- [Fair Use Policy](https://www.twingate.com/docs)
- [Automate updates with cron job](https://www.twingate.com/docs)