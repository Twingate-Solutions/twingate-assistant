# Twingate Services

## Summary
Services provide programmatic access controls for automated processes (CI/CD pipelines, custom applications) to Twingate Resources. Access is granted via Service Keys rather than Security Policies. Clients run in headless mode to automate connections.

## Key Information
- Any Resource can be assigned to a Service, User, or both
- Security Policies do **not** apply to Services — access controlled by valid Service Keys
- Service Keys authorize access to **all** Resources assigned to a Service
- Service Keys expire after **365 days** by default; unlimited expiration is configurable at creation
- Each Service Key is individually API rate-limited

## Prerequisites
- Admin access to Twingate Admin console
- Resources already defined in Twingate
- Linux or Windows Twingate client for headless mode execution

## Step-by-Step: Create a New Service

1. Navigate to **Team > Services** → click **"Create Service Account"**
2. Click **"Generate Key"** to create a Service Key
3. **Save the Service Key immediately** — it cannot be viewed again after this step
4. Click **"Add Resource"** to assign one or more Resources to the Service
5. Configure headless mode on Linux or Windows client to use the Service Key

## Service Key Lifecycle States

| State | Valid? | Actions Available | Notes |
|-------|--------|-------------------|-------|
| Active | ✅ Yes | Revoke, Edit name | Default state; expiry set at creation only |
| Revoked | ❌ No | Delete | Cannot be reactivated |
| Expired | ❌ No | Delete | Auto-expires unless set to unlimited |
| Deleted | ❌ No | None | Permanent, unrecoverable |

## Configuration Values
- **Default expiration**: 365 days
- **Unlimited expiration**: Available, set at creation time only
- **Expiry modification**: Only configurable at creation — cannot be changed afterward

## Gotchas
- **Service Key is shown only once** at creation — must be saved immediately
- Expiration can **only be set at creation time**; cannot be modified later
- Revoked keys **cannot be reactivated** — must create a new key
- **Overprovisioning keys causes throttling** — use one unique Service Key per high-traffic system (each key has individual API rate limits)
- Resources must be explicitly assigned to a Service; no inheritance from groups/policies

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Team administration / Security Policies