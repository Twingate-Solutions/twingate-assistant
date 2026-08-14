---
source: https://www.twingate.com/docs/getting-started-with-the-api
type: docs
fetched: 2026-08-14
source_version: e92a09e1fbe98f45dc336b3d284c30ceb7b9c53f8b60ef9b7e3bf4d945040b44
---

# Getting Started with the Twingate API

## Summary
Twingate exposes a GraphQL API for automating Admin Console actions, accessible directly or via Python/JavaScript CLIs. All automation methods require an API key and tenant name. The API uses standard GraphQL conventions (nodes, edges) and supports selective field querying.

## Key Information
- API type: GraphQL (not REST)
- Endpoint format: `https://<tenant_name>.twingate.com/api/graphql/`
- Auth header: `X-API-KEY: <token>`
- CLIs (Python, JavaScript) are wrappers around the same GraphQL API
- Response structure uses GraphQL `edges`/`node` pattern
- Supports orchestration integration: Ansible, Chef, Puppet

## Prerequisites
- Active Twingate tenant (tenant name required)
- API key with appropriate permissions:
  - **Read & Write** — modify objects
  - **Read, Write & Provision** — provision resources
- API client: Postman or Altair GraphQL Client (both free)

## Step-by-Step: Generate API Key
1. Open Admin Panel → **Settings** → **API**
2. Click **Generate Token**
3. Select permission level: Read & Write or Read, Write & Provision
4. **Copy token immediately** — cannot be retrieved after closing the dialog
5. Token can be disabled/re-enabled or have details modified later

## Step-by-Step: Test API (Postman)
1. Import [Postman Collection](https://www.twingate.com/docs/getting-started-with-the-api) or create new Collection
2. In Collection → **Authorization** tab: set Key=`X-API-KEY`, Value=`<your token>`
3. In Collection → **Variables** tab: add variable `tenant_name` = your tenant name
4. Create a GET request to `https://{{tenant_name}}.twingate.com/api/graphql/`
5. Send query to retrieve resources

## Step-by-Step: Test API (Altair GraphQL Client)
1. Set URL: `https://<subdomain>.twingate.com/api/graphql/`
2. Add header: `X-API-KEY` = `<your token>`
3. Click **QueriesRoot** → **Resources** → **ADD QUERY**
4. Replace `node` with `node { id name }`
5. Run query

## Configuration Values
| Parameter | Value |
|-----------|-------|
| API Endpoint | `https://<tenant>.twingate.com/api/graphql/` |
| Auth Header | `X-API-KEY` |
| Postman collection variable | `tenant_name` |

## Sample Response Structure
```json
{
  "data": {
    "resources": {
      "edges": [
        { "node": { "id": "...", "name": "...", "isActive": true } }
      ],
      "pageInfo": { "hasNextPage": false }
    }
  }
}
```

## Gotchas
- **API token is shown only once** — copy it before closing the Generate Token dialog
- Token permissions must be **Read & Write** minimum to modify objects; read-only tokens cannot make changes
- GraphQL returns only fields explicitly requested — queries must specify fields
- Pagination: check `pageInfo.hasNextPage` for large result sets

## Related Docs
- Twingate GraphQL API reference
- Python CLI documentation
- JavaScript CLI documentation
- Postman Collection (downloadable from docs page)