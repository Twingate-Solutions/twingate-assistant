# Twingate Services

## Summary
Services provide programmatic access controls for automated processes (CI/CD pipelines, custom applications) using Service Keys instead of Security Policies. Any Twingate Resource can be assigned to a Service, enabling zero trust access for non-human identities.

## Key Information
- Services live under **Team > Services** in the Admin console
- Access is granted via valid Service Keys (not Security Policies)
- Service Keys authorize access to **all Resources** assigned to that Service
- Linux and Windows clients support **headless mode** for automated connections
- Service Keys expire after **365 days by default**; unlimited expiration is configurable at creation time only

## Service Components
| Component | Details |
|-----------|---------|
| Service | Container object; configured in Admin console |
| Service Key | Auth credential; one or more per Service; rate-limited individually |
| Resources | Any Twingate Resource; one or more assignable per Service |

## Service Key Lifecycle States
| State | Valid? | Notes |
|-------|--------|-------|
| Active | Yes | Default state; name editable; expiry set at creation only |
| Revoked | No | Must revoke before delete; irreversible |
| Expired | No | Auto-expires unless set to unlimited |
| Deleted | No | Permanent; unrecoverable |

## Step-by-Step: Create a Service

1. Navigate to **Team > Services** → click **"Create Service Account"**
2. Click **"Generate Key"** to create a Service Key
3. **Copy and save the key immediately** — it cannot be viewed again after this step
4. Click **"Add Resource"** to assign Resources to the Service
5. Configure headless mode on Linux or Windows client to connect programmatically

## Configuration Values
- **Default key expiration:** 365 days (configurable to unlimited at creation time only)
- **Expiry setting:** Creation time only — cannot be changed after creation

## Gotchas
- **Service Key is only shown once** at creation — must be saved immediately
- **Security Policies do not apply** to Services; access is entirely Key-based
- **Over-provisioning keys causes throttling** — each key is individually API rate-limited; use a unique Service Key per high-traffic system
- Expiry cannot be modified after creation; plan expiration policy before generating keys
- Revoking a key is **permanent** — revoked keys cannot be reactivated, only deleted

## Related Docs
- Windows headless mode configuration guide
- Linux headless mode configuration guide
- Twingate Resources documentation
- Security Policies documentation