# Twingate Services

## Summary
Services provide programmatic access controls for automated processes (CI/CD pipelines, custom applications) to Twingate Resources. Access is granted via Service Keys rather than Security Policies. Clients run in headless mode to automate connections.

## Key Information
- Any Resource can be assigned to a Service, User, or both
- Security Policies do **not** apply to Services — access controlled solely by valid Service Keys
- One Service Key authorizes access to **all** Resources assigned to that Service
- Service Keys expire after **365 days** by default; unlimited expiration is configurable at creation time only
- Each Service Key is individually API rate-limited — use unique keys per high-traffic system

## Prerequisites
- Admin console access
- Linux or Windows Twingate client (for headless mode execution)
- Resources already defined in Twingate

## Step-by-Step: Create a Service

1. Navigate to **Team > Services** → click **"Create Service Account"**
2. Click **"Generate Key"** to create a Service Key
3. **Save the Service Key immediately** — it is only viewable/copyable at creation time
4. Click **"Add Resource"** to assign one or more Resources to the Service
5. Configure headless client using the key (see Windows or Linux headless guides)

## Service Key Lifecycle

| State | Valid? | Notes |
|-------|--------|-------|
| **Active** | Yes | Default state; expiry set at creation only; name editable |
| **Revoked** | No | Must revoke before delete; cannot be reactivated |
| **Expired** | No | Auto-expires unless created with unlimited expiration |
| **Deleted** | No | Permanent; unrecoverable |

## Gotchas
- **Key is shown only once** — no way to retrieve it after creation; losing it requires generating a new key
- Expiry can **only be configured at creation time** — cannot be modified afterward
- Overprovisioning Service Keys on a single Service Account causes throttling due to per-key rate limiting
- Revoked keys **cannot** be reactivated — deletion is the only next step
- All keys on a Service share Resource access — scope control requires separate Services

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Security Policies documentation