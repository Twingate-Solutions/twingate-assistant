# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating tokens from the Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- TrueNAS SCALE runs Linux containers; use the Linux deployment method in Admin Console to get tokens
- Connectors do **not** auto-update; use the TrueNAS "Upgrade" option manually
- Connector becomes active automatically once environment variables are correctly set

## Prerequisites
- Access to Twingate Admin Console
- Access to TrueNAS SCALE web UI
- Remote Network already created in Twingate

## Step-by-Step

1. In Admin Console → Network tab → select Remote Network → **Add** Connector
2. Choose Linux deployment method → click **Generate New Tokens** → copy both tokens
3. Note your Twingate network name (e.g., `yournetworkname` from `yournetworkname.twingate.com`)
4. In TrueNAS SCALE → **Apps** → **Launch Docker Image**
5. Set `Image repository` = `twingate/connector`, `Image tag` = `latest`
6. Scroll to **Container Environment Variables** → add 4 variables (see below)
7. Click **Save** → verify green **Active** status in TrueNAS and Admin Console

## Configuration Values

| Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network name (without `.twingate.com`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive name for this connector |
| `TWINGATE_DNS` | *(Optional)* Custom DNS server IP |
| `TWINGATE_LOG_ANALYTICS` | *(Optional)* Set to `v2` for JSON stdout logging |

**Docker image:** `twingate/connector:latest`

## Optional Configuration

**Local Network Visibility** (clients on same LAN as connector): Set **Host Interface** in the Networking section to host's network interface.

**ICMP/Ping support:** Add sysctl parameter on TrueNAS host:
- System Settings → Advanced → Sysctl → Add
- Variable: `net.ipv4.ping_group_range` | Value: `0 2147483647`
- Reboot may be required

## Gotchas
- Distinguish carefully between Access token and Refresh token — they serve different functions
- Tokens are only shown once; copy to a text editor before leaving the page
- DNS settings inherit from TrueNAS host by default unless `TWINGATE_DNS` is set
- Connector updates are manual; stagger updates across multiple connectors on the same Remote Network to avoid downtime

## Related Docs
- [Support peer-to-peer connections](https://www.twingate.com/docs/support-peer-to-peer-connections)
- [Local connection logging (analytics)](https://www.twingate.com/docs/connector-log-analytics)
- Twingate Fair Use Policy