# Twingate Headless IoT Gateway

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT devices or legacy systems that cannot run the Twingate Client directly. The gateway handles DNS resolution, NAT internet access, and secure Twingate Resource connections for all devices on the local network.

## Key Information
- Tested on Ubuntu, Debian, and Fedora-based distros only
- Script installs Bind9 (DNS), configures IPTables NAT, and installs Twingate headless Client
- Uses a Service Account (not user account) for authentication
- IoT devices point their DNS and default gateway to the Linux machine's IP
- Twingate Resources appear with CGNAT IP addresses in DNS responses

## Prerequisites
- Linux machine (Debian/Ubuntu/Fedora-based)
- `sudo` / administrative access
- Internet connection
- Twingate account with ability to create Service Accounts
- `curl` installed

## Step-by-Step

1. Update system: `sudo apt update && sudo apt upgrade -y`
2. Install curl if missing: `sudo apt install curl -y`
3. Download setup script:
   ```bash
   curl https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/main/twingate-headless-client-gateway/twingate-headless-client-gateway.sh -o gateway_config.sh
   ```
4. In Admin Console → **Teams → Services**, create a Service Account
5. Click **Generate Key**, set expiration (0 = unlimited), save/copy token
6. Save token as `service_key.json` in the same directory as `gateway_config.sh`
7. Assign at least one Resource to the Service Account (public DNS name recommended for testing)
8. Run the script:
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```

## Configuration Values

| Parameter | Description | Example |
|-----------|-------------|---------|
| Arg 1 | Path to service key JSON file | `./service_key.json` |
| Arg 2 | Local network CIDR block | `10.0.0.0/24` |

## Verification Commands

```bash
sudo systemctl status bind9      # Confirm DNS server running
sudo twingate status             # Confirm Twingate connected
nslookup twingate.resource.internal   # Should return CGNAT IP
nslookup google.com              # Should return public IP
ping 8.8.8.8                    # Test NAT/internet via gateway
```

## Gotchas
- Script only tested on Ubuntu/Debian/Fedora — other distros require manual steps
- `service_key.json` must be in the **same directory** as `gateway_config.sh` before running
- Client devices must manually set DNS **and** default gateway to the Linux machine's IP
- Service Key expiration of `0` = unlimited — set intentionally for long-running gateways
- Non-Twingate DNS (e.g., `google.com`) routes normally; only Twingate Resources return CGNAT addresses

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Main Script Repository](https://github.com/Twingate-Solutions/general-scripts)
- Bind9 DNS Server on Debian
- IPTables NAT configuration