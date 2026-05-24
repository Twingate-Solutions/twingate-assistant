# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector using Docker Compose. Requires Access Token, Refresh Token, and tenant name. Supports optional parameters for logging, DNS, restart behavior, and syslog forwarding.

## Prerequisites
- Docker and Docker Compose installed
- Access Token and Refresh Token (generated via Connector deployment flow in Admin Console)
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
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` to enable Network Events in logs |
| `TWINGATE_DNS` | Custom DNS server IP (e.g., `8.8.8.8`); rarely needed |

### Optional Docker Compose Fields
| Field | Value | Purpose |
|---|---|---|
| `container_name` | Connector name from Admin Console | Identification |
| `restart` | `always` | Auto-restart on crash |
| `network_mode` | `host` or `bridge` (default) | `host` enables local peer-to-peer |
| `sysctls: net.ipv4.ping_group_range` | `"0 2147483647"` | Enables ICMP/ping support |

## Minimal Compose File
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

## Recommended Full Compose File
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
- `TWINGATE_DNS` overrides the Remote Network's DNS config — only set when explicitly needed
- `net.ipv4.ping_group_range` sysctl must be set if using ping to test Resource connectivity
- Tokens must be pre-generated; this guide does not cover token generation (see connector deploy docs)

## Related Docs
- How to Deploy a Connector (token generation)
- Twingate Connector Logs (log level values)
- Supporting Peer-to-Peer Connections
- Fair Use Policy