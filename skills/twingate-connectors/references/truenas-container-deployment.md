# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating connector tokens from the Admin Console and configuring environment variables in the TrueNAS app UI.

## Key Information
- Uses `twingate/connector:latest` Docker image
- Connectors do **not** auto-update; manual upgrade required via TrueNAS app UI
- Connector auto-registers in Admin Console once environment variables are correctly set

## Prerequisites
- Access to Twingate Admin Console
- TrueNAS SCALE web UI access
- Remote Network already created in Twingate

## Step-by-Step

1. **Generate tokens**: Admin Console → Network tab → Remote Network → Add Connector → Linux method → Generate New Tokens → copy both tokens
2. **Launch app**: TrueNAS SCALE → Apps → Launch Docker Image
3. **Configure image**:
   - Application Name: `twingate-connector`
   - Image repository: `twingate/connector`
   - Image tag: `latest`
4. **Set environment variables** (Container Environment Variables section, click Add 4x)
5. **Save** → connector appears Active in both TrueNAS and Admin Console

## Configuration Values

| Env Var | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for connector |
| `TWINGATE_DNS` | Custom DNS server IP (optional) |
| `TWINGATE_LOG_ANALYTICS` | `v2` for detailed JSON logging to stdout (optional) |

## Gotchas
- **Token distinction matters**: Access token and Refresh token are different — do not swap them
- **ICMP/ping support**: Requires host-level sysctl change (`net.ipv4.ping_group_range = 0 2147483647`) via System Settings → Advanced → Sysctl; may require reboot
- **Local network visibility**: If clients run on the same LAN as the connector, configure the Networking section to use host network interface (DHCP or Static)
- **Updates are manual**: Use the Upgrade option in TrueNAS app UI; stagger updates across connectors on same Remote Network to avoid downtime

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/support-peer-to-peer-connections)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Local connection logging guide](https://www.twingate.com/docs/connector-log-analytics)