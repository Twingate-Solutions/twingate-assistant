---
source: https://www.twingate.com/docs/api-overview
type: docs
fetched: 2026-11-13
source_version: 5b67f252203885c451f9e154be26148c19d501a98390232a4f81e47a20f6e210
trust: official
---

# Twingate Admin API Overview

## Summary
Twingate's Admin API is GraphQL-based and lets you manage a Twingate network programmatically. Authentication uses an API token generated in the Admin Console and sent in the `X-API-KEY` header. The schema is available via introspection and is always current.

## Key Information
- **Covers:** Remote Networks, Connectors, Gateways; Resources (Kubernetes, SSH, web app) and access assignments; Groups, Users, Devices, device posture; Security Policies and DNS filtering profiles; Service Accounts and Keys; access requests, SSH CAs, serial numbers.
- **Endpoint:** `https://<subdomain>.twingate.com/api/graphql/` (method POST). Subdomain is the network name, e.g. `acme` for `acme.twingate.com`.
- **Header:** `X-API-KEY: <your API token>`, plus `Content-Type: application/json`.
- **Schema discovery:** GraphQL introspection. Clients like Altair have built-in support; Postman also supports GraphQL. Python users can use the `gql` library.
- **Terraform provider** uses this API to provision Connectors, Resources, etc.

## Prerequisites
- Admin Console access to generate a token.
- Your network's subdomain.

## Step-by-Step
1. In the Admin Console, go to **Settings > API > Generate Token**.
2. Choose a permission level (and optionally allowed ranges).
3. Send a POST request to the endpoint with the token in `X-API-KEY`.

Example:
```
curl -X POST "https://<subdomain>.twingate.com/api/graphql/" \
-H "X-API-KEY: <your API token>" \
-H "Content-Type: application/json" \
-d '{"query": "{ remoteNetworks(first: 10) { edges { node { id name } } } }"}'
```

Example query with pagination:
```
{ remoteNetworks(after: null, first: 10) { edges { node { id name } } pageInfo { startCursor hasNextPage } } }
```

## Configuration Values
**Token permission levels** (each includes the one above):
| Level | Adds |
|---|---|
| Read only | Read access to everything exposed |
| Read & Write | Create, update, delete |
| Read, Write & Provision | Generate Connector tokens, create Service Keys |

**Allowed ranges (optional):** up to 10 entries per token, each a CIDR or single IP; IPv4 and IPv6 supported; default `0.0.0.0/0, ::/0` (any address).

**Throttling (per account, per minute):** Reads 60, Writes 20.

## Gotchas
- Grant each token the lowest level it needs.
- Requests from outside a token's allowed ranges fail authentication.
- Exceeding limits within a 1-minute window returns HTTP `429`; retry after the period given in the response.
- Terraform runs failing with `429`: upgrade the Twingate provider to the latest version, which handles retries on throttling.
- Tokens can be modified, disabled, or re-enabled after creation.
- Generating Connector tokens and Service Keys requires the Read, Write & Provision level.

## Related Docs
- Getting Started with the API (Altair and Postman walkthroughs)
- API schema / introspection
- Twingate Terraform provider docs and Terraform getting started guide