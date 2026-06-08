# Getting Started with the Twingate API

## Summary
Twingate provides GraphQL APIs and Python/JavaScript CLIs for automating Admin Console actions. All methods require an API key and tenant name. The API uses GraphQL, where responses return objects as `nodes` within `edges` collections.

## Key Information
- API endpoint: `https://<tenant_name>.twingate.com/api/graphql/`
- Authentication header: `X-API-KEY: <token>`
- CLIs are wrappers around the GraphQL API
- Compatible with orchestration platforms: Ansible, Chef, Puppet
- Postman collection available for download with pre-built examples

## Prerequisites
- Active Twingate tenant (tenant name required)
- API key with appropriate permissions:
  - **Read & Write** — modify existing objects
  - **Read, Write & Provision** — full provisioning access

## Step-by-Step: Generating an API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level (Read & Write or Read, Write & Provision)
4. Copy and store the token immediately — it cannot be retrieved after closing the dialog

## Configuration Values

| Parameter | Value |
|-----------|-------|
| API endpoint | `https://<tenant>.twingate.com/api/graphql/` |
| Auth header name | `X-API-KEY` |
| Auth header value | `<api_token>` |
| Postman variable | `tenant_name` = your subdomain |

## Example: List Resources Query
```graphql
{
  resources {
    edges {
      node {
        id
        name
      }
    }
  }
}
```

**Example response structure:**
```json
{
  "data": {
    "resources": {
      "edges": [
        { "node": { "id": "UmVzb3VyY2U6...", "name": "AWS SSH" } }
      ],
      "pageInfo": { "hasNextPage": false }
    }
  }
}
```

## Gotchas
- **API token is shown only once** — copy it before closing the Generate Token dialog; it cannot be retrieved later
- Tokens can be disabled/re-enabled and have editable details after creation
- GraphQL responses only return fields explicitly requested in the query (not full objects by default)
- Pagination: check `pageInfo.hasNextPage` to determine if additional pages exist

## Related Docs
- Twingate API Reference (GraphQL schema)
- Python CLI documentation
- JavaScript CLI documentation
- Postman Collection (downloadable from docs page)