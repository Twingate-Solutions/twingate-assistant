# SaaS App Gating with Google Workspace

## Summary
Configure Google Workspace Context-Aware Access with Twingate to gate SaaS applications behind a Twingate Connector connection. Access is controlled by checking if traffic originates from Connector exit IP addresses. Context is checked continuously for Google Workspace core apps and at authentication time for SAML-based third-party apps.

## Key Information
- Works with Google Workspace core apps (Gmail, Drive, Calendar) and SAML-based third-party apps
- Functions like IP whitelisting but enforced at the IdP level
- Connector exit IP addresses serve as the trust signal in Google's access policy
- Multiple Connector IPs create an OR-based allowlist

## Prerequisites

**Twingate Admin Console:**
- Create a Resource for the target domain (e.g., `*.google.com` for Google Workspace)
- Apply a **Device-only Policy** to that Resource — prevents authentication loop where users can't reach IdP login without already being authenticated via Twingate

**Google Workspace:**
- Admin access to `admin.google.com`
- Context-Aware Access enabled (requires Google Workspace Enterprise or BeyondCorp Enterprise)

## Step-by-Step

### Twingate Setup
1. Create Resource: `*.google.com` (or target SaaS domain)
2. Assign Device-only Policy to that Resource

### Google Workspace Setup
1. Navigate to `admin.google.com` → **Security → Access and data control → Context-Aware Access**
2. Click **Access levels → CREATE ACCESS LEVEL**
3. Configure access level:
   - **Name**: e.g., `Twingate Application Control`
   - **Conditions**: Basic mode, `Meets all attributes (AND)`
   - **Attribute**: `IP subnet`
   - Enter each Connector exit IP in CIDR format (e.g., `8.8.8.8/32`); multiple IPs = OR logic
4. Click **CREATE**
5. Navigate to **Assign access levels**
6. Select target applications → click **Assign**
7. Select your new access level → **CONTINUE**
8. Configure enforcement:
   - Block desktop app access: **Yes** (recommended)
   - Block mobile app access: **Yes** (recommended)
   - Block API access: **No** (recommended default)
9. Review and click **ASSIGN**

## Configuration Values
| Field | Value |
|---|---|
| Resource domain | `*.google.com` |
| Resource policy | Device-only |
| IP subnet format | `x.x.x.x/32` (single IP) |
| IP logic | OR (multiple subnets) |

## Gotchas
- **Authentication loop risk**: Without Device-only Policy on the IdP Resource, users cannot authenticate because reaching the IdP requires prior Twingate auth
- **IP source**: Use Connector *exit* IPs (public-facing), not internal IPs — e.g., AWS Elastic IP attached to Connector instance
- **Propagation delay**: Changes may take time to apply; test after full propagation
- **API access**: Do not block API-based access to avoid breaking integrations

## Testing
1. Disconnect Twingate Client → attempt login → should see blocked access message
2. Connect Twingate Client → reload → access should succeed
3. If still blocked, verify Resource is correctly capturing and routing traffic through Connectors

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Workspace Context-Aware Access Help Center](https://support.google.com/a/answer/9275380)