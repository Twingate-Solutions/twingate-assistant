# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a userspace networking mode that runs as a local HTTP/HTTPS proxy instead of creating a kernel-level TUN interface. Traffic is not intercepted automatically—applications must explicitly route through the proxy. Designed for containers, CI/CD pipelines, and environments without root access.

## Key Information
- Default mode is TUN (root required); HTTP Proxy Mode must be explicitly enabled
- Proxy listens on configurable address/port (e.g., `0.0.0.0:9999`)
- Uses standard HTTP `CONNECT` semantics
- Available modes: TUN only (default), HTTP Proxy only (no root), Hybrid TUN+Proxy (root required)

## Prerequisites
- Twingate Linux client installed
- Authentication via either:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`
- Service accounts (Business/Enterprise plans) recommended for automated workflows

## Configuration Values

| Method | Config |
|--------|--------|
| CLI flag | `--http-proxy 0.0.0.0:9999 --tun off` |
| Env vars | `TWINGATE_HTTP_PROXY=0.0.0.0:9999`, `TWINGATE_TUN=off` |
| Config file | `/etc/twingate/network-config.json` → `{"http-proxy": "0.0.0.0:9999", "tun": "off"}` |

## Step-by-Step

**HTTP Proxy only (no root):**
```bash
twingated --http-proxy 0.0.0.0:9999 --tun off
```

**Hybrid mode (root required):**
```bash
sudo twingated --http-proxy 0.0.0.0:9999 --tun on
```

**Manage via CLI:**
```bash
twingate config networking                          # show current config
twingate config networking http-proxy=0.0.0.0:9999 tun=off
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<resource-address>
```

## Container Deployments

**Kubernetes:** Mount service key as volume, run `twingated --http-proxy 0.0.0.0:9999 --tun off`, expose port 9999.

**Docker Compose (internal only):** Do not publish port; other containers reach proxy at `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port with `"9999:9999"`; use `http://<host-ip>:9999`.

## Gotchas
- Traffic is **not** auto-intercepted—apps must explicitly use the proxy
- Publishing proxy port (`9999:9999`) exposes it to LAN; add firewall rules as needed
- Containers must share the same Docker network if port is not published
- `NO_PROXY` settings can inadvertently bypass the proxy
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Troubleshooting Checklist
1. Client running and authenticated?
2. Service key exists at `/etc/twingate/service_key.json`?
3. Application explicitly configured to use proxy?
4. Resource address matches requested domain/IP?
5. Check Admin Console → Recent Activity for the resource

## Related Docs
- Twingate Headless & AWS ECS
- Service Accounts
- Auto Lock / Just-in-Time Access
- Twingate Troubleshooting Guide