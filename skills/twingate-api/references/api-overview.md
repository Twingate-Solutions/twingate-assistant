# Twingate Admin API Overview

## Summary
Twingate provides a GraphQL-based Admin API for managing all core network constructs (Remote Networks, Connectors, Resources, Groups, Service Accounts, Devices, Users, Security Policies). Authentication uses API tokens with a custom HTTP header. Rate limiting applies per minute for read and write operations.

## Key Information
- **API Type**: GraphQL
- **Endpoint**: `https://<subdomain>.twingate.com/api/graphql/`
- **Auth Header**: `X-API-KEY: <token>`
- **Schema**: Always up-to-date via introspection at the endpoint
- **Terraform provider** available for IaC provisioning

## Prerequisites
- Access to Twingate Admin Console
- API token generated via: **Settings → API → Generate Token**

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Endpoint URL | `https://<subdomain>.twingate.com/api/graphql/` |
| HTTP Header | `X-API-KEY` |
| Read limit | 60 requests/minute |
| Write limit | 20 requests/minute |
| Throttle response | HTTP `429` |

## Supported Operations

| Resource | Operations |
|----------|-----------|
| Remote Networks | CRUD |
| Connectors | CRUD + generate tokens |
| Resources | CRUD |
| Groups | CRUD |
| Service Accounts & Keys | CRUD |
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
- **GUI**: GraphiQL (`brew install --cask graphiql`) or Altair (has built-in introspection)
- **Python**: `gql` library

## Gotchas
- Hitting the `429` limit returns a retry window in the response body — honor it
- Terraform users hitting `429` errors should **upgrade to the latest Twingate provider** (handles retries automatically)
- API tokens can be disabled/re-enabled in the Admin Console; plan for token rotation
- Pagination required for large datasets — use `pageInfo.hasNextPage` and `after` cursor

## Related Docs
- [Terraform Provider Documentation](https://www.twingate.com/docs/terraform)
- [Terraform Getting Started Guide](https://www.twingate.com/docs/terraform-getting-started)
- [GraphQL Introspection](https://graphql.org/learn/introspection/)