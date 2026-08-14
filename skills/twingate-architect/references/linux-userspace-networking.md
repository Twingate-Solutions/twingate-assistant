---
source: https://www.twingate.com/docs/linux-userspace-networking
type: docs
fetched: 2026-08-14
source_version: 2c0c0ce65dd1cbae2789d2105be90bf21117ed23274b50f43c65fca3b7c134ff
---

# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a userspace networking mode that runs as an HTTP/HTTPS proxy instead of creating a kernel-level TUN interface. This allows secure access to private resources without root privileges, suitable for containers, CI/CD pipelines, and managed workstations. Applications must explicitly configure the proxy — traffic is not intercepted automatically.

## Key Information
- **Three modes**: TUN (default, root required), HTTP Proxy only (no root), Hybrid TUN+Proxy (root required)
- Proxy uses HTTP `CONNECT` semantics on a configurable port (default example: `9999`)
- No automatic traffic interception — applications must explicitly use the proxy
- Kubernetes/Docker deployments use service key authentication at `/etc/twingate/service_key.json`
- Service accounts (Business/Enterprise plans) are the recommended approach for automated workflows

## Prerequisites
- One of:
  - Interactive: run `twingate setup`
  - Headless: place service key at `/etc/twingate/service_key.json`
- Service accounts require Business or Enterprise plan

## Configuration Values

| Method | Key | Value Example |
|--------|-----|---------------|
| CLI flag | `--http-proxy` | `0.0.0.0:9999` |
| CLI flag | `--tun` | `off` / `on` |
| Env var | `TWINGATE_HTTP_PROXY` | `0.0.0.0:9999` |
| Env var | `TWINGATE_TUN` | `off` |
| Config file | `/etc/twingate/network-config.json` | `{"http-proxy": "0.0.0.0:9999", "tun": "off"}` |

## Step-by-Step

**HTTP Proxy Only (no root):**
```bash
twingated --http-proxy 0.0.0.0:9999 --tun off
```

**Hybrid Mode (root required):**
```bash
sudo twingated --http-proxy 0.0.0.0:9999 --tun on
```

**Interactive config:**
```bash
twingate config networking http-proxy=0.0.0.0:9999 tun=off
twingate config networking  # show current config
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource-address>
```

## Container Deployments

**Kubernetes:** Mount `service_key.json` as volume secret; run `twingated --http-proxy 0.0.0.0:9999 --tun off`; expose `containerPort: 9999`.

**Docker Compose (internal only — recommended):** Do not publish port; other containers reach proxy at `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port `"9999:9999"`; clients use `http://<host-ip>:9999`.

## Gotchas
- **Traffic not auto-intercepted** — every application/script must explicitly set proxy settings
- **Publishing proxy port exposes it to LAN** — apply firewall rules or bind to specific interface
- **Container networking**: Use service name (`twingate-client:9999`) when containers share a Docker network, not `127.0.0.1`
- **`NO_PROXY` settings** may silently bypass the proxy in container environments
- **Peer-to-peer connections** should be supported to avoid Fair Use Policy bandwidth issues

## Troubleshooting
1. Confirm client is running and authenticated
2. Verify `/etc/twingate/service_key.json` exists (headless mode)
3. Confirm application is explicitly using the proxy
4. Check Resource address/alias matches requested domain or IP
5. Review Recent Activity in Admin Console
6. Check `NO_PROXY` environment variables aren't bypassing the proxy

## Related Docs
- [Twingate Headless & AWS ECS](https://www.twingate.com/docs/)
- [Service Accounts](https://www.twingate.com/docs/)
- [Auto Lock](https://www.twingate.com/docs/)
- [Just In Time Access