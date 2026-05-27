# SaaS App Gating Office 365 with Microsoft Entra ID

## Summary
Configures Microsoft Entra ID Conditional Access to restrict Office 365 access exclusively through a Twingate Connector's public IP address. Users must connect via Twingate Client to reach Office 365; direct access from other locations is blocked.

## Key Information
- Twingate acts as the allowed egress point — Connector's public IP becomes the "trusted location" in Entra ID
- Policy logic: block access from **any location** EXCEPT the trusted location (Connector IP)
- Multiple O365 domains may need separate Twingate Resources depending on apps in scope

## Prerequisites
- Office 365 Business Subscription
- Entra ID Conditional Access license
- At least one deployed Twingate Connector with a known static public IP address
- Access to Twingate Admin Console and Entra ID portal

## Step-by-Step

### 1. Add Twingate Resource
- In Admin Console, add Resource(s) in the Remote Network containing the Connector(s)
- Common O365 domains to add as Resources:
  - `portal.office.com`
  - `*.sharepoint.com`
  - `*-my.sharepoint.com`
  - `admin.microsoft.com`
  - `*-admin.sharepoint.com`
  - `admin.teams.microsoft.com`

### 2. Configure Entra ID Conditional Access

**2.1 Add Named Location**
- Navigate to Entra ID → Conditional Access → Named Locations
- Create new location with Connector's public IP in CIDR notation

**2.2 Create Conditional Access Policy**
- Target: specific user(s) or group (test on single account first)
- Target app: Office 365
- Condition — Locations:
  - **Include:** Any location
  - **Exclude:** Trusted location (Connector IP)
- Grant: **Block access**

**2.3 Enable Policy**
- Start with **Report-only** mode for testing
- Switch to **On** when validated

## Configuration Values
| Parameter | Value |
|-----------|-------|
| Named Location IP | Connector's public IP in CIDR format |
| Target Application | Office 365 |
| Location Include | Any location |
| Location Exclude | Named location (Connector IP) |
| Grant control | Block access |
| Initial policy state | Report-only → On |

## Gotchas
- **Lockout risk:** Misconfigured Conditional Access can lock out global admin accounts from the Entra portal — review policy carefully before enabling
- Policy logic is inverted: you're blocking everywhere *except* the trusted location, not explicitly allowing the trusted location
- Multiple Connector IPs must each be added as trusted locations (or combined in one named location)
- Test on a single account before applying to broader groups or all users

## Related Docs
- [SaaS App Gating with Microsoft Entra ID](https://www.twingate.com/docs/entra-id-app-gating) (parent guide)
- [Microsoft Entra ID Conditional Access licensing](https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview)
- Twingate Connector deployment documentation