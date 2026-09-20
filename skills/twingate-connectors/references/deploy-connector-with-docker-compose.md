---
source: https://www.twingate.com/docs/deploy-connector-with-docker-compose
type: docs
fetched: 2026-09-20
source_version: e05b6d70aa25fdc2a38f3b53977b5d44be186bf371b1713bdc5cd70c1ef1c7bf
---

# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector as a Docker Compose service using environment variables for authentication. Supports optional configuration for logging, DNS, restart policies, and syslog forwarding.

## Prerequisites
- Docker and Docker Compose installed
- Access Token and Refresh Token (generated via Twingate Admin Console connector deployment flow)
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)

## Configuration Values

### Required Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Tenant name (subdomain only) |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |

### Optional Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_LOG_LEVEL` | Log verbosity (e.g., `3` for detailed) |
| `TWINGATE_LOG_ANALYTICS` | Enable Network Events in logs; set to `v3` |
| `TWINGATE_DNS` | Custom DNS server IP (default: Remote Network DNS) |

### Optional Compose Keys
| Key | Description |
|---|---|
| `container_name` | Match connector name in Admin Console |
| `restart: always` | Auto-restart on crash |
| `network_mode: host` | Use host network (enables local peer-to-peer) |
| `sysctls: net.ipv4.ping_group_range: "0 2147483647"` | Enables ICMP/ping for connectivity testing |

## Step-by-Step

### Minimal Deployment
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

### Recommended Deployment (with optional params)
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
      - TWINGATE_LOG_ANALYTICS=v3
      - TWINGATE_LOG_LEVEL=3
      - TWINGATE_DNS=8.8.8.8
    network_mode: host
    sysctls:
      net.ipv4.ping_group_range: "0 2147483647"
```

### With Syslog Forwarding
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
- `network_mode: host` conflicts with explicit `ports` mappings in Compose — do not combine them
- `TWINGATE_DNS` is rarely needed; omit unless explicitly routing DNS through a custom server
- Default `network_mode` is `bridge`, which does **not** support local peer-to-peer connections
- Peer-to-peer connections are recommended to stay within the Fair Use Policy for bandwidth

## Related Docs
- [How to Deploy a Connector](https://www.twingate.com/docs/deploy-connector) — token generation
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Twingate Connector Logs](https://www.twingate.com/docs/connector-logs) — log level values