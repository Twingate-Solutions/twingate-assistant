# Exploring the Twingate APIs

## Page Title
Exploring the APIs

## Summary
Twingate's primary API interface is GraphQL, which enables precise data queries but has a steeper learning curve than REST APIs. This page provides video walkthroughs and a Postman collection to help users get started with both queries and mutations.

## Key Information
- Twingate uses **GraphQL APIs** as the official supported interface
- A **Postman collection** (JSON template) is provided with pre-built API request examples
- Content covers: basic queries, nested queries, mutations, and introspection
- Five video walkthroughs available covering beginner to advanced usage

## Prerequisites
- Twingate API Token (generated via the Twingate Admin Console)
- [Postman](https://www.postman.com/) installed (free)
- Twingate Postman collection JSON imported into Postman

## Step-by-Step Setup

1. **Install Postman** if not already installed
2. **Download the Postman collection**: Right-click the provided link → "Save Link As" → save JSON file
3. **Import JSON** into Postman environment
4. **Generate an API Token** in Twingate Admin Console (covered in Part 1 video)
5. Use collection examples to run queries and mutations

## Video Content Structure

| Part | Topic |
|------|-------|
| Part 1 | Generate API token, navigate Postman collection, basic queries |
| Part 2 | Advanced queries, nested query patterns |
| Part 3 | Mutations, variables in queries/mutations |
| Bonus 1 | Discovering queries via introspection |
| Bonus 2 | Discovering mutations via introspection |

## Configuration Values
- **API Token**: Required for all requests; generated from Twingate Admin Console
- **Variables**: Supported in both queries and mutations (covered in Part 3)

## Gotchas
- GraphQL requires more intentional query construction than REST — you must specify exactly which fields to return
- Introspection is the primary method for self-discovering available queries/mutations not documented elsewhere
- All Postman examples depend on the template collection; custom environments need the token configured separately

## Related Docs
- Twingate GraphQL API reference (introspection-based exploration)
- API Token generation (Admin Console)
- Postman collection import documentation