# Twingate Headless IoT Gateway

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT/legacy devices that cannot run the Twingate client directly. The gateway handles DNS resolution, NAT, and secure Resource access via a Service Account. All IoT devices route through this Linux host instead of running individual clients.

## Key Information
- Supported distros: Ubuntu, Debian, Fedora (others may work manually)
- Uses Bind9 for DNS, IPTables for NAT, Twingate headless client for secure access
- Devices on local network point their DNS and default gateway to the Linux machine
- Twingate Resources resolve to CGNAT IP addresses via the gateway's DNS

## Prerequisites
- Linux machine (Debian/Ubuntu/Fedora) with admin access
- Internet connection
- Twingate account with ability to create Service Accounts
- `curl` installed
- Service Account key file (`service_key.json`)

## Step-by-Step

1. **Update system and install curl**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install curl -y
   ```

2. **Download setup script**
   ```bash
   curl https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/main/twingate-headless-client-gateway/twingate-headless-client-gateway.sh -o gateway_config.sh
   ```

3. **Create Service Account**
   - Admin Console → Teams → Services → New Service Account
   - Generate Key → set expiration (0 = unlimited)
   - Download or copy token; save as `service_key.json` in same directory as script

4. **Assign a Resource** to the Service Account (use one with public DNS name for testing)

5. **Run setup script**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```

6. **Verify services**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

7. **Configure client devices** to use Linux gateway IP as DNS server and default gateway

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `./service_key.json` | Path to downloaded Service Account key file |
| `10.0.0.0/24` | Local network CIDR block (replace with actual subnet) |

## Testing

```bash
# DNS - Twingate Resource (expect CGNAT IP)
nslookup twingate.resource.internal

# DNS - External domain (expect public IP)
nslookup google.com

# Internet connectivity
ping 8.8.8.8
```

## Gotchas
- Script only tested on Ubuntu, Debian, Fedora — other distros require manual steps
- `service_key.json` must be in the same directory as `gateway_config.sh` before running
- Service Account key expiration of 0 = unlimited; plan rotation for production
- Client devices must explicitly point DNS and gateway settings to the Linux machine's IP
- Script auto-installs Bind9, IPTables NAT rules, and Twingate headless client — review before running in production

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Script Repository](https://github.com/Twingate-Solutions/general-scripts/tree/main/twingate-headless-client-gateway)
- Bind9 DNS Server on Debian
- IPTables NAT configuration