# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. Access occurs through the device's local IP address, keeping the NAS off the public internet.

## Key Information
- Replaces port forwarding (which exposes NAS to internet attacks)
- No dynamic DNS needed — use the NAS's local IP address regardless of ISP's dynamic IP assignment
- Access controlled via Twingate group management
- Connector can sometimes be installed directly on the NAS device

## Prerequisites
- Twingate account with admin access
- NAS device with known local IP address (typically `192.168.x.x` or `10.x.x.x`)
- A device on the local network capable of running a Twingate Connector (or a compatible NAS)
- Twingate client installed on the remote access device

## Step-by-Step

1. **Create Remote Network** — Add a new Remote Network in Twingate admin (e.g., "Home Network")
2. **Add NAS as Resource** — Specify the NAS's local IP address as the resource
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision"; re-authentication required
5. **Install Connector** — Install on a local network device (or directly on NAS if supported)
   - Synology DSM 6.x or earlier: see Synology DSM 6 guide
   - Synology DSM 7.x or later: see Synology DSM 7 guide
6. **Verify Connector** — Confirm connector is operational in admin console
7. **Configure Access Control** — Restrict access via group management if needed
8. **Connect** — Use Twingate client signed into an authorized account; reach NAS at its local IP

## Configuration Values
- **Resource address**: Local NAS IP (e.g., `192.168.1.x` or `10.0.0.x`)
- **Network name**: User-defined (e.g., "Home Network", "Office Network")

## Gotchas
- Re-authentication is required during the connector provisioning step
- Not all NAS devices support running a Connector directly — may need a separate device (e.g., Raspberry Pi, router) on the same network
- Connector must remain operational for remote access to work; if the host device goes offline, access is lost

## Related Docs
- Connector deployment overview
- Synology NAS Connector setup (DSM 6.x or earlier)
- Synology NAS Connector setup (DSM 7.x or later)
- Group management for access control