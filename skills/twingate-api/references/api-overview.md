## Twingate Admin API Overview

Reference for the Twingate **GraphQL Admin API** -- endpoint, capabilities, throttling limits, and recommended clients.

### Endpoint

```
https://<subdomain>.twingate.com/api/graphql/
```

**Authentication**: HTTP header `X-API-KEY: <your-api-token>`

### Capabilities

| Object | Operations |
|---|---|
| **Remote Networks** | Create, read, update, delete |
| **Connectors** | Create, read, update, delete, **generate tokens** |
| **Resources** | Create, read, update, delete |
| **Groups** | Create, read, update, delete |
| **Service Accounts + Keys** | Create, read, update, delete |
| **Policies** | Assign |
| **Devices** | Read, archive, unarchive, block, unblock, update trust status |
| **Security Policies** | Read, update |
| **Users** | Read |
| **Social Users** | Read, invite, update, delete |

### Schema Discovery

The schema is **always up-to-date and self-describing** via GraphQL **introspection**. Tools like **Altair** have built-in introspection viewers.

### Recommended Clients

| Client | Install | Use Case |
|---|---|---|
| **GraphiQL** (Mac) | `brew install --cask graphiql` | Quick GUI exploration |
| **Altair** | Open-source, multi-platform | GraphQL-friendly UI + introspection |
| **gql** (Python) | `pip install gql` | Lightweight Python integration |

### Example Query

```
{
  remoteNetworks(after: null, first: 10) {
    edges {
      node {
        id
        name
      }
    }
    pageInfo {
      startCursor
      hasNextPage
    }
  }
}
```

Returns the first 10 Remote Networks with `id` + `name`, plus pagination info. Use `after: <cursor>` from `pageInfo.startCursor` to paginate.

### Terraform Provider

The **Twingate Terraform provider** wraps this API and adds:
- Declarative state management
- Drift detection
- Idempotent operations
- Built-in retry on `429` rate-limit responses

For IaC use cases, **always prefer the Terraform provider over direct API calls**. See /docs/terraform-getting-started.

**Important**: if `terraform apply` returns 429 errors, **upgrade the Twingate provider to the latest version** -- recent versions handle throttling correctly.

### API Throttling

Default per-account limits:

| Request Type | Limit |
|---|---|
| **Reads** | 60 / minute |
| **Writes** | 20 / minute |

Exceeding the limit returns **HTTP 429** with a `Retry-After` value. Implement backoff in custom integrations.

### Decision Notes

- Use the **Terraform provider** for IaC -- it handles retries automatically
- For ad-hoc admin queries: GraphQL clients (Altair / GraphiQL / Postman) are fastest
- For Python automation: `gql` library + a few helper functions beats the Python CLI for production code
- Keep batch sizes modest -- the 60 reads/min limit is easy to hit with naive pagination

### Gotchas

- Throttling is account-wide -- if you have multiple integrations sharing one token, they compete for the budget
- Schema can evolve -- introspection-based discovery is fine for exploration, but pin to known operations in production code
- 429 responses include `Retry-After` -- respect it; aggressive retries make throttling worse

### Related Docs

- /docs/getting-started-with-the-api -- Token generation + first query walkthrough
- /docs/exploring-the-apis -- Postman collection + videos
- /docs/scim-provisioning-api -- Separate SCIM API for IdP integrations
- /docs/terraform-getting-started -- Recommended IaC path
- /docs/introduction-to-the-python-cli, /docs/introduction-to-tg-cli-javascript -- CLI wrappers
