# Deploy Twingate Connector on TrueNAS SCALE

## Summary
Deploy a Twingate Connector as a Docker container on TrueNAS SCALE using the "Launch Docker Image" feature. Requires generating connector tokens from the Admin Console and configuring environment variables in the TrueNAS app setup.

## Key Information
- Uses `twingate/connector:latest` Docker image
- TrueNAS SCALE supports Linux containers; use the Linux deployment method in Admin Console only to obtain tokens
- Connectors do **not** auto-update; manual upgrade required via TrueNAS app UI

## Prerequisites
- Access to Twingate Admin Console
- Access to TrueNAS SCALE web UI
- Existing Remote Network in Twingate

## Step-by-Step

1. In Admin Console → **Network** tab → select Remote Network → **Add** Connector
2. Choose **Linux** deployment method → click **Generate New Tokens** → copy both tokens
3. In TrueNAS SCALE web UI → **Apps** → **Launch Docker Image**
4. Set **Image repository**: `twingate/connector`, **Image tag**: `latest`, **Application Name**: e.g. `twingate-connector`
5. In **Container Environment Variables**, add 4 entries (see below)
6. Click **Save** to pull image and start container
7. Verify green **Active** status in TrueNAS and connected status in Admin Console

## Configuration Values

| Environment Variable | Value |
|---|---|
| `TWINGATE_NETWORK` | Your network name (e.g., `yournetworkname`) |
| `TWINGATE_ACCESS_TOKEN` | Access token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Admin Console |
| `TWINGATE_LABEL_HOSTNAME` | Descriptive label for this connector |
| `TWINGATE_DNS` | *(Optional)* Custom DNS server IP |
| `TWINGATE_LOG_ANALYTICS` | *(Optional)* Set to `v2` for JSON stdout logging |

## Optional Configuration

- **Custom DNS**: Add `TWINGATE_DNS` env var with DNS server IP
- **Local logging (SIEM)**: Set `TWINGATE_LOG_ANALYTICS=v2`
- **Local network visibility**: In **Networking** section, set **Host Interface** to host's network interface with DHCP or Static IPAM
- **ICMP/ping support**: Add sysctl on TrueNAS host:
  - **System Settings → Advanced → Sysctl → Add**
  - Variable: `net.ipv4.ping_group_range`, Value: `0 2147483647`, Enabled: checked
  - May require server reboot

## Gotchas

- Note which token is **Access** vs **Refresh** — they are distinct and order matters
- Access and Refresh tokens are only shown once; save them immediately
- The sysctl ping fix applies at the host level and is inherited by the container
- Stagger updates across multiple connectors on the same Remote Network to avoid downtime
- Updating requires manually selecting **Upgrade** in the TrueNAS app UI

## Related Docs
- [Support peer-to-peer connections](https://www.twingate.com/docs/connectors)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Local connection logging guide](https://www.twingate.com/docs/log-analytics)