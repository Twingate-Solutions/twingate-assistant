# Getting Started with the Twingate API

## Summary
Twingate exposes a GraphQL API for automating Admin Console actions, accessible directly or via Python/JavaScript CLIs. All API interactions require an API key and tenant name. The API follows standard GraphQL conventions with node/edges response structure.

## Key Information
- API type: GraphQL (not REST)
- Endpoint format: `https://<tenant_name>.twingate.com/api/graphql/`
- Auth header: `X-API-KEY`
- CLIs (Python and JavaScript) are wrappers around the same GraphQL API
- Compatible with orchestration platforms: Ansible, Chef, Puppet, etc.
- Postman collection available for download with pre-built examples

## Prerequisites
- Active Twingate tenant account
- API key with appropriate permissions (Read & Write or Read, Write & Provision for modifications)

## Step-by-Step: Generate API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level: `Read & Write` or `Read, Write & Provision`
4. **Copy and store the token immediately** — it cannot be retrieved after closing the generation window

## Configuration Values

| Parameter | Value |
|-----------|-------|
| API Endpoint | `https://<tenant>.twingate.com/api/graphql/` |
| Auth Header Name | `X-API-KEY` |
| Auth Header Value | Your generated API token |

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
- **Token is shown only once** — copy it before closing the Generate Token dialog; no recovery option exists
- GraphQL queries return only the fields you specify — omitting fields from your query means they won't appear in the response
- Pagination is handled via `pageInfo.hasNextPage` and cursor fields
- Token permissions must be `Read & Write` minimum to modify objects; `Read` only won't allow mutations

## Recommended API Clients
- **Postman** — better for REST-familiar users; import available Postman Collection
- **Altair GraphQL Client** — better for GraphQL beginners; has schema explorer

## Related Docs
- Twingate API Reference (GraphQL schema)
- Python CLI documentation
- JavaScript CLI documentation
- Twingate API Key management