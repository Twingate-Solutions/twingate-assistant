# Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a non-root HTTP Proxy Mode that routes HTTP/HTTPS traffic through a local proxy instead of creating a kernel-level TUN interface. Applications must explicitly send traffic through the proxy—interception is not automatic. Designed for containers, CI/CD pipelines, and restricted environments.

## Key Information
- Default mode is TUN (root required); HTTP Proxy Mode must be explicitly enabled
- Proxy runs locally (e.g., `0.0.0.0:9999`) using HTTP CONNECT semantics
- Only HTTP/HTTPS traffic supported (not arbitrary protocols)
- Service Accounts require Business or Enterprise plan

## Network Modes
| Mode | Root Required | Command |
|------|--------------|---------|
| TUN (default) | Yes | `twingated` |
| HTTP Proxy Only | No | `--tun off --http-proxy 0.0.0.0:9999` |
| Hybrid (TUN + Proxy) | Yes | `--tun on --http-proxy 0.0.0.0:9999` |

## Prerequisites
- Twingate Linux client installed
- Auth: interactive (`twingate setup`) OR headless service key at `/etc/twingate/service_key.json`

## Configuration Values

**CLI flags:**
```bash
twingated --http-proxy 0.0.0.0:9999 --tun off   # userspace, no root
sudo twingated --http-proxy 0.0.0.0:9999 --tun on  # hybrid, root required
```

**Environment variables:**
```bash
export TWINGATE_HTTP_PROXY=0.0.0.0:9999
export TWINGATE_TUN=off
```

**Config file** (`/etc/twingate/network-config.json`):
```json
{"http-proxy": "0.0.0.0:9999", "tun": "off"}
```

**CLI helpers:**
```bash
twingate config networking                              # show current config
twingate config networking http-proxy=0.0.0.0:9999 tun=off
```

## Container Deployments

**Kubernetes:** Mount service key as volume at `/etc/twingate/service_key.json`, run `twingated --http-proxy 0.0.0.0:9999 --tun off`, expose `containerPort: 9999`.

**Docker Compose (internal only):** Do NOT publish port—containers reach proxy via `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port `"9999:9999"`, configure clients to use `http://<host-ip>:9999`.

## Gotchas
- Traffic is **not** intercepted automatically—apps must explicitly use the proxy
- Publishing proxy port exposes it to LAN; use firewall rules appropriately
- `127.0.0.1:9999` vs `twingate-client:9999`—use service name when accessing from other containers in same network
- `NO_PROXY` environment variable can silently bypass the proxy
- Peer-to-peer connections recommended to stay within Fair Use Policy bandwidth limits

## Troubleshooting
```bash
# Test proxy from host
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource-address>
```
- Verify client is authenticated and running
- Confirm service key exists if headless
- Check Resource address matches domain/IP in Admin Console → Recent Activity

## Related Docs
- [Twingate Headless & AWS ECS](https://www.twingate.com/docs)
- [Service Accounts](https://www.twingate.com/docs)
- [Auto Lock / Just-in-Time Access](https://www.twingate.com/docs)
- [Twingate Troubleshooting Guide](https://www.twingate.com/docs)