# SCIM Provisioning API

## Summary
Twingate supports SCIM 2.0 for automated user provisioning via identity provider integrations. The API provides CRUD operations for Users and Groups. This API is intended for IdP integrations, not direct self-serve use.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- Supports SCIM 2.0 (`v2` in URL path)
- Content types: `application/scim+json` or `application/json`
- Rate limit: **25 requests/second per account**
- Only the **most recently generated** bearer token is valid

## Prerequisites
- Twingate Admin console access to generate bearer token
- Existing IdP integration configured
- Network name (subdomain) for base URL construction

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Auth header | `Authorization: Bearer <token>` |
| Content-Type | `application/scim+json` or `application/json` |
| Rate limit | 25 req/sec |

## User Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Username | `userName` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |

## Group Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Group name | `displayName` | Yes | No |
| Members | `members` | No | No |
| Twingate ID | `id` | Yes | Yes |

## Supported Endpoints
**Users:** `GET /Users`, `POST /Users`, `GET /Users/{id}`, `PUT /Users/{id}`, `PATCH /Users/{id}`, `DELETE /Users/{id}`

**Groups:** `GET /Groups`, `POST /Groups`, `GET /Groups/{id}`, `PUT /Groups/{id}`, `PATCH /Groups/{id}`, `DELETE /Groups/{id}`

Pagination supported on `GET /Users` and `GET /Groups`.

## Gotchas
- Only one email stored; API looks for `primary=true` first, then `type="work"`
- `DELETE /Users/{id}` and `DELETE /Groups/{id}` **permanently delete** in Twingate
- `{id}` path param is the Twingate internal ID (from `id` field in responses), not `externalId`
- Token rotation invalidates all previous tokens immediately
- `lastName` maps to `name.lastName` (not `name.familyName` per strict SCIM spec—verify behavior)

## Unsupported Operations
- `POST /.search` (RFC-7644 §3.4.3)
- `POST /Bulk` (RFC-7644 §3.7)
- `/Me` endpoint
- Sorting on filter queries
- `attributes` / `excludedAttributes` query params

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api) (see "here" link in source)
- RFC-7644 §8.1 (content types), §3.12 (error format), §3.4.2 (filtering)