# Twingate Services

## Summary
Services provide programmatic access controls for automated processes (CI/CD pipelines, custom applications) using Service Keys instead of Security Policies. Any Twingate Resource can be assigned to a Service, enabling zero-trust access for non-human identities.

## Key Information
- Services live under **Team > Services** in the Admin console
- Security Policies do **not** apply to Services — access is controlled by valid Service Keys only
- Any non-revoked, non-expired Service Key grants access to **all Resources** assigned to that Service
- Service Keys default to 365-day expiration; unlimited expiration is configurable at creation time only
- Clients run in **headless mode** (Linux or Windows) to automate Resource access

## Prerequisites
- Admin access to Twingate Admin console
- Resources already defined in Twingate
- Linux or Windows Twingate client for headless mode execution

## Step-by-Step: Create a Service

1. Navigate to **Team > Services** → click **Create Service Account**
2. Click **Generate Key** to create a Service Key
3. **Save the Service Key immediately** — it cannot be retrieved again after this step
4. Click **Add Resource** to assign one or more Resources to the Service
5. Configure headless mode client per [Windows](#) or [Linux](#) guides

## Configuration Values
| Parameter | Details |
|-----------|---------|
| Service Key expiration | Set at creation only; default 365 days; unlimited allowed |
| Headless mode | Linux client or Windows client |

## Service Key Lifecycle States

| State | Valid? | Actions Available | Notes |
|-------|--------|-------------------|-------|
| Active | ✅ Yes | Revoke, Edit name | Default state |
| Revoked | ❌ No | Delete | Cannot be reactivated |
| Expired | ❌ No | Delete | Auto-expires unless unlimited |
| Deleted | ❌ No | None | Permanent, unrecoverable |

## Gotchas
- **Service Key is shown only once** at creation — no recovery if lost; must generate a new key
- **Expiration cannot be changed** after creation
- **Must revoke before delete** — skipping revocation is not allowed
- **Rate limiting per key**: Each Service Key is individually API rate-limited; high-traffic systems should use a **unique Service Key per system** to avoid throttling
- One Service Key grants access to **all** Resources on that Service — scope Resources carefully to avoid overprivileged access

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Security Policies documentation