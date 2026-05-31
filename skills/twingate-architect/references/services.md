# Twingate Services

## Summary
Services provide programmatic, centrally-controlled access for automated processes (CI/CD pipelines, custom applications). Access is granted via Service Keys rather than Security Policies, and clients can run in headless mode to automate Resource connections.

## Key Information
- Any Twingate Resource can be assigned to a Service, a User, or both
- Security Policies do **not** apply to Services — access is controlled solely by valid Service Keys
- Service Keys expire after **365 days by default**; unlimited expiration can be set at creation time only
- Each Service Key is individually API rate-limited — use unique keys per high-traffic system to avoid throttling
- Clients supported in headless mode: Linux and Windows

## Service Components
| Component | Description |
|-----------|-------------|
| Service | Container object configured under Team > Services |
| Service Keys | Authorize access to all Resources assigned to the Service |
| Resources | Any Twingate Resource assigned to the Service |

## Prerequisites
- Admin console access
- Resources already defined in Twingate
- Linux or Windows Twingate client for headless mode execution

## Step-by-Step: Create a New Service
1. Navigate to **Team > Services** → select **Create Service Account**
2. Select **Generate Key** to create a Service Key
3. **Save the Service Key immediately** — it is only viewable/copyable at creation time
4. Select **Add Resource** to assign Resources to the Service
5. Configure headless mode on Linux or Windows client

## Service Key Lifecycle

| State | Valid? | Notes |
|-------|--------|-------|
| **Active** | Yes | Default state; name editable; expiry set at creation only |
| **Revoked** | No | Must revoke before delete; cannot be reactivated |
| **Expired** | No | Auto-expires unless unlimited expiration was set |
| **Deleted** | No | Permanent; unrecoverable |

## Gotchas
- **Service Key is only shown once** at creation — store it securely immediately
- Expiry can **only be configured at creation time** — cannot be changed afterward
- Revoked keys **cannot be reactivated** — must create a new key
- Overprovisioning keys on a single Service Account causes rate-limiting; assign one key per high-traffic system
- All Service Keys on a Service authorize access to **all** Resources assigned to that Service — no per-key Resource scoping

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Security Policies documentation