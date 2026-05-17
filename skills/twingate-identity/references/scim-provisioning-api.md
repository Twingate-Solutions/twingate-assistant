# SCIM Provisioning API

## Summary
Twingate supports SCIM 2.0 for automated user/group provisioning via identity providers. The API provides standard CRUD operations on Users and Groups via a bearer token auth scheme. This API is designed for IdP integrations, not direct self-serve use.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- Supports both `application/scim+json` and `application/json` content types
- Rate limit: **25 requests/second** per account
- Only the **most recently generated** bearer token is valid

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin Console
- Supported identity provider (see IdP integration docs)

## Configuration Values

| Parameter | Value |
|-----------|-------|
| Auth header | `Authorization: Bearer <token>` |
| Base URL pattern | `https://{network}.twingate.com/api/scim/v2/` |
| Content-Type | `application/scim+json` or `application/json` |

## API Endpoints

### Users
| Operation | Endpoint |
|-----------|----------|
| List/Search | `GET /Users` |
| Create | `POST /Users` |
| Get one | `GET /Users/{id}` |
| Replace | `PUT /Users/{id}` |
| Modify | `PATCH /Users/{id}` |
| Delete | `DELETE /Users/{id}` |

**Required User attributes:** `id`, `externalId`, `userName`

### Groups
| Operation | Endpoint |
|-----------|----------|
| List/Search | `GET /Groups` |
| Create | `POST /Groups` |
| Get one | `GET /Groups/{group-id}` |
| Replace | `PUT /Groups/{group-id}` |
| Modify | `PATCH /Groups/{group-id}` |
| Delete | `DELETE /Groups/{group-id}` |

**Required Group attributes:** `displayName`, `id`

## Gotchas
- Token rotation: generating a new token **immediately invalidates** the previous one
- Email handling: only stores one email value; prefers `primary=true`, falls back to `type="work"`
- `{id}` in user endpoints is **Twingate's internal ID** (returned in `id` field of responses), not `externalId`
- `DELETE /Users/{id}` and `DELETE /Groups/{group-id}` **permanently delete** the resource in Twingate

## Unsupported Features
- `/.search` POST endpoint
- `/Bulk` operations
- `/Me` endpoint
- Sort in filter queries
- `attributes` / `excludedAttributes` query params

## Related Docs
- [SCIM Configuration](https://www.twingate.com/docs/scim-configuration)
- [Supported IdP Integrations](https://www.twingate.com/docs/integrations)
- RFC-7644 (SCIM protocol standard)