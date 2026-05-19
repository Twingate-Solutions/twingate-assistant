# Twingate Services

## Summary
Services provide programmatic access controls for automated processes (CI/CD pipelines, custom applications) to Twingate Resources. Access is granted via Service Keys rather than Security Policies. Clients run in headless mode to enable automated Resource access.

## Key Information
- Any Resource can be assigned to a Service, User, or both
- Security Policies do **not** apply to Services — access is controlled by valid Service Keys
- Service Keys authorize access to **all** Resources assigned to that Service
- Default Service Key expiration: **365 days** (unlimited expiration available at creation)
- Each Service Key is individually API rate-limited

## Prerequisites
- Admin console access (Team tab)
- Linux or Windows Twingate client (for headless mode execution)
- Resources already defined in Twingate

## Step-by-Step: Create a Service

1. Navigate to **Team > Services** → click **"Create Service Account"**
2. Click **"Generate Key"** to create a Service Key
3. **Save the Service Key immediately** — it cannot be viewed again after this step
4. Click **"Add Resource"** to assign Resources to the Service
5. Configure headless mode using the [Windows](#) or [Linux](#) guides

## Service Key Lifecycle States

| State | Valid? | Actions Available | Notes |
|-------|--------|-------------------|-------|
| Active | Yes | Revoke, Edit name | Default state; expiry set at creation only |
| Revoked | No | Delete | Cannot be reactivated |
| Expired | No | Delete | Auto-expires unless set to unlimited |
| Deleted | No | N/A | Permanently deleted, unrecoverable |

## Gotchas
- **Service Key is only shown once** at creation — copy and store it securely immediately
- Expiration can **only be set at creation time** — cannot be modified afterward
- Revoking a key is **irreversible** — it cannot be made active again
- **Overprovisioning keys** causes throttling — use one unique Service Key per high-traffic system, not shared keys
- Deleting requires revocation first (Active → Revoked → Deleted)

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Security Policies documentation