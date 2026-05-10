# SaaS App Gating Office 365 with Microsoft Entra ID

## Summary
Configures Microsoft Entra ID Conditional Access to restrict Office 365 access exclusively through a Twingate Connector's public IP address. Users must connect via Twingate Client to reach Office 365; direct access from other IPs is blocked.

## Key Information
- Twingate acts as a network egress point — Connector's public IP becomes the only trusted source for Office 365
- Policy logic: block access from "any location" EXCEPT the trusted Connector IP (double-negative = allowlist)
- Multiple Resources may be needed to cover all O365 URLs
- Test with Report-only mode before enforcing; misconfiguration can lock out global admins

## Prerequisites
- Office 365 Business Subscription
- Entra ID Conditional Access license
- At least one deployed Twingate Connector with a known static public IP address

## Step-by-Step

### 1. Add Twingate Resources
In Admin Console, create Resources in the Remote Network for O365 URLs:
- `portal.office.com`
- `*.sharepoint.com`
- `*-my.sharepoint.com`
- `admin.microsoft.com`
- `*-admin.sharepoint.com`
- `admin.teams.microsoft.com`

### 2. Add Named Location in Entra ID
- Navigate to: Entra ID → Conditional Access → Named Locations
- Create location using Connector's public IP in CIDR notation
- This represents the trusted Twingate egress point

### 3. Create Conditional Access Policy
- **Target users**: Start with a single test account; expand later
- **Target apps**: Office 365
- **Condition — Locations**:
  - Include: `Any location`
  - Exclude: the Named Location (Connector IP) created above
- **Grant**: `Block access`

### 4. Enable Policy
- Start with `Report-only` mode to validate behavior in logs
- Switch to `On` when confirmed working

## Configuration Values

| Setting | Value |
|---|---|
| Named Location IP | Connector's public IP in CIDR (e.g., `203.0.113.10/32`) |
| Included Location | Any location |
| Excluded Location | Named Location (Connector IP) |
| Grant control | Block access |
| Initial policy state | Report-only → On |

## Gotchas
- **Admin lockout risk**: Incorrect Conditional Access config can lock out global admin accounts — review carefully before enabling
- **Multiple Connectors**: Each Connector has its own public IP; add all Connector IPs to the Named Location
- **Policy logic is inverted**: "Block from any location except trusted" = "only allow from trusted" — easy to misconfigure
- **Scope creep**: Not all O365 apps are covered by a single URL; enumerate all relevant domains as Twingate Resources

## Related Docs
- [SaaS App Gating with Microsoft Entra ID](https://www.twingate.com/docs/saas-app-gating-entra-id) (parent guide)
- Entra ID Conditional Access licensing information
- Twingate Connector deployment documentation