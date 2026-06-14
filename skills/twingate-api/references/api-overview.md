# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network resources including Remote Networks, Connectors, Resources, Groups, Service Accounts, Devices, and Users. Access requires an API token generated from the Admin Console and is available at a tenant-specific endpoint.

## Key Information
- **API Type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth Header**: `X-API-KEY: <your-api-token>`
- **Schema**: Available via GraphQL introspection at the endpoint
- **Terraform Provider**: Available for infrastructure-as-code management

## Supported Operations
| Resource | Operations |
|---|---|
| Remote Networks | CRUD |
| Connectors | CRUD + generate tokens |
| Resources | CRUD |
| Groups | CRUD |
| Service Accounts/Keys | CRUD |
| Devices | Read, archive, unarchive, block, unblock, update trust |
| Security Policies | Read, update |
| Users | Read only |
| Social Users | Read, invite, update, delete |

## Prerequisites
- Twingate Admin Console access
- API token: **Settings → API → Generate Token**

## Configuration Values
| Parameter | Value |
|---|---|
| Endpoint URL | `https://<subdomain>.twingate.com/api/graphql/` |
| HTTP Header | `X-API-KEY` |
| Read limit | 60 requests/minute |
| Write limit | 20 requests/minute |

## Rate Limiting
- **429** status returned when limits exceeded
- Response includes retry-after timing
- Reads: 60/min; Writes: 20/min
- Terraform users: upgrade to latest provider version for automatic retry handling

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
- Token can be disabled/re-enabled after creation — verify token is active if requests fail
- Terraform provider versions below latest do not auto-retry on 429 — upgrade to avoid failed runs
- Pagination required for large datasets; use `after`/`first` parameters with `pageInfo`

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection (schema discovery)