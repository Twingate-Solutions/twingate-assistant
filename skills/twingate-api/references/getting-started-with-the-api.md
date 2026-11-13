---
source: https://www.twingate.com/docs/getting-started-with-the-api
type: docs
fetched: 2026-11-13
source_version: 303ee1ec0d6316ea2d031ae7a3c20d834b5323f42ffa221a72992b770f4cf4e1
trust: official
---

# Getting Started with the API

## Summary
Twingate offers a GraphQL API plus Python and JavaScript CLIs (which wrap the API) for automating Admin Console tasks. All methods require an API token and the network subdomain. They can be used standalone or inside orchestration tools (Ansible, Chef, Puppet). The page walks through token creation and a first query listing Resources via Postman or Altair.

## Key Information
- Automation options: GraphQL API, Python CLI, JavaScript CLI.
- GraphQL endpoint: `https://<subdomain>.twingate.com/api/graphql/`
- Authentication: HTTP header `X-API-KEY: <token>`.
- Requests are `POST` with a GraphQL body.
- GraphQL responses nest objects as `node` inside `edges`. The response shape mirrors the fields requested in the query.
- Pagination uses `first: N` plus `pageInfo { startCursor hasNextPage }`.
- Recommended test clients: Postman (a downloadable Twingate Postman Collection with example requests is available) and Altair GraphQL Client (easier if new to GraphQL/REST).

## Prerequisites
- A Twingate network (sign up at twingate.com).
- Network subdomain (e.g., `acme` for `acme.twingate.com`).
- A Twingate API token.

## Step-by-Step

**Generate a token**
1. Admin Console → Settings → API (left menu).
2. Click Generate Token.
3. Choose permissions: "Read & Write" or "Read, Write & Provision" if you will modify objects; otherwise read-only suffices.
4. Copy and store the token securely.

**Query Resources in Postman**
1. Create a Collection → Authorization tab → Type: API Key, Key: `X-API-KEY`, Value: token, Add to: Header.
2. Collection Variables tab → add `tenant_name` = your subdomain.
3. Add a request: method `POST`, URL `https://{{tenant_name}}.twingate.com/api/graphql/`.
4. Body tab → GraphQL, enter:
```graphql
{
  resources(first: 10) {
    edges { node { id name createdAt updatedAt isActive } }
    pageInfo { startCursor hasNextPage }
  }
}
```
5. Click Send.

**Query in Altair**
1. Set URL to `https://<subdomain>.twingate.com/api/graphql/`.
2. Add header `X-API-KEY` with the token.
3. Click QueriesRoot → Resources → ADD QUERY.
4. Replace the highlighted `node` with `node { id name }`. No red highlights means the query matches the schema.
5. Run the query.

## Configuration Values
| Name | Value |
|---|---|
| Header | `X-API-KEY` |
| Postman variable | `tenant_name` (subdomain) |
| Endpoint | `https://<subdomain>.twingate.com/api/graphql/` |
| Token scopes | Read & Write; Read, Write & Provision |

## Gotchas
- The token cannot be retrieved after closing the Generate Token window. Copy it immediately.
- Tokens can later be edited, disabled, or re-enabled.
- Read-only tokens cannot modify objects. Select a write scope when using the CLIs or API for changes.
- The URL must include the trailing slash (`/api/graphql/`) as shown.
- Use the subdomain only, not the full domain, in `tenant_name`.
- Results are paginated. Check `hasNextPage` for more data.

## Related Docs
- Twingate API reference (GraphQL)
- Python CLI and JavaScript CLI documentation
- Twingate Postman Collection