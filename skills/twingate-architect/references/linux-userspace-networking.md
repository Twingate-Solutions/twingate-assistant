# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a non-root HTTP Proxy Mode that routes HTTP/HTTPS traffic through a local proxy instead of creating a kernel-level TUN interface. Applications must explicitly configure proxy usage—traffic is not intercepted automatically. Designed for containers, CI/CD pipelines, and environments without elevated privileges.

## Key Information
- Three modes: **TUN** (root, default), **HTTP Proxy** (no root), **TUN + HTTP Proxy** (root, hybrid)
- Proxy runs locally (e.g., port `9999`) using HTTP `CONNECT` semantics
- Only HTTP/HTTPS traffic supported (not all protocols like TUN mode)
- Service Accounts (Business/Enterprise) are recommended for automated/headless deployments

## Prerequisites
- Authentication via either:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`

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

**View/set via CLI:**
```bash
twingate config networking                          # show current
twingate config networking http-proxy=0.0.0.0:9999 tun=off
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<resource-address>
```

## Container Deployments

**Kubernetes:** Mount service key at `/etc/twingate/service_key.json`, run `twingated --http-proxy 0.0.0.0:9999 --tun off`, expose `containerPort: 9999`.

**Docker Compose (internal only):** Do not publish port; other containers reach proxy at `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port with `"9999:9999"`; use `http://<host-ip>:9999`.

## Gotchas
- Traffic is **not** auto-intercepted—apps must explicitly use the proxy
- Do not publish proxy port unless LAN/host access is needed (security risk)
- `NO_PROXY` environment variables can silently bypass the proxy
- Internal Docker containers must share the same Docker network to reach an unpublished proxy
- Use `twingate-client:9999` (not `127.0.0.1:9999`) from sibling containers

## Troubleshooting Checklist
1. Client running and authenticated?
2. Service key present at `/etc/twingate/service_key.json`?
3. App explicitly configured to use proxy?
4. Resource address matches requested domain/IP?
5. Check Admin Console → Recent Activity for the Resource

## Related Docs
- [Twingate Headless & AWS ECS](https://www.twingate.com/docs/)
- [Service Accounts](https://www.twingate.com/docs/)
- [Auto Lock / Just-in-Time Access](https://www.twingate.com/docs/)
- [Peer-to-Peer Connections](https://www.twingate.com/docs/)