# SaaS App Gate Office 365 with Microsoft Entra ID

## Summary
Configures Microsoft Entra ID Conditional Access to restrict Office 365 access exclusively through Twingate by whitelisting the Connector's public IP address. All Office 365 requests from non-Connector IPs are blocked. This is a practical implementation of the general Entra ID SaaS App Gating pattern.

## Key Information
- Traffic routed through Twingate Connector exits via the Connector's public IP, which Entra ID treats as a trusted location
- Policy logic: Block access from "any location" EXCEPT the trusted location (Connector IP) — net effect is allow-only-via-Connector
- Multiple Resources may be needed for full O365 coverage
- Conditional Access logs will show Twingate-routed access activity

## Prerequisites
- Office 365 Business Subscription
- Entra ID Conditional Access license
- At least one deployed Twingate Connector with a known static public IP address
- Note the public IP of each Connector before starting

## Step-by-Step

**1. Add Twingate Resource(s)**
- In Admin Console, create Resource(s) in the Remote Network containing your Connector(s)
- Common O365 URLs to add as Resources:
  - `portal.office.com`
  - `*.sharepoint.com`
  - `*-my.sharepoint.com`
  - `admin.microsoft.com`
  - `*-admin.sharepoint.com`
  - `admin.teams.microsoft.com`

**2. Add Named Location in Entra ID**
- Navigate to Entra ID → Conditional Access → Named locations
- Create new location with Connector's public IP in CIDR format

**3. Create Conditional Access Policy**
- Target: specific user(s) or group (test on single account first)
- App: Office 365
- Condition → Locations:
  - **Include**: Any location
  - **Exclude**: Your named Connector location
- Grant: **Block access**
- Enable as **Report-only** first for testing, then toggle **On**

## Configuration Values
| Setting | Value |
|---|---|
| Named Location | Connector public IP in CIDR notation |
| Policy scope (apps) | Office 365 |
| Location include | Any location |
| Location exclude | Connector named location |
| Grant control | Block access |

## Gotchas
- **Account lockout risk**: Misconfigured Conditional Access can lock out global admin accounts from the Entra portal — review policy carefully before enabling
- Policy logic is inverted: "Block from any location except trusted" = "allow only from trusted" — not "allow from any location except trusted"
- Always start with **Report-only** mode before activating
- Each Connector's public IP must be added as a separate named location if using multiple Connectors
- Incomplete Resource list may leave some O365 apps accessible without Twingate

## Related Docs
- [SaaS App Gating with Microsoft Entra ID](https://www.twingate.com/docs/entra-id-saas-app-gating) (general guide)
- [Microsoft Entra ID Conditional Access documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/)
- Entra ID Conditional Access licensing information