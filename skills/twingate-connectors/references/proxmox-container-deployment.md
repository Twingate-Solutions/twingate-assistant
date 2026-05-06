# Deploy Twingate Connector in Proxmox Container

## Summary
Guide for deploying a Twingate Connector inside a Proxmox VE Linux Container (LXC). Uses Ubuntu 22.04 LTS template as the base, with minimal resource requirements. Connector installation uses the standard Linux deployment script from the Admin Console.

## Key Information
- Proxmox uses LXC (Linux Containers), not full VMs
- Minimum requirements: 1 vCPU, 512MB RAM
- Tested on Proxmox 7.4-3 with Ubuntu 22.04 template
- Connectors do **not** auto-update; manual update strategy required

## Prerequisites
- Proxmox VE host with shell access
- Container template from a [supported distro](https://www.twingate.com/docs/supported-platforms) downloaded to local storage
- Twingate Admin Console access with an existing Remote Network

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
| General | Set hostname/password; leave **Nesting** checked; uncheck **Unprivileged container** to allow pings |
| Template | Select storage ID and downloaded image |
| Disks | Default 8GB sufficient |
| CPU | Default 1 vCPU |
| Memory | Default 512MB |
| Network | Set bridge + DHCP or static IP (static recommended) |
| DNS | Default or custom |

### 3. Prepare Container
```bash
apt update
apt upgrade -y
apt install curl -y
```

### 4. Install Connector
1. Open Twingate Admin Console → Remote Network → select Linux deployment
2. Click **Generate Tokens** (tokens auto-embed in script)
3. Copy deployment command and paste into container console
4. Verify Connector shows as connected in Admin Console

## Configuration Values
- **vCPU:** 1 minimum
- **RAM:** 512MB minimum
- **Disk:** 8GB default (sufficient)
- **Container user:** `root`
- **Nesting:** Must remain enabled
- **Unprivileged container:** Uncheck if ICMP/ping to resources is required

## Gotchas
- **Unprivileged containers block pings** — uncheck if Resources need to be pinged from the Connector
- **Static IP strongly recommended** — required if Resources use IP allowlisting or if network logging is in use
- **No auto-updates** — build Connectors into your patching schedule; stagger updates across multiple Connectors on the same Remote Network to avoid downtime
- `curl` must be installed before running the deployment script
- Peer-to-peer connections should be configured to stay within the Fair Use Policy bandwidth limits

## Related Docs
- [Supported Distros](https://www.twingate.com/docs/supported-platforms)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Automate Updates with Cron](https://www.twingate.com/docs/connector-updates)
- [Linux Connector Deployment](https://www.twingate.com/docs/linux-connector)