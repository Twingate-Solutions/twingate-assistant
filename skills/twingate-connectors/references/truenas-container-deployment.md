# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating tokens from the Twingate Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- TrueNAS SCALE uses Docker containers via its Apps interface
- Use Linux deployment method in Admin Console to generate tokens only (no script needed)
- Connectors do **not** auto-update; must be manually upgraded
- Container inherits host DNS by default unless overridden

## Prerequisites
- Access to Twingate Admin Console
- TrueNAS SCALE web UI access
- Existing Remote Network in Twingate

## Step-by-Step

1. In Admin Console → Network tab → select Remote Network → **Add** Connector
2. Choose Linux method → click **Generate New Tokens** → copy both tokens
3. In TrueNAS SCALE UI → **Apps** → **Launch Docker Image**
4. Set **Image repository**: `twingate/connector`, **Image tag**: `latest`
5. Scroll to **Container Environment Variables** → Add 4 entries (see below)
6. Click **Save** → verify green **Active** status in Apps and Admin Console

## Configuration Values

| Environment Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for this connector |
| `TWINGATE_DNS` | Custom DNS server IP (optional) |
| `TWINGATE_LOG_ANALYTICS` | `v2` for JSON stdout logging (optional) |

## Optional Configuration
- **Custom DNS**: Add `TWINGATE_DNS` env var with DNS server IP
- **Local logging**: Set `TWINGATE_LOG_ANALYTICS=v2` for single-line JSON to stdout
- **Local network visibility**: Set Host Interface in Networking section to use host network driver

## Gotchas
- Distinguish carefully between **Access** and **Refresh** tokens — they are separate variables
- ICMP/ping support requires adding sysctl on the **host**: `net.ipv4.ping_group_range = 0 2147483647` (System Settings → Advanced → Sysctl); may require reboot
- Connectors won't auto-update; use the **Upgrade** option in TrueNAS Apps per connector
- Stagger updates across multiple connectors on the same Remote Network to avoid downtime

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/support-peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Local connection logging guide](https://www.twingate.com/docs/log-analytics)