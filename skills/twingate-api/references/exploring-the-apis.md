## Exploring the Twingate APIs (GraphQL)

Twingate's APIs are **GraphQL-based**, not REST. This page is a video-walkthrough hub for getting started with the GraphQL Admin API using Postman.

### Key Concept: GraphQL vs REST

- **GraphQL strength**: clients craft specific queries, get back exactly the fields they need -- no over-fetching
- **GraphQL friction**: more complex to discover and learn than REST endpoints -- requires understanding query/mutation/introspection patterns

### Postman Collection

Twingate maintains a **template Postman collection** with example queries + mutations:
- Download Postman (free) if you don't have it
- Right-click the linked collection -> Save Link As -> import the JSON into Postman
- Collection contains many request examples covering common operations

### Video Walkthrough Series

| Part | Topic |
|---|---|
| **Part 1: Getting Started** | Generate API token, navigate the Postman collection, explore available Queries |
| **Part 2: Nesting** | Advanced queries; figuring out how to nest sub-queries |
| **Part 3: Mutations** | Working with mutations; using variables in queries and mutations |
| **Bonus 1: Introspection (Queries)** | Discover new queries via GraphQL introspection |
| **Bonus 2: Introspection (Mutations)** | Discover new mutations via introspection |

### Getting Started Sequence

1. **Generate API token** in Twingate Admin Console (Settings -> API)
   - Choose permissions: Read, Read/Write, or Read/Write/Provision
   - Optionally restrict by IP range
2. **Import Postman collection**
3. **Authenticate Postman**: paste API token into the collection's environment variables (typically `X-API-KEY` header)
4. **Run example queries** to confirm connectivity
5. **Explore introspection** to discover other operations

### Decision Notes

- For **interactive exploration**: Postman + introspection is the fastest path
- For **production automation**: prefer the Twingate **Terraform provider** (built on this same API) or one of the published CLI tools (Python, JavaScript)
- For **quick scripts**: the Python or JavaScript CLI wraps common operations -- avoids reinventing GraphQL queries
- **Always restrict API tokens by IP range** for production use

### Gotchas

- GraphQL learning curve is real -- expect to spend time on the intro videos before being productive
- Introspection lets you discover the schema, but the schema can change between Twingate versions -- pin to known operations rather than dynamically introspecting in production scripts
- Postman collection is a snapshot -- check for updated versions periodically

### Related Docs

- /docs/api -- GraphQL API base reference
- /docs/api-overview -- API overview / use cases
- /docs/getting-started-with-the-api -- API token generation walkthrough
- /docs/introduction-to-the-python-cli, /docs/introduction-to-tg-cli-javascript -- CLI wrappers (Python, JS)
- /docs/scim-provisioning-api -- Separate SCIM API (not GraphQL)
- /docs/terraform-getting-started -- Terraform provider (recommended for IaC use cases)
