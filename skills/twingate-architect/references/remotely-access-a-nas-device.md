# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or exposing the device to the public internet. Users access the NAS using its local IP address regardless of location, eliminating dynamic IP/DNS issues.

## Key Information
- Solves two port-forwarding problems: public internet exposure and dynamic IP instability
- NAS is accessed via its existing local IP address (e.g., `192.168.x.x` or `10.x.x.x`)
- Connector can optionally be installed directly on the NAS device (hardware-dependent)
- Access control managed via Twingate group management

## Prerequisites
- Twingate account with admin access
- NAS device with a known local IP address
- A device on the local network capable of running a Twingate Connector (or NAS itself if supported)
- Twingate client installed on the remote device needing access

## Step-by-Step

1. **Create Remote Network** — Add a new Remote Network in Twingate admin (e.g., "Home Network")
2. **Add NAS as Resource** — Specify the NAS local IP address (e.g., `192.168.1.x`)
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision"; re-authentication required
5. **Install Connector** — Deploy on a local network device or directly on the NAS:
   - Synology DSM 6.x or earlier: see Synology DSM 6 connector guide
   - Synology DSM 7.x or later: see Synology DSM 7 connector guide
6. **Verify** — Confirm connector is operational; NAS becomes accessible to authorized users
7. **Restrict Access (optional)** — Configure permissions via group management
8. **Connect** — Use Twingate client signed into an authorized account; access NAS at its local IP

## Configuration Values
- NAS Resource address: local IP format `192.168.x.x` or `10.x.x.x`

## Gotchas
- Re-authentication is required during the connector provisioning step
- Not all NAS devices support running a Connector directly — may need a separate local device
- Access is limited to accounts authorized in Twingate; group management must be configured if restriction is needed

## Related Docs
- Synology NAS Connector setup (DSM 6.x or earlier)
- Synology NAS Connector setup (DSM 7.x or later)
- Connector deployment documentation
- Group management