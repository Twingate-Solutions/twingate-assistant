# Deploy a Connector on a QNAP NAS

## Summary
Install a Twingate Connector on a QNAP NAS using Container Station (Docker). This enables secure remote access to the NAS and other local network devices without VPN or port forwarding. QNAP runs QTS (Linux-based), and the Connector runs as a Docker container.

## Key Information
- Uses the standard `twingate/connector` Docker image via Container Station
- Three environment variables required to authenticate the Connector
- After deployment, add the NAS as a Resource using its local IP address
- Peer-to-peer connections recommended for better performance and Fair Use Policy compliance

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured and running QTS
- **Container Station** installed and configured on the QNAP device
- A Twingate Remote Network created (type: "On Premise" or "Other")

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console (e.g., "Home", location: "On Premise")
2. **Generate tokens**: Click "Deploy Connector" → "Generate Tokens" (re-authentication required); copy the `docker run` command
3. **Open Container Station** on QNAP → click **Create** → search for "twingate"
4. Select `twingate/connector` image → choose `latest` version
5. Set container **Name** (use Connector name), configure CPU & Memory limits
6. Click **Advanced Settings** → go to **Environment** section
7. **Add environment variables** from the copied `docker run` command
8. Configure **Network** settings (set hostname, e.g., use Connector name)
9. Click **Continue** → **OK** to start the container
10. Verify in Admin Console that Connector shows as connected
11. **Add NAS as a Resource** using its local network IP address

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |

## Gotchas
- Tokens are only shown once after re-authentication — copy the full `docker run` command before leaving the page
- Two Connectors are created by default per Remote Network; only one needs to be deployed initially
- Must add NAS as a separate **Resource** in Admin Console after Connector is running — the Connector alone does not expose access
- Resource IP should be the NAS's **local network IP** (not localhost or container IP)

## Related Docs
- [Resources Guide](https://www.twingate.com/docs/resources)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [QNAP Getting Started Guide](https://www.qnap.com) (external)
- Twingate Starter Plan (free tier)