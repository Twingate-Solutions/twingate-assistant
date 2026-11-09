---
source: https://www.twingate.com/docs/linux-userspace-networking
type: docs
fetched: 2026-11-08
source_version: ee623d2a08ecd15c7c571ac6e7d41a14ad464c4b42d519e4af0457819c2053ae
trust: official
---

# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a non-root HTTP Proxy Mode that routes HTTP/HTTPS traffic through a local proxy instead of a kernel TUN interface. Applications must explicitly configure the proxy; traffic is not intercepted automatically. Designed for containers, CI/CD pipelines, and environments without root access.

## Key Information
- Three modes: **TUN** (default, root required), **HTTP Proxy** (no root), **TUN + HTTP Proxy** (hybrid, root required)
- Proxy listens on a configurable address/port (e.g., `0.0.0.0:9999`)
- Uses standard HTTP `CONNECT` semantics
- Only HTTP/HTTPS traffic supported (not arbitrary protocols)
- Docker image: `twingate/client:latest`

## Prerequisites
- Twingate Linux client installed
- Authentication via either:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`
- Service accounts require Business or Enterprise plan

## Configuration Values

| Method | Key | Value Example |
|--------|-----|---------------|
| CLI flag | `--http-proxy` | `0.0.0.0:9999` |
| CLI flag | `--tun` | `off` / `on` |
| Env var | `TWINGATE_HTTP_PROXY` | `0.0.0.0:9999` |
| Env var | `TWINGATE_TUN` | `off` |
| Config file | `/etc/twingate/network-config.json` | `{"http_proxy": "0.0.0.0:9999", "tun": "off"}` |

## Step-by-Step

**HTTP Proxy Only (no root):**
```bash
twingated --http-proxy 0.0.0.0:9999 --tun off
```

**Hybrid Mode (root required):**
```bash
sudo twingated --http-proxy 0.0.0.0:9999 --tun on
```

**Via config CLI:**
```bash
twingate config networking http-proxy=0.0.0.0:9999 tun=off
twingate config networking  # view current config
```

**Via config file:**
```bash
echo '{"http_proxy": "0.0.0.0:9999", "tun": "off"}' | sudo tee /etc/twingate/network-config.json
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource-hostname>
```

## Container Deployments

**Kubernetes:** Mount service key as volume at `/etc/twingate/service_key.json`; pass `--http-proxy 0.0.0.0:9999 --tun off` as container command; expose `containerPort: 9999`.

**Docker Compose (internal only):** Do **not** publish the port; other containers reference proxy as `http://twingate-client:9999` (using service name).

**Docker Compose (host/LAN access):** Publish `"9999:9999"`; clients use `http://<host-ip>:9999`.

## Gotchas
- Applications **must explicitly** configure the proxy — no automatic traffic interception
- Publishing the proxy port exposes it to the LAN; apply firewall rules accordingly
- `NO_PROXY` environment variables in consuming containers can silently bypass the tunnel
- Internal Docker containers: use service name (`twingate-client:9999`), not `127.0.0.1:9999`
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Troubleshooting Checklist
1. Client running and authenticated?
2. Service key present at `/etc/twingate/service_key.json`?
3. Application explicitly using HTTP proxy?
4. Resource address/alias matches requested domain or IP?
5. Containers on same Docker network (if port not published)?
6. Check Admin Console → Recent Activity for the Resource

## Related Docs
- [Twingate Headless & AWS ECS](https://www.twingate.com/docs/)
-