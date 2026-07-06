# Twingate Headless IoT Gateway

## Summary
Sets up a Linux machine as a centralized Twingate gateway for IoT/legacy devices that cannot run the Twingate Client directly. The gateway handles DNS resolution, NAT internet access, and secure Twingate Resource access for all devices on the local network. Uses a Service Account (headless client) rather than user-based authentication.

## Key Information
- Tested on Ubuntu, Debian, and Fedora-based distributions only
- Gateway installs: Bind9 (DNS), IPTables (NAT), Twingate headless client
- IoT devices point their DNS and default gateway to this Linux machine
- Twingate Resources return CGNAT IP addresses via DNS

## Prerequisites
- Linux machine (Debian/Ubuntu/Fedora) with admin access
- Internet connection
- Twingate account with ability to create Service Accounts
- `curl` installed
- Service Account key file (`service_key.json`)

## Step-by-Step

1. **Update system**: `sudo apt update && sudo apt upgrade -y`
2. **Install curl**: `sudo apt install curl -y`
3. **Download script**:
   ```bash
   curl https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/main/twingate-headless-client-gateway/twingate-headless-client-gateway.sh -o gateway_config.sh
   ```
4. **Create Service Account**: Admin Console → Teams → Services → New Service Account → Generate Key (set expiration; `0` = unlimited)
5. **Save key**: Paste or upload token as `service_key.json` in same directory as `gateway_config.sh`
6. **Assign a Resource** to the Service Account for testing (use one with public DNS name)
7. **Run script**:
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```

## Configuration Values

| Parameter | Description | Example |
|-----------|-------------|---------|
| Arg 1 (script) | Path to service key JSON file | `./service_key.json` |
| Arg 2 (script) | Local network CIDR block | `10.0.0.0/24` |

## Verification Commands

```bash
sudo systemctl status bind9       # Confirm DNS server running
sudo twingate status              # Confirm Twingate connected
nslookup twingate.resource.internal  # Should return CGNAT IP
nslookup google.com               # Should return public IP
ping 8.8.8.8                      # Test internet via NAT
```

## Client Device Configuration
- Set DNS server → Linux gateway IP
- Set default gateway → Linux gateway IP

## Gotchas
- Script only tested on Ubuntu, Debian, Fedora — other distros may require manual steps
- Service Account key expiration: set `0` for unlimited, otherwise access breaks on expiry
- `service_key.json` must be in the same directory as `gateway_config.sh` before running
- IoT devices must be on the same local network as the gateway machine
- The CIDR block parameter must match your actual local network range

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Main Script Repository](https://github.com/Twingate-Solutions/general-scripts/tree/main/twingate-headless-client-gateway)
- Bind9 DNS Server on Debian
- Using IPTables for NAT