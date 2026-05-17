# SaaS App Gating with Google Workspace

## Summary
Configures Google Workspace Context-Aware Access to require an active Twingate Connector connection before granting access to Google Workspace apps and SAML-based SaaS applications. Works by restricting app access to the exit IP addresses of Twingate Connectors. Context is checked continuously for core Google apps and at authentication time for third-party SAML apps.

## Key Information
- Replaces IP whitelisting at the SaaS app level; enforcement happens at the IdP level instead
- Supports Gmail, Drive, Calendar, and other SAML-based third-party applications
- Connector exit IP(s) become the authorized IP subnet(s) in Google's access policy

## Prerequisites
- Twingate Connector deployed with a known static exit IP (e.g., AWS Elastic IP)
- Google Workspace admin access
- **Twingate Admin Console setup required:**
  - Create a Resource for `*.google.com` (or relevant domain)
  - Apply a **Device-only Policy** to that Resource to prevent authentication loops

## Step-by-Step

### Twingate Setup
1. Create a Resource matching the SaaS domain (e.g., `*.google.com`)
2. Apply a Device-only Resource Policy to that Resource

### Google Workspace: Create Access Level
1. Go to `https://admin.google.com` → Security → Access and data control → Context-Aware Access
2. Click **Access levels** → **CREATE ACCESS LEVEL**
3. Fill in:
   - **Name**: e.g., `Twingate Application Control`
   - **Conditions**: Basic tab, select "Meets all attributes (AND)"
   - **Attribute**: IP subnet
   - **Value**: Enter each Connector exit IP in CIDR notation (e.g., `8.8.8.8/32`); multiple IPs are evaluated as OR
4. Click **CREATE**

### Google Workspace: Assign Access Level to Apps
1. Click **Assign access levels**
2. Select target applications from the list
3. Click **Assign** → select your access level → **CONTINUE**
4. Enforcement settings: Block desktop and mobile app access; leave API access unblocked (recommended default)
5. Review and click **ASSIGN**

## Configuration Values
| Parameter | Value/Notes |
|-----------|-------------|
| Resource domain | `*.google.com` (or target SaaS domain) |
| Resource Policy | Device-only |
| IP Subnet format | `<connector-exit-ip>/32` per Connector |
| Multiple IPs | Enter individually; treated as OR logic |

## Gotchas
- **Authentication loop risk**: Without a Device-only policy on the Google Resource, users can't reach the IdP to authenticate, blocking Twingate access entirely — creating a circular dependency
- Multiple Connector IPs must each be entered individually in the access level
- API-based access should generally remain unblocked to avoid breaking integrations
- Context is checked **continuously** for core Google apps but only **at login** for SAML apps
- If blocked after connecting Twingate client, verify the Resource is correctly capturing and routing traffic through the Connector

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Context-Aware Access Help Center](https://support.google.com/a/answer/9275380)