# SaaS App Gating with Google Workspace

## Summary
Configure Google Workspace Context-Aware Access with Twingate to gate SaaS applications behind a Connector IP check. Users must route traffic through a Twingate Connector to satisfy the IP-based access policy. Context is checked continuously for core Google Workspace apps, and at authentication time for third-party SAML apps.

## Key Information
- Works with Google Workspace core apps (Gmail, Drive, Calendar) and SAML-based third-party apps
- Mechanism: Connector exit IP acts as the trusted IP for Google's Context-Aware Access policy
- IP check occurs at IdP level, not within each SaaS app directly
- Multiple Connector IPs form an OR-based allowlist

## Prerequisites
- Twingate Admin Console access
- Google Workspace Admin access with Context-Aware Access available
- Twingate Connector(s) deployed with known static exit IPs (e.g., AWS Elastic IPs)

## Twingate Configuration Steps

1. **Create a Resource** for the target domain (e.g., `*.google.com`) mapped to a Remote Network with your Connector
2. **Apply a Device-only Policy** to the Resource — prevents auth loop where users can't reach IdP login because Twingate requires authentication first

## Google Workspace Configuration Steps

1. Go to `https://admin.google.com` → Security → Access and data control → Context-Aware Access
2. Click **Access levels** → **CREATE ACCESS LEVEL**
3. Fill in:
   - **Access level name**: e.g., "Twingate Application Control"
   - **Context conditions**: Basic tab, "Meets all attributes (AND)", Attribute = **IP subnet**
   - Enter each Connector exit IP in CIDR format (e.g., `8.8.8.8/32`); multiple IPs = OR logic
4. Click **CREATE**
5. Navigate to **Assign access levels** → select target applications
6. Click **Assign** → select your new access level → **CONTINUE**
7. Enforcement settings: block desktop and mobile app access, **leave API access unblocked** (recommended default)
8. Review and click **ASSIGN**

## Configuration Values

| Field | Value/Format |
|-------|-------------|
| Resource domain | `*.google.com` (or target SaaS domain) |
| Resource Policy | Device-only |
| IP Subnet format | `x.x.x.x/32` per Connector IP |
| Multiple IPs logic | OR (enter individually) |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the IdP Resource, users can't authenticate because accessing the login portal itself requires prior Twingate auth — apply Device-only policy to break this cycle
- API-based access should remain unblocked; blocking it may break service integrations
- If still blocked after connecting Twingate Client, verify the Resource is correctly capturing and routing traffic through the Connector

## Testing
1. Log out of Twingate Client → attempt access to gated app → should see block message
2. Log in to Twingate Client → retry → access should succeed

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Context-Aware Access Help Center](https://support.google.com/a/answer/9275380)