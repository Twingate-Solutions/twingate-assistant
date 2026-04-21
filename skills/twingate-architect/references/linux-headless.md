## Linux Headless Mode

Runs the Twingate Linux Client without a GUI, authenticating with a Service Key for automated and server environments. Supports systemd service, Docker container, and Kubernetes sidecar deployment patterns.

**Key Information:**
- Headless mode requires a Service Key from a configured Service Account
- Docker container requires `--device /dev/net/tun` and `--cap-add NET_ADMIN` -- without these, networking fails
- Service Key must be mounted to `/etc/twingate/service_key.json` in the Docker image
- AWS Fargate is NOT supported (cannot add kernel capabilities to containers)
- Logs via `journalctl` (not a file path on disk)

**Supported Distros (x86/AMD64 + ARM64):** Ubuntu 22.04/24.04 LTS, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+

**Setup (systemd):**
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup --headless /path/to/service_key.json
sudo twingate start
```

**Docker Run:**
```bash
docker run -d   -v /path/to/service-key/:/etc/twingate/service_key.json   --device /dev/net/tun   --cap-add NET_ADMIN   twingate/client:latest
```

**Docker Compose (sidecar pattern):**
- Set `network_mode: "service:twingate-client"` on dependent containers to share the Twingate network stack
- Use `network_mode: host` to capture all host-level traffic

**Kubernetes Sidecar:**
- Store Service Key as a K8s Secret: `kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json`
- Sidecar requires `NET_ADMIN` capability, `/dev/net/tun` device mount, and root user (`runAsUser: 0`)

**CI/CD Docker DNS Fix (when network sharing is not possible):**
Add Twingate DNS resolvers (`100.95.0.251`-`100.95.0.254`) to `/etc/docker/daemon.json` and restart Docker.

**Gotchas:**
- GitHub Actions users: use the official Twingate GitHub Action instead of manual systemd setup
- AWS Fargate does not support kernel capabilities -- use HTTP Proxy Mode instead

**Related Docs:**
- /docs/services -- Service Account and Service Key creation
- /docs/linux-userspace-networking -- Non-root HTTP proxy mode
- /docs/linux -- Linux Client general docs
