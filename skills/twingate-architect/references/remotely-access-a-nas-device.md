# Remotely Access a NAS Device

## Summary
Configure Twingate to provide secure remote access to a NAS device without port forwarding or dynamic DNS. Access uses the NAS's local IP address, keeping the device off the public internet.

## Key Information
- Replaces port forwarding (which exposes NAS to internet attacks)
- No dynamic DNS required — access via static local IP
- Works with any NAS; Synology DSM has dedicated setup guides
- Access control managed via Twingate group management

## Prerequisites
- Twingate account with admin access
- NAS device with known local IP (e.g., `192.168.x.x` or `10.x.x.x`)
- A device on the local network to install the Connector (can be the NAS itself if supported)
- Twingate client installed on the remote device needing access

## Step-by-Step

1. **Create Remote Network** — In Twingate admin, add a new Remote Network (e.g., "Home Network")
2. **Add NAS as Resource** — Specify the NAS local IP address as a resource on that network
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision"; re-authentication required
5. **Install Connector** — Deploy on a local network device (NAS or other machine); follow in-app instructions
   - Synology DSM 6.x or earlier: see dedicated guide
   - Synology DSM 7.x or later: see dedicated guide
6. **Verify Connector** — Confirm connector is operational in admin console
7. **Restrict Access (optional)** — Use group management to limit which users can reach the NAS
8. **Connect** — From a device with Twingate client signed in, access NAS via its local IP address

## Configuration Values
| Item | Example |
|------|---------|
| NAS local IP format | `192.168.x.x` or `10.x.x.x` |
| Resource definition | NAS IP address |

## Gotchas
- Connector must be installed on a device **on the same local network** as the NAS — not remotely
- NAS must support the Connector runtime if installing directly on it (not all NAS firmware does)
- Re-authentication is required during the Provision step — have credentials ready
- Dynamic IP from ISP is irrelevant to Twingate operation (no exposure to public internet)

## Related Docs
- Synology NAS Connector setup (DSM 6.x or earlier)
- Synology NAS Connector setup (DSM 7.x or later)
- Connector deployment documentation
- Group management