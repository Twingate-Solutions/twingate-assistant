# Exploring the Twingate APIs

## Summary
Twingate's primary API is GraphQL-based. This page provides video walkthroughs for getting started with the GraphQL API using Postman, covering queries, mutations, nesting, and introspection.

## Key Information
- Twingate uses **GraphQL APIs** (not REST)
- Official **Postman collection** available with pre-built request examples
- Videos cover: token generation, basic queries, nested queries, mutations, and introspection
- GraphQL allows precise data retrieval without over-fetching

## Prerequisites
- **Postman** installed (free): [postman.com](https://postman.com)
- Twingate **API Token** (generated via Twingate Admin Console)
- Twingate **Postman Collection** JSON file imported into Postman

## Step-by-Step Setup
1. Download and install Postman
2. Right-click the Postman collection link on the docs page → "Save Link As" → save JSON
3. Import JSON collection into Postman
4. Generate an API Token from Twingate Admin Console
5. Configure token in Postman collection environment/headers

## Learning Path (Video Series)
| Part | Topics |
|------|--------|
| Part 1 | Generate API token, navigate Postman collection, basic queries |
| Part 2 | Advanced queries, nested queries |
| Part 3 | Mutations, variables in queries/mutations |
| Bonus 1 | Discovering queries via introspection |
| Bonus 2 | Discovering mutations via introspection |

## Configuration Values
- API authentication requires an **API Token** passed in request headers
- GraphQL endpoint: not explicitly listed on this page — check Twingate API reference docs

## Gotchas
- GraphQL is less intuitive than REST; use the Postman collection as a starting point
- Introspection is available for self-discovery of schema (queries and mutations)
- All examples in videos use the provided Postman collection — import it before following along

## Related Docs
- Twingate GraphQL API Reference (introspection-based schema exploration)
- API Token generation (Twingate Admin Console)
- Postman collection JSON (linked from the docs page)