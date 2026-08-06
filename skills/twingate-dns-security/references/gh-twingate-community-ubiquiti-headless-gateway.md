---
source: https://github.com/Twingate-Community/ubiquiti-headless-gateway
type: github
fetched: 2026-08-06
source_version: 48505939ccbf648040335963761379ffb437f725
---

<!-- triage: unassigned -->

# Twingate Headless Client for Ubiquiti Gateways

## Summary
Deploys a Twingate headless client inside a systemd-nspawn Debian container on Ubiquiti UniFi OS gateways. Intercepts DNS queries from a designated VLAN via iptables and forwards them through bind9 to Twingate's split-DNS resolvers, giving all VLAN devices transparent access to Twingate-published resources without per-device client installation.

## Key Information
- Supported hardware: UDM Pro, UDM SE, UCG-Max, UXG-Pro, UXG-Max (UniFi OS 3.x+)
- Container uses host networking namespace; Twingate creates an `sdwan0` tunnel interface
- bind9 listens on port 5353 to avoid conflict with UniFi's dnsmasq on port 53
- DNS flow: `VLAN device (:53) → iptables REDIRECT → bind9 (:5353) → Twingate resolvers (100.95.0.251–254)`
- Container root is stored at `/data/custom/machines/<container-name>` (persists across firmware updates)
- Routing rules restored on boot via a dedicated `twingate-routing.service` systemd unit
- Container runs with `Capability=all` and shares the host network stack (filesystem-level isolation only)
- Default container root password is `twingate` — change it if the container is exposed

## Prerequisites
- SSH root access to the gateway
- UniFi OS 3.x or later
- Twingate account with admin access
- Twingate service account with a generated service key (JSON) and resources assigned to it
- Internet connectivity on the gateway

## Usage / Step-by-Step

**1. Generate a service key**
In the Twingate Admin Console: Team → Services → Create Service Account → Generate Key → download JSON.

**2. Copy the key to the gateway**
```bash
scp twingate-service-key.json root@<gateway-ip>:/root/
```

**3. Run setup (interactive)**
```bash
curl -sSf https://raw.githubusercontent.com/Twingate-Community/ubiquiti-headless-gateway/main/setup.sh | sudo bash
```

**3. Run setup (non-interactive)**
```bash
export CONTAINER_NAME="twingate-headless"
export TWINGATE_SERVICE_KEY_FILE="/root/twingate-service-key.json"
export TWINGATE_VLAN_SUBNET="192.168.4.0/24"
curl -sSf .../setup.sh | sudo -E bash
```

**4. Configure UniFi Network UI**
- Create a VLAN network matching `TWINGATE_VLAN_SUBNET`
- Assign devices, switch ports, or SSIDs to that VLAN

**Uninstall**
```bash
curl -sSf .../uninstall.sh | sudo bash
# Non-interactive: add --force flag and set CONTAINER_NAME env var
```

## Configuration Values

| Variable | Required | Default | Description |
|---|---|---|---|
| `CONTAINER_NAME` | No | `twingate-headless` | systemd-nspawn container name |
| `TWINGATE_SERVICE_KEY_FILE` | Yes | (prompted) | Path to service key JSON |
| `TWINGATE_VLAN_SUBNET` | No | `192.168.4.0/24` | VLAN subnet in CIDR notation |

## Gotchas
- Pass `-E` to `sudo` in non-interactive mode or env vars will not be inherited
- debootstrap downloads ~400MB; initial setup can take 10+ minutes on gateway eMMC
- Only resources explicitly assigned to the service account are accessible
- Container runs Twingate as real root due to UniFi OS kernel user namespace limitations
- After uninstall, manually remove the VLAN and any related firewall rules in the UniFi UI

## Related Docs
- [Twingate Documentation](https://docs.twingate.com)
- [Ubiquiti Gateway Connector](https://github.com/Twingate-Community/ubiquiti-gateway-connector) (inverse use case)
-