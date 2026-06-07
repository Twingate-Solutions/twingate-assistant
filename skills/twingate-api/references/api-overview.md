# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network objects (Remote Networks, Connectors, Resources, Groups, Service Accounts, Devices, Users, Policies). Access requires an API token generated from the Admin Console. The API endpoint is tenant-specific and schema is always available via introspection.

## Key Information
- **API type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth header**: `X-API-KEY: <your-token>`
- **Schema**: Always up-to-date via GraphQL introspection
- **Supported objects**: Remote Networks, Connectors, Resources, Groups, Service Accounts/Keys, Devices, Users, Security Policies

## Prerequisites
- Admin Console access to generate API token
- Navigate: **Settings > API > Generate Token**
- Token can be disabled/re-enabled after creation

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| HTTP Header | `X-API-KEY` |
| Read rate limit | 60 requests/minute |
| Write rate limit | 20 requests/minute |
| Throttle response | HTTP `429` |

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
- **GUI**: GraphiQL (`brew install --cask graphiql`) or Altair (has built-in introspection)
- **Python**: `gql` library
- **IaC**: Twingate Terraform Provider

## Gotchas
- **Rate limiting**: 60 reads/20 writes per minute; exceeding returns `429` with retry-after info
- **Terraform + 429**: Upgrade to latest Twingate Terraform provider version to handle automatic retries on throttle responses
- Pagination required for large result sets (use `after`/`first` cursor pattern)

## Related Docs
- [Terraform Provider documentation](https://www.twingate.com/docs/terraform)
- [Terraform Getting Started guide](https://www.twingate.com/docs/terraform-getting-started)
- GraphQL introspection (built into endpoint)