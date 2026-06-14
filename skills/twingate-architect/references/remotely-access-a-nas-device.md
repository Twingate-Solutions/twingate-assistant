# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. Traffic routes through Twingate's network rather than exposing the NAS directly to the internet. Users access the NAS via its local IP address regardless of physical location.

## Key Information
- Replaces port forwarding approach which exposes NAS to public internet
- No dynamic DNS needed — access NAS via its existing local IP (e.g., `192.168.x.x` or `10.x.x.x`)
- Connector must be installed on a device on the same local network as the NAS (or on the NAS itself if supported)
- Access control managed via Twingate group management

## Prerequisites
- Active Twingate account with admin access
- NAS device with a known static local IP address
- A device on the same local network capable of running a Twingate Connector (or NAS itself if compatible)
- Twingate client installed on end-user devices

## Step-by-Step

1. Create a **Remote Network** in Twingate admin console (e.g., "Home Network")
2. Add the NAS as a **Resource** using its local IP address (`192.168.x.x` or `10.x.x.x`)
3. Add a **Connector** to the Remote Network via its details page
4. **Provision** the connector (requires re-authentication)
5. Install the connector on a local network device:
   - Synology DSM 6.x or earlier: see Synology DSM 6 connector guide
   - Synology DSM 7.x or later: see Synology DSM 7 connector guide
   - Other devices: see general connector deployment docs
6. Verify connector is operational
7. Optionally restrict access via **group management**
8. Connect using Twingate client with an authorized account; use the NAS's local IP to reach it

## Configuration Values
- Resource IP: local network address of NAS (typically `192.168.x.x` or `10.x.x.x`)
- No additional ports or firewall rules required on the router

## Gotchas
- NAS must have a **static local IP** — if its local IP changes, the Twingate resource definition becomes invalid
- Connector must be on the **same local network** as the NAS to route traffic correctly
- Not all NAS devices support running a Connector directly — may need a separate machine (e.g., always-on PC or router)
- Re-authentication required during connector provisioning step

## Related Docs
- Synology NAS Connector setup (DSM 6.x or earlier)
- Synology NAS Connector setup (DSM 7.x or later)
- Connector deployment general guide
- Group management for access control