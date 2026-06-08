# Deploy Twingate Connector on Synology NAS (DSM 7.x)

## Summary
Deploy a Twingate Connector on Synology NAS running DSM 7.0+ using Docker Compose via the built-in Container Manager. Enables secure remote access to the NAS and other local network devices without VPN or port forwarding.

## Key Information
- Requires DSM 7.0 or later (use separate DSM 6 guide for older versions)
- Uses Container Manager's Docker Compose (Project) feature
- Connector runs with `network_mode: host` for local network access
- After deployment, NAS and other local devices must be added as Resources in Admin Console

## Prerequisites
- Synology NAS running DSM 7.0+
- Twingate Remote Network configured in Admin Console
- Connector created with Access Token and Refresh Token generated
- Connected to same local network as NAS during setup

## Step-by-Step

1. In Twingate Admin Console, create a Remote Network and generate a Connector with Access Token + Refresh Token
2. On your computer, create `compose.yaml` (see config below)
3. In DSM File Station, create folder: `docker/twingate-connector`
4. Open **Container Manager → Project → Create**
5. Name project `twingate-connector`, set Path to folder, upload `compose.yaml`
6. Replace placeholder values (tenant name, tokens) in the project config
7. Click Next → Next → check "Start the project once it is created" → Done
8. Verify Connector appears as live in Admin Console
9. Add NAS IP as a Resource in Admin Console to enable access

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
| `TWINGATE_ACCESS_TOKEN` | Token from Admin Console Connector setup |
| `TWINGATE_REFRESH_TOKEN` | Token from Admin Console Connector setup |

## Update Process
1. Container Manager → Image → check for "Update Available" badge
2. Click "Update available" → Update → confirm
3. New image downloads and applies automatically; no reconfiguration needed

## Gotchas
- DSM 7.2+ required for Docker Compose/Container Manager Project feature; earlier DSM 7.x may differ
- Successful deployment shows exit code 0 in Container Manager
- NAS is **not** automatically a Resource—must be added manually in Admin Console using its local IP
- Additional Connector options (custom DNS, local logging) can be added as extra environment variables per Docker Compose examples docs

## Related Docs
- [Synology NAS DSM 6 Guide](https://www.twingate.com/docs/)
- [Docker Compose Examples](https://www.twingate.com/docs/)
- [Resources Guide](https://www.twingate.com/docs/)