# Getting Started with the Twingate API

## Summary
Twingate provides GraphQL APIs and Python/JavaScript CLIs for automating Admin Console actions. All methods require an API key and tenant name. CLIs are wrappers around the GraphQL API.

## Key Information
- API type: GraphQL (not REST)
- GraphQL responses use `node` (single object) and `edges` (collections) structure
- Responses only return fields explicitly requested in the query
- API endpoint format: `https://<tenant_name>.twingate.com/api/graphql/`
- Postman Collection available for download with pre-built examples
- Recommended clients: Postman or Altair GraphQL Client

## Prerequisites
- Active Twingate tenant
- API key with appropriate permissions:
  - **Read** – read-only access
  - **Read & Write** – modify objects
  - **Read, Write & Provision** – modify + provision objects

## Generating an API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level (Read & Write or Read, Write & Provision for modifications)
4. Copy and store the token immediately — **cannot be retrieved after closing the modal**
5. Tokens can be modified, disabled, or re-enabled after creation

## Configuration Values

| Parameter | Value |
|-----------|-------|
| API endpoint | `https://<tenant>.twingate.com/api/graphql/` |
| Auth header name | `X-API-KEY` |
| Auth header value | `<your_api_token>` |
| Postman variable | `tenant_name` |

## Example: List Resources Query
```graphql
{
  resources {
    edges {
      node {
        id
        name
        createdAt
        updatedAt
        isActive
      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}
```

## Gotchas
- API token is shown **only once** — copy it before closing the generation modal
- Token requires **Read & Write** minimum to make changes; read-only token will not work for mutations
- GraphQL is not REST — field selection is required in queries; omitting fields means they won't be returned
- Pagination: check `pageInfo.hasNextPage` to determine if additional results exist

## Related Docs
- Twingate API Reference (GraphQL schema)
- Python CLI documentation
- JavaScript CLI documentation
- Twingate Postman Collection (downloadable from the page)