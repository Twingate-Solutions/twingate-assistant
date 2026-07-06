# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector using Docker Compose with mandatory and optional configuration parameters. Requires pre-generated Access and Refresh tokens from the Admin Console. Supports optional syslog forwarding and peer-to-peer networking.

## Key Information
- Docker image: `twingate/connector:latest`
- Three deployment variants: minimal, recommended with options, syslog forwarding
- `network_mode: host` enables local peer-to-peer connections
- Default network mode is `bridge`

## Prerequisites
- Docker and Docker Compose installed
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)
- Access Token and Refresh Token (generate via Connector deployment flow in Admin Console)

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
| `TWINGATE_LOG_ANALYTICS` | Enable network events in logs; set to `v2` |
| `TWINGATE_DNS` | Custom DNS server IP (e.g., `8.8.8.8`) |

### Syslog Logging Options
| Option | Example Value |
|---|---|
| `driver` | `syslog` |
| `syslog-address` | `udp://<ip>:514` |
| `syslog-format` | `rfc5424` |
| `syslog-facility` | `daemon` |
| `tag` | Connector name |

## Step-by-Step (Recommended Deployment)

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

## Gotchas
- `TWINGATE_DNS` is rarely needed; Connector uses Remote Network's DNS by default
- `sysctls: net.ipv4.ping_group_range: "0 2147483647"` required for ICMP/ping to work against Twingate Resources
- `network_mode: host` required for local peer-to-peer connections; incompatible with some Docker networking features
- Omitting `restart: always` means the connector won't recover automatically from crashes

## Related Docs
- How to deploy a Connector (token generation)
- Twingate Connector logs (log level values)
- Support peer-to-peer connections
- Fair Use Policy