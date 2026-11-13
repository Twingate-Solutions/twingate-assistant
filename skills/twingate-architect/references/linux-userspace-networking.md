---
source: https://www.twingate.com/docs/linux-userspace-networking
type: docs
fetched: 2026-11-13
source_version: 1c515af169c26bc295261f2eb81555f95d9f911ca4579f1457a8236f9f9a4d03
trust: official
---

# Userspace Networking (Linux HTTP Proxy Mode)

## Summary
Twingate's Linux client can run without root by acting as a local HTTP/HTTPS proxy instead of creating a TUN interface. Applications must explicitly send traffic through the proxy, and Twingate applies identity-based access to it. This suits containers, CI/CD, and workstations without sudo.

## Key Information
- **Network modes:**
  - TUN (default): full tunneling, root required.
  - HTTP Proxy: HTTP/HTTPS only, no root, disabled by default.
  - TUN + HTTP Proxy: hybrid, root required, disabled by default.
- The client listens on a local port (example: `9999`) and accepts standard HTTP `CONNECT`.
- Traffic is **not** intercepted automatically; apps must be configured to use the proxy.
- Service accounts (Business and Enterprise plans) are the easiest option for automation.

## Prerequisites
One of:
- **Interactive:** run `twingate setup`.
- **Headless:** place a service key at `/etc/twingate/service_key.json`.

## Step-by-Step
1. Authenticate (interactive setup or service key).
2. Start in proxy-only mode: `twingated --http-proxy 0.0.0.0:9999 --tun off`
3. Point the application at `http://<host>:9999`.
4. Test: `curl -v --proxy http://127.0.0.1:9999 https://<resource-address>`

## Configuration Values
- **CLI flags:** `--http-proxy <addr:port>`, `--tun on|off`
- **Env vars:** `TWINGATE_HTTP_PROXY=0.0.0.0:9999`, `TWINGATE_TUN=off`
- **Config file:** `/etc/twingate/network-config.json`
  ```json
  {"http_proxy": "0.0.0.0:9999", "tun": "off"}
  ```
- **CLI helpers:**
  - `twingate config networking` (show current config)
  - `twingate config networking http-proxy=0.0.0.0:9999 tun=off`
  - `twingate config networking http-proxy=0.0.0.0:9999 tun=on`
  - Omitting `tun` leaves TUN on.

### Containers
- **Kubernetes:** Deployment using image `twingate/client:latest`, command `["/usr/sbin/twingated","--http-proxy","0.0.0.0:9999","--tun","off"]`, containerPort 9999. Mount the service key secret at `/etc/twingate/service_key.json` using `subPath`.
- **Docker Compose:** service `twingate-client` with image `twingate/client:latest` and command `--http-proxy 0.0.0.0:9999 --tun off`. Mount `./service_key.json:/etc/twingate/service_key.json:ro`.
  - For other containers on the same network, do **not** publish the port; they reach the proxy at `http://twingate-client:9999`.
  - For host or LAN access, publish `"9999:9999"` and use `http://<host-ip>:9999`.
- **Uptime Kuma example:** Settings → Proxies → add an HTTP proxy with host `twingate-client` and port `9999`, then assign it to the relevant monitors.

## Gotchas
- Hybrid mode (`--tun on`) requires `sudo`.
- Publishing the proxy port exposes it to the LAN; use firewall rules or interface binding.
- Only apps or monitors explicitly configured with the proxy are tunneled.
- `NO_PROXY` settings can bypass the proxy unintentionally.
- Use the right address: `twingate-client:9999` inside the Docker network, `127.0.0.1:9999` from the host.
- The Resource address or alias must match the requested domain or IP.

## Troubleshooting
- Confirm the client is running and authenticated.
- Check that the service key exists at `/etc/twingate/service_key.json` (headless mode).
- Review Recent Activity for the Resource in the Admin Console.

## Related Docs
- Twingate Headless & AWS ECS
- Service Accounts
- Usage-based Auto-lock and just-in-time access
- Peer-to-peer connections and the Fair Use Policy
- Twingate Troubleshooting Guide