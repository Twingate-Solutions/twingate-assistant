## Getting Started with the Twingate API

Quickstart for using the Twingate **GraphQL Admin API** -- generate a token, send your first query, understand the response shape.

### Three Automation Paths

| Path | Best For |
|---|---|
| **GraphQL APIs (direct)** | Custom integrations, ad-hoc queries, exploring the schema |
| **Python CLI** | Python-default shops; quick scripts |
| **JavaScript CLI** | JS/TS shops; quick scripts |

All three can be integrated into orchestration platforms (Ansible, Chef, Puppet, etc.).

### Prerequisites

- Twingate **API Token**
- Twingate **Tenant Name** (subdomain in `<tenant>.twingate.com`)

### Generating an API Token

1. Open **Admin Console**
2. **Settings -> API**
3. Click **Generate Token**
4. Choose permissions:
   - **Read** -- queries only
   - **Read & Write** -- modify objects (most use cases)
   - **Read, Write & Provision** -- includes Connector token generation
5. Copy the token immediately -- it's not retrievable later
6. Optionally restrict by IP range

You can disable / re-enable / modify token details after creation, but cannot view the token value again.

### Recommended GraphQL Clients

| Client | Strength |
|---|---|
| **Postman** | Familiar if you know REST APIs; Twingate publishes a Postman collection with example queries |
| **Altair GraphQL Client** | Friendlier for GraphQL-first users; built-in introspection / schema browsing |

### First API Call (Postman Pattern)

1. Create a new **Collection** in Postman
2. **Authorization** tab -> Type: **API Key**
   - Key: `X-API-KEY`
   - Value: paste your Twingate API token
3. **Variables** tab -> add `tenant_name` = your tenant subdomain
4. Add a request to `https://{{tenant_name}}.twingate.com/api/graphql/`
5. Run a basic query (e.g., list Resources)

### First API Call (Altair Pattern)

1. URL: `https://<subdomain>.twingate.com/api/graphql/`
2. Header: `X-API-KEY: <your-token>`
3. Click **QueriesRoot -> Resources -> ADD QUERY**
4. Replace `node` block with:
   ```
   node {
     id
     name
   }
   ```
5. **Run query**

### Understanding GraphQL Response Shape

GraphQL returns a **nested structure** matching your query:

```
{
  "data": {
    "resources": {
      "edges": [
        { "node": { "id": "UmVzb3VyY2U6...", "name": "AWS SSH" } },
        { "node": { "id": "UmVzb3VyY2U6...", "name": "AWS Grafana" } }
      ],
      "pageInfo": {
        "startCursor": "YXJyYXljb25uZWN0aW9uOjA=",
        "hasNextPage": false
      }
    }
  }
}
```

- **`edges`** -- collection wrapper
- **`node`** -- individual object with the fields you requested
- **`pageInfo`** -- pagination cursor for fetching subsequent pages
- The response shape **mirrors the query shape** -- key advantage of GraphQL over REST

### Decision Notes

- For one-off interactive exploration: Postman + Twingate's published collection
- For repeated automation: pick one CLI (Python or JS) and stick with it
- For IaC: skip the API entirely and use the **Terraform provider** -- it wraps the API and adds drift management
- Always restrict API tokens by IP for production use

### Gotchas

- Tokens are **sensitive credentials** -- store in a secret manager, never commit to git
- Token re-display is impossible -- save securely on first generate
- GraphQL learning curve is real if you're coming from REST -- expect a learning period
- Pagination via `pageInfo.hasNextPage` and cursors -- don't assume all results come in one response

### Related Docs

- /docs/api-overview -- API capabilities + endpoint URL + throttling limits
- /docs/exploring-the-apis -- Postman collection + video walkthroughs
- /docs/introduction-to-the-python-cli, /docs/introduction-to-tg-cli-javascript -- CLI wrappers
- /docs/scim-provisioning-api -- Separate SCIM API
- /docs/terraform-getting-started -- IaC alternative
