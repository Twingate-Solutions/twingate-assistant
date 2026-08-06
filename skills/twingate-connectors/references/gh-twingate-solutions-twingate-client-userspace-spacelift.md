---
source: https://github.com/Twingate-Solutions/twingate-client-userspace-spacelift
type: github
fetched: 2026-08-06
source_version: d50c5dfa0f236065a664e76cc6bf5255beede99f
---

<!-- triage: unassigned -->

# Twingate Userspace + Proxytunnel on Spacelift

## Summary
Runs Twingate's userspace HTTP proxy mode inside Spacelift CI/CD runner containers to reach private network resources without root, TUN devices, or NET_ADMIN capabilities. Uses `proxytunnel` to bridge TCP protocols (Postgres, MySQL, SSH, etc.) through Twingate's HTTP CONNECT proxy. All three components (twingated, proxytunnel, application) run as unprivileged processes in a single container.

## Key Information
- Traffic path: `psql → proxytunnel (TCP :LOCAL_PORT) → twingated (HTTP proxy :9999) → Twingate network → private resource`
- If `TUNNEL_DEST` is unset, only the HTTP proxy starts; tools supporting `http_proxy`/`https_proxy` can use it directly
- Runner image based on Ubuntu 22.04; includes `twingated`, `proxytunnel`, `psql`, `procps`
- `init.sh` is baked into the image and invoked via Spacelift's `before_init` hook
- Docker Compose setup included for local validation before Spacelift deployment
- GitHub Actions workflow builds on PR (no push) and builds+pushes on merge to main

## Prerequisites
- Twingate account with a configured resource and service account
- Twingate connector running in the same network as the target resource
- Spacelift account
- Docker Hub account (to host the custom runner image)
- GitHub repo secrets: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`

## Usage / Step-by-Step

**Local validation:**
```bash
cp .env.example .env   # fill in all values
docker compose up
PGPASSWORD='...' psql -h localhost -p 5432 -U postgres -d postgres -c "SELECT 1;"
```

**Spacelift deployment:**
1. Build and push runner image:
   ```bash
   docker build --platform linux/amd64 -t <user>/spacelift-twingate:latest .
   docker push <user>/spacelift-twingate:latest
   ```
2. Update `.spacelift/config.yml` with your image reference
3. Create Spacelift stack pointing to this repo (vendor: Terraform)
4. Set environment variables in stack settings
5. Verify with a Task: `PGPASSWORD="$DB_PASSWORD" psql -h 127.0.0.1 -p "$TUNNEL_LOCAL_PORT" -U "$DB_USER" -d "$DB_NAME" -c "SELECT 1;"`

## Configuration Values

| Variable | Required | Secret | Description |
|---|---|---|---|
| `TWINGATE_SERVICE_KEY` | Yes | Yes | Full JSON content of Twingate service key |
| `TUNNEL_DEST` | No | No | Private resource, e.g. `db.internal:5432`; omit for proxy-only mode |
| `TUNNEL_LOCAL_PORT` | If `TUNNEL_DEST` set | No | Local TCP port for proxytunnel listener |
| `TWINGATE_PROXY_PORT` | No | No | Twingate HTTP proxy port (default: `9999`) |
| `DB_USER` / `DB_PASSWORD` / `DB_NAME` | Smoke test only | `DB_PASSWORD` yes | Used in Docker Compose smoke test |

## Gotchas
- Runner image must be AMD64 (`--platform linux/amd64`); Spacelift public workers are AMD64
- `TWINGATE_SERVICE_KEY` is read from env directly by `twingated`; no file or `/etc/twingate` needed
- `/run/user/1983` must be pre-created and owned by UID 1983 (Spacelift user) in the Dockerfile
- Do not use inline `&&`-chained hooks for background processes; use `init.sh` instead (Spacelift uses `dash`)
- Increase `sleep 12` in `init.sh` if tunnel isn't ready before commands execute
- Rebuild and repush image after any change to `Dockerfile` or `init.sh`
- `spacelift` user requires a home directory for `.terraformrc`; do not use `--no-create