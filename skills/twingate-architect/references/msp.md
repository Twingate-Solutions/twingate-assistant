## Managed Service Providers (MSP Portal)

Multi-tenant portal for MSPs to manage Customer Networks and consolidated billing. Each Customer Network is an isolated Twingate account with its own Resources, Connectors, and users.

**Getting Started:**
- Sign up at the MSP portal signup page; credit card required but each Customer Network gets a 14-day free POC period
- Choose a unique MSP Portal URL at signup — cannot be changed after creation; recommended pattern: `companymsp` for portal, `company` for own network

**User Management:**
- MSP portal users are separate from Customer Network users; adding someone to the MSP Portal does not grant them Customer Network access
- Users can be added manually or synced via an Identity Provider

**Removing Customer Networks:**
- **Offboard Network** -- Customer Network access continues until end of billing cycle, then downgraded to Starter and removed from MSP; no longer charged
- **Delete Network** -- access continues until end of billing cycle, then permanently deleted; no longer charged

**Related Docs:**
- /docs/customer-networks -- Creating and managing individual Customer Networks
- /docs/msp-billing -- Consolidated billing details and license calculation
