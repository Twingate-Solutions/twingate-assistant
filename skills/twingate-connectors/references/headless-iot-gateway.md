# Twingate Headless IoT Gateway

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT/legacy devices that cannot run the Twingate Client directly. The gateway handles DNS resolution, NAT, and secure Twingate Resource access for all devices on the local network using a Service Account.

## Key Information
- Uses Twingate headless Client + Bind9 DNS + IPTables NAT on a single Linux machine
- All downstream devices point their DNS and default gateway to this Linux machine
- Twingate Resources appear as CGNAT IP addresses in DNS responses
- Script tested on Ubuntu, Debian, Fedora; other distros require manual steps

## Prerequisites
- Debian-based (Ubuntu/Debian) or Fedora Linux machine with admin access
- Internet connection
- Twingate account with ability to create Service Accounts
- `curl` installed
- Service Account with at least one Resource assigned for testing

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

3. **Create Service Account key**
   - Admin Console → Teams → Services → New Service Account
   - Click "Generate Key", set expiration (0 = unlimited)
   - Download or copy token → save as `service_key.json` in same directory as script

4. **Run setup script**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```

5. **Verify services**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

6. **Configure client devices** to use Linux gateway IP as both DNS server and default gateway

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `./service_key.json` | Path to Service Account token file |
| `10.0.0.0/24` | Local network CIDR block (replace with actual subnet) |

## Testing
```bash
# DNS resolution for Twingate Resource (expect CGNAT IP)
nslookup twingate.resource.internal

# External DNS (expect public IP)
nslookup google.com

# Internet connectivity
ping 8.8.8.8
```

## Gotchas
- `service_key.json` must be in the **same directory** as `gateway_config.sh` before running
- Script installs Bind9, configures NAT, and installs headless Client automatically — verify no conflicts with existing DNS/firewall configs
- Non-Debian/non-Fedora distros not tested; follow manual steps from script logic
- Service Account key expiration of 0 = unlimited; set appropriate expiration for production
- Assign a Resource to the Service Account **before** testing or DNS resolution via Twingate won't work

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Main Script Repository](https://github.com/Twingate-Solutions/general-scripts)
- Bind9 DNS Server on Debian
- IPTables NAT configuration