# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API is GraphQL-based. This page provides video walkthroughs and a Postman collection to help users get started with querying and mutating Twingate resources via the GraphQL API.

## Key Information
- Twingate's official API is GraphQL (not REST)
- A Postman collection with pre-built request examples is available for download
- Videos cover: token generation, basic queries, nested queries, mutations, and introspection
- GraphQL introspection can be used to self-discover available queries and mutations

## Prerequisites
- Twingate account with API access
- Postman installed (free)
- Twingate Postman collection imported (JSON file downloaded from docs page)
- API token generated from Twingate Admin Console

## Step-by-Step (Getting Started)
1. Download and install Postman
2. Download the Twingate Postman collection JSON (right-click → Save Link As)
3. Import the JSON collection into Postman
4. Generate an API token in the Twingate Admin Console
5. Configure the token in Postman collection variables
6. Use collection examples to run queries/mutations

## Learning Path
| Part | Topic |
|------|-------|
| Part 1 | Generate API token, navigate Postman collection, basic queries |
| Part 2 | Advanced queries, nested queries |
| Part 3 | Mutations, variables in queries/mutations |
| Bonus 1 | Discovering queries via introspection |
| Bonus 2 | Discovering mutations via introspection |

## Configuration Values
- **API Token**: Generated from Twingate Admin Console; used as authentication credential in API requests
- **GraphQL endpoint**: Configured within the Postman collection (specific URL not stated on this page)

## Gotchas
- GraphQL is less intuitive than REST; nesting syntax requires specific attention (covered in Part 2)
- Variables in mutations must be declared correctly (covered in Part 3)
- Introspection is the primary method for discovering undocumented or new API fields

## Related Docs
- Twingate GraphQL API reference (linked from Admin Console)
- API Token generation documentation
- Postman collection (template provided by Twingate)