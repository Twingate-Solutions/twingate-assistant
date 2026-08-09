---
source: https://github.com/Twingate-Labs/tgcli-web-py
type: github
fetched: 2026-08-09
source_version: 663036bc90de254cb071194c99da373bf3ba27ef
---

# tgcli-web-py

## Summary
Browser-based API explorer for Twingate tenants built as a single-file FastAPI app with an embedded SPA frontend. Imports directly from the `tgcli` Python library (does not shell out to a binary). Supports tenant-to-tenant export/import, entity browsing, diff review, health dashboard, and global search.

---

## Key Information
- Single `app.py` file; FastAPI backend + embedded HTML/CSS/JS frontend
- Delegates all API logic (queries, pagination, rate limiting, retry) to the upstream `tgcli` Python library
- Supports 15 entity types; Browse/Export available for all, Import available for a subset
- Concurrent offset-based pagination (4x faster than sequential) with 429 rate-limit handling
- Multi-tenant session management with keychain storage
- Self-updating via Settings panel in the UI
- Three UI themes: dark, light, WCAG AAA accessible

---

## Prerequisites
- **Docker** (recommended), **or** Python 3.9+
- Twingate API key — generate at `https://docs.twingate.com/docs/api-overview`
- Tenant subdomain (e.g., `acme` from `acme.twingate.com`)

---

## Usage / Step-by-Step

### Docker (recommended)
```bash
docker run -p 8080:8080 \
  -e TWINGATE_API_KEY=tgp_xxxx \
  -e TWINGATE_TENANT=acme \
  ghcr.io/twingate-labs/tgcli-web
```
Open `http://localhost:8080`.

### Docker Compose
1. Create `.env` with `TWINGATE_API_KEY` and `TWINGATE_TENANT`
2. `docker compose up -d`
3. Sessions persist in `tgcli-data` volume; clear with `docker compose down -v`

### Kubernetes
```bash
kubectl create namespace tgcli-web
kubectl -n tgcli-web create secret generic tgcli-web-secret \
  --from-literal=TWINGATE_API_KEY=tgp_xxxx \
  --from-literal=TWINGATE_TENANT=acme
kubectl apply -k k8s/
kubectl -n tgcli-web port-forward svc/tgcli-web 8080:80
```

### pip install
```bash
pip install git+https://github.com/Twingate-Labs/tgcli-web-py.git
tgcli-web serve                        # default: localhost:8080
tgcli-web serve --port 3000 --host 0.0.0.0
```
Credentials entered via the UI when not set as env vars.

---

## Configuration Values

| Variable | Required | Default | Description |
|---|---|---|---|
| `TWINGATE_API_KEY` | No | — | API key; auto-creates session on startup when combined with `TWINGATE_TENANT` |
| `TWINGATE_TENANT` | No | — | Tenant subdomain (e.g., `acme`) |
| `TWINGATE_HOSTNAME` | No | `twingate.com` | Override for staging/dev environments |

**CLI flags (`tgcli-web serve`):**
- `--port` — listening port (default `8080`)
- `--host` — bind address (default `localhost`)

---

## Gotchas
- **Linux/CI keyring**: Headless environments require a keyring backend:
  ```bash
  pip install keyrings.alt
  export PYTHON_KEYRING_BACKEND=keyrings.alt.file.PlaintextKeyring
  ```
- Import is not supported for: Service Account Keys, Certificate Authorities, DNS Security, Access Requests, Devices, Security Policies, Serial Numbers
- If `TWINGATE_API_KEY` is set without `TWINGATE_TENANT` (or vice versa), auto-session creation does not occur
- New entity types added upstream to `tgcli` appear automatically in the UI without changes to this repo

---

## Related Docs
- Upstream CLI: [Twingate-