# Twingate Headless IoT Gateway

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT/legacy devices that cannot run the Twingate Client directly. The gateway handles DNS resolution, NAT internet access, and secure Twingate Resource access for all devices on the local network via a headless client and Service Account.

## Key Information
- Uses Twingate headless client + Bind9 DNS + IPTables NAT on a single Linux gateway machine
- IoT/legacy devices point their DNS and default gateway to this Linux machine
- Twingate Resources resolve to CGNAT IP addresses via the gateway's DNS
- Tested on Ubuntu, Debian, and Fedora; other distros may require manual steps
- Service Account + Service Key Token used for authentication (no user login required)

## Prerequisites
- Debian-based (Ubuntu/Debian) or Fedora Linux machine
- `sudo`/admin access
- Internet connection
- Twingate account with ability to create Service Accounts
- `curl` installed

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
   - Click "Generate Key" → set expiration (0 = unlimited)
   - Download or copy the Service Key Token

4. **Save token file**
   - Save token as `service_key.json` in the same directory as `gateway_config.sh`

5. **Assign a Resource** to the Service Account for testing (use one with a public DNS name)

6. **Run setup script**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```

7. **Verify services**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

8. **Configure client devices** to use the Linux gateway's IP as both DNS server and default gateway

## Configuration Values

| Parameter | Description |
|-----------|-------------|
| `./service_key.json` | Path to Service Account key file (arg 1) |
| `10.0.0.0/24` | Local network CIDR block (arg 2) |

Script auto-installs and configures: Bind9, IPTables NAT rules, Twingate headless client.

## Verification Tests

```bash
# On client device:
nslookup twingate.resource.internal  # Should return CGNAT IP
nslookup google.com                   # Should return public IP
ping 8.8.8.8                          # Internet connectivity
```

## Gotchas
- Script only tested on Ubuntu, Debian, Fedora — other distros need manual configuration
- `service_key.json` must be in the **same directory** as `gateway_config.sh` before running
- Set key expiration to `0` for non-expiring tokens (IoT deployments often need this)
- All IoT devices must be on the **same local network** as the gateway machine

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Main Script Repository](https://github.com/Twingate-Solutions/general-scripts)
- Bind9 DNS Server on Debian
- IPTables NAT configuration