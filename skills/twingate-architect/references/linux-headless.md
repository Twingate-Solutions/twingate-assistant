# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for GUI-less server environments using a Service Key for authentication. It supports systemd service, Docker container, Kubernetes sidecar, and CI/CD integration patterns. Requires a Service Account and Service Key from the Twingate Admin console.

## Key Information
- Headless mode uses Service Keys (not user credentials)
- Relies on `systemd` and `glibc`; distributions without these are unlikely compatible
- Docker image available: `twingate/client:latest`
- AWS Fargate not supported (no kernel capability support)
- Twingate DNS resolvers: `100.95.0.251–100.95.0.254`

## Prerequisites
- Twingate account with permissions to create Services
- Service Key JSON file from Admin console → Services
- Supported Linux distribution (Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+; x64-only: Arch, NixOS, Gentoo, ThinPro)

## Step-by-Step: systemd Installation
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup --headless /path/to/service_key.json
sudo twingate start
twingate status
sudo twingate stop
```

## Step-by-Step: Docker
```bash
docker run -d \
  -v /path/to/service-key/:/etc/twingate/service_key.json \
  --device /dev/net/tun \
  --cap-add NET_ADMIN \
  twingate/client:latest
```

## Step-by-Step: Kubernetes Secret
```bash
kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json
```

## Configuration Values

| Parameter | Value/Description |
|-----------|-------------------|
| `--headless` | Flag for `twingate setup` to enable headless mode |
| Service key mount path (Docker/K8s) | `/etc/twingate/service_key.json` |
| Required device | `/dev/net/tun` |
| Required capability | `NET_ADMIN` |
| Docker network sharing | `network_mode: "service:twingate-client"` |
| K8s sidecar image | `twingate/client:latest` |
| Twingate DNS IPs | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |

## Gotchas
- Docker containers **must** have `--device /dev/net/tun` and `--cap-add NET_ADMIN` or connection fails
- Services sharing the Twingate network stack must use `network_mode: "service:twingate-client"` in Docker Compose
- Kubernetes sidecars require `privileged: true` and `runAsUser: 0`
- Containerized CI/CD jobs that can't share network namespaces need Docker daemon DNS reconfigured to use Twingate resolvers
- `--network host` required if Client needs to capture all host interface traffic

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker Headless Image](https://www.twingate.com/docs/docker)
- [GitHub Action](https://github.com/twingate/github-action)