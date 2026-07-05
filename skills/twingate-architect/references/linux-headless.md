# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for GUI-less server environments using a Service Key for authentication. It supports deployment as a systemd service, Docker container, or Kubernetes sidecar. Requires `systemd` and `glibc` on the host.

## Key Information
- Headless mode uses Service Keys (not user credentials) from the Twingate Admin console
- Docker image: `twingate/client:latest`
- Service key must be mounted to `/etc/twingate/service_key.json` in Docker
- Logs accessible via `journalctl`
- Requires `NET_ADMIN` capability and `/dev/net/tun` device in containerized environments

## Prerequisites
- Twingate account with permission to create Services
- Service Key JSON file created in Admin console
- Supported Linux distro with `systemd` and `glibc`
- For containers: kernel capability support (AWS Fargate **not supported**)

## Supported Distributions
- **x86/AMD64 + ARM64:** Ubuntu 22.04/24.04 LTS, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+
- **x86/AMD64 only:** Arch Linux, ThinPro, NixOS, Gentoo

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

### Kubernetes Secret Setup
```bash
kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json
```

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Setup flag | `--headless` |
| Service key path (container) | `/etc/twingate/service_key.json` |
| Docker capability | `NET_ADMIN` |
| Docker device | `/dev/net/tun` |
| Twingate DNS resolvers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| Docker Compose host network | `network_mode: host` |
| Share container network | `network_mode: "service:twingate-client"` |

## Gotchas
- **AWS Fargate unsupported** — no kernel capability support
- Containers sharing a network must use `network_mode: "service:twingate-client"` to route through Twingate
- When Docker containers can't share network namespace, update `/etc/docker/daemon.json` with Twingate DNS resolvers and restart Docker
- Kubernetes sidecar requires `privileged: true`, `runAsUser: 0`, and `NET_ADMIN` capability with `ALL` dropped
- `--network host` needed if Client must capture all host interface traffic

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker prebuilt image](https://www.twingate.com/docs/docker)
- [GitHub Actions integration](https://www.twingate.com/docs/github-actions)