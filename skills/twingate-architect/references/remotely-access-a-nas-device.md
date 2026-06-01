# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. It avoids exposing the NAS to the public internet and allows access via the same local IP address regardless of your ISP's dynamic IP assignment.

## Key Information
- Solves two port-forwarding problems: public internet exposure and dynamic IP address changes
- NAS is accessed via its local IP address (e.g., `192.168.x.x` or `10.x.x.x`)
- Connector can sometimes be installed directly on the NAS device (model-dependent)
- Synology DSM has dedicated setup guides for DSM 6.x and DSM 7.x

## Prerequisites
- Twingate account with admin access
- NAS device on a local network with a known local IP address
- A device on the same local network to host the Connector (or the NAS itself if supported)
- Twingate client installed on the remote device needing access

## Step-by-Step

1. **Create Remote Network** — In Twingate admin console, add a new Remote Network (e.g., "Home Network" or "Office Network")
2. **Add NAS as Resource** — Specify the NAS's local IP address (e.g., `192.168.x.x` or `10.x.x.x`)
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision" next to the new connector; re-authentication required
5. **Install Connector** — Follow in-app instructions to install on a local network device or directly on the NAS
   - Synology DSM 6.x or earlier: see dedicated guide
   - Synology DSM 7.x or later: see dedicated guide
6. **Verify Connectivity** — Once connector is operational, the NAS is accessible to authorized users
7. **Restrict Access (optional)** — Use group management to limit which users can access the NAS
8. **Connect Remotely** — Use Twingate client signed into an authorized account; access NAS at its local IP

## Configuration Values
- NAS IP address format: typically `192.168.x.x` or `10.x.x.x`
- No special ports or DNS configuration required

## Gotchas
- Re-authentication is required during the connector provisioning step
- Not all NAS devices support running a Connector directly — may need a separate host on the same network
- Connector must be operational before remote access works

## Related Docs
- Connector setup on Synology DSM 6.x or earlier
- Connector setup on Synology DSM 7.x or later
- Deploying Connectors (general)
- Group Management (access restrictions)