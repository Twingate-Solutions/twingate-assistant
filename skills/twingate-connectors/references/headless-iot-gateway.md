# Twingate Headless IoT Gateway

## Summary
Configures a Linux machine as a centralized Twingate gateway for IoT/legacy devices that cannot run the Twingate client directly. The gateway handles DNS resolution, NAT, and secure Twingate Resource access for all devices on the local network via a single Service Account.

## Key Information
- Gateway runs Twingate headless client + Bind9 DNS + IPTables NAT
- IoT devices point their DNS and default gateway to the Linux machine's IP
- Twingate Resources resolve to CGNAT IPs; external DNS resolves normally
- Script tested on Ubuntu, Debian, and Fedora-based systems only
- Service Account + Service Key Token used for authentication (not user credentials)

## Prerequisites
- Linux machine (Debian/Ubuntu/Fedora-based)
- Administrative (sudo) access
- Internet connection
- Twingate Service Account with generated Service Key Token (`.json`)
- At least one Resource assigned to the Service Account

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
   - Download or copy the Service Key Token JSON

4. **Place `service_key.json`** in the same directory as `gateway_config.sh`

5. **Run setup script**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```
   Replace `10.0.0.0/24` with your actual local network CIDR.

6. **Verify services**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

7. **Configure IoT devices** to use the Linux gateway's IP as both DNS server and default gateway.

## Configuration Values

| Parameter | Description | Example |
|-----------|-------------|---------|
| `./service_key.json` | Path to Service Key Token file | `./service_key.json` |
| `<CIDR>` | Local network CIDR block | `10.0.0.0/24` |

## Gotchas
- Script only tested on Ubuntu, Debian, Fedora — other distros require manual steps
- Service Key expiration of `0` = unlimited; plan rotation for production use
- `service_key.json` must be in the same directory as `gateway_config.sh` before running
- IoT devices must have both DNS **and** gateway settings pointing to the Linux machine for full functionality
- Test Resource should have a public DNS name for easier validation

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless-client)
- [Main Script Repository](https://github.com/Twingate-Solutions/general-scripts)
- Bind9 DNS Server on Debian
- IPTables NAT configuration