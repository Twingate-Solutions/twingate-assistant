---
source: https://github.com/Twingate-Solutions/twingate-partner-api
type: github
fetched: 2026-10-18
source_version: 506924d75f762eee5cd90bb39ed445b8dfe93a2f
trust: official
---

<!-- triage: unassigned -->

# Twingate Partner API

A GraphQL API for distributors, MSSPs, and vendors to manage Twingate customer portfolios programmatically. Supports listing networks, reading license counts, and provisioning MSP Portals.

## Key Information

- Three queries (`partner`, `networks`, `network`) and one mutation (`mspNetworkCreate`)
- Transport: HTTPS, GraphQL over a partner-supplied regional endpoint (e.g., `https://api.us2.twingate.com/partners`)
- Auth: two request headers — `X-PARTNER-ID` and `X-API-KEY` — required on every call, server-side only
- Schema available in SDL and introspection JSON formats for use with Altair, Postman, Insomnia, or code generators
- A local mock server is included for development without live credentials

## Prerequisites

- Credentials (`TWINGATE_PARTNER_ID`, `TWINGATE_PARTNER_API_KEY`, and endpoint URL) issued by Twingate's partner team
- Without credentials: run `tools/mock-server/` locally and point `TWINGATE_PARTNER_API_URL` at `http://localhost:4000/partners`

## Quick Start

```bash
curl "$TWINGATE_PARTNER_API_URL" \
  -H 'Content-Type: application/json' \
  -H "X-PARTNER-ID: $TWINGATE_PARTNER_ID" \
  -H "X-API-KEY: $TWINGATE_PARTNER_API_KEY" \
  -d '{"query":"{ partner { id name } }"}'
```

## Configuration Values

| Variable | Required | Notes |
|---|---|---|
| `TWINGATE_PARTNER_ID` | Yes | Issued by partner team |
| `TWINGATE_PARTNER_API_KEY` | Yes | Issued by partner team |
| `TWINGATE_PARTNER_API_URL` | Yes | Regional URL, e.g. `https://api.us2.twingate.com/partners` |

## Repo Layout

| Path | Contents |
|---|---|
| `docs/01-overview.md` | Concepts: Partners, MSP Networks, Customer Networks |
| `docs/02-getting-started.md` | Auth, first call, tooling setup, mock server |
| `docs/03-api-reference.md` | Operations, types, enums, errors, limits |
| `docs/04-workflows.md` | Portfolio dashboard, billing export, provisioning, PSA sync |
| `docs/05-best-practices.md` | Security, reliability, troubleshooting |
| `schema/` | SDL and introspection JSON |
| `queries/` | Ready-to-run GraphQL operations |
| `examples/curl/` | Shell + jq scripts |
| `examples/python/` | Python client and workflow scripts |
| `examples/django/` | Django dashboard with CSV export |
| `examples/nextjs/` | Next.js App Router (TypeScript) dashboard |
| `examples/powershell/` | PowerShell module (5.1 and 7+) |
| `tools/mock-server/` | Local mock with fake data |

## Gotchas

- The API endpoint URL is region-specific and must be obtained from the Twingate partner team; there is no public default
- Credentials must only be used server-side; never expose `X-API-KEY` in client-side code
- The mock server path differs from production: use `/partners` suffix at `http://localhost:4000/partners`

## Related Docs

- `docs/03-api-reference.md` — full operation and type reference
- `docs/04-workflows.md` — billing, provisioning, and PSA sync patterns
- `docs/05-best-practices.md` — security and reliability guidance