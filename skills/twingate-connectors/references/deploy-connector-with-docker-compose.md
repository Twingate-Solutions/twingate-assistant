# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector as a Docker Compose service. Requires Access Token and Refresh Token generated from the Admin Console. Supports optional parameters for logging, analytics, restart behavior, and syslog forwarding.

## Prerequisites
- Access Token and Refresh Token (generated via Connector deployment flow in Admin Console)
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)
- Docker and Docker Compose installed

## Configuration Values

### Required Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Tenant name (not full URL) |
| `TWINGATE_ACCESS_TOKEN` | Generated connector access token |
| `TWINGATE_REFRESH_TOKEN` | Generated connector refresh token |

### Optional Environment Variables
| Variable | Value | Purpose |
|---|---|---|
| `TWINGATE_LOG_LEVEL` | `3` (recommended) | Detailed logs for troubleshooting |
| `TWINGATE_LOG_ANALYTICS` | `v2` | Enables Network Events in container logs |

### Optional Compose-Level Settings
| Setting | Value | Purpose |
|---|---|---|
| `restart` | `always` | Auto-restart on crash |
| `network_mode` | `host` or `bridge` (default) | `host` enables local peer-to-peer |
| `sysctls: net.ipv4.ping_group_range` | `"0 2147483647"` | Enables ICMP/ping to Resources |

## Minimal Configuration
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

## Recommended Configuration
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

## Syslog Forwarding
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
- `network_mode: host` is required for **local** peer-to-peer connections; default `bridge` mode does not support this
- `net.ipv4.ping_group_range` sysctl must be explicitly set if using ping for Resource connectivity testing
- Peer-to-peer connections are recommended to avoid Fair Use Policy bandwidth limits
- `container_name` should match the Connector name in Admin Console for easier identification

## Related Docs
- [How to Deploy a Connector](https://www.twingate.com/docs/connector) (token generation)
- [Twingate Connector Logs](https://www.twingate.com/docs/connector-logs) (log level options)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)