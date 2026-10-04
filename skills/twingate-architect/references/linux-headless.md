---
source: https://www.twingate.com/docs/linux-headless
type: docs
fetched: 2026-10-04
source_version: c7e7ca7fa9e83b17aadb1977cc432e8b53a4a3e8bb175ce112daa306d5695e31
trust: official
---

# Linux Headless Mode

## Summary
The Twingate Linux Client can run in headless mode for server/CI/CD environments without a GUI, authenticated via a Service Key instead of interactive login. It supports systemd, Docker, Kubernetes sidecar, and CI/CD deployment patterns. Requires a Service Account and Service Key from the Twingate Admin console.

## Key Information
- Headless mode uses `--headless` flag with `twingate setup` + a Service Key JSON file
- Docker image: `twingate/client:latest`
- Requires `systemd` and `glibc` on host
- Twingate DNS resolvers: `100.95.0.251–100.95.0.254`

## Prerequisites
- Twingate account with permissions to create Services
- Service Key JSON downloaded from Admin console → Services
- Supported Linux distro (Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, Arch, NixOS, Gentoo — x86/AMD64 and ARM64)
- Docker deployments: kernel must support `NET_ADMIN` capability (AWS Fargate **not** supported)

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

| Parameter | Value/Flag |
|---|---|
| Setup flag | `--headless` |
| Service key mount path (Docker/K8s) | `/etc/twingate/service_key.json` |
| Required device | `/dev/net/tun` |
| Required capability | `NET_ADMIN` |
| Host network mode | `--network host` or `network_mode: host` |
| Docker network sharing | `network_mode: "service:twingate-client"` |
| DNS resolvers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |

## Gotchas
- **AWS Fargate unsupported**: Cannot add kernel capabilities required (`NET_ADMIN`, `/dev/net/tun`)
- **Docker DNS issue in CI/CD**: Containers not sharing the Twingate network namespace use host `/etc/resolv.conf`; must manually add Twingate DNS to `/etc/docker/daemon.json` and restart Docker
- Service key must be mounted at exactly `/etc/twingate/service_key.json` in Docker/K8s
- K8s sidecar requires `privileged: true` and `runAsUser: 0`
- Logs via `journalctl`; use `twingate help setup` for additional CLI options

## Related Docs
- [Linux Client (interactive)](https://www.twingate.com/docs/linux)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker image](https://hub.docker.com/r/twingate/client)
- [GitHub Action](https://github.com/twingate/github-action)