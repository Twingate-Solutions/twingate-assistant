# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for GUI-less environments using a Service Key instead of interactive authentication. Supports deployment as a systemd service, Docker container, or Kubernetes sidecar. Requires `NET_ADMIN` capability and `/dev/net/tun` device access in containerized environments.

## Key Information
- Headless mode uses Service Keys (not user credentials) for authentication
- Relies on `systemd` and `glibc` — distributions including these are most compatible
- Docker image: `twingate/client:latest`
- Service key must be mounted to `/etc/twingate/service_key.json` in containers
- Twingate DNS resolvers: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`

## Prerequisites
- Twingate account with Service management permissions
- Service account and Service Key created in Admin console
- Supported Linux distro (Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+; x64-only: Arch, ThinPro, NixOS, Gentoo)

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

| Parameter | Value/Flag |
|-----------|-----------|
| Headless flag | `--headless /path/to/service_key.json` |
| Container service key path | `/etc/twingate/service_key.json` |
| Required device | `/dev/net/tun` |
| Required capability | `NET_ADMIN` |
| Host network mode | `--network host` or `network_mode: host` |

## Docker Compose Patterns
- **Shared network stack**: Set `network_mode: "service:twingate-client"` on dependent services
- **Kubernetes secret**: `kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json`
- **K8s sidecar**: Requires `NET_ADMIN` capability, `privileged: true`, `runAsUser: 0`

## Gotchas
- AWS Fargate and compute engines that don't support kernel capabilities are **not supported**
- Containerized CI/CD jobs sharing host DNS may fail — must update `/etc/docker/daemon.json` with Twingate DNS resolvers and restart Docker
- `--device /dev/net/tun` and `--cap-add NET_ADMIN` are **required** for Docker; missing either breaks connectivity
- `network_mode` on a service disables its own port mappings — expose ports on the Twingate client service instead

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker image docs](https://www.twingate.com/docs/docker)
- [GitHub Action](https://github.com/twingate/github-action)