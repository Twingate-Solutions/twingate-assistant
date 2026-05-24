# SCIM Provisioning API

## Summary
Twingate supports SCIM 2.0 for automated user/group provisioning via identity provider integrations. This API is intended for IdP integrations only, not self-serve use. Bearer token auth is required for all endpoints.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- SCIM version: 2.0
- Supports both `application/scim+json` and `application/json` content types
- Rate limit: **25 requests/second per account**
- Only the most recently generated token is valid

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin console

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Auth header | `Authorization: Bearer <token>` |
| Base URL pattern | `https://{network}.twingate.com/api/scim/v2/` |
| Content-Type | `application/scim+json` or `application/json` |

## User Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|----------------|---------------|----------|--------|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Username | `userName` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |

## Group Attributes

| Twingate Field | SCIM Attribute | Required | Unique |
|----------------|---------------|----------|--------|
| Group name | `displayName` | Yes | No |
| Members | `members` | No | No |
| Twingate ID | `id` | Yes | Yes |

## Supported Endpoints

**Users:** `GET`, `POST /Users` | `GET`, `PUT`, `PATCH`, `DELETE /Users/{id}`

**Groups:** `GET`, `POST /Groups` | `GET`, `PUT`, `PATCH`, `DELETE /Groups/{group-id}`

Both Users and Groups support pagination on list endpoints.

## Gotchas
- Only **one email** is stored; API looks for `primary=true` or `type="work"`
- `{id}` in path must be the Twingate-assigned ID (from SCIM `id` field), not `externalId`
- Token rotation invalidates all previous tokens immediately
- `DELETE /Users/{id}` and `DELETE /Groups/{group-id}` permanently delete the resource in Twingate

## Unsupported Features
- `/.search` (POST-based queries)
- `/Bulk` operations
- `/Me` endpoint
- Sorting on filter queries
- `attributes` and `excludedAttributes` query params

## Related Docs
- [Supported IdP Integrations](https://www.twingate.com/docs/scim-provisioning-api) (see "here" link in source)
- [SCIM Configuration](https://www.twingate.com/docs/scim-provisioning-api)
- RFC-7644 (SCIM protocol specification)