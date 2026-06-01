# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for server environments without a GUI, using a Service Key for authentication. It supports deployment as a systemd service, Docker container, or Kubernetes sidecar. Requires `systemd` and `glibc` on the host.

## Key Information
- Headless mode uses a **Service Key** (not user credentials) from a Service account in the Admin console
- Supported architectures: x86/AMD64 and ARM64 (Docker image runs latest stable Debian)
- Docker image: `twingate/client:latest`
- Logs available via `journalctl`
- AWS Fargate is **not supported** (no kernel capability support)

## Prerequisites
- Twingate account with permissions to create Services
- Service Key JSON file downloaded from Admin console
- For Docker: `/dev/net/tun` device and `NET_ADMIN` capability available on host

## Supported Distributions
Ubuntu 22.04/24.04 LTS, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, Arch, ThinPro, NixOS, Gentoo (x64 only for last four)

## Step-by-Step: systemd Installation

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

| Context | Parameter/Value |
|---|---|
| Setup flag | `--headless` |
| Service key mount path (Docker/K8s) | `/etc/twingate/service_key.json` |
| Docker required device | `/dev/net/tun` |
| Docker required capability | `NET_ADMIN` |
| Twingate DNS resolvers | `100.95.0.251–100.95.0.254` |
| Share network in Compose | `network_mode: "service:twingate-client"` |
| Host network mode | `--network host` / `network_mode: host` |

## Kubernetes Setup
```bash
kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json
```
Sidecar requires: `NET_ADMIN` capability, `privileged: true`, `runAsUser: 0`, `/dev/net/tun` volume mount as `CharDevice`.

## CI/CD DNS Fix (Containerized Jobs)
When containers can't share network namespace, update Docker daemon DNS:
```bash
sudo systemctl stop docker
sudo jq '. + {"dns": ["100.95.0.251","100.95.0.252","100.95.0.253","100.95.0.254"]}' \
  /etc/docker/daemon.json > tmp && sudo mv tmp /etc/docker/daemon.json
sudo systemctl start docker
```

## Gotchas
- Docker containers **must** have `--device /dev/net/tun` AND `--cap-add NET_ADMIN` or connection fails
- AWS Fargate is unsupported
- Containers using host's `/etc/resolv.conf` won't resolve Twingate Resources—update Docker DNS config
- For shared networking in Compose, dependent services use `network_mode: "service:twingate-client"` (not a shared bridge network)

## Related Docs
- [Linux Client](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker Image](https://www.twingate.com/docs/docker)
- [GitHub Action](https://www.twingate.com/docs/github-actions)