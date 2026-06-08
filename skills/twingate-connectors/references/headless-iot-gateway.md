# Twingate Headless IoT Gateway

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT devices or legacy systems that cannot run the Twingate Client directly. The gateway handles DNS resolution, NAT internet access, and secure Twingate Resource access for all devices on the local network.

## Key Information
- Uses Twingate headless Client + Bind9 DNS + IPTables NAT on a single Linux gateway
- Tested on Ubuntu, Debian, and Fedora-based distros only
- Requires a Service Account (not a user account) with a generated Service Key Token
- IoT/legacy devices point their DNS and default gateway to this Linux machine
- Twingate Resources return CGNAT IP addresses via DNS

## Prerequisites
- Debian/Ubuntu or Fedora Linux machine with admin access
- Internet connection on the gateway machine
- Twingate Service Account with a generated Service Key (`service_key.json`)
- At least one Resource assigned to the Service Account

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

3. **Create Service Account:** Admin Console → Teams → Services → New Service Account → Generate Key → save as `service_key.json` in same directory as script

4. **Run the script:**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```
   Parameters: `<path_to_service_key.json>` `<local_network_CIDR>`

5. **Verify services:**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

6. **Configure client devices:** Set DNS and default gateway to the Linux machine's IP

## Configuration Values

| Parameter | Description | Example |
|-----------|-------------|---------|
| `service_key.json` | Service Account token file path | `./service_key.json` |
| Local CIDR | Network block for NAT gateway scope | `10.0.0.0/24` |

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
- `service_key.json` must be in the **same directory** as `gateway_config.sh` before running
- Set token expiration to `0` for unlimited — otherwise gateway breaks when key expires
- Script installs Bind9, IPTables NAT rules, and Twingate headless Client automatically — review before running on production systems
- Other Linux distros may work but require manual steps from the script
- Assign a Resource with a **public DNS name** to the Service Account for easiest initial testing

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Main Script Repository](https://github.com/Twingate-Solutions/general-scripts/tree/main/twingate-headless-client-gateway)
- Bind9 DNS Server on Debian
- Using IPTables for NAT