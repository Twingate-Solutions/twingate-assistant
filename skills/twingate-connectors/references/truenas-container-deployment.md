---
source: https://www.twingate.com/docs/truenas-container-deployment
type: docs
fetched: 2026-09-20
source_version: 88d8250a509a4abc80a219cdc03bb3addb2ca32beee354b117485cfe9bfb481a
---

# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating tokens from the Admin Console and configuring environment variables in the TrueNAS app interface.

## Key Information
- Uses `twingate/connector:latest` Docker image
- TrueNAS SCALE supports Linux containers via its Apps interface
- Connectors do **not** auto-update; manual upgrades required
- Connector status auto-refreshes in Admin Console once tokens are configured correctly

## Prerequisites
- Access to Twingate Admin Console
- Access to TrueNAS SCALE web UI
- Remote Network already created in Twingate

## Step-by-Step

1. **Generate tokens**: Admin Console → Network tab → Remote Network → Add Connector → Linux method → Generate New Tokens → copy both Access and Refresh tokens
2. **Launch container**: TrueNAS SCALE → Apps → Launch Docker Image
3. **Configure image**: `twingate/connector` / tag: `latest`
4. **Set environment variables**: Add 4 vars in Container Environment Variables section (see below)
5. **Save** → container pulls image and starts; verify green "Active" status

## Configuration Values

| Environment Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for this connector |
| `TWINGATE_DNS` | Custom DNS server IP (optional) |
| `TWINGATE_LOG_ANALYTICS` | `v3` for detailed JSON logging to stdout (optional) |

## Optional Configurations

**Local Network Visibility** (clients on same LAN as connector):
- Networking section → set Host Interface to host's interface
- Set IPAM Type to DHCP or Static

**ICMP/Ping Support** (sysctl on host):
- System Settings → Advanced → Sysctl → Add
- Variable: `net.ipv4.ping_group_range` / Value: `0 2147483647`
- May require reboot

## Gotchas
- Note which token is Access vs. Refresh — they are distinct and order matters
- Tokens are shown only once; save them before leaving the Admin Console page
- ICMP support requires host-level sysctl change, not just container config
- Updates must be done manually via the TrueNAS "Upgrade" option per application; stagger updates across connectors on the same Remote Network to avoid downtime
- Container inherits DNS from TrueNAS host by default unless `TWINGATE_DNS` is set

## Related Docs
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Local connection logging guide](https://www.twingate.com/docs/log-analytics)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)