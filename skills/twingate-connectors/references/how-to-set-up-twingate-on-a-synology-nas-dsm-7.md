# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploys a Twingate Connector on Synology NAS running DSM 7.0+ using Container Manager's Docker Compose service. Enables secure remote access to the NAS and other local network devices without VPN server setup or port forwarding. DSM 6.x requires a separate guide.

## Key Information
- Requires DSM 7.0 or later (DSM 6.x has separate guide)
- Uses Container Manager (built-in Docker Compose) in DSM 7.2+
- Connector runs with `network_mode: host`
- Updates available via Container Manager → Image without manual intervention

## Prerequisites
- Synology NAS running DSM 7.0+
- Remote Network created in Twingate Admin Console
- Connector tokens generated (Access Token + Refresh Token) from Admin Console → Deploy Connector → Docker → Generate Tokens
- Container Manager installed on DSM

## Step-by-Step

1. In Twingate Admin Console, create a Remote Network and generate Connector tokens
2. In DSM File Station, create folder: `docker/twingate-connector`
3. On local machine, create `compose.yaml` (see config below)
4. Open Container Manager → Project → Create
5. Name project `twingate-connector`, set Path to created folder, upload `compose.yaml`
6. Replace placeholder values with actual tenant name and tokens
7. Click Next → Next → check "Start the project once it is created" → Done
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

| Parameter | Description |
|---|---|
| `TWINGATE_NETWORK` | Tenant name from `https://tenant.twingate.com/networks` |
| `TWINGATE_ACCESS_TOKEN` | Token from Admin Console |
| `TWINGATE_REFRESH_TOKEN` | Token from Admin Console |

## Update Process
Container Manager → Image → "Update Available" → Update → confirm warning → automatic download and apply with no downtime.

## Gotchas
- Must be on the same local network as the NAS to access DSM web interface during setup
- After deployment, NAS must be explicitly added as a Resource in Admin Console (not automatic)
- Additional connector options (custom DNS, local connection logging) must be configured before copying the deploy command
- See Docker Compose examples doc for additional environment parameters

## Related Docs
- [Synology NAS DSM 6 guide](https://www.twingate.com/docs/synology-nas-dsm-6)
- [Docker Compose examples](https://www.twingate.com/docs/docker-compose)
- [Resources guide](https://www.twingate.com/docs/resources)