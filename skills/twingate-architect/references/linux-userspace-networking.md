# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a userspace networking mode via HTTP/HTTPS proxy, enabling secure access to private resources without root privileges. Instead of creating a kernel TUN interface, the client runs as a local HTTP proxy on a configurable port. Applications must explicitly route traffic through the proxy.

## Key Information
- Three modes: TUN (default, root required), HTTP Proxy (no root), TUN + HTTP Proxy (hybrid, root required)
- Proxy uses standard HTTP `CONNECT` semantics
- Traffic is **not** intercepted automatically — apps must explicitly use the proxy
- Default example proxy port: `9999`
- Ideal for CI/CD, Docker, Kubernetes, and rootless workstations

## Prerequisites
- Twingate Linux client installed
- Authentication via one of:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`
- Service accounts (for headless) require Business or Enterprise plan

## Configuration Values

| Method | Config |
|--------|--------|
| CLI flag | `--http-proxy 0.0.0.0:9999 --tun off` |
| Env vars | `TWINGATE_HTTP_PROXY=0.0.0.0:9999`, `TWINGATE_TUN=off` |
| Config file | `/etc/twingate/network-config.json` → `{"http-proxy": "0.0.0.0:9999", "tun": "off"}` |

## Step-by-Step

**HTTP Proxy Only (no root):**
```bash
twingated --http-proxy 0.0.0.0:9999 --tun off
```

**Hybrid mode (root required):**
```bash
sudo twingated --http-proxy 0.0.0.0:9999 --tun on
```

**Interactive config management:**
```bash
twingate config networking                              # view current
twingate config networking http-proxy=0.0.0.0:9999 tun=off  # set proxy-only
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource>
```

## Container Deployments

**Kubernetes:** Mount service key as volume at `/etc/twingate/service_key.json`, pass `--http-proxy 0.0.0.0:9999 --tun off` as container command, expose port `9999`.

**Docker Compose (internal only):** Do not publish port; other containers reach proxy via `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port `9999:9999`; clients use `http://<host-ip>:9999`.

## Gotchas
- Applications must explicitly configure the proxy — no automatic traffic interception
- Publishing the proxy port exposes it to LAN; apply firewall rules as needed
- In Docker Compose, use service name (`twingate-client:9999`) not `127.0.0.1` for inter-container access
- Check `NO_PROXY` settings aren't inadvertently bypassing the proxy
- Peer-to-peer connections are unavailable in this mode; all traffic routes through Twingate relays (bandwidth Fair Use Policy applies)

## Troubleshooting Checklist
1. Client running and authenticated
2. Service key present at `/etc/twingate/service_key.json` (headless)
3. App explicitly using HTTP proxy
4. Resource address/alias matches requested domain or IP
5. Containers on same Docker network (if port not published)
6. Check Admin Console → Recent Activity for the resource

## Related Docs
- [Twingate Headless & AWS ECS](https://www.twingate.com/docs/)
- [Service Accounts](https://www.twingate.com/docs/)
- [Auto Lock](https://www.twingate.com/docs/) / [Just in Time Access](https://www.twingate.com/docs/)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs/)