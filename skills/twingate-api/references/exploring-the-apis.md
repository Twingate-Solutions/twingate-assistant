# Exploring the Twingate APIs

## Summary
Twingate uses GraphQL APIs as its primary interface. This page provides video walkthroughs for getting started with the GraphQL API using a provided Postman collection, covering queries, nesting, mutations, and introspection.

## Key Information
- Twingate's official API is GraphQL-based
- A pre-built Postman collection is provided with example requests
- Videos cover: basic queries, nested queries, mutations, and introspection
- API token generation is required before use

## Prerequisites
- Postman installed (free)
- Twingate Postman collection imported (download JSON from docs page, import into Postman)
- API token generated from Twingate admin console

## Learning Path (Video Series)

| Part | Topic |
|------|-------|
| Part 1 | Generate API token, navigate Postman collection, basic queries |
| Part 2 | Advanced queries, nested queries |
| Part 3 | Mutations, variables in queries/mutations |
| Bonus 1 | Discovering queries via introspection |
| Bonus 2 | Discovering mutations via introspection |

## Configuration Values
- **API Token**: Generated via Twingate admin UI; used to authenticate all API requests
- **Endpoint**: Standard Twingate GraphQL endpoint (configured in Postman collection)

## Gotchas
- GraphQL is less intuitive than REST; use the Postman collection as a starting reference rather than building requests from scratch
- Introspection is the primary method for discovering available queries/mutations not explicitly documented
- Variables in mutations (Part 3) are a separate concept from query parameters—review before building automation

## Related Docs
- Twingate GraphQL API reference
- API token management
- Postman collection (linked on the docs page)