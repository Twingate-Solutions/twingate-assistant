# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network resources including Remote Networks, Connectors, Resources, Groups, Service Accounts, Devices, and Users. Access requires an API token generated from the Admin Console. Rate limiting applies at 60 reads/min and 20 writes/min.

## Key Information
- API is GraphQL-based with full schema introspection available at the endpoint
- Supports CRUD operations for: Remote Networks, Connectors, Resources, Groups, Service Accounts/Keys, Devices, Users, Security Policies
- Schema documentation is auto-generated and always current via introspection
- Terraform provider available for infrastructure-as-code workflows

## Prerequisites
- Twingate Admin Console access
- API token generated via: **Settings → API → Generate Token**
- Your Twingate account subdomain

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Endpoint URL | `https://<subdomain>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY: <your-api-token>` |

## API Rate Limits

| Request Type | Limit |
|-------------|-------|
| Reads | 60/minute |
| Writes | 20/minute |
| Exceeded response | HTTP `429` with retry-after info |

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
- **IaC**: Twingate Terraform Provider

## Gotchas
- Tokens can be disabled/enabled after creation; manage carefully
- HTTP `429` errors from Terraform: upgrade to latest Twingate provider version — older versions don't handle retry logic automatically
- Pagination required for large result sets; use `pageInfo.hasNextPage` and cursor-based pagination

## Related Docs
- Terraform Provider documentation
- Terraform Getting Started guide
- GraphQL introspection (for schema exploration via Altair or similar tools)