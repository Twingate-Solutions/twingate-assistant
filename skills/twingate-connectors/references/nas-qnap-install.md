---
source: https://www.twingate.com/docs/nas-qnap-install
type: docs
fetched: 2026-08-14
source_version: 212dd961bea66798b4b52473c088dda0362bcd5da16d8556dc795f3d3bc91bed
---

# Deploy Twingate Connector on QNAP NAS

## Summary
Install a Twingate Connector on a QNAP NAS using Container Station (Docker). This enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector runs as a Docker container via Container Station
- Two Connectors are auto-created when you create a Remote Network; only one needs to be deployed
- After deployment, add QNAP as a Resource using its local IP address for remote access
- Peer-to-peer connections recommended to improve performance and comply with Fair Use Policy

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured per [QNAP getting started guide](https://www.qnap.com)
- Container Station installed on QNAP

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console (type: "On Premise" or "Other")
2. **Generate tokens**: Click "Deploy Connector" → select default Docker option → click "Generate Tokens" → copy the `docker run` command
3. **Open Container Station** on QNAP → click "Create" → search "Twingate"
4. **Select image**: Choose `twingate/connector`, version `latest`
5. **Basic config**: Set container Name (use Connector name), configure CPU & Memory limits
6. **Advanced Settings → Environment**: Add three variables from the `docker run` command:
   - `TWINGATE_NETWORK`
   - `TWINGATE_ACCESS_TOKEN`
   - `TWINGATE_REFRESH_TOKEN`
7. **Advanced Settings → Network**: Set hostname (e.g., use Connector name)
8. Click **Continue → OK** to start the container
9. Verify in Admin Console that Connector shows as connected

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Generated access token |
| `TWINGATE_REFRESH_TOKEN` | Generated refresh token |

**Docker Image:** `twingate/connector:latest`

## Gotchas
- Tokens require re-authentication to view after clicking "Generate Tokens"
- Copy the full `docker run` command to a text editor before switching to QNAP — values are needed during container setup
- Container Station must be installed separately on QNAP before starting
- After connector is running, the NAS itself still needs to be added as a Resource in the Admin Console (not automatic)

## Related Docs
- [Resources Guide](https://www.twingate.com/docs/resources) — add QNAP NAS as a Resource
- [Peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer) — recommended for bandwidth optimization
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)
- [Twingate Starter Plan](https://www.twingate.com/pricing)