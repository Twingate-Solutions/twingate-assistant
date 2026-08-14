---
source: https://www.twingate.com/docs/how-to-set-up-twingate-on-a-synology-nas-dsm-7
type: docs
fetched: 2026-08-14
source_version: 4784cb8a4fc35a1f9b1bad17600f145cb7b73ab792f48aae6dfd3c3543f2ce78
---

# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploys a Twingate Connector on Synology NAS running DSM 7.0+ using Docker Compose via Container Manager. Enables secure remote access to the NAS and other local network devices without VPN or port forwarding. DSM 7.2+ uses the built-in Docker Compose service through Container Manager.

## Key Information
- Uses Container Manager's Project feature (Docker Compose) in DSM 7.2+
- Connector runs in `host` network mode to access local network devices
- DSM 6.x requires a separate guide (different deployment method)
- Updates are handled through Container Manager's Image update UI—no manual steps needed

## Prerequisites
- Synology NAS running DSM 7.0+
- Twingate Remote Network already created in Admin Console
- Container Manager installed on DSM
- Access to Twingate Admin Console to generate tokens
- Browser access to DSM web interface (default: `https://<NAS-IP>:5001`)

## Step-by-Step

1. In Twingate Admin Console → Network → Remote Network → select Connector → **Deploy Connector** → **Docker** → **Generate Tokens**
2. On local machine, create `compose.yaml` (see below)
3. In DSM File Station, create folder: `docker/twingate-connector/`
4. Open **Container Manager** → **Project** → **Create**
5. Name project `twingate-connector`, set Path to the folder, upload `compose.yaml`
6. Replace placeholder values with tenant name and tokens from Admin Console
7. Click **Next** → **Next** → check **"Start the project once it is created"** → **Done**
8. Verify Connector shows as live in Admin Console
9. Add NAS as a Resource in Admin Console using its local IP address

## Configuration Values

**compose.yaml:**
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
| `network_mode` | `host` (required) |

## Update Process
1. Container Manager → **Image** → click **"Update Available"**
2. Click **Update** → acknowledge warning → **Update**
3. New image downloads and applies automatically; no container restart needed

## Gotchas
- DSM 6.x users must use the separate DSM 6 guide—this guide is DSM 7.0+ only
- `network_mode: host` is required for Connector to reach local network devices
- Tokens are single-use; generate new tokens per Connector instance
- NAS itself must be added as a separate Resource in Admin Console after Connector is live
- Additional options (custom DNS, local connection logging) available via Docker Compose examples

## Related Docs
- [Synology NAS DSM 6 guide](https://www.twingate.com/docs/synology-dsm-6)
- [Docker Compose examples](https://www.twingate.com/docs/docker)
- [Resources guide](https://www.twingate.com/docs/resources)