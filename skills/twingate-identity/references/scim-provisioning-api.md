# Twingate SCIM Provisioning API

## Summary
Twingate supports SCIM 2.0 for automatic user provisioning with identity providers. The API provides standard CRUD operations for Users and Groups. Intended for use with supported IdP integrations, not direct self-serve implementation.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- SCIM version: 2.0
- Rate limit: 25 requests/second per account
- Only most recently generated bearer token is valid
- Supports `application/scim+json` and `application/json` content types
- Errors follow RFC-7644 section 3.12 format

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin console
- Supported identity provider integration

## Configuration Values

**Authorization Header:**
```
Authorization: Bearer <token>
```

**User SCIM Attributes:**
| Field | SCIM Attribute | Required | Unique |
|-------|---------------|----------|--------|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |
| Username | `userName` | Yes | Yes |

**Group SCIM Attributes:**
| Field | SCIM Attribute | Required | Unique |
|-------|---------------|----------|--------|
| Group name | `displayName` | Yes | No |
| Members | `members` | No | No |
| Twingate ID | `id` | Yes | Yes |

## API Endpoints

**Users:**
- `GET /Users` — list/filter (pagination supported)
- `POST /Users` — create
- `GET /Users/{id}` — retrieve
- `PUT /Users/{id}` — replace
- `PATCH /Users/{id}` — modify
- `DELETE /Users/{id}` — delete (permanent)

**Groups:**
- `GET /Groups` — list/filter (pagination supported)
- `POST /Groups` — create
- `GET /Groups/{group-id}` — retrieve
- `PUT /Groups/{group-id}` — replace
- `PATCH /Groups/{group-id}` — modify
- `DELETE /Groups/{group-id}` — delete (permanent)

## Gotchas
- Only **one email** is stored per user — API picks `primary=true` or `type="work"` from multi-value `emails` attribute
- Token rotation invalidates previous tokens immediately (only latest token valid)
- `DELETE` on users/groups is **permanent** in Twingate
- `{id}` path parameter uses **Twingate's internal ID** (from `id` field in response), not `externalId`

## Unsupported Features
- `/.search` POST endpoint
- `/Bulk` operations
- `/Me` endpoint
- Sort parameters in filter queries
- `attributes` and `excludedAttributes` query params

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api) (linked in page)
- [SCIM Configuration](https://www.twingate.com/docs/scim-provisioning-api)
- RFC-7644 (SCIM protocol specification)