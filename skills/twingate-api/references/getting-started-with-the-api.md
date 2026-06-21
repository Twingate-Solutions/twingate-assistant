# Getting Started with the Twingate API

## Summary
Twingate provides GraphQL APIs and Python/JavaScript CLIs for automating Admin Console actions. All automation methods require an API key and tenant name. The API follows GraphQL conventions where objects are returned as `nodes` within `edges`.

## Key Information
- API endpoint: `https://<tenant_name>.twingate.com/api/graphql/`
- Authentication header: `X-API-KEY: <token>`
- CLIs are wrappers around the GraphQL API
- Compatible with orchestration platforms (Ansible, Chef, Puppet)
- Postman collection available for download with pre-built examples

## Prerequisites
- Active Twingate tenant
- API key with appropriate permissions:
  - **Read & Write** — for querying and modifying objects
  - **Read, Write & Provision** — for provisioning operations
- API client (Postman or Altair GraphQL Client)

## Generating an API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level (Read & Write or Read, Write & Provision)
4. Copy and store token immediately — cannot be retrieved after closing the dialog
5. Tokens can later be modified, disabled, or re-enabled

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
- **Token is shown only once** — copy immediately before closing the Generate Token dialog; no way to retrieve it afterward
- GraphQL responses only return fields explicitly requested in the query (by design)
- Results are paginated; check `pageInfo.hasNextPage` for additional pages
- Replace `subdomain` placeholder in all URLs with actual tenant name

## Related Docs
- Twingate API Reference
- Python CLI documentation
- JavaScript CLI documentation
- Postman Collection (downloadable from docs page)