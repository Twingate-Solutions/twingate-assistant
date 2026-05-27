# Deploy Twingate Connector in a Proxmox Container

## Summary
Guide for deploying a Twingate Connector inside a Proxmox LXC container. Uses standard Linux deployment method after container creation. Connector runs as a service within a lightweight container rather than a full VM.

## Key Information
- Proxmox uses LXC containers (not full VMs)
- Minimum specs: 1 vCPU, 512MB RAM
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 template
- Connectors do **not** auto-update — must manage manually or via cron

## Prerequisites
- Proxmox host with a downloaded container template (supported distro required)
- Ubuntu 22.04 LTS recommended
- Access to Twingate Admin Console with a Remote Network configured
- `curl` installed in the container

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
| General | Uncheck **Unprivileged container** to allow pings |
| Template | Select storage + downloaded template image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Select bridge; DHCP or static IP (static recommended) |
| DNS | Default or custom |

### 3. Prepare Container (Console as root)
```bash
apt update
apt upgrade -y
apt install curl -y
```

### 4. Deploy Connector
1. Log in to Twingate Admin Console
2. Navigate to target Remote Network
3. Select **Linux** deployment method
4. Click **Generate Tokens** (tokens auto-included in script)
5. Copy and paste the deployment command into the container console

## Configuration Values
- **Unprivileged container**: Uncheck if ICMP/ping to Resources is needed
- **Nesting**: Must remain enabled
- **Static IP**: Recommended if Resources use IP allowlists or logging is required

## Gotchas
- Tokens are embedded automatically in the generated deploy script — no manual copying needed
- Connectors won't self-update; stagger updates across multiple Connectors on the same Remote Network to avoid downtime
- Must use a [supported distro](https://www.twingate.com/docs) for the container template
- Enable peer-to-peer connections to avoid Fair Use Policy bandwidth issues

## Related Docs
- [Supported distros](https://www.twingate.com/docs)
- [Peer-to-peer connections](https://www.twingate.com/docs)
- [Automate updates with cron job](https://www.twingate.com/docs)
- [Fair Use Policy](https://www.twingate.com/docs)