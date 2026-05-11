# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating tokens from the Twingate Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- TrueNAS SCALE runs the Connector as a Docker container via its Apps interface
- Use the **Linux** deployment method in Admin Console to generate tokens (even though it's Docker)
- Connectors do **not** auto-update; manual upgrade required via TrueNAS UI
- Connector becomes active automatically once environment variables are correctly set

## Prerequisites
- Access to Twingate Admin Console
- TrueNAS SCALE web UI access
- Target Remote Network already created in Twingate

## Step-by-Step

1. **Admin Console**: Network tab → Select Remote Network → Add Connector → Choose Linux → Generate New Tokens → Copy both tokens
2. **TrueNAS UI**: Apps → Launch Docker Image
3. Fill in application settings:
   - Application Name: `twingate-connector` (or descriptive name)
   - Image repository: `twingate/connector`
   - Image tag: `latest`
4. Add 4 Container Environment Variables (see below)
5. Click Save → wait for Active status

## Configuration Values

| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for this connector |

**Optional variables:**

| Variable | Value | Purpose |
|---|---|---|
| `TWINGATE_DNS` | Custom DNS IP | Override inherited DNS from host |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable JSON stdout logging for SIEM |

## Optional: Local Network Visibility
If Clients run on the same local network as the Connector, set **Host Interface** in the Networking section to enable host network driver.

## Gotchas
- Distinguish carefully between **Access** and **Refresh** tokens — they are separate fields
- ICMP/ping support requires a host-level `sysctl` setting (not container-level):
  - Path: System Settings → Advanced → Sysctl
  - Variable: `net.ipv4.ping_group_range` | Value: `0 2147483647`
  - May require TrueNAS reboot
- Connectors must be **manually upgraded** via the TrueNAS Upgrade option; stagger updates across multiple connectors to avoid downtime

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Local connection logging guide](https://www.twingate.com/docs/log-analytics)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)