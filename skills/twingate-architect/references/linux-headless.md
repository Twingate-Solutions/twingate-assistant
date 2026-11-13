---
source: https://www.twingate.com/docs/linux-headless
type: docs
fetched: 2026-11-13
source_version: 37ae3f2ebd3b15f80e508de559959319adf3574ced0285c2a52ee98b28d76fdf
trust: official
---

# Linux Headless Mode

## Summary
The Twingate Linux Client can run headless (no GUI) as a background systemd service, authenticated with a Service Key. It can also run in Docker, as a Kubernetes sidecar, or in CI/CD jobs. This is the mode to use for servers and automated workloads.

## Key Information
- Headless mode is enabled via `twingate setup --headless <path-to-service_key.json>`, or `--headless=-` to read the key from stdin.
- Service Key comes from a Service configured in the Twingate Admin Console.
- Install steps are the same as for the interactive Linux Client.
- Supported distros (x86/AMD64 and ARM64): Ubuntu 22.04/24.04/26.04, Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+.
- Supported distros (x64/AMD64 only): Arch, HP ThinPro, NixOS, Gentoo.
- Client requires `systemd` and `glibc`. Derived distros (e.g., RHEL 10) generally work but are untested.
- Logs are available via `journalctl`.
- Docker image: `twingate/client:latest` (Debian-based).
- GitHub Action is available and installs the client as a systemd service on the runner.

## Prerequisites
- Twingate account with permission to create Services and Service Keys.
- A Service Account and Service Key (JSON file).
- Docker/Kubernetes: Service Key available on the host or stored as a Secret.

## Step-by-Step

**systemd install**
1. Install the client using the standard installer from `binaries.twingate.com` (see the Linux Client docs for the exact command).
2. `sudo twingate setup --headless /path/to/service_key.json`
3. `sudo twingate start`
4. `twingate status`
5. `sudo twingate stop` to stop.

**Docker**
```
docker run -d \
  -v /path/to/service_key.json:/etc/twingate/service_key.json \
  --device /dev/net/tun \
  --cap-add NET_ADMIN \
  twingate/client:latest
```

**Docker Compose**: same options via `devices: [/dev/net/tun]`, `cap_add: [NET_ADMIN]`, and a volume mapping `${SERVICE_KEY_PATH}:/etc/twingate/service_key.json`. Use `restart: unless-stopped` and `tty: true`.

**Sharing the network stack**: set `network_mode: "service:twingate-client"` on other services so their traffic routes through Twingate.

**Kubernetes sidecar**
1. `kubectl create secret generic twingate-service-key --from-file=key.json=/path/to/service_key.json`
2. Add a `twingate/client:latest` sidecar container with `NET_ADMIN`, `privileged: true`, and runAsUser 0.
3. Mount the `/dev/net/tun` hostPath (CharDevice) and the secret at `/etc/twingate/service_key.json` (subPath `key.json`).

## Configuration Values
- `--headless[=-]`: enables headless mode on `twingate setup`.
- `twingate help setup`: lists additional options, including the default log level.
- Service Key path in container: `/etc/twingate/service_key.json`.
- Required container flags: `--device /dev/net/tun`, `--cap-add NET_ADMIN`.
- `--network host` or `network_mode: host`: captures all host traffic.
- Twingate local DNS resolvers: `100.95.0.251`, `.252`, `.253`, `.254`.

## CI/CD: Containerized Jobs Without a Shared Network
1. Run the headless client on the runner host (systemd or GitHub Action).
2. Stop Docker.
3. Add the four Twingate DNS resolvers to `dns` in `/etc/docker/daemon.json` (the page's example uses `jq`).
4. Restart Docker.
5. Verify with `docker info | grep DNS`.

## Gotchas
- Without `/dev/net/tun` and `NET_ADMIN`, the containerized client cannot connect.
- Platforms that can't add kernel capabilities (e.g., AWS Fargate) can't use TUN mode. Use userspace networking instead (see AWS ECS Configurations).
- By default, Docker examples only serve containers on the same Docker network or sharing the client's network stack.
- Containers that don't share the client's network namespace use the host's `/etc/resolv.conf`, so DNS for private Resources fails unless Docker DNS is overridden.
- The K8s sidecar example runs privileged as root. Review it against your security policies.
- Page notes examples may reference outdated versions and are a guide only; follow production best practices.

## Related Docs
- Linux Client (interactive mode, installation, logs)
- Services (Service Accounts and Keys)
- Userspace networking
- AWS ECS Configurations
- Twingate GitHub Action
- Prebuilt Docker image (`twingate/client`)