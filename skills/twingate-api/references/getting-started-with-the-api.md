# Getting Started with the Twingate API

## Summary
Twingate provides GraphQL APIs and Python/JavaScript CLIs for automating Admin Console actions. All methods require an API key and tenant name. The API follows GraphQL conventions where responses return objects as `nodes` within `edges` collections.

## Key Information
- API type: GraphQL
- Base URL: `https://<tenant_name>.twingate.com/api/graphql/`
- CLIs (Python and JavaScript) are wrappers over the same GraphQL API
- Compatible with orchestration platforms: Ansible, Chef, Puppet, etc.
- Recommended API clients: Postman or Altair GraphQL Client

## Prerequisites
- Active Twingate tenant
- API key with appropriate permissions (Read & Write or Read, Write & Provision)

## Generating an API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level:
   - **Read & Write** – for read/modify operations
   - **Read, Write & Provision** – for provisioning operations
4. Copy and store the token immediately (cannot be retrieved after closing the dialog)

## Configuration Values

| Parameter | Value |
|-----------|-------|
| API Endpoint | `https://<tenant_name>.twingate.com/api/graphql/` |
| Auth Header Name | `X-API-KEY` |
| Auth Header Value | `<your_api_token>` |
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
- **API token is shown only once** – copy it before closing the Generate Token dialog; it cannot be retrieved afterward
- GraphQL is field-selective – only request the fields you need; server only returns specified fields
- Pagination: check `pageInfo.hasNextPage` to determine if additional pages exist
- Postman Collection is available for download with pre-built example requests

## Related Docs
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [Python CLI](https://www.twingate.com/docs/python-cli)
- [JavaScript CLI](https://www.twingate.com/docs/javascript-cli)
- [Postman Collection](https://www.twingate.com/docs/postman-collection) (downloadable)