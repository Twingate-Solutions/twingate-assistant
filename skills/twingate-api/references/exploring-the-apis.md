---
source: https://www.twingate.com/docs/exploring-the-apis
type: docs
fetched: 2026-11-13
source_version: 203e794d0fe5c35b5ccb3b93e1432daf778a94e870446359dd2b086e552fc827
trust: official
---

# Page Title
Exploring the APIs (Twingate Docs)

## Summary
This page introduces Twingate's official GraphQL APIs and points to a series of video walkthroughs that use a template Postman collection. It covers generating an API token, writing queries, nesting, mutations, variables, and using introspection to discover queries and mutations. The page itself contains almost no written procedures; the content lives in the embedded videos.

## Key Information
- Twingate's official APIs are **GraphQL** APIs.
- GraphQL lets you request only the fields you need, but is less intuitive than typical REST APIs.
- All walkthroughs use a template **Postman collection** (JSON file) containing many example requests.
- Video series:
  1. **Part 1**: Generate an API token, navigate the Postman collection, explore available queries.
  2. **Part 2**: Advanced queries and nesting queries.
  3. **Part 3**: Mutations, exploring mutations, and using variables in queries and mutations.
  4. **Bonus 1**: Discover new queries using introspection.
  5. **Bonus 2**: Discover new mutations using introspection.

## Prerequisites
- Postman (free) installed.
- The Twingate template Postman collection JSON, downloaded from the link on the docs page (right-click, "Save Link As") and imported into Postman.
- A Twingate API token (generation is shown in Part 1).

## Step-by-Step (as implied by the page)
1. Install Postman.
2. Download and import the Twingate Postman collection.
3. Generate an API token in Twingate (see Part 1 video).
4. Run the example queries from the collection.
5. Progress to nested queries, then mutations with variables.
6. Use GraphQL introspection to discover schema elements beyond the examples.

## Configuration Values
- None are specified in the page text. The API token and endpoint configuration are demonstrated in the videos and in the Postman collection, not listed on this page.

## Gotchas
- The page text does not state the API endpoint URL or token scopes. Check the Postman collection or the Twingate API docs for these.
- Most instructional content is in embedded YouTube videos, so it is not available as text.
- GraphQL has a learning curve compared with REST, so expect to rely on introspection and the example collection.

## Related Docs
- Twingate API overview and API token generation docs (see the Twingate docs site).
- Twingate GraphQL API reference (schema, queries, mutations).
- Postman collection download link (on the source page).

Source: https://www.twingate.com/docs/exploring-the-apis