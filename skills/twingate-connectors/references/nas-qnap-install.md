# Deploy a Connector on a QNAP NAS

## Summary
Install a Twingate Connector on a QNAP NAS using Container Station (Docker) to enable secure remote access to the NAS and other local network devices. The process involves creating a Remote Network in Twingate, generating tokens, then deploying the official `twingate/connector` Docker image via QNAP's Container Station.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector runs as a Docker container via Container Station
- Two Connectors are auto-created when you create a new Remote Network
- After deployment, add the NAS as a Resource using its local IP address
- Peer-to-peer connections recommended to improve performance and stay within Fair Use Policy bandwidth limits

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured and running QTS
- **Container Station** installed and configured on the QNAP device

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console (e.g., "Home", location: "On Premise" or "Other")
2. Click **Deploy Connector** on one of the auto-created Connectors
3. Select default Docker option → click **Generate Tokens** (re-authentication required)
4. Copy the `docker run` command — retain the three token values
5. In QNAP Container Station → **Create** → search for "twingate" → select `twingate/connector` image → version: `latest`
6. Set container **Name** (use Connector name), configure CPU & Memory limits
7. Click **Advanced Settings** → **Environment** section → add three variables (see below)
8. Click **Network** tab → set hostname (e.g., Connector name)
9. Click **Continue** → **OK** to start container
10. Verify in Admin Console that Connector shows as connected
11. Add NAS as a **Resource** using its local network IP address

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name/ID |
| `TWINGATE_ACCESS_TOKEN` | Access token from generated deploy command |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from generated deploy command |

- **Docker image:** `twingate/connector:latest`

## Gotchas
- Tokens are only shown once after re-authentication — copy the full `docker run` command before leaving the page
- Container Station must be installed separately on QNAP before starting
- CPU/Memory limits depend on specific QNAP hardware — set appropriately to avoid resource contention
- To access the NAS remotely, it must be explicitly added as a Resource in the Admin Console (not automatic)

## Related Docs
- [Resources Guide](https://www.twingate.com/docs/resources) — adding Resources after Connector deployment
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [QNAP Getting Started Guide](https://www.qnap.com) (external)