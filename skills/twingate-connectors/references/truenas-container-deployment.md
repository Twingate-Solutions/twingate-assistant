# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating connector tokens from the Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- Uses `twingate/connector:latest` Docker image via TrueNAS SCALE's app launcher
- Connectors do **not** auto-update; manual upgrade required via TrueNAS UI
- Token generation uses Linux deployment method in Admin Console (not Docker-specific)

## Prerequisites
- Access to Twingate Admin Console
- TrueNAS SCALE server with Apps feature available
- Remote Network already created in Twingate

## Step-by-Step

1. In Admin Console → Network tab → select Remote Network → **Add** connector
2. Select Linux deployment method → click **Generate New Tokens**
3. Copy and save both Access token and Refresh token (note which is which)
4. In TrueNAS SCALE UI → **Apps** → **Launch Docker Image**
5. Set Application Name (e.g., `twingate-connector`), Image repository `twingate/connector`, tag `latest`
6. Scroll to **Container Environment Variables** → Add 4 variables (see below)
7. Click **Save** to pull image and start container

## Configuration Values

### Required Environment Variables
| Name | Value |
|------|-------|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive label for this connector |

### Optional Environment Variables
| Name | Value | Purpose |
|------|-------|---------|
| `TWINGATE_DNS` | DNS server IP | Override inherited DNS from host |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable JSON stdout logging for SIEM |

## Additional Configuration

**Local Network Visibility** (clients on same LAN as connector):
- Networking section → set **Host Interface** to host's interface
- Set IPAM Type to DHCP or Static

**ICMP/Ping Support** (sysctl on host):
- System Settings → Advanced → Sysctl → Add
- Variable: `net.ipv4.ping_group_range` | Value: `0 2147483647`
- Enable checkbox → Save → may require reboot

## Gotchas
- Distinguish Access token vs. Refresh token carefully — they are different fields
- Container inherits host DNS by default; set `TWINGATE_DNS` to override
- Connectors must be updated manually; stagger updates across multiple connectors on the same Remote Network to avoid downtime
- ICMP support requires a host-level sysctl change, not a container setting

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Local connection logging guide](https://www.twingate.com/docs/connector-logging)
- Twingate Fair Use Policy