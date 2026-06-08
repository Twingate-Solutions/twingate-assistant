# Remotely Access a NAS Device

## Summary
Configure Twingate to securely access a NAS device remotely without port forwarding or dynamic DNS. Traffic routes through a Connector installed on the local network, keeping the NAS off the public internet while remaining accessible via its local IP address.

## Key Information
- Eliminates need for port forwarding (avoids direct internet exposure)
- No dynamic DNS required; access NAS via its static local IP (e.g., `192.168.x.x` or `10.x.x.x`)
- Connector can be installed on the NAS itself (device-dependent) or another local machine
- Synology NAS has dedicated setup guides for DSM 6.x and DSM 7.x

## Prerequisites
- Twingate account with admin access
- NAS device with known local IP address
- A device on the local network capable of running a Twingate Connector
- Twingate client installed on the remote access device

## Step-by-Step

1. **Create Remote Network** — In Twingate admin console, add a new Remote Network (e.g., "Home Network" or "Office Network")
2. **Add NAS as Resource** — Specify the NAS local IP address (e.g., `192.168.x.x` or `10.x.x.x`)
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision" next to the new connector (re-authentication required)
5. **Install Connector** — Deploy on a local network device following in-app instructions:
   - Synology DSM 6.x or earlier: see dedicated guide
   - Synology DSM 7.x or later: see dedicated guide
6. **Verify Connector** — Confirm connector is operational in the admin console
7. **Configure Access Control** (optional) — Restrict NAS access via group management
8. **Connect Remotely** — Use Twingate client signed into an authorized account; reach NAS at its local IP

## Configuration Values
- Resource address: local NAS IP (e.g., `192.168.1.x`, `10.0.0.x`)
- No special ports or DNS entries required

## Gotchas
- Connector installation on NAS depends on NAS hardware/OS support — verify compatibility before choosing the NAS as the connector host
- Re-authentication is required during the Provision step
- Remote access only works on devices with Twingate client installed and signed into an authorized account
- Access restrictions are managed through groups, not at the resource level directly

## Related Docs
- [Connector on Synology DSM 6.x or earlier](#)
- [Connector on Synology DSM 7.x or later](#)
- [Deploying Connectors](/docs/connectors)
- [Group Management](/docs/groups)