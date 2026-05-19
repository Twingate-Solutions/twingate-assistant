# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploys a Twingate Connector as a Docker container application on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating connector tokens from the Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- Uses `twingate/connector:latest` Docker image
- Connector tokens are generated via Linux deployment method in Admin Console
- Container does not auto-update; manual upgrades required
- Connector status auto-refreshes in Admin Console once environment variables are set correctly

## Prerequisites
- Access to Twingate Admin Console
- Access to TrueNAS SCALE web UI
- Existing Remote Network in Twingate
- Connector Access Token and Refresh Token (generated from Admin Console)

## Step-by-Step

1. In Admin Console → Network tab → select Remote Network → **Add** connector
2. Select Linux method → **Generate New Tokens** → copy both tokens (note which is Access vs Refresh)
3. In TrueNAS SCALE → **Apps** → **Launch Docker Image**
4. Set **Image repository** = `twingate/connector`, **Image tag** = `latest`
5. Add 4 Container Environment Variables (see below)
6. Click **Save** to deploy

## Configuration Values

### Required Environment Variables
| Name | Value |
|------|-------|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for connector |

### Optional Environment Variables
| Name | Value | Purpose |
|------|-------|---------|
| `TWINGATE_DNS` | DNS server IP | Custom DNS instead of host DNS |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enables JSON stdout logging for SIEM |

### Local Network Visibility (same-subnet clients)
- Set **Host Interface** in Networking section to host's interface
- Choose DHCP or Static for IPAM Type

## Gotchas
- **Token identity matters**: Access Token and Refresh Token are distinct — do not swap them
- **No auto-updates**: Use TrueNAS app **Upgrade** option manually; stagger upgrades across multiple connectors on same Remote Network
- **ICMP/ping support**: Requires sysctl parameter on TrueNAS host:
  - `System Settings → Advanced → Sysctl → Add`
  - Variable: `net.ipv4.ping_group_range` | Value: `0 2147483647`
  - May require server reboot

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/support-peer-to-peer-connections)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Local connection logging guide](https://www.twingate.com/docs/connector-logs)