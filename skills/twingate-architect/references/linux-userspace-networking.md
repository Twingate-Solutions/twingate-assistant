# Twingate Linux Userspace Networking (HTTP Proxy Mode)

## Summary
Twingate's Linux client supports a userspace networking mode that runs as an HTTP/HTTPS proxy instead of creating a kernel-level TUN interface. This enables secure access to Twingate resources without root privileges, ideal for containers, CI/CD pipelines, and restricted environments. Applications must explicitly route traffic through the proxy—interception is not automatic.

## Key Information
- Default mode is TUN (root required); HTTP Proxy Mode must be explicitly enabled
- Proxy uses HTTP `CONNECT` semantics; only HTTP/HTTPS traffic supported
- Default example port: `9999`
- Three modes: TUN only (default), HTTP Proxy only (no root), Hybrid TUN+Proxy (root required)

## Prerequisites
- Twingate Linux client installed
- Authentication via one of:
  - Interactive: `twingate setup`
  - Headless: service key at `/etc/twingate/service_key.json`
- Service accounts require Business or Enterprise plan

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

**CLI config helpers:**
```bash
twingate config networking                              # show current config
twingate config networking http-proxy=0.0.0.0:9999 tun=off  # proxy only
```

**Test proxy:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://<twingate-resource>
```

## Container Deployments

**Kubernetes:** Mount service key as volume at `/etc/twingate/service_key.json`; run `twingated --http-proxy 0.0.0.0:9999 --tun off`; expose containerPort `9999`.

**Docker Compose (internal only):** Do not publish port; other containers reference proxy as `http://twingate-client:9999`.

**Docker Compose (host/LAN access):** Publish port `"9999:9999"`; reference as `http://<host-ip>:9999`.

## Gotchas
- Traffic is **not** auto-intercepted—apps must explicitly use the proxy
- Publishing proxy port exposes it to LAN; use firewall rules to restrict access
- Use `twingate-client:9999` (not `127.0.0.1:9999`) for same-network Docker containers
- Check `NO_PROXY` settings aren't bypassing the proxy unintentionally
- Peer-to-peer connections recommended to stay within Fair Use bandwidth policy

## Troubleshooting Checklist
1. Client running and authenticated
2. Service key present at `/etc/twingate/service_key.json` (headless)
3. Application explicitly configured to use proxy
4. Resource address/alias matches requested domain/IP
5. Check Admin Console → Recent Activity for the resource

## Related Docs
- [Twingate Headless & AWS ECS](https://www.twingate.com/docs/)
- Twingate Troubleshooting Guide
- Service Accounts documentation
- Auto Lock / Just-in-Time Access features