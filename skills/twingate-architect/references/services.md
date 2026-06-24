# Twingate Services

## Summary
Services provide programmatic access controls for automated processes (CI/CD pipelines, custom applications) to Twingate Resources. Access is granted via Service Keys rather than Security Policies. Clients run in headless mode to automate connections.

## Key Information
- Any Resource can be assigned to a Service, User, or both
- Security Policies do NOT apply to Services — access controlled solely by valid Service Keys
- One Service Key authorizes access to ALL Resources assigned to that Service
- Service Keys expire after 365 days by default; unlimited expiration can be set at creation time only
- Each Service Key is individually API rate-limited

## Prerequisites
- Admin console access (Team tab)
- Linux or Windows Twingate client (for headless mode execution)
- Resources already defined in Twingate

## Step-by-Step: Create a Service

1. Navigate to **Team > Services** → click **"Create Service Account"**
2. Click **"Generate Key"** to create a Service Key
3. **Save the Service Key immediately** — it cannot be retrieved after this step
4. Click **"Add Resource"** to assign one or more Resources to the Service
5. Configure headless mode on Linux or Windows client to use the Service Key

## Configuration Values
- **Service Key expiry**: Set at creation time only; default = 365 days; unlimited expiration available
- **Headless mode**: Supported on Linux and Windows clients (see platform-specific guides)

## Service Key Lifecycle States

| State | Valid? | Notes |
|-------|--------|-------|
| Active | Yes | Default state; editable name; expiry set at creation only |
| Revoked | No | Must revoke before delete; cannot reactivate |
| Expired | No | Auto-expires unless set to unlimited |
| Deleted | No | Permanent; unrecoverable |

## Gotchas
- **Service Key is shown only once** at creation — must be saved immediately
- **Expiry cannot be modified** after creation
- **Overprovisioning Service Keys** causes throttling — use one unique Service Key per high-traffic system
- Revoked keys **cannot be reactivated** — must create a new key
- Security Policies are bypassed entirely for Services; no MFA or device policy enforcement

## Related Docs
- Linux headless mode configuration guide
- Windows headless mode configuration guide
- Twingate Resources documentation
- Team administration / Admin console