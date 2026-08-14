---
source: https://www.twingate.com/docs/scim-provisioning-api
type: docs
fetched: 2026-08-14
source_version: 241437697866c8479de3a14921c1fe82148b5a91a191aa1d5dd376f361833476
---

# Twingate SCIM Provisioning API

## Summary
Twingate implements SCIM 2.0 for automated user provisioning via identity provider integrations. The API supports standard CRUD operations for Users and Groups. This is not intended for self-serve use—it backs supported IdP integrations only.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- SCIM version: 2.0
- Rate limit: 25 requests/second per account
- Only most recently generated bearer token is valid
- Supports `application/scim+json` and `application/json` content types
- Errors follow RFC-7644 section 3.12

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin console

## Configuration Values

**Authorization Header:**
```
Authorization: Bearer <token>
```

**User Attributes:**

| Twingate Field | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Username | `userName` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |

**Group Attributes:**

| Twingate Field | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Group name | `displayName` | Yes | No |
| Members | `members` | No | No |
| Twingate ID | `id` | Yes | Yes |

## API Endpoints

**Users:**
- `GET /Users` — list/filter (paginated)
- `POST /Users` — create
- `GET /Users/{id}` — retrieve
- `PUT /Users/{id}` — replace
- `PATCH /Users/{id}` — modify
- `DELETE /Users/{id}` — delete (permanent)

**Groups:**
- `GET /Groups` — list/filter (paginated)
- `POST /Groups` — create
- `GET /Groups/{group-id}` — retrieve
- `PUT /Groups/{group-id}` — replace
- `PATCH /Groups/{group-id}` — modify
- `DELETE /Groups/{group-id}` — delete (permanent)

## Gotchas
- `{id}` in user/group endpoints is the Twingate-internal ID returned in the `id` field of responses, not `externalId`
- Only one email is stored: prefers `primary=true`, falls back to `type="work"`
- Only the most recently generated token is valid—regenerating invalidates the previous token
- DELETE operations permanently delete the user/group in Twingate
- `name.lastName` is the SCIM attribute (not standard `name.familyName`)

## Unsupported Features
- `/.search` (POST-based queries)
- `/Bulk` operations
- `/Me` endpoint
- Sorting in filter queries
- `attributes` and `excludedAttributes` query params
- `/ServiceProviderConfig` (listed as "coming soon")

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api) (see "here" link in source)
- RFC-7644 (SCIM protocol specification)