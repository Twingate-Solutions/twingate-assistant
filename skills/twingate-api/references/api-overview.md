---
source: https://www.twingate.com/docs/api-overview
type: docs
fetched: 2026-09-06
source_version: 4dba3e500229c780ef51d7540ef05147db171d02e9906ab72aeefc6e24814fa5
---

# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for programmatic management of network resources. Access requires generating an API token from the Admin Console and authenticating via a custom HTTP header. The API covers remote networks, connectors, resources, users, groups, devices, and service accounts.

## Key Information
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Protocol**: GraphQL
- **Auth header**: `X-API-KEY: <token>`
- **Schema**: Self-documented via GraphQL introspection at the endpoint

## Prerequisites
- Admin Console access to generate API token
- Token permission level appropriate for operations needed

## Token Permission Levels
| Level | Capabilities |
|-------|-------------|
| Read only | Read all API-exposed data |
| Read & Write | Read + create, update, delete |
| Read, Write & Provision | Read/Write + generate Connector tokens, create Service Keys |

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Endpoint URL | `https://<subdomain>.twingate.com/api/graphql/` |
| Auth header name | `X-API-KEY` |
| Default allowed IP ranges | `0.0.0.0/0, ::/0` |
| Max IP range entries per token | 10 |
| Read rate limit | 60 requests/minute |
| Write rate limit | 20 requests/minute |
| Rate limit response code | `429` |

## Setup Steps
1. Log into Admin Console
2. Navigate to **Settings → API → Generate Token**
3. Assign minimum required permission level
4. Optionally restrict to specific CIDR ranges or IPs
5. Use token value in `X-API-KEY` header for all requests

## Example Query
```graphql
{
  remoteNetworks(after: null, first: 10) {
    edges {
      node {
        id
        name
      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}
```

## Recommended GraphQL Clients
- **GUI**: GraphiQL (`brew install --cask graphiql`) or Altair (has built-in introspection/schema browser)
- **Python**: `gql` library

## Gotchas
- Rate limiting returns `429` — response includes retry-after timing; upgrade Terraform provider to latest version to handle retries automatically
- Requests from IPs outside allowed ranges fail authentication silently (auth failure, not IP error)
- Grant tokens minimum required permissions (least privilege)
- Schema is always current via introspection — prefer introspection over static docs for field-level details

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection (for schema/type exploration)