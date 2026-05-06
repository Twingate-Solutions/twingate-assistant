# Deploy a Connector on a QNAP NAS

## Summary
Install a Twingate Connector on a QNAP NAS using Container Station (Docker). This enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector deploys as a Docker container via Container Station
- Two Connectors are auto-created when you create a new Remote Network
- After deployment, add the NAS as a Resource using its local IP address

## Prerequisites
- Twingate account (Starter plan free)
- QNAP device configured ([QNAP getting started guide](https://www.qnap.com))
- Container Station installed on the QNAP device

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console (name: "Home", location: "On Premise" or "Other")
2. **Generate tokens**: Click "Deploy Connector" → select default Docker option → "Generate Tokens" (re-auth required) → copy the `docker run` command
3. **Open Container Station** on QNAP → click **Create** → search "Twingate"
4. **Select image**: `twingate/connector`, version: `latest`
5. **Basic settings**: Set container Name (use Connector name), configure CPU & Memory Limit
6. **Advanced Settings → Environment**: Add the three required variables (see below)
7. **Advanced Settings → Network**: Set hostname (e.g., use Connector name)
8. Click **Continue** → **OK** to start the container

## Configuration Values (Environment Variables)

| Variable | Source |
|---|---|
| `TWINGATE_NETWORK` | From generated `docker run` command |
| `TWINGATE_ACCESS_TOKEN` | From generated `docker run` command |
| `TWINGATE_REFRESH_TOKEN` | From generated `docker run` command |

## Gotchas
- Must re-authenticate in Admin Console before tokens are displayed
- Only 3 env vars needed from the `docker run` command (copy full command to text editor first)
- Container Station must be installed separately on QNAP before starting
- After Connector is running, the NAS itself still needs to be added as a **Resource** in the Admin Console using its local IP
- Consider enabling peer-to-peer connections to avoid Fair Use Policy bandwidth issues

## Related Docs
- [Resources guide](https://www.twingate.com/docs/resources)
- [Support peer-to-peer connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Starter plan](https://www.twingate.com/pricing)
- [Fair Use Policy](https://www.twingate.com/fair-use-policy)