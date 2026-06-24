# Twingate SCIM Provisioning API

## Summary
Twingate implements SCIM 2.0 for automated user provisioning via identity provider integrations. The API supports standard CRUD operations on Users and Groups. This API is intended for use with supported IdP integrations, not direct self-serve implementation.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- SCIM version: 2.0
- Rate limit: 25 requests/second per account
- Supports `application/scim+json` and `application/json` content types
- Errors follow RFC-7644 section 3.12

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin console (only most recently generated token is valid)

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Auth header | `Authorization: Bearer <token>` |
| Content-Type | `application/scim+json` or `application/json` |
| Base URL pattern | `https://{network}.twingate.com/api/scim/v2/` |

## User Attributes

| SCIM Attribute | Required | Unique |
|----------------|----------|--------|
| `id` | Yes | Yes |
| `externalId` | Yes | Yes |
| `userName` | Yes | Yes |
| `emails[primary eq true]` | No | No |
| `name.givenName` | No | No |
| `name.lastName` | No | No |
| `active` | No | No |

## Group Attributes

| SCIM Attribute | Required | Unique |
|----------------|----------|--------|
| `displayName` | Yes | No |
| `id` | Yes | Yes |
| `members` | No | No |

## Endpoints

**Users:**
- `GET /Users` — list/filter (paginated)
- `POST /Users` — create
- `GET /Users/{id}` — retrieve
- `PUT /Users/{id}` — replace
- `PATCH /Users/{id}` — modify
- `DELETE /Users/{id}` — delete permanently

**Groups:**
- `GET /Groups` — list/filter (paginated)
- `POST /Groups` — create
- `GET /Groups/{group-id}` — retrieve
- `PUT /Groups/{group-id}` — replace
- `PATCH /Groups/{group-id}` — modify
- `DELETE /Groups/{group-id}` — delete permanently

## Gotchas
- Only the **most recently generated** bearer token is valid; generating a new token invalidates the previous one
- Email: only one email stored; priority is `primary=true`, fallback is `type="work"`
- `{id}` in path must be the Twingate-assigned ID (returned in SCIM `id` field), not `externalId`
- `DELETE` on users/groups is **permanent** deletion in Twingate

## Unsupported Operations
- `POST /.search` (RFC-7644 §3.4.3)
- `/Bulk` endpoint (RFC-7644 §3.7)
- `/Me` endpoint (RFC-7644 §3.11)
- Sorting in filter queries (RFC-7644 §3.4.2.3)
- `attributes` and `excludedAttributes` query params

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api) (see "here" link in original)
- RFC-7644 (SCIM Protocol specification)