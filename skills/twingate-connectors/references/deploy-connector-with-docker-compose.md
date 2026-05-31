# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector as a Docker Compose service. Requires Access Token and Refresh Token pre-generated from the Admin Console. Supports optional parameters for logging, DNS, restart behavior, and peer-to-peer connections.

## Prerequisites
- Docker and Docker Compose installed
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)
- Access Token and Refresh Token (generated via Admin Console connector deployment flow)

## Configuration Values

### Required Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Tenant name (not full URL) |
| `TWINGATE_ACCESS_TOKEN` | Generated access token |
| `TWINGATE_REFRESH_TOKEN` | Generated refresh token |

### Optional Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_LOG_LEVEL` | Log verbosity (e.g., `3` for detailed) |
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` to enable Network Events in logs |
| `TWINGATE_DNS` | Custom DNS server IP (e.g., `8.8.8.8`); overrides Remote Network DNS |

### Optional Compose Parameters
| Parameter | Value | Purpose |
|---|---|---|
| `restart` | `always` | Auto-restart on crash |
| `network_mode` | `host` | Enables local peer-to-peer connections |
| `sysctls: net.ipv4.ping_group_range` | `"0 2147483647"` | Enables ICMP/ping to Resources |
| `container_name` | Connector name from Admin Console | Identification |

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
- `TWINGATE_DNS` is rarely needed; default uses Remote Network's DNS config—only override if required
- `network_mode: host` conflicts with Docker's default `bridge` mode; required for local peer-to-peer but changes container networking behavior
- `net.ipv4.ping_group_range` sysctl only needed if using ping to test Resource connectivity
- Tokens must be generated fresh per connector from the Admin Console before deployment

## Related Docs
- [How to Deploy a Connector](https://www.twingate.com/docs/connector) (token generation)
- [Twingate Connector Logs](https://www.twingate.com/docs/connector-logs) (log level values)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)
- [Fair Use Policy](https://www.twingate.com/docs/fair-use-policy)