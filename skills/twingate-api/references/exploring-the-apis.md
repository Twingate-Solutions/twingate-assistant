# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API is GraphQL-based, enabling precise queries that return only requested data. The page provides video walkthroughs and a Postman collection to help users get started with the GraphQL API, covering queries, mutations, nesting, and introspection.

## Key Information
- Twingate uses **GraphQL APIs** as its official supported API type
- A **Postman collection** (JSON template) is provided with pre-built examples
- Content is organized into 3 core parts + 2 bonus introspection guides
- Videos cover: token generation, basic queries, nested queries, mutations, and variables

## Prerequisites
- **Postman** installed (free download)
- Twingate **API Token** (generated during Part 1 walkthrough)
- Twingate Postman collection JSON imported into Postman

## Step-by-Step Setup

1. Download and install [Postman](https://www.postman.com/)
2. Right-click the Twingate Postman collection link → "Save Link As" → download JSON
3. Import the JSON file into Postman
4. Generate an API Token (covered in Part 1 video)
5. Use collection examples to run queries and mutations

## Video Content Breakdown

| Part | Topics Covered |
|------|----------------|
| Part 1 | Generate API Token, navigate Postman collection, basic queries |
| Part 2 | Advanced queries, nesting queries |
| Part 3 | Mutations, exploring mutations, variables in queries/mutations |
| Bonus 1 | Discovering new queries via introspection |
| Bonus 2 | Discovering new mutations via introspection |

## Configuration Values
- **API Token**: Required for all API requests; generated from Twingate admin console
- **API Type**: GraphQL (not REST)

## Gotchas
- GraphQL is less intuitive than REST — use the provided Postman collection rather than building requests from scratch
- Must use "Save Link As" to download the Postman JSON (direct click may not work correctly)
- Postman collection examples are the primary learning tool; all videos reference it

## Related Docs
- Twingate GraphQL API reference
- API Token generation documentation
- Postman documentation (external)