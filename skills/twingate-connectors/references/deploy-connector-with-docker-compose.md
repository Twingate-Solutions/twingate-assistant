## Deploy Connector with Docker Compose

Step-by-step guide to deploying a Twingate Connector using Docker Compose, including required and optional configuration parameters.

**Prerequisites:**
- Access Token and Refresh Token (generated from the Admin Console Connector deployment page)
- Twingate tenant name (the `<name>` subdomain from your Admin Console URL)

**Minimal docker-compose.yml:**
```yaml
services:
  twingate-connector:
    image: twingate/connector:latest
    environment:
      - TWINGATE_NETWORK=<TENANT NAME>
      - TWINGATE_ACCESS_TOKEN=<ACCESS TOKEN>
      - TWINGATE_REFRESH_TOKEN=<REFRESH TOKEN>
```

**Recommended Additional Parameters:**
- `container_name`: set to match the Connector name in the Admin Console
- `restart: always`: auto-restart on crash
- `TWINGATE_LOG_LEVEL=3`: detailed logs for troubleshooting
- `TWINGATE_LOG_ANALYTICS=v2`: enables Network Events in container logs
- `network_mode: host`: allows local P2P connections (container uses host network stack)
- `net.ipv4.ping_group_range: "0 2147483647"` sysctl: enables ICMP/ping support for Resource connectivity testing

**Syslog Forwarding (optional):**
```yaml
logging:
  driver: syslog
  options:
    syslog-address: "udp://<syslog-ip>:514"
    syslog-format: "rfc5424"
    syslog-facility: daemon
    tag: "<CONNECTOR NAME>"
```

**Gotchas:**
- Without `network_mode: host`, P2P connections to local resources may not work; use `host` mode when P2P is needed
- Access Token and Refresh Token are single-use for registration; keep them secure and do not reuse across Connector instances

**Related Docs:**
- /docs/connector-deployment -- General Connector deployment options
- /docs/connector-real-time-logs -- Log level reference
- /docs/local-peer-to-peer-best-practices -- P2P configuration
