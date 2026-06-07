# SaaS App Gating with Google Workspace

## Summary
Combines Twingate Connector exit IPs with Google Workspace Context-Aware Access to gate SaaS applications behind Twingate connectivity. Access approval happens at the IdP level based on IP address, similar to IP whitelisting but enforced during authentication. Core Google Workspace apps are checked continuously; SAML-based third-party apps are checked at authentication time.

## Key Information
- Works with Google Workspace core apps (Gmail, Drive, Calendar) and SAML-based third-party applications
- Control plane: Google Context-Aware Access evaluates the Connector's egress IP
- Multiple Connector IPs combine as OR logic in the access level
- Context-Aware Access is applied per-application via Google Admin console

## Prerequisites
- Google Workspace with Context-Aware Access enabled
- Twingate Connectors with known, stable egress IPs (e.g., AWS Elastic IPs)
- Twingate Admin Console access

## Step-by-Step

### Twingate Configuration
1. Create a Twingate Resource for the SaaS domain (e.g., `*.google.com`)
2. Apply a **Device-only Policy** to that Resource — prevents auth loop where IdP access requires Twingate auth before Twingate auth is possible

### Google Admin Configuration
1. Navigate to `https://admin.google.com` → Security → Access and data control → Context-Aware Access
2. Click **Access levels** → **CREATE ACCESS LEVEL**
3. Fill in:
   - **Name**: e.g., "Twingate Application Control"
   - **Conditions**: Basic mode, "Meets all attributes (AND)", Attribute = `IP subnet`
   - Add each Connector egress IP in CIDR notation (e.g., `8.8.8.8/32`); multiple IPs = OR logic
4. Save the access level
5. Click **Assign access levels** → select target applications
6. Click **Assign** → select your new access level → **CONTINUE**
7. Enforcement settings: block desktop and mobile app access; leave API access unblocked (default) → **CONTINUE**
8. Review and click **ASSIGN**

## Configuration Values
| Field | Value |
|-------|-------|
| Resource domain | `*.google.com` (or target SaaS domain) |
| Resource Policy | Device-only |
| IP Subnet format | `<egress_ip>/32` per Connector |
| Condition logic | AND within one IP entry; OR across multiple IP entries |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the IdP Resource, users can't authenticate to Twingate because accessing the IdP requires Twingate to already be authenticated
- **Mobile/API**: Blocking API access may break service accounts or integrations — leave API enforcement disabled by default
- **IP stability**: Connector egress IPs must be static (e.g., Elastic IPs in AWS); dynamic IPs will break access
- **Propagation delay**: Policy changes may not take effect immediately; test after allowing time to propagate

## Testing
1. Disconnect Twingate Client → attempt login → should see "blocked" message
2. Connect Twingate Client → retry → access should succeed
3. If still blocked, verify the Resource is correctly routing traffic through the Connector

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Context-Aware Access Help Center](https://support.google.com/a/answer/9275380)