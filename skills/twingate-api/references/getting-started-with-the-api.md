# Getting Started with the Twingate API

## Summary
Twingate exposes GraphQL APIs for automating admin tasks, accessible directly or via Python/JavaScript CLIs. All API access requires an API key and tenant name. The API follows standard GraphQL conventions with nodes/edges response structure.

## Key Information
- API type: GraphQL (not REST)
- Endpoint format: `https://<tenant_name>.twingate.com/api/graphql/`
- CLIs (Python and JavaScript) are wrappers around these same GraphQL APIs
- Compatible with orchestration platforms: Ansible, Chef, Puppet, etc.
- Postman collection available for download with pre-built example requests

## Prerequisites
- Active Twingate tenant
- API key with appropriate permissions (Read & Write or Read, Write & Provision)

## Step-by-Step: Generate API Key
1. Open Admin Panel → Settings → API
2. Click **Generate Token**
3. Select permission level: **Read & Write** or **Read, Write & Provision** (required for modifying objects)
4. Copy and store token immediately — cannot be retrieved after closing the dialog

## Configuration Values

| Parameter | Value |
|-----------|-------|
| API Endpoint | `https://<tenant_name>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY: <token>` |
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
- **Token is shown only once** — copy it before closing the Generate Token dialog; no way to retrieve it afterward
- Token can be disabled/re-enabled or have details modified after creation
- GraphQL responses only return fields explicitly requested in the query — structure your queries to include needed fields
- Pagination: check `pageInfo.hasNextPage` to determine if additional results exist

## Recommended API Clients
- **Postman** — better if familiar with REST APIs; import available Postman Collection
- **Altair GraphQL Client** — better for GraphQL-native exploration with schema browsing

## Related Docs
- Twingate API Reference
- Python CLI documentation
- JavaScript CLI documentation
- Twingate API Keys documentation