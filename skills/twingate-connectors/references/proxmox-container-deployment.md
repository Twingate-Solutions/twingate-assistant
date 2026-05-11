# Deploy Twingate Connector in a Proxmox Container

## Summary
Deploys a Twingate Connector inside a Proxmox LXC container using Ubuntu 22.04. The process involves creating an LXC container, installing prerequisites, then running the Twingate deployment script from the Admin Console.

## Key Information
- Proxmox uses LXC containers (lightweight, not full VMs)
- Minimum resources: 1 vCPU, 512MB RAM
- Connectors do **not** auto-update; must be manually updated or via cron
- Stagger updates across multiple Connectors on same Remote Network to avoid downtime
- Enable peer-to-peer connections to stay within Fair Use Policy bandwidth limits

## Prerequisites
- Proxmox VE installed (tested on 7.4-3)
- Supported Linux distro template downloaded (guide uses Ubuntu 22.04 LTS)
- Access to Twingate Admin Console with target Remote Network configured

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
| General | Set hostname, password; keep **Nesting** checked; uncheck **Unprivileged container** to allow pings |
| Template | Select storage ID and downloaded template image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge interface; DHCP or static IP (static recommended) |
| DNS | Default or custom |

### 3. Install Prerequisites in Container
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
5. Optionally enable local connection logs (for SIEM)
6. Copy and paste the generated deployment command into the container console

## Configuration Values
- **Username for console login:** `root`
- **Storage location:** any Proxmox storage ID that allows container templates as content type
- **Deployment script:** auto-generated in Admin Console (includes tokens)

## Gotchas
- **Unprivileged container** must be **unchecked** if ICMP/ping to Resources is needed
- **Nesting** must remain **checked**
- Static IP strongly recommended if Resources need to allowlist the Connector IP or for network logging
- `curl` must be installed before running the deployment script
- Connectors never self-update — plan update strategy explicitly; use cron for automation

## Related Docs
- [Supported Linux distros](https://www.twingate.com/docs)
- [Peer-to-peer connections support](https://www.twingate.com/docs)
- [Fair Use Policy](https://www.twingate.com/docs)
- [Automating updates with cron](https://www.twingate.com/docs)