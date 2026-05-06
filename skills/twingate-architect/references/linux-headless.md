# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for server/GUI-less environments using a Service Key for authentication. It supports systemd service, Docker container, Kubernetes sidecar, and CI/CD deployment patterns. Requires `NET_ADMIN` capability and `/dev/net/tun` device access in containerized environments.

## Key Information
- Headless mode uses Service Keys (not user credentials) from Twingate Admin console
- Requires `systemd` and `glibc` on Linux; distributions without these may not work
- Docker image: `twingate/client:latest`
- Service key must be mounted to `/etc/twingate/service_key.json` in containers
- Twingate DNS resolvers: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`

## Prerequisites
- Twingate account with permissions to create Services
- Valid Service Key JSON file from Admin console
- Supported distro: Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, Arch, NixOS, Gentoo (x64 only)

## Step-by-Step (systemd)
```bash
# Install
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
# Configure headless mode
sudo twingate setup --headless /path/to/service_key.json
# Start/stop
sudo twingate start
twingate status
sudo twingate stop
```

## Configuration Values

| Context | Parameter/Flag | Value/Notes |
|---|---|---|
| CLI | `--headless` | Path to service_key.json |
| Docker | `--device` | `/dev/net/tun` (required) |
| Docker | `--cap-add` | `NET_ADMIN` (required) |
| Docker volume | `-v` | `/path/to/key:/etc/twingate/service_key.json` |
| Docker Compose | `network_mode` | `"service:twingate-client"` for shared networking |
| Kubernetes | `securityContext.capabilities.add` | `NET_ADMIN` |
| Kubernetes secret | `kubectl create secret generic` | `twingate-service-key --from-file=key.json=...` |

## Gotchas
- **AWS Fargate not supported** — compute engines that don't support kernel capabilities are incompatible
- **Container DNS failures**: Containers not sharing Twingate's network stack won't resolve private Resources via DNS; must add Twingate DNS resolvers to `/etc/docker/daemon.json` (requires Docker restart)
- Docker containers sharing a network stack use `network_mode: "service:twingate-client"` — port mappings must be defined on the Twingate service, not the dependent container
- Kubernetes sidecar requires `privileged: true` and `runAsUser: 0`
- `--network host` Docker option needed if Client must capture all host network traffic

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker image for headless Client](https://www.twingate.com/docs/docker)
- [GitHub Action](https://www.twingate.com/docs/github-actions)