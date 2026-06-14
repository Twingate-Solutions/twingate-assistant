# Getting Started with the Twingate API

## Summary
Twingate exposes a GraphQL API for automating Admin Console actions, accessible directly or via Python/JavaScript CLIs. All access requires an API key and tenant name. The API follows standard GraphQL conventions with nodes and edges.

## Key Information
- API type: GraphQL (not REST)
- Endpoint: `https://<tenant_name>.twingate.com/api/graphql/`
- Auth header: `X-API-KEY: <token>`
- CLIs (Python, JavaScript) are wrappers around the same GraphQL API
- Responses use GraphQL structure: objects = `node`, collections = `edges`
- Postman collection available for download with pre-built examples

## Prerequisites
- Active Twingate tenant
- API key with appropriate permissions:
  - **Read & Write** — modify existing objects
  - **Read, Write & Provision** — create/provision new objects

## Generating an API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level (Read & Write or Read, Write & Provision)
4. **Copy token immediately** — cannot be retrieved after closing the modal
5. Token can be disabled/re-enabled or have details modified after creation

## Configuration Values

| Parameter | Value |
|-----------|-------|
| API endpoint | `https://<tenant>.twingate.com/api/graphql/` |
| Auth header key | `X-API-KEY` |
| Auth header value | `<your_api_token>` |
| Postman variable | `tenant_name` |

## Example Query (List Resources)
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
- Token is shown **only once** at generation time — store it securely immediately
- GraphQL queries are field-selective; only requested fields are returned — be explicit about needed fields
- Altair will show schema validation errors (red highlights) if query fields don't match schema
- Pagination: check `pageInfo.hasNextPage` to determine if additional results exist

## Recommended API Clients
- **Postman** — better for REST-familiar users; import pre-built collection
- **Altair GraphQL Client** — better for GraphQL-native workflow, schema browser included

## Related Docs
- Twingate API Reference
- Python CLI documentation
- JavaScript CLI documentation
- Twingate API Key management