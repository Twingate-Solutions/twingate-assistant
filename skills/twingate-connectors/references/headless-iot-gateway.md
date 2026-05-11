# Twingate Headless IoT Gateway

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT/legacy devices that cannot run the Twingate Client directly. The gateway handles DNS resolution, NAT, and secure Resource access via a headless Twingate Client and Service Account.

## Key Information
- Supports Debian/Ubuntu and Fedora-based Linux distributions
- Uses Bind9 for DNS, IPTables for NAT, and Twingate headless Client
- All IoT devices route traffic through the Linux gateway (DNS + default gateway)
- Twingate Resources appear as CGNAT IP addresses in DNS responses

## Prerequisites
- Linux machine (Ubuntu/Debian/Fedora; others may work but untested)
- Administrative (sudo) access
- Twingate account with ability to create Service Accounts
- Service Account with at least one Resource assigned

## Step-by-Step

1. **Update system and install curl:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install curl -y
   ```

2. **Download setup script:**
   ```bash
   curl https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/main/twingate-headless-client-gateway/twingate-headless-client-gateway.sh -o gateway_config.sh
   ```

3. **Create Service Account key:**
   - Admin Console → Teams → Services → New Service Account
   - Click "Generate Key", set expiration (0 = unlimited)
   - Download or copy the token; save as `service_key.json` in same directory as script

4. **Run setup script:**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```
   Parameters: `<path-to-service-key.json>` `<local-network-CIDR>`

5. **Verify services:**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

6. **Configure IoT devices:** Point DNS and default gateway to the Linux machine's IP

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `./service_key.json` | Path to downloaded Service Account key file |
| `10.0.0.0/24` | Local network CIDR block (replace with actual subnet) |

## Testing

```bash
# DNS for Twingate Resource (expect CGNAT IP)
nslookup twingate.resource.internal

# External DNS (expect public IP)
nslookup google.com

# Internet connectivity
ping 8.8.8.8
```

## Gotchas
- `service_key.json` must be in the same directory as `gateway_config.sh` before running
- Script only tested on Ubuntu, Debian, and Fedora — other distros require manual steps
- IoT devices must explicitly set both DNS **and** default gateway to the Linux machine's IP
- Assign a Resource to the Service Account before testing; public DNS name recommended for initial validation
- Service key expiration of 0 = unlimited; consider security implications for production

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Twingate Scripts Repository](https://github.com/Twingate-Solutions/general-scripts)
- Bind9 DNS Server on Debian
- IPTables NAT configuration