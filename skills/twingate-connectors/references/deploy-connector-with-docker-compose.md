---
source: https://www.twingate.com/docs/deploy-connector-with-docker-compose
type: docs
fetched: 2026-08-14
source_version: 78dd9b863d6e5418094a73cff8996fa5c16f923cba7e43d843650b407bae5121
---

# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector using Docker Compose with required auth tokens and tenant configuration. Supports optional parameters for logging, DNS, restart policies, and syslog forwarding.

## Prerequisites
- Access Token and Refresh Token (generated via Connector deployment flow in Admin Console)
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)
- Docker and Docker Compose installed

## Configuration Values

### Required Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Tenant name |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |

### Optional Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_LOG_LEVEL` | Log verbosity (e.g., `3`) |
| `TWINGATE_LOG_ANALYTICS` | Enable Network Events in logs (`v2`) |
| `TWINGATE_DNS` | Custom DNS server IP (e.g., `8.8.8.8`) |

### Other Optional Settings
- `container_name`: Match to Admin Console Connector name
- `restart: always`: Auto-restart on crash
- `network_mode: host`: Enables local peer-to-peer connections
- `sysctls: net.ipv4.ping_group_range: "0 2147483647"`: Enables ICMP/ping support

## Minimal Compose Config
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

## Recommended Compose Config
```yaml
services:
  twingate_connector:
    container_name: <CONNECTOR NAME>
    restart: always
    image: "twingate/connector:latest"
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
      - TWINGATE_LOG_ANALYTICS=v2
      - TWINGATE_LOG_LEVEL=3
      - TWINGATE_DNS=8.8.8.8
    network_mode: host
    sysctls:
      net.ipv4.ping_group_range: "0 2147483647"
```

## Syslog Forwarding Config
```yaml
    logging:
      driver: syslog
      options:
        syslog-address: "udp://<syslog server IP>:514"
        syslog-format: "rfc5424"
        syslog-facility: daemon
        tag: "<CONNECTOR NAME>"
```

## Gotchas
- `TWINGATE_DNS` is rarely needed; Connector uses Remote Network's DNS by default
- `network_mode: host` required for local peer-to-peer connections (bypasses bridge networking)
- Without `restart: always`, connector won't recover from crashes automatically
- Peer-to-peer connections are needed to comply with the Fair Use Policy for bandwidth

## Related Docs
- How to deploy a Connector (token generation)
- Twingate Connector logs (log level values)
- Support peer-to-peer connections