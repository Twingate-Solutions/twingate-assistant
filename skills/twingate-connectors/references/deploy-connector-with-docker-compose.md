# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector using Docker Compose with environment variables for authentication. Requires pre-generated tokens from the Admin Console. Supports optional parameters for logging, DNS, networking, and log forwarding.

## Prerequisites
- Access Token and Refresh Token (generated via [deploy a Connector](https://www.twingate.com/docs/deploy-connector) flow)
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)
- Docker Compose installed

## Configuration Values

### Required Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_NETWORK` | Tenant name (not full URL) |
| `TWINGATE_ACCESS_TOKEN` | Generated connector access token |
| `TWINGATE_REFRESH_TOKEN` | Generated connector refresh token |

### Optional Environment Variables
| Variable | Description |
|---|---|
| `TWINGATE_LOG_LEVEL` | Log verbosity (e.g., `3` for detailed) |
| `TWINGATE_LOG_ANALYTICS` | Set to `v2` to enable Network Events in logs |
| `TWINGATE_DNS` | Custom DNS server IP (e.g., `8.8.8.8`); overrides Remote Network DNS |

### Optional Compose Fields
| Field | Value | Purpose |
|---|---|---|
| `network_mode` | `host` | Enables local peer-to-peer connections |
| `sysctls: net.ipv4.ping_group_range` | `"0 2147483647"` | Enables ICMP/ping to Resources |
| `restart` | `always` | Auto-restart on crash |

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
- `TWINGATE_DNS` overrides the Remote Network's DNS config — only use if explicitly needed
- `network_mode: host` required for local peer-to-peer connections; default (`bridge`) does not support this
- `container_name` should match the Connector name in Admin Console for correlation
- Peer-to-peer connections are recommended to stay within Fair Use Policy bandwidth limits

## Related Docs
- [Deploy a Connector](https://www.twingate.com/docs/deploy-connector) (token generation)
- [Twingate Connector Logs](https://www.twingate.com/docs/connector-logs)
- [Support Peer-to-Peer Connections](https://www.twingate.com/docs/peer-to-peer)