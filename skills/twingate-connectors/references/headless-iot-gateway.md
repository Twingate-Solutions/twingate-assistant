## Headless IoT Gateway

Sets up a Linux machine as a centralized Twingate headless Client gateway for IoT devices and legacy systems that cannot run the Twingate Client directly. The gateway handles DNS, NAT, and Twingate Resource access on behalf of devices on the local network.

**Use Cases:**
- IoT devices (smart thermostats, cameras, sensors) needing access to remote management servers
- Legacy systems incompatible with the Twingate Client

**Prerequisites:**
- Linux machine on a supported Debian-based distro (Ubuntu, Debian) or Fedora
- Administrative (root/sudo) access
- Twingate Service Account with a generated Service Key Token

**Step-by-Step:**
1. Update system: `sudo apt update && sudo apt upgrade -y && sudo apt install curl -y`
2. Download setup script:
   ```
   curl https://raw.githubusercontent.com/Twingate-Solutions/general-scripts/main/twingate-headless-client-gateway/twingate-headless-client-gateway.sh -o gateway_config.sh
   ```
3. In Twingate Admin Console: Teams → Services → create a Service Account → Generate Key → download/copy `service_key.json` to the same folder as the script
4. Assign a Resource to the Service Account for testing
5. Run: `sudo ./gateway_config.sh ./service_key.json 10.0.0.0/24` (replace CIDR with your local network)
   - Script installs Bind9, configures NAT, and installs the Twingate headless Client
6. Verify: `sudo systemctl status bind9` and `sudo twingate status`
7. Point IoT device DNS and gateway to the Linux gateway's IP
8. Test: Twingate Resource FQDNs should resolve to CGNAT IPs; external DNS resolves normally; internet access works via NAT

**Related Docs:**
- /docs/linux-headless -- Linux headless Client documentation
- /docs/services -- Service Accounts overview
