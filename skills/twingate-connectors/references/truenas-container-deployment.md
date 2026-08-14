---
source: https://www.twingate.com/docs/truenas-container-deployment
type: docs
fetched: 2026-08-14
source_version: d28c2176104bcc1d16ff3ec46143be76feba381141722ca44db1de112170ab1a
---

# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating connector tokens from the Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- TrueNAS SCALE uses Docker containers via its Apps interface
- Use the **Linux deployment method** in Admin Console to generate tokens (not Docker method)
- Connectors do **not** auto-update; manual upgrade required via TrueNAS UI
- Container shows as `Active` (green) once successfully connected

## Prerequisites
- Access to Twingate Admin Console
- TrueNAS SCALE web UI access
- Existing Remote Network in Twingate to attach connector to

## Step-by-Step

1. In Admin Console → Network tab → select Remote Network → **Add** connector
2. Select Linux deployment method → **Generate New Tokens** → copy both tokens
3. Note your Twingate network name (e.g., `yournetworkname`)
4. In TrueNAS SCALE → **Apps** → **Launch Docker Image**
5. Fill in application settings and add 4 environment variables
6. Click **Save** to pull image and launch

## Configuration Values

**Docker Image:**
- Repository: `twingate/connector`
- Tag: `latest`

**Required Environment Variables:**
| Name | Value |
|------|-------|
| `TWINGATE_NETWORK` | Your network name (no `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for this connector |

**Optional Environment Variables:**
| Name | Value | Purpose |
|------|-------|---------|
| `TWINGATE_DNS` | DNS server IP | Custom DNS instead of host-inherited |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Local JSON logging to stdout (SIEM integration) |

## Gotchas
- **Distinguish tokens carefully**: Access token ≠ Refresh token; they must be assigned to correct variables
- **No auto-updates**: Must manually use TrueNAS "Upgrade" option; stagger updates across connectors to avoid downtime
- **ICMP/ping support**: Requires host-level sysctl `net.ipv4.ping_group_range = 0 2147483647` (System Settings → Advanced → Sysctl); may require reboot
- **Same-LAN clients**: Enable host network driver in Networking section and configure `Host Interface` for local network visibility
- **Peer-to-peer**: Configure P2P connections to stay within Fair Use Policy bandwidth limits

## Related Docs
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Local connection logging guide](https://www.twingate.com/docs/log-analytics)
- Twingate Fair Use Policy