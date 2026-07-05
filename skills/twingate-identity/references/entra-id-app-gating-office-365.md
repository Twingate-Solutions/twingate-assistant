# SaaS App Gate Office 365 with Microsoft Entra ID

## Summary
Configures Microsoft Entra ID Conditional Access to restrict Office 365 access exclusively through a Twingate Connector's public IP address. Users must be connected to Twingate to access Office 365; all other access paths are blocked.

## Key Information
- Twingate Resource is created for Office 365 URLs in a Remote Network
- Entra ID Conditional Access uses a Named Location (Connector's public IP) as the trusted location
- Policy logic: block access from **any location EXCEPT** the trusted location (Connector IP)
- Multiple Office 365 URLs may need separate Resources depending on apps protected

## Prerequisites
- Office 365 Business Subscription
- Entra ID Conditional Access license
- At least one deployed Twingate Connector with a known public IP address

## Step-by-Step

**1. Add Twingate Resource**
- In Admin Console, create a Resource in the Remote Network containing the Connector
- Map to relevant Office 365 URLs as needed

**2. Add Named Location in Entra ID**
- Navigate to Entra ID → Conditional Access → Named Locations
- Create location using Connector's public IP in CIDR format

**3. Create Conditional Access Policy**
- Assign policy to target users (test on single account first)
- Target app: Office 365
- Condition: Include **Any location**, Exclude the **trusted Named Location**
- Grant: **Block access**

**4. Enable Policy**
- Start with **Report-only** mode for testing
- Switch to **On** when validated

## Configuration Values

| Item | Value/Notes |
|------|-------------|
| Trusted location | Connector public IP in CIDR notation |
| Target application | Office 365 (Entra app selector) |
| Condition – Include | Any location |
| Condition – Exclude | Named location (Connector IP) |
| Grant action | Block access |

**Office 365 URLs to consider for Resources:**
- `portal.office.com`
- `*.sharepoint.com`
- `*-my.sharepoint.com`
- `admin.microsoft.com`
- `*-admin.sharepoint.com`
- `admin.teams.microsoft.com`

## Gotchas
- **Lockout risk**: Misconfigured Conditional Access can lock out all accounts including global admins — verify policy carefully before enabling
- Always test on a **single user account** before applying to groups
- Use **Report-only mode** before setting policy to **On**
- Each Connector used for access must have its public IP included in the Named Location

## Related Docs
- [SaaS App Gating with Microsoft Entra ID](https://www.twingate.com/docs/entra-id-app-gating) (parent guide)
- [Entra ID Conditional Access licensing](https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory-pricing)
- Twingate Connector deployment documentation