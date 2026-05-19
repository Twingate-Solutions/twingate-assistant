# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core resources (networks, connectors, resources, groups, users, devices, policies). Access requires an API token and is available at a tenant-specific endpoint. Rate limiting applies at 60 reads/20 writes per minute.

## Key Information
- **API type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth header**: `X-API-KEY: <token>`
- **Schema**: Self-documented via GraphQL introspection
- **Supported operations**: CRUD on Remote Networks, Connectors, Resources, Groups, Service Accounts/Keys, Devices (read/archive/block/trust), Security Policies (read/update), Users (read), Social Users (full CRUD + invite)

## Prerequisites
- Admin Console access to generate API token
- Navigate: **Settings > API > Generate Token**
- Token can be disabled/enabled or modified after creation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| HTTP Header | `X-API-KEY` |
| Read limit | 60 requests/minute |
| Write limit | 20 requests/minute |
| Rate limit response | HTTP `429` |

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
- Rate limit `429` responses include a retry-after period in the response body
- Terraform provider older versions do **not** handle `429` retries automatically — upgrade to latest version if hitting throttling issues
- API schema is always current via introspection; no separate static schema docs needed
- Pagination required for large result sets — use `pageInfo.hasNextPage` and cursors

## Related Docs
- [Terraform Provider documentation](https://www.twingate.com/docs/terraform)
- [Terraform Getting Started guide](https://www.twingate.com/docs/terraform-getting-started)
- [GraphQL Introspection](https://graphql.org/learn/introspection/)