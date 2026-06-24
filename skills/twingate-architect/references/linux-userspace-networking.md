# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a non-root HTTP Proxy Mode that routes HTTP/HTTPS traffic through a local proxy instead of creating a kernel-level TUN interface. Applications must explicitly configure the proxy—traffic is not intercepted automatically. Designed for containers, CI/CD pipelines, and environments without sudo access.

## Key Information
- Default mode is TUN (root required); HTTP Proxy Mode must be explicitly enabled
- Proxy runs locally (e.g., `0.0.0.0:9999`) using standard HTTP CONNECT semantics
- Only HTTP/HTTPS traffic supported (no arbitrary protocols like in TUN mode)
- Three modes: TUN only (default), HTTP Proxy only (no root), Hybrid TUN + Proxy (root required)

## Prerequisites
- Twingate Linux client installed
- Authentication: either interactive (`twingate setup`) or headless service key at `/etc/twingate/service_key.json`
- Service accounts (Business/Enterprise plans) recommended for automation

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

**Interactive config:**
```bash
twingate config networking http-proxy=0.0.0.0:9999 tun=off
twingate config networking  # view current settings
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource>
```

## Container Deployments

**Kubernetes:** Mount service key as volume at `/etc/twingate/service_key.json`; run `twingated --http-proxy 0.0.0.0:9999 --tun off`; expose containerPort 9999.

**Docker Compose (internal only):** Do NOT publish port; other containers reach proxy via `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port with `"9999:9999"`; clients use `http://<host-ip>:9999`.

## Gotchas
- Traffic is **not** auto-intercepted—applications must explicitly set the proxy
- Publishing proxy port exposes it to LAN; use firewall rules to restrict access
- Internal Docker containers use service name (`twingate-client:9999`), not `127.0.0.1:9999`
- `NO_PROXY` environment variable can silently bypass the proxy
- Peer-to-peer connections should be supported to stay within Fair Use bandwidth policy

## Troubleshooting
1. Verify client is running and authenticated
2. Confirm service key exists at `/etc/twingate/service_key.json`
3. Confirm application is explicitly using proxy settings
4. Verify Resource address matches requested domain/IP in Admin Console
5. Check Recent Activity in Admin Console for the Resource

## Related Docs
- Twingate Headless & AWS ECS
- Service Accounts documentation
- Auto lock / Just-in-time access
- Twingate Troubleshooting Guide