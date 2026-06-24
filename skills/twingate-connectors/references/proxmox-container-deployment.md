# Deploy Twingate Connector in Proxmox Container

## Summary
Deploys a Twingate Connector inside a Proxmox LXC container using the Linux deployment script. Uses standard Proxmox container creation workflow followed by the Twingate Admin Console token generation process.

## Key Information
- Minimum container specs: 1 vCPU, 512MB RAM
- Uses LXC containers (not full VMs)
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 template
- Connectors do **not** auto-update; must be managed manually or via cron

## Prerequisites
- Proxmox host with shell access
- Container template downloaded (Ubuntu 22.04 LTS recommended)
- Supported Linux distro template available in storage
- Access to Twingate Admin Console with a configured Remote Network

## Step-by-Step

### 1. Download Container Template
```bash
pveam update
pveam list
pveam download <storageLocation> <templateName>
```

### 2. Create Container (Proxmox UI)
- **General**: Set hostname/password; keep **Nesting** checked; uncheck **Unprivileged container** to allow pings
- **Template**: Select storage ID and downloaded image
- **Disks**: Default 8GB sufficient
- **CPU**: 1 vCPU default
- **Memory**: 512MB default
- **Network**: Assign bridge interface; recommend **static IP** over DHCP
- **DNS**: Default or custom

### 3. Prepare Container
```bash
apt update
apt upgrade -y
apt install curl -y
```

### 4. Deploy Connector
1. In Twingate Admin Console → Remote Network → select **Linux** deployment
2. Click **Generate Tokens**
3. Copy the generated deployment command (tokens auto-included)
4. Paste and run in container console

## Configuration Values

| Setting | Recommended Value |
|---|---|
| vCPU | 1 |
| RAM | 512MB minimum |
| Disk | 8GB |
| Nesting | Enabled |
| Unprivileged container | Disabled (if pings needed) |
| IP assignment | Static (preferred) |

## Gotchas
- **Unprivileged container** must be unchecked to allow ICMP/ping to Resources
- Static IP strongly recommended if Resources require allowlisting the Connector IP or for network logging
- `curl` must be installed before running the deployment script
- Connectors won't self-update — stagger updates across multiple Connectors on the same Remote Network to avoid downtime
- Peer-to-peer connections should be configured to comply with Fair Use Policy bandwidth limits

## Related Docs
- [Supported Linux distros](https://www.twingate.com/docs)
- [Peer-to-peer connections](https://www.twingate.com/docs)
- [Automate updates via cron job](https://www.twingate.com/docs)
- [Fair Use Policy](https://www.twingate.com/docs)