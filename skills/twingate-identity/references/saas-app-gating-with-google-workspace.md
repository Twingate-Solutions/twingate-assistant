# SaaS App Gating with Google Workspace

## Summary
Configure Google Workspace Context-Aware Access to require an active Twingate Connector connection before granting access to Google Workspace apps and SAML-based SaaS applications. Traffic is routed through Twingate Connectors, and Google validates the exit IP against an allowlist. Context is checked continuously for core Google apps, and at authentication time for third-party SAML apps.

## Key Information
- Works with Google Workspace core apps (Gmail, Drive, Calendar) and SAML-based third-party apps
- Uses Connector exit IP addresses as the trust signal (similar to IP whitelisting, but enforced at IdP level)
- Multiple Connector IPs form an OR-based allowlist in the access level

## Prerequisites
- Twingate Admin Console access
- Google Workspace Admin access with Context-Aware Access available
- Twingate Connector(s) deployed with known static exit IP addresses (e.g., AWS Elastic IPs)
- **Twingate Resource created** for target domain (e.g., `*.google.com`)
- **Device-only Policy** applied to that Resource — prevents authentication loop where users can't reach the IdP login page because Twingate auth is required first

## Step-by-Step

### Twingate Setup
1. Create a Resource for the target SaaS domain (e.g., `*.google.com`)
2. Apply a **Device-only Resource Policy** to that Resource to avoid auth loop

### Google Workspace: Create Access Level
1. Go to `https://admin.google.com` → Security → Access and data control → Context-Aware Access
2. Click **Access levels** → **CREATE ACCESS LEVEL**
3. Fill in:
   - **Name**: e.g., "Twingate Application Control"
   - **Condition logic**: "Meets all attributes (AND)"
   - **Attribute**: IP subnet
   - **Value**: Each Connector exit IP in CIDR notation (e.g., `8.8.8.8/32`); multiple IPs = OR logic
4. Click **CREATE**

### Google Workspace: Assign Access Level
1. Navigate back → click **Assign access levels**
2. Select target applications from the list
3. Click **Assign** → select your access level → **CONTINUE**
4. Enforcement settings: Block desktop and mobile app access; **leave API access unblocked** (recommended default)
5. Review and click **ASSIGN**

## Configuration Values
| Field | Value |
|---|---|
| Resource domain | `*.google.com` (or target SaaS domain) |
| Resource Policy | Device-only |
| IP Subnet format | `<exit_ip>/32` per Connector |
| Multiple IPs | Each entered separately (OR logic) |

## Gotchas
- **Auth loop**: Without a Device-only Policy on the IdP Resource, users cannot authenticate because accessing the login page itself requires prior Twingate auth
- **Multiple Connectors**: Each Connector's exit IP must be added individually to the access level
- **API access**: Do not block API-based access by default — only block desktop/mobile clients
- If testing fails after enabling Twingate Client, verify the Resource is correctly capturing and routing traffic through the Connector

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Context-Aware Access Help Center](https://support.google.com/a/answer/9275380)