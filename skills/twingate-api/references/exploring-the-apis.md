# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API is GraphQL-based, offering precise data retrieval. This page provides video walkthroughs and a Postman collection to help users get started with queries, mutations, and introspection—even without prior GraphQL experience.

## Key Information
- Twingate uses **GraphQL APIs** (not REST)
- Official **Postman collection** available with pre-built request examples
- Videos cover: token generation, basic queries, nested queries, mutations, and introspection
- Introspection can be used to self-discover available queries and mutations

## Prerequisites
- **Postman** installed (free download)
- Twingate **Postman collection** imported (download JSON, import into Postman)
- **API Token** generated from Twingate admin console (covered in Part 1)

## Step-by-Step (Video Series)

| Part | Topic | Covers |
|------|-------|--------|
| Part 1 | Getting Started | Generate API token, navigate Postman collection, basic queries |
| Part 2 | Nesting | Advanced queries, nested query patterns |
| Part 3 | Mutations | Create/update/delete operations, using variables in queries/mutations |
| Bonus 1 | Query Introspection | Self-discover available queries via introspection |
| Bonus 2 | Mutation Introspection | Self-discover available mutations via introspection |

## Configuration Values
- **API Token**: Generated via Twingate admin UI; used to authenticate all API requests
- **Postman collection**: Imported as JSON; contains working examples for all major operations

## Gotchas
- GraphQL requires precise query construction—missing fields or wrong nesting returns errors, not partial data
- Must use **variables** in mutations (covered in Part 3) rather than hardcoding values directly in query strings
- Introspection is the recommended method for discovering undocumented or new API fields

## Related Docs
- Twingate GraphQL API reference (linked via Postman collection examples)
- API Token generation (covered in Part 1 video)