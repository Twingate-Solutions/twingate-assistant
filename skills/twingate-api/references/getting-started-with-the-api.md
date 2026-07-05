# Getting Started with the Twingate API

## Summary
Twingate provides GraphQL APIs and Python/JavaScript CLIs for automating Admin Console actions. All automation methods require an API key and tenant name. APIs follow GraphQL conventions where responses return objects as `nodes` within `edges` collections.

## Key Information
- API endpoint format: `https://<tenant_name>.twingate.com/api/graphql/`
- Authentication via `X-API-KEY` header
- CLIs are wrappers around the GraphQL API
- Responses use GraphQL structure: objects as `nodes`, collections as `edges`
- API keys cannot be retrieved after closing the generation dialog — save immediately

## Prerequisites
- Active Twingate tenant
- API key with appropriate permissions:
  - **Read & Write** — modify objects
  - **Read, Write & Provision** — full access including provisioning

## Step-by-Step: Generate API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level (Read & Write or Read, Write & Provision)
4. Copy and store the token immediately (not retrievable afterward)

## Configuration Values
| Parameter | Value |
|-----------|-------|
| API endpoint | `https://<tenant>.twingate.com/api/graphql/` |
| Auth header name | `X-API-KEY` |
| Auth header value | `<your_api_token>` |

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

## Testing Tools
- **Postman** — recommended if familiar with REST; [Postman Collection available](https://www.twingate.com/docs/getting-started-with-the-api) for import
- **Altair GraphQL Client** — recommended for GraphQL newcomers; includes schema browser

## Gotchas
- API token is shown **only once** at creation — no recovery from UI
- GraphQL queries must match the API schema exactly (Altair highlights schema mismatches in red)
- Only `Read & Write` or higher permission tokens can modify objects; read-only tokens cannot make changes

## Related Docs
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [Python CLI](https://www.twingate.com/docs/python-cli)
- [JavaScript CLI](https://www.twingate.com/docs/javascript-cli)
- [Generating an API Key](https://www.twingate.com/docs/api-key)