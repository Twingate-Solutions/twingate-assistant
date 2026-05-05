## SCIM Provisioning API

Reference doc for Twingate's SCIM 2.0 API. **Not for self-serve use** -- this exists to support the supported IdP integrations (Okta, Entra ID, OneLogin, JumpCloud, Google Workspace).

### Base URL

```
https://{network}.twingate.com/api/scim/v2/
```

`{network}` = your Twingate subdomain. Example for `autoco.twingate.com`:
```
https://autoco.twingate.com/api/scim/v2/
```

`v2` = SCIM 2.0 (the only supported version).

### Authentication

- **Long-lived bearer token** required on every request
- Header: `Authorization: Bearer <token>`
- Token created and rotated in the Twingate Admin Console
- **Only the most recent token is valid** -- creating a new token immediately invalidates the prior one

Example:
```
GET /Users?count=100
Host: <network>.twingate.com
Accept: application/scim+json
Authorization: Bearer h480dj...s93hd8
```

### User Resource

**Attributes:**

| Twingate User | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Twingate ID | `id` | Yes | Yes |
| Origin ID | `externalId` | Yes | Yes |
| Email | `emails[primary eq true]` | No | No |
| First name | `name.givenName` | No | No |
| Last name | `name.lastName` | No | No |
| Active | `active` | No | No |
| Username | `userName` | Yes | Yes |

**Email handling**: Twingate stores **one** email -- looks for `primary=true` first, then `type="work"`.

**Operations:**
- `GET /Users` -- search/filter users (pagination supported)
- `POST /Users` -- create a user
- `GET /Users/{id}` -- retrieve a user
- `PUT /Users/{id}` -- replace a user
- `PATCH /Users/{id}` -- modify a user
- `DELETE /Users/{id}` -- delete a user (hard delete in Twingate)

`{id}` = the Twingate user ID returned in the SCIM `id` field.

### Group Resource

**Attributes:**

| Twingate Group | SCIM Attribute | Required | Unique |
|---|---|---|---|
| Group name | `displayName` | Yes | No |
| Members | `members` | No | No |
| Twingate ID | `id` | Yes | Yes |

**Operations:**
- `GET /Groups` -- search/filter groups (pagination supported)
- `POST /Groups` -- create a group
- `GET /Groups/{group-id}` -- retrieve a group
- `PUT /Groups/{group-id}` -- replace a group
- `PATCH /Groups/{group-id}` -- modify a group
- `DELETE /Groups/{group-id}` -- delete a group (hard delete in Twingate)

### Content Type

Both supported:
- `application/scim+json` (per RFC-7644 section 8.1)
- `application/json`

### Errors

Error responses follow **RFC-7644 section 3.12** (standard SCIM error format).

### Rate Limits

- **25 requests/second per Twingate account**

### Limitations (Not Supported)

- `/.search` endpoint (POST-based queries) -- RFC-7644 section 3.4.3
- `/Bulk` endpoint -- RFC-7644 section 3.7
- `/Me` endpoint -- RFC-7644 section 3.11
- Sorting on filter queries -- RFC-7644 section 3.4.2.3
- `attributes` and `excludedAttributes` query params -- RFC-7644 sections 3.4.2.5 and 3.9

### Decision Notes

- For supported IdPs: use the dedicated configuration guides (Okta SCIM, Entra ID, OneLogin SCIM, etc.) -- they handle the underlying API for you
- Only use the SCIM API directly for **custom integrations** when no supported IdP fits (rare)
- Token rotation: deliberately the previous token becomes invalid when generating a new one -- always plan a sync window if rotating in production

### Gotchas

- Rotating the SCIM token invalidates the active token immediately -- coordinate with the IdP to update the token without lost sync
- Hard deletes (DELETE) cannot be undone -- prefer `active=false` PATCH for soft deletion if your IdP supports it
- Email handling defaults: only one email is stored; multi-email users may surprise you
- The 25 req/s rate limit applies per Twingate account; bulk operations need careful pacing

### Related Docs

- /docs/identity-providers -- Supported IdP integrations (preferred over direct SCIM use)
- /docs/okta-scim-configuration, /docs/onelogin-configuration-scim -- Per-IdP SCIM setup
- /docs/api-overview -- Twingate Admin GraphQL API (separate from SCIM)
