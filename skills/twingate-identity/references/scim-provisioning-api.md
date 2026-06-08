# Twingate SCIM Provisioning API

## Summary
Twingate implements SCIM 2.0 for automated user/group provisioning via identity providers. This API supports standard CRUD operations on Users and Groups. Not intended for self-serve use—designed for IdP integration (Okta, Azure AD, etc.).

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- SCIM version: 2.0
- Rate limit: 25 requests/second per account
- Supports `application/scim+json` and `application/json` content types
- Only most recently generated bearer token is valid

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin Console

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Auth header | `Authorization: Bearer <token>` |
| Base URL pattern | `https://{network}.twingate.com/api/scim/v2/` |
| Content-Type | `application/scim+json` or `application/json` |

## API Operations

**Users** (`/Users`)
- `GET /Users` — list/filter (paginated)
- `POST /Users` — create
- `GET /Users/{id}` — retrieve
- `PUT /Users/{id}` — replace
- `PATCH /Users/{id}` — modify
- `DELETE /Users/{id}` — delete (permanent)

**Groups** (`/Groups`)
- `GET /Groups` — list/filter (paginated)
- `POST /Groups` — create
- `GET /Groups/{group-id}` — retrieve
- `PUT /Groups/{group-id}` — replace
- `PATCH /Groups/{group-id}` — modify
- `DELETE /Groups/{group-id}` — delete (permanent)

## User Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|----------------|----------------|----------|--------|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |
| Username | `userName` | Yes | Yes |

## Group Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|----------------|----------------|----------|--------|
| Group name | `displayName` | Yes | No |
| Members | `members` | No | No |
| Twingate ID | `id` | Yes | Yes |

## Gotchas
- Only **one email** stored per user—API selects `primary=true` or `type="work"` from multi-value `emails`
- `DELETE` operations are **permanent** for both users and groups
- Only the **most recently generated** token is valid; regenerating invalidates previous tokens
- `{id}` in path refers to Twingate's internal ID (from `id` field in responses), not `externalId`

## Unsupported Features
- `/.search` (POST-based queries)
- `/Bulk` operations
- `/Me` endpoint
- Sorting in filter queries
- `attributes` / `excludedAttributes` query params

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api) (see "here" link in source)
- RFC-7644 (SCIM protocol specification)