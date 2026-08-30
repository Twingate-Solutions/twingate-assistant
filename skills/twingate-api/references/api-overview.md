---
source: https://www.twingate.com/docs/api-overview
type: docs
fetched: 2026-08-30
source_version: 9643b1f301f406bdf6e7947db425d6465e2119cc9696a2e51577ed3109bc8380
---

# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for programmatic network management. Access requires an API token from the Admin Console and is available at a tenant-specific endpoint. Rate limiting applies at 60 reads/20 writes per minute.

## Key Information
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth header**: `X-API-KEY: <token>`
- **Schema**: Always current via GraphQL introspection at the endpoint
- **Covers**: Remote Networks, Connectors, Resources, Groups, Users, Devices, Service Accounts, Security Policies, DNS profiles, Access Requests

## Prerequisites
- Admin Console access to generate API token
- Token permission level appropriate for intended operations

## Token Permission Levels
| Level | Capabilities |
|-------|-------------|
| Read only | Read all API-exposed data |
| Read & Write | Read + create, update, delete |
| Read, Write & Provision | Above + generate Connector tokens, create Service Keys |

**Principle of least privilege**: Grant lowest level needed.

## Configuration Values
- **HTTP Header**: `X-API-KEY`
- **Allowed IP ranges**: Up to 10 entries (CIDR or single IP); default `0.0.0.0/0, ::/0`
- **Rate limits**: 60 reads/min, 20 writes/min → `429` on breach
- **Retry**: `429` response includes retry-after time

## Step-by-Step: Get API Token
1. Log into Admin Console
2. Navigate to **Settings → API → Generate Token**
3. Select permission level
4. Optionally restrict source IP ranges
5. Copy token value (store securely)

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

## Recommended Clients
- **GUI**: GraphiQL (`brew install --cask graphiql`) or Altair (has built-in introspection)
- **Python**: `gql` library
- **IaC**: Twingate Terraform provider

## Gotchas
- Requests from IPs outside allowed ranges fail authentication silently (auth failure, not range error)
- Terraform `429` errors: upgrade to latest Twingate provider version for built-in retry handling
- Rate limits are per-account, not per-token; multiple integrations share the same limits
- Pagination required for large result sets — use `pageInfo.hasNextPage` and cursors

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection (schema reference via Altair or similar)