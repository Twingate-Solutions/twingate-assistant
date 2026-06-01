# Twingate SCIM Provisioning API

## Summary
Twingate supports SCIM 2.0 for automated user provisioning via identity provider integrations. This API is not intended for self-serve use—it backs supported IdP integrations. Provides full CRUD operations for Users and Groups.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- Supports SCIM version 2.0
- Rate limit: 25 requests/second per account
- Content types: `application/scim+json` or `application/json`
- Errors follow RFC-7644 section 3.12 format

## Prerequisites
- Twingate network name
- Long-lived bearer token generated from Twingate Admin console
- Only the most recently generated token is valid

## Configuration Values

**Auth Header:**
```
Authorization: Bearer <token>
```

**User SCIM Attributes:**
| Field | SCIM Attribute | Required | Unique |
|-------|---------------|----------|--------|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Username | `userName` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |

**Group SCIM Attributes:**
| Field | SCIM Attribute | Required | Unique |
|-------|---------------|----------|--------|
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
- `DELETE /Users/{id}` — delete (permanently removes user)

**Groups:**
- `GET /Groups` — list/filter (paginated)
- `POST /Groups` — create
- `GET /Groups/{group-id}` — retrieve
- `PUT /Groups/{group-id}` — replace
- `PATCH /Groups/{group-id}` — modify
- `DELETE /Groups/{group-id}` — delete (permanently removes group)

## Gotchas
- Only one email stored per user; prefers `primary=true` then `type="work"`
- `{id}` in path uses Twingate's internal ID (from SCIM `id` response field), not `externalId`
- Token rotation invalidates previous tokens immediately
- **Unsupported:** `/.search` (POST queries), `/Bulk`, `/Me`, sorting, `attributes`/`excludedAttributes` query params

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api) (see "here" link in source)
- RFC-7644 sections 3.4.2.3, 3.4.2.5, 3.7, 3.9, 3.11, 3.12, 8.1