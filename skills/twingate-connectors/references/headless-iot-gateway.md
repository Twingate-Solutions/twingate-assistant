---
source: https://www.twingate.com/docs/headless-iot-gateway
type: docs
fetched: 2026-08-14
source_version: 98876d783bb21e21c2fee27975c10ad347c147cdfc5c2aaf60b2a83c60c71123
---

# Headless IoT Gateway Setup

## Page Title
How to Create a Gateway for IoT Using the Headless Client

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT/legacy devices that cannot run the Twingate Client directly. The gateway handles DNS resolution (via Bind9), NAT routing, and Twingate tunnel termination on behalf of downstream devices. All IoT devices route traffic through this single gateway machine.

## Key Information
- Gateway machine runs Twingate headless Client; downstream devices need zero Twingate software
- Uses a **Service Account** (not user account) for authentication
- Script automates: Bind9 install/config, IPTables NAT rules, Twingate headless Client install
- Tested on Ubuntu, Debian, Fedora; other distros require manual steps
- Twingate Resources appear at CGNAT IP addresses from downstream devices' perspective

## Prerequisites
- Debian-based or Fedora Linux machine with admin/sudo access
- Twingate account with ability to create Service Accounts
- Service Account Key (JSON token file)
- IoT devices on same local network, configurable DNS/gateway settings
- `curl` installed on gateway machine

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

3. **Create Service Account:**
   - Admin Console → Teams → Services → New Service Account
   - Generate Key → set expiration (0 = unlimited)
   - Download/copy token → save as `service_key.json` in same directory as script

4. **Assign at least one Resource to the Service Account** (use a public DNS name for testing)

5. **Run setup script:**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```

6. **Verify services:**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

7. **Configure IoT devices:** point DNS and default gateway to gateway machine's IP

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `./service_key.json` | Path to Service Account key file (arg 1) |
| `10.0.0.0/24` | Local network CIDR block (arg 2) |

## Testing
```bash
# From downstream device:
nslookup <twingate-resource-hostname>  # Should return CGNAT IP
nslookup google.com                    # Should return public IP
ping 8.8.8.8                           # Internet connectivity check
```

## Gotchas
- Script only tested on Ubuntu, Debian, Fedora — other distros need manual execution of equivalent steps
- Service Key expiration: setting to `0` gives unlimited; otherwise key rotation required before expiry
- `service_key.json` must be in the **same directory** as `gateway_config.sh` (or provide correct path)
- IoT devices must have their DNS *and* default gateway manually pointed to the Linux gateway machine
- Twingate Resources resolve to CGNAT addresses — downstream devices don't need to know this, but firewall rules must not block CGNAT ranges

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Main Script Repository](https://github.com/Twingate-Solutions/general-scripts)
- Bind9 DNS Server on Debian (external)
- IPTables NAT documentation (external)