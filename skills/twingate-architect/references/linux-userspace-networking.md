# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a non-root HTTP Proxy Mode that routes HTTP/HTTPS traffic through a local proxy instead of creating a kernel-level TUN interface. Applications must explicitly configure the proxy—traffic is not intercepted automatically. Designed for containers, CI/CD pipelines, and environments without root access.

## Key Information
- Default mode is TUN (root required); HTTP Proxy Mode must be explicitly enabled
- Proxy uses HTTP `CONNECT` semantics; only HTTP/HTTPS traffic supported
- Default proxy port example: `9999` (configurable)
- Service accounts (Business/Enterprise) recommended for automated/headless deployments

## Network Modes
| Mode | Root Required | Command |
|------|--------------|---------|
| TUN only (default) | Yes | `twingated` |
| HTTP Proxy only | No | `twingated --http-proxy 0.0.0.0:9999 --tun off` |
| Hybrid (TUN + Proxy) | Yes | `sudo twingated --http-proxy 0.0.0.0:9999 --tun on` |

## Prerequisites
- Authentication via one of:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`

## Configuration Values

**CLI Flags:**
- `--http-proxy <addr:port>` — enable proxy and set listen address
- `--tun on|off` — enable/disable TUN interface

**Environment Variables:**
```bash
export TWINGATE_HTTP_PROXY=0.0.0.0:9999
export TWINGATE_TUN=off
```

**Config File** (`/etc/twingate/network-config.json`):
```json
{"http-proxy": "0.0.0.0:9999", "tun": "off"}
```

**CLI Helpers:**
```bash
twingate config networking                              # show current config
twingate config networking http-proxy=0.0.0.0:9999 tun=off
```

## Container Deployments

**Kubernetes:** Mount service key as volume, pass `--http-proxy` and `--tun off` as container command args, expose port 9999.

**Docker Compose (internal only):** Do NOT publish port; containers reference proxy as `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port with `ports: - "9999:9999"`; clients use `http://<host-ip>:9999`.

## Testing
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource-address>
```

## Gotchas
- Traffic is **not** automatically intercepted—each application must be explicitly configured to use the proxy
- Publishing the proxy port exposes it to LAN; use firewall rules to restrict access
- `NO_PROXY` environment variables can bypass the proxy unintentionally in container environments
- Peer-to-peer connections are recommended for bandwidth Fair Use Policy compliance
- HTTP Proxy Mode supports HTTP/HTTPS only—not arbitrary TCP/UDP protocols

## Troubleshooting Checklist
1. Client running and authenticated
2. `/etc/twingate/service_key.json` present (headless mode)
3. Application explicitly configured to use proxy
4. Resource address matches requested domain/IP
5. Containers on same Docker network (if port not published)
6. Check Admin Console → Recent Activity for the Resource

## Related Docs
- [Twingate Headless & AWS ECS](https://www.twingate.com/docs/)
- Service Accounts documentation
- Auto Lock / Just-in-Time Access features
- Twingate Troubleshooting Guide