# Deploy a Connector on a QNAP NAS

## Summary
Install a Twingate Connector on a QNAP NAS using Container Station (Docker). This enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector deploys as a Docker container via Container Station
- Uses the standard `twingate/connector` Docker image (`latest` tag)
- After deployment, add the NAS as a Resource using its local IP address

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured per QNAP's getting started guide
- **Container Station** installed and configured on QNAP

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console → name it (e.g., "Home"), location: "On Premise" or "Other"
2. **Generate tokens**: Click "Deploy Connector" on one of the auto-created Connectors → Generate Tokens → re-authenticate → copy the `docker run` command
3. **Open Container Station** on QNAP → click **Create** → search for "twingate"
4. Select `twingate/connector` image → choose `latest` version
5. Set container **Name** (use Connector name), configure CPU & Memory Limit
6. Click **Advanced Settings** → go to **Environment** section
7. **Add environment variables** (from the copied `docker run` command):

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Generated access token |
| `TWINGATE_REFRESH_TOKEN` | Generated refresh token |

8. Go to **Network** tab → set hostname (can use Connector name)
9. Click **Continue** → **OK** to start the container
10. Verify in Admin Console: Connector shows as connected
11. **Add NAS as a Resource** using its local IP address

## Gotchas
- Tokens require re-authentication to view — keep the Deploy Connector page open during QNAP setup
- Only three env vars needed from the `docker run` command (not the full command)
- Must add the QNAP as a Twingate **Resource** separately after Connector is running
- Consider enabling peer-to-peer connections to avoid Fair Use Policy bandwidth limits

## Related Docs
- [Resources guide](https://www.twingate.com/docs/resources)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Starter plan](https://www.twingate.com/pricing)
- QNAP Getting Started Guide (QNAP documentation)