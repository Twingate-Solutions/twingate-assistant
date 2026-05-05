## Twingate GraphQL API Schema Reference

The `/docs/api` page is the **full GraphQL schema documentation** for the Twingate Admin API -- introspection-style listing of every query, mutation, type, and field. Very large (60K+ chars).

For practical use:

- **/docs/api-overview** has the conceptual overview, capabilities matrix, and throttling limits
- **/docs/getting-started-with-the-api** walks through token generation + first query
- **/docs/exploring-the-apis** has Postman collection + video walkthroughs
- The hand-maintained schema reference for plugin use is at `skills/twingate-api/references/graphql-schema-reference.md` (kept current outside the auto-update pipeline)

### When to Read This Page Directly

- When you need the **exact field name** or **type** for a specific query/mutation
- When introspecting via Postman / Altair / GraphiQL is unavailable
- When auditing the API surface for what's currently exposed

### Endpoint Recap

```
https://<subdomain>.twingate.com/api/graphql/
```

Header: `X-API-KEY: <token>`

### Capabilities Surface (high level)

| Object | Operations |
|---|---|
| Remote Networks | CRUD |
| Connectors | CRUD + token generation |
| Resources | CRUD |
| Groups | CRUD |
| Service Accounts + Keys | CRUD |
| Devices | Read, archive, unarchive, block, unblock, update trust |
| Security Policies | Read, update, assign |
| Users (incl. Social Users) | Read, invite (social only), update, delete |

### Throttling

- 60 reads / minute per account
- 20 writes / minute per account
- 429 response with `Retry-After` if exceeded

### Decision Notes

- Prefer the **Terraform provider** for IaC (handles retries, drift)
- Prefer one of the **CLIs** (Python, JS) for ad-hoc admin scripts
- Use the raw GraphQL API directly only for custom integrations or edge cases
- Do not introspect schemas in production scripts -- pin to known operations and watch the changelog

### Related Docs

- /docs/api-overview -- Conceptual overview + throttling
- /docs/getting-started-with-the-api -- First-call walkthrough
- /docs/exploring-the-apis -- Postman + videos
- /docs/introduction-to-the-python-cli, /docs/introduction-to-tg-cli-javascript -- CLIs
- /docs/scim-provisioning-api -- Separate SCIM API (not GraphQL)
- /docs/terraform-getting-started -- IaC alternative
