# Linux Headless Mode

## Summary
Twingate's Linux Client can run in headless mode for server/GUI-less environments using a Service Key for authentication. Supports systemd service, Docker container, Kubernetes sidecar, and CI/CD pipeline deployments. Requires `NET_ADMIN` capability and `/dev/net/tun` access in containerized environments.

## Key Information
- Headless mode uses a Service Key (not user credentials) from the Twingate Admin console
- Relies on `systemd` and `glibc`; distributions without these are less likely to be compatible
- Docker image: `twingate/client:latest`
- Service key must be mounted to `/etc/twingate/service_key.json` in Docker
- Twingate DNS resolvers: `100.95.0.251`, `100.95.0.252`, `100.95.0.253`, `100.95.0.254`

## Prerequisites
- Twingate account with permissions to create Services
- Valid Service Key JSON file
- Supported Linux distro (Ubuntu 22.04/24.04, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, and others for x86/AMD64 and ARM64)
- AWS Fargate is **not** supported (no kernel capability support)

## Step-by-Step: systemd Installation
```bash
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash
sudo twingate setup --headless /path/to/service_key.json
sudo twingate start
twingate status
sudo twingate stop
```

## Configuration Values

| Context | Parameter/Key | Value |
|---|---|---|
| CLI | `--headless` | Path to service_key.json |
| Docker required device | `--device` | `/dev/net/tun` |
| Docker required cap | `--cap-add` | `NET_ADMIN` |
| Docker volume mount path | `-v` target | `/etc/twingate/service_key.json` |
| Docker Compose env var | `SERVICE_KEY_PATH` | Path to service key on host |
| Kubernetes secret key | `subPath` | `key.json` |
| Host network mode | `--network` | `host` |

## Gotchas
- Container deployments **require** both `--device /dev/net/tun` AND `--cap-add NET_ADMIN` — missing either prevents connection
- For Docker Compose multi-container setups, dependent services must use `network_mode: "service:twingate-client"` to route through Twingate
- When containers can't share network namespaces in CI/CD, Docker's DNS must be updated to Twingate resolvers (`daemon.json`) — requires stopping/restarting Docker daemon
- Kubernetes: store service key as a Secret, mount via `subPath: key.json`; pod needs `privileged: true` and `NET_ADMIN`

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Docker prebuilt image](https://www.twingate.com/docs/docker)
- [GitHub Action](https://github.com/twingate/github-action)
- Logs: `journalctl` (see main Linux Client docs)