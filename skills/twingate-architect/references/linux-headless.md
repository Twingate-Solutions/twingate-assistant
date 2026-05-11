# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for GUI-less environments using a Service Key for authentication. It supports systemd service, Docker container, and Kubernetes sidecar deployment patterns. Requires `NET_ADMIN` capability and `/dev/net/tun` device access for network tunneling.

## Key Information
- Headless mode uses Service Keys (not user credentials) from a Service account in Admin console
- Requires `systemd` and `glibc` on the host
- Docker image: `twingate/client:latest`
- Service key must be mounted at `/etc/twingate/service_key.json` in containers
- Twingate DNS resolvers: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`

## Prerequisites
- Twingate account with permissions to create Services and Service Keys
- Supported Linux distro (Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, Arch, NixOS, Gentoo)
- `systemd` and `glibc` present on host

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

| Parameter | Value/Flag |
|-----------|-----------|
| Setup flag | `--headless` |
| Service key path (container) | `/etc/twingate/service_key.json` |
| Required device | `/dev/net/tun` |
| Required capability | `NET_ADMIN` |
| Docker network sharing | `network_mode: "service:twingate-client"` |
| Host network mode | `--network host` |

## Gotchas
- **AWS Fargate not supported** — cannot add kernel capabilities to containers
- Docker containers sharing a network namespace need `network_mode: "service:twingate-client"` to route through Twingate
- When network sharing isn't possible in CI/CD, Docker's `/etc/docker/daemon.json` must be updated with Twingate DNS resolvers and Docker restarted
- Kubernetes sidecar requires `privileged: true`, `runAsUser: 0`, and both `NET_ADMIN` capability and `/dev/net/tun` volume mount
- `twingate help setup` shows additional CLI options including log level configuration

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services documentation](https://www.twingate.com/docs/services)
- [Docker image for headless client](https://www.twingate.com/docs/docker)
- [GitHub Action](https://github.com/twingate/github-action)