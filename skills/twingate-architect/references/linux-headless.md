# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for GUI-less server environments using a Service Key for authentication. It supports systemd-based installation, Docker containers, and Kubernetes sidecar patterns. Requires `NET_ADMIN` capability and `/dev/net/tun` access in containerized deployments.

## Key Information
- Headless mode uses Service Keys (not user credentials) from Twingate Admin console
- Requires `systemd` and `glibc` on Linux hosts
- Docker image: `twingate/client:latest`
- Service key must be mounted at `/etc/twingate/service_key.json` in containers
- AWS Fargate and other compute engines that don't support kernel capabilities are **not supported**

## Prerequisites
- Twingate account with permissions to create Services
- Service Key JSON file from Admin console → Services
- Supported Linux distribution (Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, Arch, NixOS, Gentoo, ThinPro)

## Step-by-Step

### systemd Installation
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup --headless /path/to/service_key.json
sudo twingate start
twingate status
sudo twingate stop
```

### Docker Run
```bash
docker run -d \
  -v /path/to/service-key/:/etc/twingate/service_key.json \
  --device /dev/net/tun \
  --cap-add NET_ADMIN \
  twingate/client:latest
```

### Kubernetes Secret
```bash
kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json
```

## Configuration Values

| Parameter | Value/Description |
|-----------|------------------|
| `--headless` | Flag for `twingate setup` to enable headless mode |
| Service key mount path | `/etc/twingate/service_key.json` |
| Required device | `/dev/net/tun` |
| Required capability | `NET_ADMIN` |
| Twingate DNS resolvers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| Docker Compose host networking | `network_mode: host` |
| Docker Compose service networking | `network_mode: "service:twingate-client"` |

## Gotchas
- **Containers sharing networks**: Use `network_mode: "service:twingate-client"` so dependent containers route through Twingate
- **CI/CD containerized jobs**: If network namespace sharing isn't possible, update `/etc/docker/daemon.json` with Twingate DNS resolvers and restart Docker daemon
- **Kubernetes**: Must set `privileged: true`, `runAsUser: 0`, drop all capabilities then add `NET_ADMIN`, and mount `/dev/net/tun` as `CharDevice`
- **Host network capture**: Add `--network host` or `network_mode: host` to capture all host interface traffic
- Logs available via `journalctl`

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker headless image](https://www.twingate.com/docs/docker)
- [GitHub Actions integration](https://www.twingate.com/docs/github-actions)