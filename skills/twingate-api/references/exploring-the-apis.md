# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API is GraphQL-based. This page provides video walkthroughs and a Postman collection to help users get started with queries, mutations, and introspection—even without prior GraphQL experience.

## Key Information
- Twingate APIs use **GraphQL** (not REST)
- A **Postman collection template** is provided with pre-built request examples
- Content is split into 3 core videos + 2 bonus introspection guides
- API tokens are required for authentication (generated via Twingate admin)

## Prerequisites
- Postman installed (free)
- Twingate Postman collection imported (download JSON via provided link, import into Postman)
- API token generated from Twingate dashboard

## Step-by-Step (Video Series)

**Part 1 – Getting Started**
1. Generate an API token in Twingate
2. Import and navigate the Postman collection
3. Run basic GraphQL queries

**Part 2 – Nesting**
1. Build more complex queries
2. Use nested query structures to retrieve related data in one request

**Part 3 – Mutations**
1. Construct mutations (write operations)
2. Use variables within queries and mutations

**Bonus 1 & 2 – Introspection**
- Use GraphQL introspection to self-discover available queries and mutations without external docs

## Configuration Values
| Item | Details |
|------|---------|
| API Type | GraphQL |
| Auth | API Token (generated in Twingate admin UI) |
| Tooling | Postman (with Twingate template collection) |

## Gotchas
- GraphQL is less intuitive than REST—query structure must be precise or requests fail silently/return errors
- Must use the Twingate-specific Postman collection; generic GraphQL clients require manual schema setup
- Introspection must be enabled/available on the endpoint to use the bonus discovery methods

## Related Docs
- Twingate API reference (GraphQL schema)
- API Token generation guide
- Postman collection download (linked from this page)