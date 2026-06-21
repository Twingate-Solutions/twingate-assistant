# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API is GraphQL-based. This page provides video walkthroughs for getting started with the GraphQL API using Postman, covering basic queries through mutations and introspection.

## Key Information
- Twingate uses **GraphQL APIs** as its official supported API format
- A **Postman collection template** is provided with pre-built example requests
- Content is structured across 3 core videos + 2 bonus introspection guides

## Prerequisites
- **Postman** installed (free download)
- Twingate **Postman collection** imported (download JSON via "Save Link As" from docs page)
- Twingate **API Token** (generated during Part 1)

## Video Content Breakdown

| Part | Topics Covered |
|------|---------------|
| Part 1 | Generate API Token, navigate Postman collection, basic Queries |
| Part 2 | Advanced Queries, nested Queries |
| Part 3 | Mutations, Variables in Queries/Mutations |
| Bonus 1 | Discovering Queries via Introspection |
| Bonus 2 | Discovering Mutations via Introspection |

## Step-by-Step (Getting Started)
1. Install Postman
2. Download Twingate Postman collection JSON from docs page
3. Import collection into Postman
4. Generate an API Token (covered in Part 1 video)
5. Configure token in Postman collection
6. Execute example requests from collection

## Configuration Values
- **API Token**: Required for all requests; generated from Twingate Admin Console
- **API Type**: GraphQL (not REST)

## Gotchas
- GraphQL is more complex and less intuitive than REST APIs — use the Postman collection to avoid manually constructing queries
- Must use "Save Link As" to download the Postman collection JSON (direct click may not work)
- Introspection is the method for self-discovering available queries/mutations not explicitly documented

## Related Docs
- Twingate GraphQL API reference
- API Token generation (Admin Console)
- Postman documentation (external)