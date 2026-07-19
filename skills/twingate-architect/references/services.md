# Twingate Services

## Summary
Services provide programmatic access control for automated processes (CI/CD pipelines, custom applications) by assigning Resources directly to a Service account authorized via Service Keys. Security Policies do not apply to Services; access is controlled entirely by valid Service Keys.

## Key Information
- Any Twingate Resource can be assigned to a Service, User, or both
- Service Keys authorize access to **all** Resources assigned to that Service
- Linux and Windows clients support headless mode for automated access
- Service Keys expire after **365 days by default**; unlimited expiration is configurable at creation only
- Each Service Key is individually API rate-limited

## Prerequisites
- Admin console access
- Resources already defined in Twingate
- Linux or Windows Twingate client (for headless mode execution)

## Step-by-Step: Create a Service

1. Navigate to **Team > Services** → click **Create Service Account**
2. Click **Generate Key** to create a Service Key
3. **Copy and save the Service Key immediately** — it cannot be viewed again after this step
4. Click **Add Resource** to assign one or more Resources to the Service
5. Configure headless mode on Linux or Windows client using the saved key

## Service Key Lifecycle States

| State | Valid? | Notes |
|-------|--------|-------|
| **Active** | Yes | Default state; expiry only settable at creation |
| **Revoked** | No | Must revoke before delete; cannot be reactivated |
| **Expired** | No | Auto-expires unless set to unlimited |
| **Deleted** | No | Permanent; unrecoverable |

## Gotchas
- **Service Key is only visible once** — save it immediately after generation; no recovery option
- **Expiry cannot be changed after creation** — decide at creation time whether to use unlimited expiration
- **Overprovisioning causes throttling** — each Service Key has its own API rate limit; use one unique Service Key per high-traffic system
- **Security Policies do not apply** — Services bypass policy enforcement; access control relies solely on key validity
- Revoked keys cannot be reactivated — must generate a new key

## Configuration Values
- Default Service Key expiration: **365 days**
- Unlimited expiration: configurable at creation time only

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide