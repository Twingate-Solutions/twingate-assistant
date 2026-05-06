# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector as a Docker Compose service using environment variables for authentication. Supports optional configuration for logging, analytics, ping handling, and syslog forwarding.

## Prerequisites
- Docker and Docker Compose installed
- Access Token and Refresh Token (generated via Connector deployment flow in Admin Console)
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)

## Configuration Values

### Required Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Tenant name (subdomain only) |
| `TWINGATE_ACCESS_TOKEN` | Generated connector access token |
| `TWINGATE_REFRESH_TOKEN` | Generated connector refresh token |

### Optional Environment Variables
| Variable | Value | Description |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` | Verbose logging for troubleshooting |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enable Network Events in container logs |

### Optional Compose Fields
| Field | Value | Description |
|---|---|---|
| `restart` | `always` | Auto-restart on crash |
| `network_mode` | `host` or `bridge` | `host` enables local peer-to-peer |
| `sysctls: net.ipv4.ping_group_range` | `"0 2147483647"` | Enables ICMP/ping to Resources |

## Minimal Template
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

## Recommended Template
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
    network_mode: host
    sysctls:
      net.ipv4.ping_group_range: "0 2147483647"
```

## Syslog Forwarding Addition
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
- `network_mode: host` is required for local peer-to-peer connections; default `bridge` mode does not support this
- `net.ipv4.ping_group_range` sysctl must be set explicitly if using ping-based connectivity testing to Resources
- `container_name` should match the Connector name in Admin Console for easier identification
- Peer-to-peer connections are recommended to stay within Fair Use Policy bandwidth limits

## Related Docs
- How to deploy a Connector (token generation)
- Twingate Connector logs (log level values)
- Support peer-to-peer connections