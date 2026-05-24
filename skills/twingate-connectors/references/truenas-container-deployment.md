# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating connector tokens from the Admin Console and configuring environment variables in the TrueNAS app UI.

## Key Information
- TrueNAS SCALE uses Docker containers via its Apps UI
- Use **Linux deployment method** in Admin Console to generate tokens only (don't follow Linux-specific install steps)
- Connectors do **not** auto-update; manual upgrade required via TrueNAS UI
- Note which token is Access vs Refresh — they are distinct values

## Prerequisites
- Access to Twingate Admin Console
- TrueNAS SCALE web UI access
- Existing Remote Network in Twingate

## Step-by-Step

1. Admin Console → **Network** tab → select Remote Network → **Add** connector
2. Choose Linux method → **Generate New Tokens** → copy both Access and Refresh tokens
3. Note your Twingate network name (e.g., `yournetworkname`)
4. TrueNAS UI → **Apps** → **Launch Docker Image**
5. Set **Image repository**: `twingate/connector`, **Image tag**: `latest`
6. Scroll to **Container Environment Variables** → click **Add** 4 times
7. Fill in all four required env vars (see below)
8. Click **Save** — connector appears as **Active** in Apps and Admin Console

## Configuration Values

**Required Environment Variables:**
| Name | Value |
|------|-------|
| `TWINGATE_NETWORK` | Your network name (without `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for this connector |

**Optional Environment Variables:**
| Name | Value | Purpose |
|------|-------|---------|
| `TWINGATE_DNS` | DNS server IP | Override inherited DNS |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable JSON stdout logging for SIEM |

**For local network visibility:** Set **Host Interface** in Networking section to host's interface; configure IPAM as DHCP or Static.

## Gotchas
- **ICMP/ping support** requires host-level sysctl: `net.ipv4.ping_group_range = 0 2147483647` (System Settings → Advanced → Sysctl); may require reboot
- Connectors won't show as active in Admin Console until container is running with correct env vars
- Stagger updates across connectors on the same Remote Network to avoid downtime
- Updates require manual **Upgrade** action per application in TrueNAS UI

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/support-peer-to-peer-connections)
- [Local connection logging guide](https://www.twingate.com/docs/connector-log-analytics)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)