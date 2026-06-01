# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating connector tokens from the Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- Uses `twingate/connector:latest` Docker image via TrueNAS SCALE's app launcher
- Connectors do **not** auto-update; manual upgrade required via TrueNAS UI
- Use Linux deployment method in Admin Console to generate tokens (even though it's Docker-based)

## Prerequisites
- Access to Twingate Admin Console
- TrueNAS SCALE server with Apps feature available
- Remote Network already created in Twingate

## Step-by-Step

1. **Generate tokens**: Admin Console → Network tab → Remote Network → Add Connector → Linux method → Generate New Tokens → copy both tokens
2. **Launch app**: TrueNAS SCALE → Apps → Launch Docker Image
3. **Configure image**:
   - Application Name: `twingate-connector` (or descriptive name)
   - Image repository: `twingate/connector`
   - Image tag: `latest`
4. **Add environment variables** (click Add 4 times in Container Environment Variables section)
5. **Save** — pulls image and starts container

## Configuration Values

| Environment Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive label for this connector |
| `TWINGATE_DNS` | Custom DNS server IP (optional) |
| `TWINGATE_LOG_ANALYTICS` | `v2` for JSON stdout logging (optional) |

## Optional Configuration

- **Custom DNS**: Add `TWINGATE_DNS` env var with DNS server IP
- **Local logging/SIEM**: Set `TWINGATE_LOG_ANALYTICS=v2` (outputs single-line JSON to stdout)
- **Local network visibility**: Set Host Interface in Networking section to host's interface (DHCP or Static)
- **ICMP/ping support**: Add sysctl on TrueNAS host:
  - System Settings → Advanced → Sysctl → Add
  - Variable: `net.ipv4.ping_group_range` / Value: `0 2147483647`
  - May require server reboot

## Gotchas

- Distinguish between **Access** token and **Refresh** token — they serve different functions
- Tokens are only shown once; copy them before leaving the Admin Console page
- Connector status in Admin Console updates automatically once container is running with correct env vars
- Updates are manual — use the **Upgrade** option in TrueNAS Apps UI; stagger updates across connectors on same Remote Network to avoid downtime

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Local connection logging guide](https://www.twingate.com/docs/connector-logs)