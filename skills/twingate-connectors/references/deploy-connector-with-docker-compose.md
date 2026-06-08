# Deploy Connector with Docker Compose

## Summary
Deploys a Twingate Connector as a Docker Compose service. Requires pre-generated Access and Refresh tokens from the Admin Console. Supports optional parameters for logging, DNS, restart behavior, and syslog forwarding.

## Prerequisites
- Docker and Docker Compose installed
- Access Token and Refresh Token (generated via Admin Console connector deployment flow)
- Twingate tenant name (e.g., `<name>` from `https://<name>.twingate.com`)

## Configuration Values

| Parameter | Required | Description |
|-----------|----------|-------------|
| `TWINGATE_NETWORK` | Yes | Tenant name |
| `TWINGATE_ACCESS_TOKEN` | Yes | Connector access token |
| `TWINGATE_REFRESH_TOKEN` | Yes | Connector refresh token |
| `TWINGATE_LOG_LEVEL` | No | Log verbosity (e.g., `3`) |
| `TWINGATE_LOG_ANALYTICS` | No | Enable Network Events in logs (`v2`) |
| `TWINGATE_DNS` | No | Custom DNS server IP; defaults to Remote Network DNS |

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
      - TWINGATE_DNS=8.8.8.8
    network_mode: host
    sysctls:
      net.ipv4.ping_group_range: "0 2147483647"
```

## Syslog Forwarding Configuration
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
- `restart: always` ensures the container recovers from crashes automatically
- `network_mode: host` enables local peer-to-peer connections by sharing the host network stack; default is `bridge`
- `net.ipv4.ping_group_range: "0 2147483647"` is required if using `ping` for connectivity testing to Twingate Resources
- `container_name` should match the Connector name in the Admin Console for easier identification

## Gotchas
- `TWINGATE_DNS` is rarely needed; omit unless custom DNS routing is explicitly required
- `network_mode: host` is Linux-only; not supported on Docker Desktop for Mac/Windows
- Peer-to-peer connections require additional setup (separate guide); `host` network mode is one prerequisite

## Related Docs
- How to deploy a Connector (token generation)
- Twingate Connector logs (log level values)
- Support peer-to-peer connections
- Fair Use Policy