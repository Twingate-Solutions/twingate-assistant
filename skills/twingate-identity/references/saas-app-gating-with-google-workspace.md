# SaaS App Gating with Google Workspace

## Page Title
How to Configure SaaS App Gating with Google Workspace

## Summary
Combines Twingate Connector exit IPs with Google Workspace Context-Aware Access to gate SaaS applications—access is only permitted when traffic routes through a Twingate Connector. Context is checked continuously for core Google Workspace apps and at authentication time for third-party SAML apps.

## Key Information
- Works with Google Workspace core apps (Gmail, Drive, Calendar) and SAML-based third-party apps
- Mechanism: Connector exit IP is used as the allowed IP in Google's Context-Aware Access policy
- Context-Aware Access is IP-subnet-based; multiple IPs form an OR list
- Blocking applies to desktop/mobile apps; API access typically left unblocked (default)

## Prerequisites

**Twingate Admin Console:**
- Create a Twingate Resource for the SaaS domain (e.g., `*.google.com`)
- Apply a **Device-only Resource Policy** to that Resource to prevent authentication loops (users must reach the IdP login portal before Twingate auth is established)

**Google Workspace:**
- Admin access to `https://admin.google.com`
- Context-Aware Access feature enabled
- Know the public exit IP(s) of your Twingate Connector(s) (e.g., AWS Elastic IPs)

## Step-by-Step

1. **Twingate**: Create Resource for `*.google.com` (or relevant domain), assign Device-only Policy
2. **Google Admin**: Navigate to **Security → Access and data control → Context-Aware Access**
3. Click **Access levels → CREATE ACCESS LEVEL**
4. Fill in:
   - Name (e.g., `Twingate Application Control`)
   - Conditions: `Meets all attributes (AND)` → Attribute: `IP subnet`
   - Enter each Connector exit IP in CIDR notation (e.g., `8.8.8.8/32`); multiple IPs = OR logic
5. Click **CREATE**
6. Navigate to **Assign access levels**, select target applications
7. Click **Assign** on selected apps, choose your new access level, click **CONTINUE**
8. On enforcement screen: block desktop/mobile access, leave API access unblocked → **CONTINUE**
9. Review and click **ASSIGN**

## Configuration Values

| Field | Value/Format |
|---|---|
| Resource domain | `*.google.com` (or app-specific FQDN) |
| Resource Policy | Device-only |
| IP Subnet format | `x.x.x.x/32` per Connector IP |
| Multiple IPs logic | OR (each entered separately) |
| Enforcement default | Block desktop + mobile; allow API |

## Gotchas
- **Auth loop risk**: Without Device-only Policy on the IdP Resource, users can't authenticate because Twingate requires auth before granting network access to the IdP
- **Multiple Connectors**: All Connector exit IPs must be added individually to the access level—missing one will cause intermittent blocks
- **SAML apps**: Context checked only at authentication time, not continuously
- **Testing**: Clear browser state and test without Twingate Client connected first to confirm blocking works before verifying access

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Workspace Context-Aware Access Help Center](https://support.google.com/a/answer/9275380)