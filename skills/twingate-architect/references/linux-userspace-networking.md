# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a userspace networking mode via HTTP/HTTPS proxy, eliminating the need for root privileges. Instead of creating a kernel-level TUN interface, the client runs as a local HTTP/HTTPS proxy. Applications must explicitly route traffic through the proxy.

## Key Information
- Three modes: TUN (default, root required), HTTP Proxy only (no root), Hybrid TUN+HTTP Proxy (root required)
- Default proxy port: `9999`
- Traffic is **not** automatically intercepted — apps must explicitly use the proxy
- Uses standard HTTP `CONNECT` semantics
- Service Accounts require Business/Enterprise plan

## Prerequisites
- Authentication via one of:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`

## Configuration Values

| Method | Config |
|--------|--------|
| CLI flag | `--http-proxy 0.0.0.0:9999` |
| CLI flag | `--tun off` or `--tun on` |
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

**Persistent config:**
```bash
echo '{"http-proxy": "0.0.0.0:9999", "tun": "off"}' | sudo tee /etc/twingate/network-config.json
```

**Interactive CLI:**
```bash
twingate config networking http-proxy=0.0.0.0:9999 tun=off
twingate config networking  # show current config
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource>
```

## Container Deployments

**Kubernetes:** Mount service key at `/etc/twingate/service_key.json`, run `twingated --http-proxy 0.0.0.0:9999 --tun off`, expose port `9999`.

**Docker Compose (internal only):** Do not publish port; other containers access via `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port `"9999:9999"`, access via `http://<host-ip>:9999`.

## Gotchas
- Applications must explicitly configure proxy — no automatic traffic interception
- Publishing proxy port exposes it to LAN — add firewall rules as needed
- `NO_PROXY` environment variables can silently bypass the proxy
- Internal Docker network containers use service name (`twingate-client:9999`), not `127.0.0.1`
- Hybrid mode still requires root despite proxy component not needing it

## Troubleshooting Checklist
1. Client running and authenticated
2. Service key exists at correct path (headless mode)
3. App explicitly using proxy
4. Resource address/alias matches requested domain/IP
5. Check Recent Activity in Admin Console
6. Verify shared Docker network for unpublished proxy

## Related Docs
- Twingate Headless & AWS ECS
- Service Accounts documentation
- Auto Lock / Just-in-Time Access features
- Twingate Troubleshooting Guide