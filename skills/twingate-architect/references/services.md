# Twingate Services

## Summary
Services provide programmatic access controls for automated processes (CI/CD pipelines, custom applications) to Twingate Resources. Access is granted via Service Keys rather than Security Policies, and clients can run in headless mode to automate connections.

## Key Information
- Any Resource can be assigned to a Service, User, or both
- Security Policies do **not** apply to Services — access is controlled solely by valid Service Keys
- Clients (Linux or Windows) can run in headless mode for automated access
- Service Keys expire after **365 days by default**; unlimited expiration is configurable at creation time only
- Any non-revoked, non-expired Service Key grants access to **all Resources** assigned to that Service

## Service Components
| Component | Description |
|-----------|-------------|
| Service | Container object configured under Team > Services |
| Service Key | Authorization credential; one or more per Service |
| Resources | One or more Twingate Resources assigned to the Service |

## Prerequisites
- Admin access to Twingate Admin console
- Resources already defined in Twingate
- Linux or Windows Twingate client (for headless mode)

## Step-by-Step: Create a Service
1. Navigate to **Team > Services** → select **Create Service Account**
2. Select **Generate Key** to create a Service Key
3. **Save the Service Key immediately** — it is only displayed once
4. Select **Add Resource** to assign Resources to the Service
5. Configure headless client using Windows or Linux headless mode guides

## Service Key Lifecycle

| State | Valid? | Actions Available | Notes |
|-------|--------|-------------------|-------|
| Active | ✅ Yes | Revoke, Edit name | Default state; expiry set at creation only |
| Revoked | ❌ No | Delete | Cannot be reactivated |
| Expired | ❌ No | Delete | Auto-expires unless set to unlimited |
| Deleted | ❌ No | N/A | Permanent, unrecoverable |

## Gotchas
- **Service Key is only shown once** at creation — copy and store it immediately
- **Expiry cannot be changed after creation** — plan expiration at key generation time
- **Overprovisioning Service Keys**: Each key is individually API rate-limited; use a unique Service Key per high-traffic system to avoid throttling
- Revoking a key is required before deletion; revocation is irreversible

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation