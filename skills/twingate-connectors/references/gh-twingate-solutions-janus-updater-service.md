---
source: https://github.com/Twingate-Solutions/janus-updater-service
type: github
fetched: 2026-08-06
source_version: c07ed7dd42c394e5def628b1e9bf6f6f9f965ac5
---

<!-- triage: unassigned -->

# Janus Updater Service

## Summary
Janus is a label-driven Docker container image updater that monitors running containers and automatically recreates them when a newer image is available. It preserves all original container configuration (labels, mounts, networks, resource limits) and provides rollback on failed recreation.

## Key Information
- Scans Docker engine every 30 seconds for containers labeled `janus.autoupdate.enable=true`
- Recreate workflow: stop → rename to `<name>.janus-old.<timestamp>` → start new → remove old (or rollback)
- Outputs structured JSON logs to stdout
- Will **not** update itself (containers named `janus` are excluded)
- Image: `ghcr.io/twingate-solutions/janus-updater-service:latest`

## Prerequisites
- Docker socket access (`/var/run/docker.sock`) — grants full Docker daemon control, equivalent to root
- For private registries: `~/.docker/config.json`

## Usage / Step-by-Step

**1. Run Janus via Docker Compose:**
```yaml
services:
  janus:
    image: ghcr.io/twingate-solutions/janus-updater-service:latest
    container_name: janus
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${HOME}/.docker/config.json:/root/.docker/config.json:ro  # optional
```

**2. Label containers to enable updates:**
```yaml
labels:
  janus.autoupdate.enable: "true"
  janus.autoupdate.interval: "600"      # optional
  janus.autoupdate.monitor-only: "false" # optional
```

## Configuration Values

### Environment Variables
| Variable | Default | Description |
|---|---|---|
| `JANUS_DEFAULT_INTERVAL` | `300` | Check interval (seconds) for unlabeled containers |
| `JANUS_LOG_LEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `JANUS_MAX_CONCURRENT_UPDATES` | `1` | Max simultaneous container updates |
| `JANUS_STOP_TIMEOUT` | `10` | Seconds before force-killing stopped container |
| `JANUS_LABEL_PREFIX` | `janus.autoupdate` | Label namespace prefix |

### Container Labels
| Label | Required | Default | Description |
|---|---|---|---|
| `janus.autoupdate.enable` | Yes | — | Set `true` to enable |
| `janus.autoupdate.interval` | No | `JANUS_DEFAULT_INTERVAL` | Per-container check interval (min: 5s) |
| `janus.autoupdate.monitor-only` | No | `false` | Log only, no recreation |

## Gotchas
- **Docker socket = root access.** Only run in trusted environments.
- **Compose stacks:** Janus is not Compose-aware. After Janus updates a container, running `docker compose up` will overwrite it. Use `monitor-only` mode with Compose stacks.
- **Downtime during updates:** Old container stops before new one starts. Use `monitor-only` for zero-downtime requirements.
- **Rollback can fail:** If rollback fails after a bad update, the container is left stopped. Watch for `rollback_failed` log events.
- **Stateful containers:** Not recommended for databases unless the image upgrade is safe to apply via restart.
- **Self-update:** Must be done manually.
- Only 3 most recent versioned images retained in registry; older versions are deleted.

## Related Docs
- [GitHub Container Registry](https://ghcr.io/twingate-solutions/janus-updater-service)
- [Docker socket security](https://docs.docker.com/engine/security/)