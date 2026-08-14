---
source: https://www.twingate.com/docs/services
type: docs
fetched: 2026-08-14
source_version: 6554f3bc53b81ebe347dca34c278faba08d6283b22d1549b8829b175e6bbd3e7
---

# Twingate Services

## Summary
Services provide programmatic access control for automated processes (CI/CD pipelines, custom applications) to Twingate Resources. Access is granted via Service Keys rather than Security Policies. Clients run in headless mode to enable automated Resource access.

## Key Information
- Any Resource can be assigned to a Service, User, or both
- Security Policies do **not** apply to Services — access controlled by valid Service Keys
- Service Keys authorize access to **all** Resources assigned to a Service
- Service Keys expire after **365 days** by default; unlimited expiration available at creation time only
- Expiry can only be configured at creation time — cannot be changed afterward
- Each Service Key is individually API rate-limited

## Prerequisites
- Admin console access (Team tab)
- Linux or Windows Twingate client (for headless mode execution)
- Resources already defined in Twingate

## Step-by-Step: Create a New Service

1. Navigate to **Team > Services** → click **"Create Service Account"**
2. Click **"Generate Key"** to create a Service Key
3. **Copy and save the Service Key immediately** — only viewable once at creation
4. Click **"Add Resource"** to assign Resources to the Service
5. Configure headless mode on Linux or Windows client to use the Service Key

## Configuration Values
| Parameter | Value/Notes |
|---|---|
| Default key expiration | 365 days |
| Expiration options | Configurable at creation only; unlimited allowed |
| Key scope | Authorizes all Resources on the Service |

## Service Key Lifecycle States

| State | Valid? | Notes |
|---|---|---|
| **Active** | Yes | Default state; name editable |
| **Revoked** | No | Must revoke before delete; cannot reactivate |
| **Expired** | No | Auto-expires unless set to unlimited |
| **Deleted** | No | Permanent, unrecoverable |

## Gotchas
- **Service Key is only shown once** — save it immediately at creation
- **Expiry is immutable** after creation — plan accordingly
- **Overprovisioning Service Keys** on one Service causes rate-limiting; use one unique Service Key per high-traffic system
- Revoking a key is irreversible — cannot return to Active state
- Deleted keys are permanently gone

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Team/Admin console documentation