## Linux Userspace Networking (HTTP Proxy Mode)

Runs the Twingate Linux Client without root privileges using an HTTP/HTTPS proxy instead of a TUN interface. Applications must explicitly route traffic through the proxy; traffic is not intercepted automatically. Designed for containers, CI/CD, and privilege-restricted environments.

**Key Information:**
- TUN mode (default) requires root; HTTP Proxy Mode does not
- HTTP Proxy Mode listens on a configurable port (default example: `9999`) for HTTP CONNECT requests
- Applications must explicitly configure the proxy -- traffic is NOT automatically captured
- Auth: interactive (`twingate setup`) or headless (service key at `/etc/twingate/service_key.json`)

**Network Modes:**
- TUN only (default) -- full tunneling, all protocols, root required
- HTTP Proxy only -- HTTP/HTTPS traffic only, no root, explicit proxy config required
- TUN + HTTP Proxy -- hybrid, root required

**Configuration:**
```bash
# HTTP Proxy only (no root)
twingated --http-proxy 0.0.0.0:9999 --tun off

# Via environment variables
export TWINGATE_HTTP_PROXY=0.0.0.0:9999
export TWINGATE_TUN=off
twingated

# Via config file
echo '{"http-proxy": "0.0.0.0:9999", "tun": "off"}' | sudo tee /etc/twingate/network-config.json
```

**Docker Compose (proxy used only by other containers in same project):**
- Do NOT publish the port; reference as `http://twingate-client:9999` from other containers

**Docker Compose (proxy exposed to host/LAN):**
- Publish port: `ports: - "9999:9999"` -- exposes to LAN; apply firewall rules as needed

**Kubernetes:**
```yaml
command: ["/usr/sbin/twingated", "--http-proxy", "0.0.0.0:9999", "--tun", "off"]
ports:
  - containerPort: 9999
```

**Testing:**
```bash
curl -v --proxy http://127.0.0.1:9999 https://ipinfo.io/what-is-my-ip
```

**Gotchas:**
- Traffic is not auto-intercepted -- each application must explicitly configure the proxy
- `NO_PROXY` environment variables can silently bypass the proxy
- Publishing the Docker proxy port exposes it to the LAN -- restrict with firewall rules

**Related Docs:**
- /docs/linux-headless -- TUN mode headless deployment
- /docs/services -- Service Account setup
- /docs/linux -- Linux Client general docs
