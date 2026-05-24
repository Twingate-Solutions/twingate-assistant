# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API is GraphQL-based. This page provides video walkthroughs to onboard developers unfamiliar with GraphQL, covering queries, mutations, nesting, and introspection. A Postman collection is provided as the primary tool for exploration.

## Key Information
- Twingate uses **GraphQL APIs** (not REST)
- Official Postman collection available for download (JSON import)
- All video walkthroughs use the Postman collection
- API supports: queries, nested queries, mutations, variables, and introspection

## Prerequisites
- Postman installed (free)
- Twingate Postman collection imported (JSON file from docs page)
- Twingate API Token generated (covered in Part 1)

## Step-by-Step (Video Series)

| Part | Topic | Covers |
|------|-------|--------|
| Part 1 | Getting Started | Generate API token, navigate Postman collection, basic queries |
| Part 2 | Nesting | Advanced queries, nested query construction |
| Part 3 | Mutations | Create/modify resources, use variables in queries/mutations |
| Bonus 1 | Query Introspection | Discover available queries via introspection |
| Bonus 2 | Mutation Introspection | Discover available mutations via introspection |

## Configuration Values
- **API Token**: Generated via Twingate admin UI (required for all API calls)
- **Postman Collection**: Import JSON from docs page link

## Gotchas
- GraphQL is less intuitive than REST — use the Postman collection to avoid trial-and-error
- Must use introspection to discover undocumented or newer query/mutation fields
- Variables must be explicitly declared in GraphQL mutations (covered in Part 3)

## Related Docs
- Twingate API Token generation (linked in Part 1 content)
- GraphQL official documentation (external reference)
- Postman documentation for collection imports