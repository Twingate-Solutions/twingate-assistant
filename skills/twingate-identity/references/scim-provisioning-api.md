# Twingate SCIM Provisioning API

## Summary
Twingate supports SCIM 2.0 for automated user provisioning via identity provider integrations. This API enables managing users and groups through standard SCIM endpoints. Not intended for self-serve use—designed for supported IdP integrations.

## Key Information
- Base URL: `https://{network}.twingate.com/api/scim/v2/`
- Supports SCIM 2.0
- Rate limit: 25 requests/second per account
- Only most recently generated bearer token is valid
- Supports both `application/scim+json` and `application/json` content types

## Prerequisites
- Twingate network name
- Bearer token generated from Twingate Admin console

## Configuration Values

**Authorization Header:**
```
Authorization: Bearer {token}
```

## API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/Users` | Search/filter users (paginated) |
| POST | `/Users` | Create user |
| GET | `/Users/{id}` | Retrieve user |
| PUT | `/Users/{id}` | Replace user |
| PATCH | `/Users/{id}` | Modify user |
| DELETE | `/Users/{id}` | Delete user |

**User Attributes:**
| SCIM Attribute | Required | Unique |
|----------------|----------|--------|
| `id` | Yes | Yes |
| `externalId` | Yes | Yes |
| `userName` | Yes | Yes |
| `emails[primary eq true]` | No | No |
| `name.givenName` | No | No |
| `name.lastName` | No | No |
| `active` | No | No |

### Groups
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/Groups` | Search/filter groups (paginated) |
| POST | `/Groups` | Create group |
| GET | `/Groups/{group-id}` | Retrieve group |
| PUT | `/Groups/{group-id}` | Replace group |
| PATCH | `/Groups/{group-id}` | Modify group |
| DELETE | `/Groups/{group-id}` | Delete group |

**Group Attributes:**
| SCIM Attribute | Required | Unique |
|----------------|----------|--------|
| `displayName` | Yes | No |
| `id` | Yes | Yes |
| `members` | No | No |

## Gotchas
- Only one email value stored from multi-valued `emails`; Twingate selects `primary=true` or `type="work"`
- Only the most recently generated token is valid—rotating tokens invalidates previous ones
- `{id}` in user endpoints is Twingate's internal ID (from `id` field), not `externalId`
- `DELETE /Users/{id}` permanently deletes the user in Twingate

## Unsupported Operations
- `/.search` POST endpoint
- `/Bulk` endpoint
- `/Me` endpoint
- Sorting in filter queries
- `attributes` and `excludedAttributes` query params

## Related Docs
- [SCIM Configuration](https://www.twingate.com/docs/scim-configuration)
- [Supported IdP Integrations](https://www.twingate.com/docs/identity-provider-integration)
- RFC-7644 (SCIM Protocol)