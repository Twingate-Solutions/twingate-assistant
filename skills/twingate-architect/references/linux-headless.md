# Linux Headless Mode

## Summary
Twingate Linux Client can run in headless mode for server/GUI-less environments using a Service Key instead of interactive authentication. Supports systemd service, Docker container, Kubernetes sidecar, and CI/CD deployment patterns.

## Key Information
- Requires a **Service Key** (JSON file) from Twingate Admin console → Services
- Uses `--headless` flag on `twingate setup` command
- Relies on `systemd` and `glibc`; distributions lacking these may not work
- Docker image: `twingate/client:latest`

## Prerequisites
- Twingate account with permissions to create Services and Service Keys
- Supported Linux distros: Ubuntu 22.04/24.04 LTS, Debian 9+, Fedora 40+, CentOS Stream 9+, Oracle Linux 8+, Arch, NixOS, Gentoo (x64 only)
- Docker deployments require `/dev/net/tun` device and `NET_ADMIN` capability
- AWS Fargate **not supported** (cannot add kernel capabilities)

## Step-by-Step (systemd)

```bash
# Install
curl https://binaries.twingate.com/client/linux/install.sh | sudo bash

# Configure headless mode with service key
sudo twingate setup --headless /path/to/service_key.json

# Start / stop / status
sudo twingate start
twingate status
sudo twingate stop
```

## Configuration Values

| Context | Parameter/Key | Value |
|---|---|---|
| CLI | `--headless` | Path to `service_key.json` |
| Docker volume mount | Container path | `/etc/twingate/service_key.json` |
| Kubernetes secret key | `subPath` | `key.json` |
| Twingate DNS resolvers | IPs | `100.95.0.251–100.95.0.254` |

**Docker run (minimum required flags):**
```bash
docker run -d \
  -v /path/to/service-key/:/etc/twingate/service_key.json \
  --device /dev/net/tun \
  --cap-add NET_ADMIN \
  twingate/client:latest
```

**Kubernetes secret creation:**
```bash
kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json
```

## Gotchas
- Docker containers **must** have `--device /dev/net/tun` and `--cap-add NET_ADMIN`; missing either prevents connectivity
- Containers sharing a Docker network with the client must use `network_mode: "service:twingate-client"` to route through Twingate
- Containerized CI/CD jobs that can't share network namespaces need Docker daemon DNS updated to Twingate resolvers (`100.95.0.251–254`); requires Docker restart
- For host-wide traffic capture in Docker, add `--network host`
- Kubernetes sidecar requires `privileged: true` and `runAsUser: 0`

## Logs
```bash
journalctl -u twingate  # view logs
```

## Related Docs
- [Linux Client (interactive mode)](https://www.twingate.com/docs/linux-client)
- [Services & Service Keys](https://www.twingate.com/docs/services)
- [Twingate Docker image](https://www.twingate.com/docs/linux-headless#docker)
- [GitHub Actions integration](https://github.com/twingate/github-action)