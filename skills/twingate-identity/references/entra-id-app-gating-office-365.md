# SaaS App Gate Office 365 with Microsoft Entra ID

## Summary
Configures Microsoft Entra ID Conditional Access to restrict Office 365 access exclusively through a Twingate Connector's public IP address. Users must connect via the Twingate Client to route traffic through the Connector, satisfying the Conditional Access policy. Direct access attempts are blocked.

## Key Information
- Policy logic: Block access from **any location** EXCEPT the trusted location (Connector IP) — net effect allows only Connector-routed traffic
- Multiple O365 domains may need separate Twingate Resources
- Conditional Access logs will show activity for verification
- Test with "Report-only" mode before enabling live

## Prerequisites
- Office 365 Business Subscription
- Entra ID Conditional Access license
- At least one deployed Twingate Connector with a known static public IP address
- Access to Twingate Admin Console and Entra ID admin portal

## Step-by-Step

### 1. Add Twingate Resources
In Admin Console, create Resources in the relevant Remote Network for O365 domains:
- `portal.office.com`
- `*.sharepoint.com`
- `*-my.sharepoint.com`
- `admin.microsoft.com`
- `*-admin.sharepoint.com`
- `admin.teams.microsoft.com`

### 2. Add Named Location in Entra ID
- Navigate to: **Entra ID → Conditional Access → Named locations**
- Create location using Connector's public IP in CIDR format
- This represents the trusted egress point

### 3. Create Conditional Access Policy
- Navigate to: **Conditional Access → Policies → New policy**
- **Users**: Start with a single test account; expand later
- **Apps**: Select Office 365
- **Conditions → Locations**:
  - Include: **Any location**
  - Exclude: **[Your named Connector location]**
- **Grant**: Set to **Block access**

### 4. Enable Policy
- Initially set to **Report-only** for testing
- Toggle to **On** when validated

## Configuration Values

| Setting | Value |
|---|---|
| Named location IP | Connector's public CIDR (e.g., `203.0.113.10/32`) |
| Location condition - Include | Any location |
| Location condition - Exclude | Trusted Connector named location |
| Grant control | Block access |
| Initial policy state | Report-only → On |

## Gotchas
- **Lockout risk**: Misconfigured Conditional Access can lock out global admin accounts — review policy carefully before enabling
- Policy logic is inverted: "Block from anywhere except Connector IP" = "Allow only via Connector IP"
- Each Connector has its own public IP; add all Connector IPs if using multiple Connectors for redundancy
- Entra Conditional Access requires a separate license (P1 or P2)

## Related Docs
- [SaaS App Gating with Microsoft Entra ID](https://www.twingate.com/docs/entra-id-saas-app-gating) (parent guide)
- [Microsoft Entra ID Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/)
- Entra ID licensing information (linked in prerequisites)