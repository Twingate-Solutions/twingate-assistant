# Twingate MSP Portal

## Summary
Twingate's MSP portal provides multi-tenant management for Managed Service Providers to create and manage Customer Networks and consolidated billing. Each Customer Network represents a complete customer account with its own resources, connectors, and team members.

## Key Information
- MSP Portal is separate from Customer Networks; users added to the portal must be explicitly added to individual Customer Networks for access
- 14-day free POC period per Customer Network before billing begins
- Credit card required at signup
- Consolidated monthly billing across all Customer Networks
- Users can be added manually or via Identity Provider sync

## Prerequisites
- Credit card for account creation
- Signup at Twingate MSP portal signup page

## Step-by-Step

### Initial Setup
1. Sign up at the MSP portal with credit card info
2. Choose MSP Portal URL (permanent — cannot be changed)
3. Add users to MSP Portal (manual or IdP sync)
4. Create Customer Networks for each client

### Offboarding a Customer
1. Click ellipses (`...`) at end of customer row
2. Select either:
   - **Offboard Network**: Access retained until end of billing cycle → downgraded to Starter tier, removed from MSP Network
   - **Delete Network**: Access retained until end of billing cycle → permanently deleted

## Configuration Values

| Setting | Notes |
|---|---|
| MSP Portal URL | Unique, immutable after creation |
| Recommended URL pattern | `yourcompanymsp` or `yourcompanyportal` |
| POC period | 14 days per Customer Network |
| Billing | Consolidated monthly |

## Gotchas
- **URLs are permanent** — cannot be changed after creation; plan naming carefully
- Reserve `yourcompany` URL for your own internal network by using a suffix for the MSP portal URL
- MSP Portal users ≠ Customer Network users; access must be granted separately per network
- Both offboard and delete options retain access until end of billing cycle — neither is immediate

## Related Docs
- MSP Billing page (linked in portal docs)
- Customer Networks page (linked in portal docs)
- Identity Provider sync documentation