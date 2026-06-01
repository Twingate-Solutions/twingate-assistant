# Deploy a Connector on a QNAP NAS

## Summary
Install a Twingate Connector on a QNAP NAS device using Container Station (Docker). This enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector runs as a Docker container via Container Station
- Uses standard `twingate/connector` Docker image (latest tag)
- Three environment variables required for authentication
- After deployment, add QNAP as a Resource using its local IP address

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured per [QNAP getting started guide](https://www.qnap.com)
- **Container Station** installed and running on QNAP

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console → name it (e.g., "Home") → select "On Premise" or "Other"
2. **Generate tokens**: Click "Deploy Connector" on one of the auto-created Connectors → select default Docker option → click "Generate Tokens" → copy the `docker run` command
3. **Open Container Station** on QNAP → click "Create" → search for "twingate"
4. **Select image**: Choose `twingate/connector` → select `latest` version
5. **Basic settings**: Set container Name (use Connector name), configure CPU & Memory Limit
6. **Advanced Settings → Environment**: Add the three required environment variables (see below)
7. **Advanced Settings → Network**: Set hostname (Connector name recommended)
8. Click "Continue" → "OK" to start container
9. Verify in Admin Console that Connector shows as connected
10. Add QNAP as a **Resource** using its local network IP address

## Configuration Values

| Environment Variable | Source |
|---|---|
| `TWINGATE_NETWORK` | From generated `docker run` command |
| `TWINGATE_ACCESS_TOKEN` | From generated `docker run` command |
| `TWINGATE_REFRESH_TOKEN` | From generated `docker run` command |

## Gotchas
- Must re-authenticate in Twingate Admin Console before tokens are displayed
- Copy the full `docker run` command to a text editor before switching to QNAP setup
- Network configuration in Container Station may need adjustment based on your specific network setup
- Peer-to-peer connections should be configured to stay within Fair Use Policy bandwidth limits
- After Connector is running, the NAS itself still needs to be added separately as a Twingate Resource

## Related Docs
- [Resources guide](https://www.twingate.com/docs/resources)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/fair-use-policy)
- [Twingate Starter plan](https://www.twingate.com/pricing)