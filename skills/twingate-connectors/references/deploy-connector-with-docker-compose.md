# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector using Docker Compose with required auth tokens and tenant configuration. Supports optional parameters for reliability, logging, DNS, and peer-to-peer connectivity. Log forwarding to syslog is also supported.

## Key Information
- Docker image: `twingate/connector:latest`
- Three required environment variables; all others optional
- `network_mode: host` enables local peer-to-peer connections
- Syslog forwarding configured via Docker logging driver

## Prerequisites
- Docker and Docker Compose installed
- Access Token and Refresh Token (generated via Connector deployment flow in Admin Console)
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)

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
| `TWINGATE_LOG_ANALYTICS` | Enable network event logs (`v2`) |
| `TWINGATE_DNS` | Custom DNS server IP (e.g., `8.8.8.8`) |

### Optional Compose Fields
| Field | Value | Purpose |
|---|---|---|
| `restart` | `always` | Auto-restart on crash |
| `network_mode` | `host` | Enable local peer-to-peer |
| `sysctls: net.ipv4.ping_group_range` | `"0 2147483647"` | Allow ICMP/ping |

## Minimal Compose Template
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

## Recommended Compose Template
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
- `network_mode: host` conflicts with bridge networking; choose based on whether local peer-to-peer is needed
- `TWINGATE_DNS` overrides Remote Network DNS config — rarely needed; only set if required
- `container_name` should match the Connector name in Admin Console for clarity
- Without `restart: always`, container won't recover from crashes automatically

## Related Docs
- How to deploy a Connector (token generation)
- Support peer-to-peer connections
- Twingate Connector logs (log level values)
- Fair Use Policy (bandwidth)