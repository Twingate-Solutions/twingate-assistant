# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. Traffic stays off the public internet, and users access the NAS via its local IP address regardless of physical location.

## Key Information
- Solves two port-forwarding problems: public exposure and dynamic IP tracking
- NAS is accessed using its LAN IP address (e.g., `192.168.x.x` or `10.x.x.x`) even when remote
- Connector can be installed on the NAS itself (device-dependent) or another machine on the same network
- Synology NAS has dedicated connector setup guides for DSM 6.x and DSM 7.x

## Prerequisites
- Twingate account with admin access
- NAS device on a local network with a known local IP address
- A device on the same local network capable of running a Twingate Connector
- Twingate client installed on end-user devices

## Step-by-Step

1. **Create Remote Network** — In Twingate admin console, add a new Remote Network (e.g., "Home Network" or "Office Network")
2. **Add NAS as Resource** — Specify the NAS local IP address (e.g., `192.168.1.x` or `10.0.0.x`)
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision"; re-authentication required
5. **Install Connector** — Follow in-console instructions to deploy on a local network device
   - Synology DSM 6.x or earlier: see dedicated guide
   - Synology DSM 7.x or later: see dedicated guide
   - General deployments: see connector deployment docs
6. **Verify** — Confirm connector is operational in the admin console
7. **Restrict Access (optional)** — Use group management to limit which users can reach the NAS resource
8. **Connect** — End users with Twingate client installed and authorized access connect to NAS at its local IP

## Configuration Values
| Parameter | Example Value |
|---|---|
| NAS IP address format | `192.168.x.x` or `10.x.x.x` |
| Resource type | IP address |

## Gotchas
- Connector must be on a device **on the same local network** as the NAS if not installed directly on the NAS
- Re-authentication is required during connector provisioning step
- NAS must support Docker or the connector runtime if installing directly on the NAS
- Access control defaults to open for authorized network users; explicitly configure groups if restriction is needed

## Related Docs
- Synology DSM 6.x Connector Setup
- Synology DSM 7.x Connector Setup
- Connector Deployment (general)
- Group Management