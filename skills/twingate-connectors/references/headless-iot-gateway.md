# Twingate Headless IoT Gateway

## Summary
Configure a Linux machine as a centralized Twingate gateway for IoT devices or legacy systems that cannot run the Twingate Client directly. The gateway handles DNS resolution (via Bind9), NAT internet access (via iptables), and secure Twingate Resource access using a Service Account.

## Key Information
- Tested on Ubuntu, Debian, and Fedora-based distributions only
- Uses a Service Account (not user account) for headless authentication
- Gateway handles DNS + NAT + Twingate tunneling for downstream devices
- IoT/client devices point their DNS and default gateway to this Linux machine
- Twingate assigns CGNAT IP addresses to Resources

## Prerequisites
- Linux machine (Debian/Ubuntu/Fedora-based)
- Administrative (sudo) access
- Internet connection
- Twingate account with permission to create Service Accounts
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
   - Click "Generate Key", set expiration (0 = unlimited)
   - Download or copy the Service Key Token

4. **Save token file**
   - Save token as `service_key.json` in same directory as `gateway_config.sh`

5. **Assign at least one Resource** to the Service Account (use a public DNS name for testing)

6. **Run setup script**
   ```bash
   sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24
   ```

7. **Verify services**
   ```bash
   sudo systemctl status bind9
   sudo twingate status
   ```

8. **Configure client devices** to use Linux gateway IP as both DNS server and default gateway

## Configuration Values

| Parameter | Description | Example |
|-----------|-------------|---------|
| Arg 1 | Path to service key JSON file | `./service_key.json` |
| Arg 2 | Local network CIDR block | `10.0.0.0/24` |

Script auto-installs and configures: **Bind9**, **iptables NAT**, **Twingate headless client**

## Testing Commands
```bash
# Twingate Resource DNS (expect CGNAT IP)
nslookup twingate.resource.internal

# External DNS (expect public IP)
nslookup google.com

# Internet connectivity
ping 8.8.8.8
```

## Gotchas
- Script only tested on Ubuntu, Debian, Fedora — other distros require manual steps
- Service Key expiration of 0 = unlimited; plan rotation for production
- Client devices must explicitly set both DNS **and** gateway to the Linux machine's IP
- Service Account must have Resources assigned before testing connectivity

## Related Docs
- [Linux Headless Clients](https://www.twingate.com/docs/linux-headless)
- [Script Repository](https://github.com/Twingate-Solutions/general-scripts/tree/main/twingate-headless-client-gateway)
- Bind9 DNS Server on Debian
- IPTables NAT configuration