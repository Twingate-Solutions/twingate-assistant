# Deploy a Connector on a QNAP NAS

## Summary
Installs a Twingate Connector as a Docker container on a QNAP NAS via Container Station to enable secure remote access to the NAS and other local network devices. Uses the standard Twingate Connector Docker image with environment variable-based authentication.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector deployed via Container Station (Docker)
- Two Connectors are auto-created when setting up a new Remote Network
- After deployment, the QNAP NAS must be added as a Resource separately in Admin Console
- Peer-to-peer connections recommended to reduce bandwidth and comply with Fair Use Policy

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured and running QTS
- **Container Station** installed and configured on the QNAP device

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console (type: "On Premise" or "Other")
2. Click **Deploy Connector** on one of the auto-created Connectors
3. Select default Docker option → click **Generate Tokens** (re-auth required)
4. Copy the `docker run` command values to a text editor
5. In Container Station on QNAP → **Create** → search `twingate` → select `twingate/connector`
6. Choose `latest` image version
7. Set container **Name** (use Connector name), configure CPU & Memory limits
8. Click **Advanced Settings** → **Environment** section
9. Add the three required environment variables
10. Configure **Network** settings (set hostname, e.g. use Connector name)
11. Click **Continue** → **OK** to start the container
12. Verify connection in Twingate Admin Console
13. Add QNAP NAS as a **Resource** using its local IP address

## Configuration Values

| Environment Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Your Twingate network name |
| `TWINGATE_ACCESS_TOKEN` | Access token from Generate Tokens step |
| `TWINGATE_REFRESH_TOKEN` | Refresh token from Generate Tokens step |

- **Docker image:** `twingate/connector:latest`

## Gotchas
- Tokens require **re-authentication** before they are displayed — have credentials ready
- The QNAP NAS itself is **not automatically a Resource**; must be added manually via Admin Console using its local IP
- CPU/Memory limits depend on physical hardware available — no specific values given in docs

## Related Docs
- [Resources Guide](https://www.twingate.com/docs/resources)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Starter Plan](https://www.twingate.com/pricing)
- QNAP Getting Started Guide (external)