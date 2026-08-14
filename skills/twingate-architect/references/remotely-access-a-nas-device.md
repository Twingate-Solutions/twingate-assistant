---
source: https://www.twingate.com/docs/remotely-access-a-nas-device
type: docs
fetched: 2026-08-14
source_version: b822b4d863318cecbfa2214fe4fa873626c6312be92ceef3e18bbd45b76abf9c
---

# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. Access uses the same local IP address as on-network connections, with no public internet exposure.

## Key Information
- Replaces port forwarding (which exposes NAS to internet attacks)
- Eliminates dynamic IP/DDNS complications
- NAS remains accessible via its local IP (e.g., `192.168.x.x` or `10.x.x.x`)
- Access control managed via Twingate group management

## Prerequisites
- Twingate account with admin access
- NAS device with known local IP address
- A device on the local network capable of running a Twingate Connector (may be the NAS itself if supported)
- Twingate client installed on devices needing remote access

## Step-by-Step

1. Create a **Remote Network** in Twingate admin console (e.g., "Home Network")
2. Add the NAS as a **Resource** using its local IP address (`192.168.x.x` or `10.x.x.x`)
3. Add a **Connector** to the Remote Network via the network's detail page
4. Click **Provision** next to the connector (re-authentication required)
5. Install the Connector on a local network device:
   - Synology DSM 6.x or earlier: see Synology DSM 6 connector guide
   - Synology DSM 7.x or later: see Synology DSM 7 connector guide
   - Other devices: see general connector deployment docs
6. Verify Connector is operational
7. Optionally restrict NAS access via **group management**
8. Access NAS remotely using its local IP from any device with Twingate client signed into an authorized account

## Configuration Values
- Resource address: local IP of NAS (typically `192.168.x.x` or `10.x.x.x`)
- No special ports or firewall rules required on router

## Gotchas
- Connector installation on NAS itself depends on what the NAS OS supports — may need a separate local device
- Must re-authenticate when provisioning a connector
- Remote users must have Twingate client installed and be signed into an account with access permissions

## Related Docs
- Connector setup on Synology DSM 6.x or earlier
- Connector setup on Synology DSM 7.x or later
- General connector deployment
- Group management (access control)