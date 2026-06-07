# SaaS App Gate Office 365 with Microsoft Entra ID

## Summary
Configures Microsoft Entra ID Conditional Access to restrict Office 365 access exclusively through Twingate Connectors. Traffic from non-Twingate IP addresses is blocked; traffic routed via Connector's public IP is permitted.

## Key Information
- Twingate Resources are created for Office 365 URLs in a Remote Network
- Entra ID Conditional Access uses the Connector's public IP as a "trusted location"
- Policy logic: block access from **any location EXCEPT** the trusted location (Connector IP)
- Multiple Office 365 domains may require separate Resources

## Prerequisites
- Office 365 Business Subscription
- Entra ID Conditional Access license
- At least one deployed Twingate Connector with a known public IP address
- Access to Twingate Admin Console and Entra ID portal

## Step-by-Step

### 1. Add Twingate Resources
Create Resources in the Admin Console for Office 365 URLs within the target Remote Network. Relevant domains:
- `portal.office.com`
- `*.sharepoint.com`
- `*-my.sharepoint.com`
- `admin.microsoft.com`
- `*-admin.sharepoint.com`
- `admin.teams.microsoft.com`

### 2. Configure Entra ID Conditional Access

**2.1 Add Named Location**
- Navigate to Entra ID → Conditional Access → Named locations
- Create location using Connector's public IP in CIDR format

**2.2 Create Conditional Access Policy**
- Go to Policies → New policy
- **Users**: Target a test user first; expand scope after validation
- **Apps**: Select Office 365
- **Conditions → Locations**:
  - Include: `Any location`
  - Exclude: the Named location (Connector IP)
- **Grant**: Set to `Block access`

**2.3 Enable Policy**
- Start with `Report-only` mode for testing
- Switch to `On` when validated

## Configuration Values

| Setting | Value |
|---|---|
| Named location type | IP ranges (CIDR) |
| Location include | Any location |
| Location exclude | Connector public IP named location |
| Grant control | Block access |
| Initial policy state | Report-only → On |

## Gotchas
- **Lockout risk**: Misconfigured Conditional Access can lock out all accounts including global admins — review policy carefully before enabling
- **Logic is inverted**: The policy *blocks* from "any location" but *excludes* the trusted IP — this grants access only via the Connector
- **Multiple domains**: Single Resource for `portal.office.com` may not cover all Office 365 apps; add Resources per domain as needed
- **Test first**: Apply policy to a single test account before rolling out broadly

## Related Docs
- [SaaS App Gating with Microsoft Entra ID](https://www.twingate.com/docs/entra-id-saas-app-gating) (parent guide)
- [Microsoft Entra ID Conditional Access documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/)
- Entra ID Conditional Access licensing information