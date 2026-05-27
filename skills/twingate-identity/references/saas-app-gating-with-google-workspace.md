# SaaS App Gating with Google Workspace

## Summary
Configure Google Workspace Context-Aware Access with Twingate to require an active Connector connection before users can access Google Workspace apps and SAML-based SaaS applications. This uses Connector exit IP addresses as the trust signal rather than per-app IP allowlists. Context is checked continuously for core Google apps and at authentication time for third-party SAML apps.

## Key Information
- Works with Google Workspace core apps (Gmail, Drive, Calendar) and SAML-based third-party apps
- Trust signal = exit IP address of the Twingate Connector's Remote Network
- Multiple Connector IPs create an OR-based list in the access level
- Context checked **continuously** for Google core apps; **at auth time** for SAML apps

## Prerequisites

**Twingate Admin Console:**
1. Create a Resource for the target domain (e.g., `*.google.com` for Google Workspace)
2. Apply a **Device-only Policy** to that Resource — prevents auth loop where users can't reach the IdP login page because Twingate requires authentication first

## Step-by-Step

### Create Context-Aware Access Level (Google Admin)
1. Go to `https://admin.google.com` → Security → Access and data control → Context-Aware Access
2. Click **Access levels** → **CREATE ACCESS LEVEL**
3. Fill in:
   - **Access level name**: e.g., "Twingate Application Control"
   - **Context conditions**: Tab = BASIC, logic = "Meets all attributes (AND)"
   - **Attribute**: IP subnet
   - Enter each Connector exit IP in CIDR format (e.g., `8.8.8.8/32`); multiple IPs = OR logic
4. Click **CREATE**

### Assign Access Level to Applications
1. From Context-Aware Access main screen → **Assign access levels**
2. Select target applications from the eligible list
3. Click **Assign** at the top
4. Select your new access level → **CONTINUE**
5. Enforcement settings: block desktop and mobile app access; **do not block API-based access** (recommended default)
6. Review and click **ASSIGN**

## Configuration Values

| Field | Value |
|---|---|
| Resource domain (Google) | `*.google.com` |
| Resource Policy type | Device-only |
| Attribute type | IP subnet |
| IP format | `<connector-exit-ip>/32` |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the IdP Resource, users cannot authenticate to reach Twingate, creating a deadlock
- **Multiple IPs**: Each Connector exit IP must be added individually in CIDR notation; they form an OR list
- **API access**: Blocking API-based access is not recommended — leave at default (unblocked)
- **Testing**: Disable Twingate Client first to confirm block, then re-enable to confirm access

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Context-Aware Access Help Center](https://support.google.com/a/answer/9275380)