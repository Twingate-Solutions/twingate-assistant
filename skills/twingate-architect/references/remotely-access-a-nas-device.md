# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. Traffic stays off the public internet, and the NAS is accessed via its local IP address regardless of location.

## Key Information
- Solves two port-forwarding problems: public internet exposure and dynamic IP issues
- NAS is accessed using its local network IP (e.g., `192.168.x.x` or `10.x.x.x`)
- Connector can potentially be installed directly on the NAS device
- Synology DSM has dedicated setup guides for DSM 6.x and DSM 7.x

## Prerequisites
- Twingate account with admin access
- NAS device with known local IP address
- A device on the local network capable of running a Twingate Connector (or NAS itself if supported)
- Twingate client installed on remote devices needing access

## Step-by-Step

1. **Create Remote Network** — In Twingate admin console, add a new Remote Network (e.g., "Home Network" or "Office Network")
2. **Add NAS as Resource** — Specify the NAS local IP address (e.g., `192.168.x.x` or `10.x.x.x`)
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision"; re-authentication required
5. **Install Connector** — Deploy on a local network device following in-console instructions; options include:
   - The NAS itself (if supported)
   - Synology DSM 6.x or earlier: use dedicated guide
   - Synology DSM 7.x or later: use dedicated guide
6. **Verify Connectivity** — Confirm connector is operational; NAS becomes accessible to authorized users
7. **Restrict Access (optional)** — Use group management to limit which users can reach the NAS
8. **Connect Remotely** — Use Twingate client signed into an authorized account; access NAS at its local IP address

## Configuration Values
| Parameter | Example Value |
|-----------|--------------|
| NAS Resource IP | `192.168.x.x` or `10.x.x.x` |

## Gotchas
- Re-authentication is required during the Provision step
- Not all NAS devices support running a Connector — a separate local device may be needed
- Access control is **not automatic**; must configure group management explicitly if restrictions are needed
- Client device must be signed into an account **authorized** for the NAS resource

## Related Docs
- Synology NAS Connector setup (DSM 6.x or earlier)
- Synology NAS Connector setup (DSM 7.x or later)
- Connector deployment documentation
- Group management