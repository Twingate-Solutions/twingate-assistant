---
source: https://www.twingate.com/docs/scim-provisioning-api
type: docs
fetched: 2026-08-05
source_version: 0494f174f8ec032bb7bed51e74e828f981b7001ce24d2926aa5868595bf84375
---

# Twingate SCIM Provisioning API

## Summary
Twingate supports SCIM 2.0 for automatic user provisioning via identity provider integrations. The API provides endpoints for managing Users and Groups. This API is intended for IdP integrations, not self-serve use.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- SCIM version: 2.0
- Rate limit: 25 requests/second per account
- Supported content types: `application/scim+json` and `application/json`
- Only the most recently generated bearer token is valid

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin console
- Existing IdP integration configured

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Auth header | `Authorization: Bearer <token>` |
| Base URL pattern | `https://{network}.twingate.com/api/scim/v2/` |
| Content-Type | `application/scim+json` or `application/json` |

## User Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |
| Username | `userName` | Yes | Yes |

## Group Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Group name | `displayName` | Yes | No |
| Members | `members` | No | No |
| Twingate ID | `id` | Yes | Yes |

## User Endpoints
- `GET /Users` — list/filter users (pagination supported)
- `POST /Users` — create user
- `GET /Users/{id}` — get single user
- `PUT /Users/{id}` — replace user
- `PATCH /Users/{id}` — modify user
- `DELETE /Users/{id}` — delete user permanently

## Group Endpoints
- `GET /Groups` — list/filter groups (pagination supported)
- `POST /Groups` — create group
- `GET /Groups/{group-id}` — get single group
- `PUT /Groups/{group-id}` — replace group
- `PATCH /Groups/{group-id}` — modify group
- `DELETE /Groups/{group-id}` — delete group permanently

## Gotchas
- Only one email is stored; lookup priority is `primary=true`, then `type="work"`
- `{id}` in user/group paths is the **Twingate ID** (from `id` field in responses), not `externalId`
- Only the most recent bearer token is valid — regenerating invalidates previous tokens
- `DELETE` on users/groups is **permanent** in Twingate

## Unsupported Features
- `/.search` POST endpoint
- `/Bulk` operations
- `/Me` endpoint
- Sorting on filter queries
- `attributes` and `excludedAttributes` query params

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api)
- RFC-7644 (SCIM protocol specification)