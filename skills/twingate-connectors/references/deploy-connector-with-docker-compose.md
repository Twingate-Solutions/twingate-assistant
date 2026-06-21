# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector using Docker Compose. Requires Access Token, Refresh Token, and tenant name. Supports optional parameters for logging, DNS, restart behavior, and peer-to-peer connections.

## Prerequisites
- Access Token and Refresh Token (generated via Connector deployment flow in Admin Console)
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)
- Docker and Docker Compose installed

## Configuration Values

### Required Environment Variables
| Variable | Description |
|----------|-------------|
| `TWINGATE_NETWORK` | Tenant name (not full URL) |
| `TWINGATE_ACCESS_TOKEN` | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Connector refresh token |

### Optional Environment Variables
| Variable | Description |
|----------|-------------|
| `TWINGATE_LOG_LEVEL` | Log verbosity (e.g., `3` for detailed) |
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` to enable Network Events in logs |
| `TWINGATE_DNS` | Custom DNS server IP (e.g., `8.8.8.8`); overrides Remote Network default |

### Docker Compose Parameters
| Parameter | Value | Purpose |
|-----------|-------|---------|
| `restart` | `always` | Auto-restart on crash |
| `network_mode` | `host` | Enables local peer-to-peer connections |
| `sysctls: net.ipv4.ping_group_range` | `"0 2147483647"` | Enables ICMP/ping to Resources |

## Minimal Config
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

## Recommended Config
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
- `TWINGATE_DNS` is rarely needed; omit unless overriding Remote Network DNS
- `network_mode: host` is required for local peer-to-peer connections; default is `bridge`
- `container_name` should match the Connector name in Admin Console for easy identification
- Peer-to-peer connections affect Fair Use Policy bandwidth — configure to support them

## Related Docs
- How to deploy a Connector (token generation)
- Twingate Connector logs (log level values)
- Support peer-to-peer connections