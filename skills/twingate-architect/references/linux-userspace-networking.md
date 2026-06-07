# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a non-root HTTP Proxy Mode that routes HTTP/HTTPS traffic through a local proxy instead of a kernel-level TUN interface. Applications must explicitly direct traffic to the proxy; there is no automatic interception. Designed for containers, CI/CD pipelines, and environments where root access is unavailable.

## Key Information
- Three modes: **TUN** (root required, default), **HTTP Proxy** (no root), **TUN + HTTP Proxy** (root required, hybrid)
- Proxy uses standard HTTP `CONNECT` semantics
- Default example proxy port: `9999`
- Traffic is **not** intercepted automatically—apps must explicitly use the proxy
- Service accounts (Business/Enterprise) are the recommended auth method for automation

## Prerequisites
- Authentication via either:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`

## Configuration Values

| Method | Value |
|--------|-------|
| CLI flag | `--http-proxy 0.0.0.0:9999` |
| CLI flag | `--tun off` / `--tun on` |
| Env var | `TWINGATE_HTTP_PROXY=0.0.0.0:9999` |
| Env var | `TWINGATE_TUN=off` |
| Config file | `/etc/twingate/network-config.json` |

## Step-by-Step

**HTTP Proxy Only (no root):**
```bash
twingated --http-proxy 0.0.0.0:9999 --tun off
```

**Hybrid Mode (root required):**
```bash
sudo twingated --http-proxy 0.0.0.0:9999 --tun on
```

**Persistent config file:**
```bash
echo '{"http-proxy": "0.0.0.0:9999", "tun": "off"}' | sudo tee /etc/twingate/network-config.json
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource>
```

## Container Deployment Notes

- **Kubernetes**: Mount service key as volume at `/etc/twingate/service_key.json`; pass `--http-proxy 0.0.0.0:9999 --tun off` as command args
- **Docker Compose (internal only)**: Do NOT publish port; other containers reach proxy via `http://twingate-client:9999`
- **Docker Compose (host/LAN access)**: Publish port `"9999:9999"`; clients use `http://<host-ip>:9999`

## Gotchas
- Publishing the proxy port exposes it to the LAN—apply firewall rules accordingly
- `NO_PROXY` environment variables can silently bypass the proxy in containers
- Internal Docker containers must share the same Docker network if port is not published
- Use `twingate-client:9999` (not `127.0.0.1:9999`) when proxying from sibling containers
- Peer-to-peer connections are not available in HTTP Proxy Mode (affects Fair Use Policy for bandwidth)

## Troubleshooting Checklist
1. Client running and authenticated
2. Service key exists at `/etc/twingate/service_key.json`
3. Application explicitly configured to use proxy
4. Resource address/alias matches requested domain or IP
5. Check Recent Activity in Admin Console

## Related Docs
- Twingate Headless & AWS ECS
- Service Accounts
- Twingate Troubleshooting Guide
- Auto Lock / Just In Time Access