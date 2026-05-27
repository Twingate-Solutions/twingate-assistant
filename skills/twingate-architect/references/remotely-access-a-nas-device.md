# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. Traffic routes through a Connector on your local network, keeping the NAS off the public internet and accessible via its local IP address.

## Key Information
- Replaces port forwarding (which exposes NAS to internet attacks)
- No dynamic DNS required — access NAS using its static local IP
- NAS remains accessible via same IP as local network access (e.g., `192.168.x.x` or `10.x.x.x`)
- Access control managed via Twingate group management

## Prerequisites
- Active Twingate account with admin access
- NAS device with known local IP address
- A device on the local network capable of running a Twingate Connector (can be the NAS itself if supported)
- Twingate client installed on remote device needing access

## Step-by-Step

1. **Create Remote Network** — In Twingate admin, add a new Remote Network (e.g., "Home Network" or "Office Network")
2. **Add NAS as Resource** — Specify the NAS local IP address (e.g., `192.168.x.x` or `10.x.x.x`)
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision" next to the new connector (re-authentication required)
5. **Install Connector** — Deploy on a local network device following in-app instructions:
   - Synology DSM 6.x or earlier: see Synology DSM 6 guide
   - Synology DSM 7.x or later: see Synology DSM 7 guide
   - Other devices: see general connector deployment docs
6. **Verify Connector** — Confirm connector is operational in admin console
7. **Configure Access Control** — Restrict NAS access via group management if needed
8. **Connect Remotely** — Use Twingate client on remote device, signed into authorized account; access NAS at its local IP

## Configuration Values
- **Resource address**: Local NAS IP (e.g., `192.168.1.x`, `10.0.0.x`)
- No special ports or firewall rules required on the router

## Gotchas
- Re-authentication is required during the Connector provisioning step
- Not all NAS devices support running a Connector directly — may need a separate device (e.g., Raspberry Pi, another server) on the same network
- Connector must remain online and operational for remote access to work
- Access is restricted by group membership — newly added users won't have access unless explicitly authorized

## Related Docs
- Synology NAS Connector setup (DSM 6.x or earlier)
- Synology NAS Connector setup (DSM 7.x or later)
- Connector deployment overview
- Group management