---
source: https://www.twingate.com/docs/api-overview
type: docs
fetched: 2026-08-14
source_version: 3e8b79aebd571f3b8c90040478a901615406c0254a9ac4684876cec7329b28af
---

# Twingate Admin API Overview

## Page Title
API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network objects (Remote Networks, Connectors, Resources, Groups, Service Accounts, Devices, Users, Policies). Access requires an API token generated from the Admin Console. The API endpoint is tenant-specific and schema is always available via introspection.

## Key Information
- **API Type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth Header**: `X-API-KEY: <your-api-token>`
- **Schema**: Self-documenting via GraphQL introspection
- **Terraform Provider**: Available for IaC management of Twingate resources

## Prerequisites
- Access to Twingate Admin Console
- API token generated via: **Settings → API → Generate Token**
- Know your Twingate subdomain

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| HTTP Header | `X-API-KEY` |
| Read limit | 60 requests/minute |
| Write limit | 20 requests/minute |
| Rate limit response | HTTP `429` |

## Supported Operations by Object

| Object | Operations |
|--------|-----------|
| Remote Networks | CRUD |
| Connectors | CRUD + generate tokens |
| Resources | CRUD |
| Groups | CRUD |
| Service Accounts/Keys | CRUD |
| Devices | Read, archive, unarchive, block, unblock, update trust |
| Security Policies | Read, update |
| Users | Read only |
| Social Users | Read, invite, update, delete |

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

## Gotchas
- Rate limiting returns HTTP `429` — response includes retry timing
- Terraform provider older versions do **not** handle `429` retries automatically; upgrade to latest version
- Pagination required for large result sets (use `after`/`first` + `pageInfo`)
- API tokens can be disabled/enabled but must be generated from Admin Console (no API-based token creation)

## Related Docs
- [Terraform Provider Documentation](https://www.twingate.com/docs/terraform)
- [Terraform Getting Started Guide](https://www.twingate.com/docs/terraform-getting-started)
- [GraphQL Introspection](https://graphql.org/learn/introspection/)