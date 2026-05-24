# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network objects (Resources, Groups, Connectors, Remote Networks, etc.). Access requires an API token generated from the Admin Console. Rate limiting applies with separate read/write limits.

## Key Information
- **API type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth header**: `X-API-KEY: <your-token>`
- **Schema**: Always current via GraphQL introspection at the endpoint
- **Supported operations**: Full CRUD on Remote Networks, Connectors, Resources, Groups, Service Accounts/Keys; read/update on Devices, Security Policies, Users; Social Users management; Policy assignment

## Prerequisites
- Access to Twingate Admin Console
- API token: Settings → API → Generate Token

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY` |
| Read limit | 60 req/min |
| Write limit | 20 req/min |
| Rate limit response | HTTP `429` |

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
- **GUI**: GraphiQL (`brew install --cask graphiql`) or Altair (has built-in introspection/schema browser)
- **Python**: `gql` library

## Gotchas
- Rate limit: **60 reads / 20 writes per minute** — exceeding returns `429` with retry-after info
- Terraform users hitting `429` should upgrade to latest Twingate provider (handles retries automatically)
- Token can be disabled/re-enabled but must be generated from Admin Console (no API bootstrap)

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection for live schema reference