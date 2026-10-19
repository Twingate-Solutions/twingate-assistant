---
source: https://www.twingate.com/docs/api-overview
type: docs
fetched: 2026-10-18
source_version: c44aa1ae66dca17c6a6184a06d1c3a0644bf91ed9d9abb856a85709da57aecbb
trust: official
---

# Twingate Admin API Overview

## Page Title
API Overview — Twingate Admin GraphQL API

## Summary
Twingate provides a GraphQL-based Admin API for programmatic network management. All requests use HTTP POST with an API token in the `X-API-KEY` header. The API covers resources, users, groups, devices, service accounts, security policies, and more.

## Key Information
- **API type:** GraphQL (schema discoverable via introspection)
- **Endpoint pattern:** `https://<subdomain>.twingate.com/api/graphql/`
- **Auth header:** `X-API-KEY: <token>`
- **Rate limits:** 60 reads/min, 20 writes/min; exceeding returns HTTP 429
- **Pagination:** Cursor-based (`after`, `first` params; `pageInfo.hasNextPage`)

## Prerequisites
- Active Twingate account with Admin Console access
- API token generated at **Settings → API → Generate Token**

## Token Permissions (least-privilege order)
| Level | Capabilities |
|---|---|
| Read only | All read operations |
| Read & Write | Read + create/update/delete |
| Read, Write & Provision | Above + Connector tokens + Service Keys |

## Configuration Values
| Parameter | Value |
|---|---|
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| Method | `POST` |
| Auth header | `X-API-KEY: <your API token>` |
| Content-Type | `application/json` |

## Example Request
```bash
curl -X POST "https://<subdomain>.twingate.com/api/graphql/" \
  -H "X-API-KEY: <your API token>" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ remoteNetworks(first: 10) { edges { node { id name } } } }"}'
```

## Example Query (paginated)
```graphql
{
  remoteNetworks(after: null, first: 10) {
    edges { node { id name } }
    pageInfo { startCursor hasNextPage }
  }
}
```

## Gotchas
- **Rate limiting:** 429 responses include a retry-after time; upgrade Terraform provider to latest to handle retries automatically
- **IP allowlisting:** Tokens can be restricted to up to 10 CIDR/IP entries; default allows all (`0.0.0.0/0, ::/0`)
- **Token scope:** Grant minimum required permission level per token
- **Schema:** Always fetch live schema via introspection — do not rely on cached/static copies

## Recommended Clients
- **GUI:** GraphiQL (`brew install --cask graphiql`) or Altair (has built-in introspection viewer)
- **Python:** `gql` library
- **IaC:** Twingate Terraform Provider (see separate docs)

## Related Docs
- Terraform Provider docs + Getting Started guide
- Twingate API token settings (Admin Console → Settings → API)
- GraphQL introspection (for live schema browsing)