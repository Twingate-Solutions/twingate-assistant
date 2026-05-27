# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploy a Twingate Connector on Synology NAS running DSM 7.0+ using Container Manager's Docker Compose service. The Connector enables secure remote access to the NAS and other local network devices without VPN or port forwarding. DSM 6.x users must use a separate guide.

## Key Information
- Uses DSM 7.2+ built-in Container Manager (Docker Compose)
- Connector runs with `network_mode: host` to access local network devices
- Enables remote access to NAS and any other device on the same network
- Updates are handled in-place via Container Manager without manual intervention

## Prerequisites
- Synology NAS running DSM 7.0 or later
- Remote Network created in Twingate Admin Console
- Connector tokens (Access Token + Refresh Token) generated from Admin Console
- Container Manager installed on DSM
- Access to DSM web interface (default: `https://<NAS-IP>:5001`)

## Step-by-Step

1. In Twingate Admin Console → Networks → select Remote Network → Deploy Connector → Docker → Generate Tokens
2. In DSM File Station, create folder: `docker/twingate-connector`
3. On local computer, create `compose.yaml` (see below)
4. Open Container Manager → Project → Create
5. Name project `twingate-connector`, set Path to created folder, upload `compose.yaml`
6. Replace placeholder values with actual tenant name and tokens
7. Click Next → Next → check "Start the project once it is created" → Done
8. Verify Connector appears as live in Twingate Admin Console
9. Add NAS as a Resource using its local IP address

## Configuration Values (`compose.yaml`)

```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
    network_mode: host
```

| Parameter | Value |
|---|---|
| `TWINGATE_NETWORK` | Tenant name from `https://tenant.twingate.com/networks` |
| `TWINGATE_ACCESS_TOKEN` | Generated in Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Generated in Admin Console |
| `network_mode` | Must be `host` |

## Update Process
1. Container Manager → Image → check for "Update Available"
2. Click "Update Available" → Update → confirm
3. New image downloads and applies automatically; no reconfiguration needed

## Gotchas
- DSM 6.x requires a different deployment guide entirely
- Must add NAS as a Resource in Admin Console separately — deploying the Connector alone doesn't grant access
- Tokens are single-use; generate new tokens per Connector instance
- Additional Docker Compose parameters available via Docker Compose examples doc

## Related Docs
- Synology NAS DSM 6 guide (for older DSM versions)
- Docker Compose examples (additional Connector configuration options)
- Twingate Resources guide (adding Resources after Connector deployment)