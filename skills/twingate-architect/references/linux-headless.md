# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for GUI-less server environments using a Service Key for authentication. It supports systemd service, Docker container, and Kubernetes sidecar deployment patterns. Headless mode is triggered by passing `--headless` to the `twingate setup` command.

## Key Information
- Requires a **Service Key** (JSON file) from a Service account in the Twingate Admin console
- Relies on `systemd` and `glibc`; distributions including these are most compatible
- Docker image: `twingate/client:latest`
- AWS Fargate and other compute engines that don't support kernel capabilities are **not supported**

## Prerequisites
- Twingate account with permissions to create Services
- Service Key JSON file downloaded from Admin console
- Supported Linux distribution (Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, and others for x86/AMD64 only)

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
|-----------|-------------------|
| Service key mount path (Docker/K8s) | `/etc/twingate/service_key.json` |
| Required device | `/dev/net/tun` |
| Required capability | `NET_ADMIN` |
| Twingate DNS resolvers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| Docker Compose host network option | `network_mode: host` |
| Share container network | `network_mode: "service:twingate-client"` |

## Gotchas
- Docker containers **must** have `--device /dev/net/tun` and `--cap-add NET_ADMIN` or the client cannot connect
- Services sharing the Twingate Client's network stack must set `network_mode: "service:twingate-client"` in Docker Compose
- Containerized CI/CD jobs that can't share network namespaces need Docker's `/etc/docker/daemon.json` updated with Twingate DNS resolvers (requires Docker restart)
- K8s sidecar requires `privileged: true` and `runAsUser: 0`
- Logs accessible via `journalctl`

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker headless image](https://www.twingate.com/docs/docker)
- [GitHub Action](https://github.com/twingate/github-action)