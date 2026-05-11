# Deploy a Connector on a QNAP NAS

## Summary
Install a Twingate Connector on a QNAP NAS using Container Station (Docker). This enables secure remote access to the NAS and other local network devices without VPN servers or port forwarding.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector deploys as a Docker container via Container Station
- Two Connectors are created by default when you create a Remote Network
- Connector image: `twingate/connector` (use `latest` tag)
- After deployment, add the NAS as a Resource using its local IP address

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured and running QTS
- Container Station installed on the QNAP device

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console — name it (e.g., "Home"), location: "On Premise" or "Other"
2. **Generate tokens** — click "Deploy Connector" on one of the auto-created Connectors → select Docker → click "Generate Tokens" (re-authentication required)
3. **Copy the `docker run` command** to a text editor for reference
4. **Open Container Station** on QNAP → click "Create" → search "Twingate" → select `twingate/connector` image → choose `latest`
5. **Configure container**:
   - Set Name to Connector name
   - Set CPU & Memory Limit as appropriate
6. **Advanced Settings → Environment** — add the three required variables (see below)
7. **Advanced Settings → Network** — set hostname (e.g., use Connector name)
8. Click **Continue → OK** to start the container
9. Verify in Admin Console that Connector shows as connected
10. **Add the NAS as a Resource** using its local network IP address

## Configuration Values (Environment Variables)

| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Access token from generated tokens |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from generated tokens |

## Gotchas
- Tokens are only shown once after re-authentication — copy them immediately
- Resource must be explicitly added in Admin Console after Connector is running; the NAS is not automatically accessible
- Consider enabling peer-to-peer connections to avoid Fair Use Policy bandwidth limits
- CPU/Memory limits depend on your specific QNAP hardware — set appropriately

## Related Docs
- [Resources Guide](https://www.twingate.com/docs) — adding network resources
- [Support peer-to-peer connections](https://www.twingate.com/docs) — P2P setup
- [Twingate Starter Plan](https://www.twingate.com/pricing)
- QNAP Getting Started Guide (external)