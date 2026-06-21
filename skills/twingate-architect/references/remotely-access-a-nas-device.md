# Remotely Access a NAS Device

## Summary
Twingate enables secure remote access to NAS devices without port forwarding or dynamic DNS. Traffic is not exposed to the public internet, and the NAS is accessed via its local IP address regardless of remote location.

## Key Information
- Replaces port forwarding (which exposes NAS to internet attacks)
- Eliminates dynamic IP/dynamic DNS issues
- NAS is accessed using its local LAN IP address (e.g., `192.168.x.x` or `10.x.x.x`)
- Access control managed via Twingate group management

## Prerequisites
- Active Twingate account with admin access
- NAS device on local network with a known static local IP
- A device on the same local network capable of running a Twingate Connector (can be the NAS itself if supported)
- Twingate client installed on remote access device

## Step-by-Step

1. **Create Remote Network** — In Twingate admin console, add a new Remote Network (e.g., "Home Network")
2. **Add NAS as Resource** — Specify the NAS local IP address (e.g., `192.168.1.50`)
3. **Add Connector** — Click "Add connector" on the Remote Network details page
4. **Provision Connector** — Click "Provision"; re-authentication required
5. **Install Connector** — Deploy on a local network device (options below)
6. **Verify** — Confirm connector is operational in admin console
7. **Restrict Access (optional)** — Configure via group management
8. **Connect** — Use Twingate client on remote device; access NAS via its local IP

## Connector Installation Options for Synology NAS
- DSM 6.x or earlier: See Synology DSM 6.x connector guide
- DSM 7.x or later: See Synology DSM 7.x connector guide
- General connector deployment: See connector deployment docs

## Configuration Values
| Parameter | Example Value |
|-----------|--------------|
| Remote Network name | "Home Network", "Office Network" |
| NAS IP (Resource address) | `192.168.x.x` or `10.x.x.x` |

## Gotchas
- Connector can be installed on the NAS itself **only if** the NAS supports it — otherwise needs a separate local device
- Re-authentication is required during the Provision step
- NAS must have a stable local IP (configure static DHCP lease or static IP on NAS to prevent local IP changes)

## Related Docs
- Synology DSM 6.x Connector Setup
- Synology DSM 7.x Connector Setup
- Connector Deployment (general)
- Group Management