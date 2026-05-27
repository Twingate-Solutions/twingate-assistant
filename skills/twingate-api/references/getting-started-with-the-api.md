# Getting Started with the Twingate API

## Summary
Twingate exposes GraphQL APIs for automating Admin Console actions, accessible directly or via Python/JavaScript CLIs. All API access requires an API key and tenant name. The API follows standard GraphQL conventions with nodes and edges.

## Key Information
- API type: GraphQL
- Endpoint: `https://<tenant_name>.twingate.com/api/graphql/`
- Authentication: `X-API-KEY` header
- CLIs (Python and JavaScript) are wrappers around the same GraphQL API
- Compatible with orchestration platforms: Ansible, Chef, Puppet

## Prerequisites
- Active Twingate tenant
- API Key with appropriate permission level:
  - **Read** — read-only access
  - **Read & Write** — modify objects
  - **Read, Write & Provision** — full provisioning access

## Generating an API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level (Read & Write or Read, Write & Provision for mutations)
4. Copy and store the token immediately — **it cannot be retrieved again after closing the dialog**
5. Tokens can be modified, disabled, or re-enabled after creation

## Configuration Values

| Parameter | Value |
|-----------|-------|
| API endpoint | `https://<tenant>.twingate.com/api/graphql/` |
| Auth header name | `X-API-KEY` |
| Auth header value | `<your_api_token>` |

## Testing the API

**Postman setup:**
1. Create a Collection → Authorization tab → Key: `X-API-KEY`, Value: `<token>`
2. Variables tab → add `tenant_name` variable
3. Import Twingate's [Postman Collection](https://www.twingate.com/docs/getting-started-with-the-api) for pre-built examples

**Altair GraphQL Client setup:**
1. Set URL to `https://<subdomain>.twingate.com/api/graphql/`
2. Add header `X-API-KEY: <token>`
3. Use schema explorer to build queries

**Example: List Resources**
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
- API token is shown **only once** at generation time — store it immediately
- GraphQL responses only return fields explicitly requested in the query
- Pagination: check `pageInfo.hasNextPage` for large result sets
- Use `Read, Write & Provision` (not just `Read & Write`) if provisioning resources programmatically

## Related Docs
- [Twingate API Reference](https://www.twingate.com/docs/api)
- [Python CLI](https://www.twingate.com/docs/python-cli)
- [JavaScript CLI](https://www.twingate.com/docs/javascript-cli)
- [Postman Collection Download](https://www.twingate.com/docs/getting-started-with-the-api)