# Twingate MSP Portal

## Summary
Twingate's MSP portal provides a multi-tenant management interface for managed service providers to create and manage Customer Networks and consolidated billing. Each Customer Network represents a complete customer account with its own Resources, Connectors, and team members.

## Key Information
- MSP portal has separate user access from Customer Networks — users added to MSP portal must be explicitly added to each Customer Network for access
- Each new Customer Network includes a 14-day free POC period before billing begins
- Credit card required at signup but not charged during POC period
- Consolidated monthly billing across all Customer Networks
- Users can be added manually or synced via Identity Provider

## Prerequisites
- Credit card on file to create Customer Networks
- Unique URL selected at signup (cannot be changed after creation)

## URL Naming Convention
- MSP Portal URL and all Customer Network URLs must be globally unique and **permanent**
- Recommended pattern: use `yourcompanymsp` or `yourcompanyportal` for the MSP portal URL
- Reserve `yourcompany` for your own internal Twingate network

## Customer Network Removal Options

| Option | Access Until | End State |
|---|---|---|
| **Offboard Network** | End of billing cycle | Downgraded to Starter tier, removed from MSP, no further charges |
| **Delete Network** | End of billing cycle | Permanently deleted, no further charges |

Both options: click ellipses (⋯) at end of network row to access.

## Gotchas
- URLs **cannot be changed** after creation — plan naming convention carefully before signup
- MSP portal users ≠ Customer Network users; separate addition required for each network
- "Offboard" vs "Delete" distinction matters — offboard preserves customer access at Starter tier, delete removes the network entirely

## Related Docs
- [MSP Billing page](https://www.twingate.com/docs/msp-billing)
- [Customer Networks page](https://www.twingate.com/docs/customer-networks)
- [MSP Portal signup](https://www.twingate.com/msp-signup)