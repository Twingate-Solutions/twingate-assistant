# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network constructs (Resources, Groups, Connectors, Remote Networks, Devices, Users, Service Accounts, Policies). Access requires an API token and is available at a subdomain-specific endpoint. Rate limiting applies per minute for reads and writes.

## Key Information
- API type: GraphQL
- Endpoint: `https://<subdomain>.twingate.com/api/graphql/`
- Auth header: `X-API-KEY: <token>`
- Schema always up-to-date via introspection at the endpoint
- Terraform provider wraps this API for IaC workflows

## Prerequisites
- Admin Console access to generate API token
- Navigate: **Settings > API > Generate Token**
- Token can be disabled/enabled or modified after creation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY` |
| Read limit | 60 requests/minute |
| Write limit | 20 requests/minute |
| Rate limit response | HTTP `429` |

## Supported Operations
- **Remote Networks**: CRUD
- **Connectors**: CRUD + token generation
- **Resources**: CRUD
- **Groups**: CRUD
- **Service Accounts/Keys**: CRUD
- **Devices**: Read, archive, unarchive, block, unblock, trust status update
- **Security Policies**: Read, update
- **Users**: Read
- **Social Users**: Read, invite, update, delete
- **Policies**: Assign

## Example Query
```graphql
{
  remoteNetworks(after: null, first: 10) {
    edges {
      node { id name }
    }
    pageInfo { startCursor hasNextPage }
  }
}
```

## Recommended Clients
- **GUI**: GraphiQL (`brew install --cask graphiql`), Altair (has built-in introspection)
- **Python**: `gql` library
- **IaC**: Twingate Terraform provider

## Gotchas
- Rate limit: 60 reads/min, 20 writes/min — exceeding returns `429`
- Terraform `429` errors: upgrade to latest Twingate provider version (handles retry logic)
- Retry timing specified in the `429` response body
- Token must be in HTTP header, not query params

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection (schema discovery)