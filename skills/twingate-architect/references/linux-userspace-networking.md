# Linux Userspace Networking (HTTP Proxy Mode)

## Page Title
Twingate Linux Userspace Networking — HTTP Proxy Mode

## Summary
Twingate's Linux client supports a non-root HTTP Proxy Mode that runs a local HTTP/HTTPS proxy instead of creating a kernel-level TUN interface. Applications must explicitly route traffic through the proxy; traffic is not intercepted automatically. Designed for containers, CI/CD pipelines, and environments without root access.

## Key Information
- Default mode is TUN (root required); HTTP Proxy Mode must be explicitly enabled
- Proxy listens on a configurable address/port (e.g., `0.0.0.0:9999`)
- Uses standard HTTP `CONNECT` semantics
- Three modes: TUN only (default), HTTP Proxy only (no root), Hybrid TUN + HTTP Proxy (root required)
- Business/Enterprise plans required for Service Accounts (headless auth)

## Prerequisites
- Authentication method: either interactive (`twingate setup`) or headless (service key at `/etc/twingate/service_key.json`)
- Root NOT required for HTTP Proxy only mode
- Root required for Hybrid or TUN modes

## Configuration Values

| Method | Config |
|--------|--------|
| CLI flag | `--http-proxy 0.0.0.0:9999 --tun off` |
| Env var | `TWINGATE_HTTP_PROXY=0.0.0.0:9999`, `TWINGATE_TUN=off` |
| Config file | `/etc/twingate/network-config.json` → `{"http-proxy": "0.0.0.0:9999", "tun": "off"}` |

## Step-by-Step

**HTTP Proxy Only (no root):**
```bash
twingated --http-proxy 0.0.0.0:9999 --tun off
```

**Hybrid Mode (root required):**
```bash
sudo twingated --http-proxy 0.0.0.0:9999 --tun on
```

**Interactive config helpers:**
```bash
twingate config networking                          # show current config
twingate config networking http-proxy=0.0.0.0:9999 tun=off
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource>
```

## Container Deployments

**Kubernetes:** Mount service key as volume; pass `--http-proxy 0.0.0.0:9999 --tun off` as command args; expose `containerPort: 9999`.

**Docker Compose (internal only):** Do NOT publish port; other containers reach proxy at `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port `"9999:9999"`; clients use `http://<host-ip>:9999`.

## Gotchas
- Traffic is **not** auto-intercepted — applications must explicitly use the proxy
- Publishing proxy port exposes it to LAN; add firewall rules as needed
- Use `twingate-client:9999` (not `127.0.0.1:9999`) when accessing proxy from sibling containers
- Check `NO_PROXY` env vars aren't accidentally bypassing the proxy
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Troubleshooting Checklist
1. Client running and authenticated?
2. Service key present at `/etc/twingate/service_key.json`?
3. Application explicitly configured to use proxy?
4. Resource address/alias matches requested domain or IP?
5. Containers on same Docker network (if port not published)?
6. Check Admin Console → Recent Activity for the Resource

## Related Docs
- Twingate Headless & AWS ECS
- Service Accounts
- Auto Lock / Just-in-Time Access
- Twingate Troubleshooting Guide
- Support peer-to-peer connections