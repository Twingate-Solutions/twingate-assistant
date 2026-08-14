---
source: https://www.twingate.com/docs/saas-app-gating-with-google-workspace
type: docs
fetched: 2026-08-14
source_version: 952a6e450b2bebc083f8f1efc9e015b162e6bb39ba612153b3253753e5995f9f
---

# SaaS App Gating with Google Workspace

## Summary
Configures Google Workspace Context-Aware Access to require traffic routing through Twingate Connectors before accessing Google Workspace apps and SAML-based SaaS applications. Access control works by validating the exit IP of Twingate Connectors at the IdP level. Context is checked continuously for core Google apps and at authentication time for third-party SAML apps.

## Key Information
- Supported apps: Core Google Workspace (Gmail, Drive, Calendar) + SAML-based third-party apps
- Mechanism: Connector exit IPs are whitelisted in Google's Context-Aware Access policy
- Multiple Connector IPs form an OR-based list in the access level
- Device-only policy on the IdP resource prevents authentication loops

## Prerequisites
- Twingate Admin Console access
- Google Workspace Admin access with Context-Aware Access available
- Twingate Connector(s) with known static exit IPs (e.g., AWS Elastic IPs)
- **Create a Twingate Resource** for the SaaS domain (e.g., `*.google.com`)
- **Apply a Device-only Policy** to the IdP Resource to avoid chicken-and-egg auth loops

## Step-by-Step

### Twingate Setup
1. Create a Resource for the target domain (e.g., `*.google.com`)
2. Apply a **Device-only Resource Policy** to that Resource

### Google Admin Console
1. Navigate to `https://admin.google.com` → Security → Access and data control → Context-Aware Access
2. Click **Access levels** → **CREATE ACCESS LEVEL**
3. Fill in:
   - **Name**: e.g., "Twingate Application Control"
   - **Context conditions**: Basic tab, select "Meets all attributes (AND)"
   - **Attribute**: IP subnet
   - **IP Subnet**: Enter each Connector exit IP in CIDR notation (e.g., `8.8.8.8/32`); multiple IPs = OR logic
4. Click **CREATE**
5. Navigate back → click **Assign access levels**
6. Select target applications → click **Assign**
7. Select your new access level → click **CONTINUE**
8. Enforcement settings: Block desktop and mobile access; leave API access unblocked (default) → **CONTINUE**
9. Review and click **ASSIGN**

## Configuration Values
| Field | Value/Format |
|-------|-------------|
| Resource domain | `*.google.com` (or specific SaaS FQDN) |
| Resource Policy type | Device-only |
| IP Subnet format | `<exit_ip>/32` per Connector |
| Condition logic | AND within an entry; OR across multiple IP entries |

## Gotchas
- **Auth loop risk**: Without a Device-only policy on the IdP Resource, users cannot authenticate to get Twingate access, blocking them from the IdP entirely
- Connector exit IPs must be static (e.g., Elastic IPs in AWS); dynamic IPs will break the policy
- Context-Aware Access checks are **continuous** for core Google apps but only **at login** for SAML apps
- If access remains blocked after connecting Twingate client, verify the Resource correctly captures and routes traffic through the Connector

## Related Docs
- [Create a Twingate Resource](https://www.twingate.com/docs)
- [Device-only Resource Policy](https://www.twingate.com/docs)
- [Google Context-Aware Access Help Center](https://support.google.com)