---
source: https://www.twingate.com/docs/linux-headless
type: docs
fetched: 2026-08-14
source_version: 82a57a72066bc64eb628c0cd03227ee6bb4235a084496d85e32c4e9a0c6f8110
---

# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for GUI-less environments using a Service Key. It supports deployment as a systemd service, Docker container, Kubernetes sidecar, or in CI/CD pipelines.

## Key Information
- Requires a **Service Key** (JSON file) from Twingate Admin console under Services configuration
- Uses `--headless` flag with `twingate setup` command
- Depends on `systemd` and `glibc`
- Docker image: `twingate/client:latest`
- Service key must be mounted to `/etc/twingate/service_key.json` in Docker

## Prerequisites
- Twingate account with permissions to create Services
- Service Key JSON file created in Admin console
- Supported Linux distribution with systemd + glibc

## Supported Distributions
**x86/AMD64 + ARM64:** Ubuntu 22.04/24.04 LTS, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+  
**x86/AMD64 only:** Arch Linux, ThinPro, NixOS, Gentoo  
**Not supported:** AWS Fargate (no kernel capability support)

## Step-by-Step

### systemd Installation
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup --headless /path/to/service_key.json
sudo twingate start
twingate status
sudo twingate stop
```

### Docker
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

| Parameter | Value |
|-----------|-------|
| Service key mount path | `/etc/twingate/service_key.json` |
| Required device | `/dev/net/tun` |
| Required capability | `NET_ADMIN` |
| Twingate DNS resolvers | `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254` |
| Docker image | `twingate/client:latest` |

## Gotchas
- **Docker requires both** `--device /dev/net/tun` AND `--cap-add NET_ADMIN` — missing either breaks connectivity
- **AWS Fargate unsupported** — cannot add kernel capabilities
- **Shared networking in Docker Compose:** Use `network_mode: "service:twingate-client"` on dependent services
- **Host network option:** Use `--network host` or `network_mode: host` to capture all host traffic
- **CI/CD containerized jobs:** When containers can't share network namespace, update Docker's DNS to Twingate resolvers in `/etc/docker/daemon.json` (requires Docker restart)
- **Kubernetes:** Use `privileged: true` and mount `/dev/net/tun` as `CharDevice`; store service key as a K8s Secret

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker image docs](https://www.twingate.com/docs/linux-headless#docker)
- [GitHub Action](https://github.com/twingate/github-action)