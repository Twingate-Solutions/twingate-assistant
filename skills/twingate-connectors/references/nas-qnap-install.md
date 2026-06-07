# Deploy a Connector on a QNAP NAS

## Summary
Installs a Twingate Connector as a Docker container on a QNAP NAS device using Container Station. Enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding.

## Key Information
- QNAP runs QTS (Linux-based OS); Connector is deployed via Docker through Container Station
- Use `twingate/connector` image, select `latest` tag
- Two Connectors are auto-created when you create a new Remote Network; only one needs deployment
- After deployment, add the NAS as a Resource using its local IP address

## Prerequisites
- Twingate account (Starter plan is free)
- QNAP device configured and running QTS
- Container Station installed on QNAP

## Step-by-Step

1. **Create Remote Network** in Twingate Admin Console (e.g., "Home", type: "On Premise" or "Other")
2. **Generate tokens**: Click **Deploy Connector** → leave default Docker option → **Generate Tokens** (re-auth required) → copy the `docker run` command
3. **Open Container Station** on QNAP → **Create** → search `twingate` → select `twingate/connector` → install with `latest` tag
4. **Configure container**:
   - Set **Name** to Connector name
   - Set CPU & Memory limits as appropriate
5. **Advanced Settings → Environment**: Add the three required variables (see below)
6. **Advanced Settings → Network**: Set hostname (e.g., Connector name)
7. Click **Continue** → **OK** to start the container
8. Verify in Admin Console that Connector shows as connected
9. **Add Resources** in Admin Console using the NAS's local IP address

## Configuration Values

| Environment Variable | Source |
|---|---|
| `TWINGATE_NETWORK` | From generated `docker run` command |
| `TWINGATE_ACCESS_TOKEN` | From generated `docker run` command |
| `TWINGATE_REFRESH_TOKEN` | From generated `docker run` command |

## Gotchas
- Must re-authenticate in Twingate Admin Console before tokens are visible
- Peer-to-peer connections should be configured to avoid bandwidth Fair Use Policy issues
- Resource must be explicitly added in Admin Console using the NAS's local network IP — connectivity is not automatic after Connector deployment

## Related Docs
- [Container Station setup (QNAP)](https://www.qnap.com)
- [Twingate Resources guide](https://www.twingate.com/docs/resources)
- [Support peer-to-peer connections](https://www.twingate.com/docs/connector-peer-to-peer)
- [Twingate Starter plan](https://www.twingate.com/pricing)