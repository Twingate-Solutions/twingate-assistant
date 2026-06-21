# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core resources (networks, connectors, resources, groups, users, devices, service accounts, policies). Access requires an API token generated from the Admin Console. The API endpoint is tenant-specific and uses a custom header for authentication.

## Key Information
- **API type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth header**: `X-API-KEY: <token>`
- **Schema**: Available via GraphQL introspection at the endpoint
- **Rate limits**: 60 reads/min, 20 writes/min; exceeding returns HTTP `429`
- **Terraform provider** available for IaC management

## Prerequisites
- Admin Console access to generate API token
- Navigate: Settings → API → Generate Token

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Endpoint URL | `https://<subdomain>.twingate.com/api/graphql/` |
| Auth header name | `X-API-KEY` |
| Read limit | 60 requests/min |
| Write limit | 20 requests/min |
| Rate limit response | HTTP `429` |

## Supported Operations
| Resource | Operations |
|----------|-----------|
| Remote Networks | CRUD |
| Connectors | CRUD + generate tokens |
| Resources | CRUD |
| Groups | CRUD |
| Service Accounts/Keys | CRUD |
| Devices | Read, archive, unarchive, block, unblock, update trust |
| Security Policies | Read, update |
| Users | Read |
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
- **GUI**: GraphiQL (`brew install --cask graphiql`), Altair (has built-in introspection)
- **Python**: `gql` library

## Gotchas
- Rate limit `429` responses include a retry-after period in the response body — respect it
- Terraform users hitting `429` errors should upgrade to the latest Twingate provider version, which handles retries automatically
- API tokens can be disabled/re-enabled in the Admin Console after creation
- Pagination required for large result sets; use `pageInfo.hasNextPage` and cursors

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection (for live schema)