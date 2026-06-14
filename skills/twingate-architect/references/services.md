# Twingate Services

## Summary
Services provide programmatic, centrally-controlled access for automated processes (CI/CD pipelines, custom apps). Access is granted via Service Keys rather than Security Policies. Resources can be assigned to Services, Users, or both.

## Key Information
- Services are found under **Team > Services** in the Admin console
- Service Keys authorize access to **all** Resources assigned to a Service
- Security Policies do **not** apply to Services — only valid Service Keys control access
- Clients run in **headless mode** (Linux or Windows) to automate connections
- Service Keys expire after **365 days** by default; unlimited expiration is configurable at creation time only

## Service Components
| Component | Description |
|-----------|-------------|
| Service | Container object for configuration |
| Service Key(s) | Auth tokens; one or more per Service |
| Resource(s) | Any Twingate Resource assigned to the Service |

## Prerequisites
- Admin access to Twingate Admin console
- Resources already defined in Twingate
- Linux or Windows Twingate client for headless mode

## Step-by-Step: Create a Service

1. Navigate to **Team > Services** → click **Create Service Account**
2. Click **Generate Key** to create a Service Key
3. **Copy and save the Service Key immediately** — it cannot be viewed again after this step
4. Click **Add Resource** to assign Resources to the Service
5. Configure headless mode on Linux or Windows client

## Service Key Lifecycle

| State | Valid? | Notes |
|-------|--------|-------|
| Active | ✅ Yes | Default state; expiry only settable at creation |
| Revoked | ❌ No | Must revoke before delete; cannot reactivate |
| Expired | ❌ No | Auto-expires unless unlimited expiration set |
| Deleted | ❌ No | Permanent; unrecoverable |

## Gotchas
- **Service Key is only shown once** at creation — store it securely immediately
- **Expiry cannot be changed after creation** — plan expiration policy upfront
- **Overprovision warning**: Each Service Key is individually API rate-limited; use a **unique Service Key per high-traffic system** to avoid throttling
- Revoking a key is required before deletion; revoked keys cannot be reactivated
- One Service Key grants access to **all** Resources on that Service — scope Resources carefully

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Security Policies documentation