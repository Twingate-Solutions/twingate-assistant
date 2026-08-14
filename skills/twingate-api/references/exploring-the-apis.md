---
source: https://www.twingate.com/docs/exploring-the-apis
type: docs
fetched: 2026-08-14
source_version: a498eaa725f011fad82907ec7b45c7e749a0cb3a21622dcb1e55341e8113e277
---

# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API is GraphQL-based, allowing precise data queries without over-fetching. This page provides video walkthroughs and a Postman collection to help users get started with the GraphQL API, covering queries, mutations, nesting, and introspection.

## Key Information
- Twingate officially supports **GraphQL APIs**
- A **Postman collection** (JSON template) is provided with pre-built API request examples
- Content is structured across 3 core parts + 2 bonus introspection guides
- All video walkthroughs use the Postman collection as the demo environment

## Prerequisites
- A Twingate account with API access
- [Postman](https://www.postman.com/) installed (free)
- Twingate Postman collection imported (download JSON from docs page, import into Postman)
- An **API Token** generated from Twingate admin console

## Step-by-Step Learning Path

**Part 1 – Getting Started**
1. Generate an API Token in Twingate admin
2. Import Postman collection
3. Navigate available queries in the collection

**Part 2 – Nesting**
1. Build advanced queries
2. Nest related queries together to retrieve linked data in one call

**Part 3 – Mutations**
1. Construct mutation requests (create/update/delete operations)
2. Use variables within queries and mutations for reusability

**Bonus 1 – Query Introspection**
- Use GraphQL introspection to self-discover available queries

**Bonus 2 – Mutation Introspection**
- Use GraphQL introspection to self-discover available mutations

## Configuration Values
- **API Token**: Generated in Twingate admin UI; used as Bearer token in request headers
- **Postman Collection**: JSON file imported into Postman (link on docs page)

## Gotchas
- GraphQL is less intuitive than REST; start with the Postman collection before writing raw queries
- Must use introspection to discover undocumented or new API fields — no static full schema reference provided on this page
- Variables in mutations must be declared in the query definition and passed separately in the Postman variables panel

## Related Docs
- Twingate GraphQL API reference (separate schema/introspection)
- API Token generation guide
- Postman import documentation