# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network objects (Remote Networks, Connectors, Resources, Groups, Service Accounts, Devices, Users, Policies). Access requires an API token generated from the Admin Console. The API endpoint is tenant-specific and schema is always current via introspection.

## Key Information
- **API type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth header**: `X-API-KEY: <your-api-token>`
- **Schema**: Self-documented via GraphQL introspection at the endpoint
- **Terraform provider** available for IaC management

## Prerequisites
- Admin Console access to generate API token
- Navigate: Settings → API → Generate Token
- Token can be disabled/re-enabled after creation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY` |
| Read limit | 60 requests/minute |
| Write limit | 20 requests/minute |
| Rate limit response | HTTP `429` |

## Supported Operations by Object
- **Remote Networks**: CRUD
- **Connectors**: CRUD + generate tokens
- **Resources**: CRUD
- **Groups**: CRUD
- **Service Accounts/Keys**: CRUD
- **Devices**: Read, archive, unarchive, block, unblock, update trust status
- **Security Policies**: Read, update; assign to objects
- **Users**: Read only
- **Social Users**: Read, invite, update, delete

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
- Rate limits are per-minute windows; hitting them returns `429` with retry-after info
- Terraform provider versions prior to latest may not handle `429` retries automatically — upgrade to latest if Terraform runs fail with `429`
- Pagination required for large result sets (use `after`/`first` + `pageInfo`)

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection (schema discovery)