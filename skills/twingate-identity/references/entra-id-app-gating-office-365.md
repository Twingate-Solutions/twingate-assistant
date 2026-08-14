---
source: https://www.twingate.com/docs/entra-id-app-gating-office-365
type: docs
fetched: 2026-08-14
source_version: 61df7741106d7f9b8b40861bde330a6d11c5eee6c7c47e036982929ecb749d3f
---

# SaaS App Gate Office 365 with Microsoft Entra ID

## Summary
Configures Microsoft Entra ID Conditional Access to restrict Office 365 access exclusively through Twingate by treating the Connector's public IP as a trusted location. Access from any other location is blocked. This is a practical implementation of the general Entra ID SaaS App Gating pattern.

## Key Information
- Traffic must route through a Twingate Connector; the Connector's public IP becomes the allowlisted "trusted location"
- Conditional Access logic: block access from "any location" EXCEPT the trusted location (inverted logic)
- Multiple Resources may be needed for full Office 365 coverage

## Prerequisites
- Office 365 Business Subscription
- Entra ID Conditional Access license
- At least one deployed Twingate Connector with a known static public IP address

## Step-by-Step

### 1. Add Twingate Resources
Create Resources in the Admin Console for Office 365 URLs:
- `portal.office.com`
- `*.sharepoint.com`
- `*-my.sharepoint.com`
- `admin.microsoft.com`
- `*-admin.sharepoint.com`
- `admin.teams.microsoft.com`

### 2. Add Named Location in Entra ID
- Navigate to **Entra ID → Conditional Access → Named locations**
- Create new location using the Connector's **public CIDR IP address**

### 3. Create Conditional Access Policy
- **Users**: Target specific test user first, then expand scope
- **Cloud apps**: Select Office 365
- **Conditions → Locations**:
  - Include: **Any location**
  - Exclude: The named location (Connector's IP)
- **Grant**: **Block access**

### 4. Enable Policy
- Start with **Report-only** mode for testing
- Switch to **On** when validated

## Configuration Values
| Parameter | Value |
|---|---|
| Named location type | IP ranges (CIDR) |
| Location include | Any location |
| Location exclude | Connector public IP (named location) |
| Grant control | Block access |
| Initial policy state | Report-only → On |

## Gotchas
- **Lockout risk**: Misconfigured Conditional Access can lock out global admin accounts from the Entra portal — verify policy carefully before enabling
- **Inverted logic**: The policy blocks "any location except trusted" — this is intentional but counterintuitive
- **Multiple Connectors**: Each Connector's public IP must be added to the trusted location
- **Multiple Resources**: Full Office 365 protection requires adding all relevant Microsoft domain Resources in Twingate, not just one

## Related Docs
- [SaaS App Gating with Microsoft Entra ID](https://www.twingate.com/docs/entra-id-saas-app-gating) (general pattern)
- [Microsoft Entra ID Conditional Access documentation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/)
- Entra ID Conditional Access licensing information