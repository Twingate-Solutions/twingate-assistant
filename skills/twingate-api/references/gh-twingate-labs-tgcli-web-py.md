---
source: https://github.com/Twingate-Labs/tgcli-web-py
type: github
fetched: 2026-08-06
source_version: ca4ddf2212cf024a3529de7c1a3f82f4d7ad8841
---

<!-- triage: unassigned -->

# tgcli-web-py

## Summary
Browser-based web UI for the Twingate CLI that runs as a single-file FastAPI application with an embedded SPA frontend. Delegates all API logic (GraphQL queries, pagination, rate limiting) to the `tgcli` Python library. Supports tenant entity browsing, export/import with diff review, health dashboards, and multi-tenant session management.

---

## Key Information
- Single `app.py` file; imports directly from `tgcli` Python modules (no subprocess calls)
- Supports Docker, Docker Compose, Kubernetes, and pip install
- Export/import uses ZIP files with real-time diff review and conflict resolution
- Concurrent offset-based pagination with 429 rate limit handling
- Multi-tenant session management via system keychain
- New entity types added upstream to `tgcli` appear automatically in the UI

---

## Prerequisites
- Docker (recommended), **or** Python 3.9+
- Twingate API key ([docs.twingate.com/docs/api-overview](https://docs.twingate.com/docs/api-overview))
- Linux headless/CI: `pip install keyrings.alt` + `PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring`

---

## Usage / Step-by-Step

**Docker (recommended):**
```bash
docker run -p 8080:8080 \
  -e TWINGATE_API_KEY=tgp_xxxx \
  -e TWINGATE_TENANT=acme \
  ghcr.io/twingate-labs/tgcli-web
```

**Docker Compose:**
```bash
# Create .env with TWINGATE_API_KEY and TWINGATE_TENANT, then:
docker compose up -d
```

**Kubernetes:**
```bash
kubectl create namespace tgcli-web
kubectl -n tgcli-web create secret generic tgcli-web-secret \
  --from-literal=TWINGATE_API_KEY=tgp_xxxx \
  --from-literal=TWINGATE_TENANT=acme
kubectl apply -k k8s/
kubectl -n tgcli-web port-forward svc/tgcli-web 8080:80
```

**pip install:**
```bash
pip install git+https://github.com/Twingate-Labs/tgcli-web-py.git
tgcli-web serve                        # default: localhost:8080
tgcli-web serve --port 3000 --host 0.0.0.0
```

Open `http://localhost:8080` after any method.

---

## Configuration Values

| Variable | Required | Default | Description |
|---|---|---|---|
| `TWINGATE_API_KEY` | No | — | API key; auto-creates session on startup when combined with `TWINGATE_TENANT` |
| `TWINGATE_TENANT` | No | — | Tenant subdomain (e.g., `acme` for `acme.twingate.com`) |
| `TWINGATE_HOSTNAME` | No | `twingate.com` | Override for staging/dev environments |

**CLI flags (`tgcli-web serve`):**
- `--port` — listening port (default `8080`)
- `--host` — bind address (default `localhost`)

---

## Gotchas
- Session data persists in the `tgcli-data` Docker volume; run `docker compose down -v` to reset
- `TWINGATE_API_KEY` + `TWINGATE_TENANT` must both be set to trigger auto-login on container start
- Linux/headless environments require a keyring backend; without it, session storage silently fails
- Import is not supported for all entities (Service Account Keys, Certificate Authorities, DNS Security, Access Requests, Devices, Security Policies, Serial Numbers are export-only)
- Updates via the Settings panel require a server restart to take effect

---

## Related Docs
- Upstream CLI: [github.com/Twingate-Labs/Twingate-CLI](https://github.com/Twingate-Labs/Twingate-CLI)
- T