# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector using Docker Compose with required auth tokens and tenant configuration. Supports optional parameters for logging, analytics, ping handling, and network mode. Log forwarding to syslog is also supported.

## Prerequisites
- Docker and Docker Compose installed
- Twingate tenant name (`<name>` from `https://<name>.twingate.com`)
- Access Token and Refresh Token (generated via the deploy a Connector flow in Admin Console)

## Configuration Values

| Parameter | Required | Description |
|-----------|----------|-------------|
| `TWINGATE_NETWORK` | Yes | Tenant name |
| `TWINGATE_ACCESS_TOKEN` | Yes | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Yes | Connector refresh token |
| `TWINGATE_LOG_LEVEL` | No | Log verbosity (e.g., `3`) |
| `TWINGATE_LOG_ANALYTICS` | No | Enable Network Events in logs (`v2`) |

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

## Key Information
- `restart: always` ensures container auto-restarts on crash
- `network_mode: host` enables local peer-to-peer connections (vs default `bridge`)
- `net.ipv4.ping_group_range: "0 2147483647"` required for ICMP/ping to work against Twingate Resources
- `TWINGATE_LOG_ANALYTICS=v2` enables Network Events visibility in container logs
- `container_name` should match the Connector name shown in Admin Console

## Gotchas
- `network_mode: host` and explicit port mappings are mutually exclusive in Docker Compose
- Peer-to-peer connections require `host` network mode; `bridge` mode disables local P2P
- Without `restart: always`, connector stays down after container crashes or host reboots
- Tokens must be pre-generated from Admin Console before deployment

## Related Docs
- How to deploy a Connector (token generation)
- Twingate Connector logs (log level values)
- Support peer-to-peer connections
- Fair Use Policy