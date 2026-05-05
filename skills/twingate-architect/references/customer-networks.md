## Customer Networks (MSP)

MSP portal concept for managing end-customer Twingate deployments. Each Customer Network is a separate Twingate account managed under the MSP portal.

**Provisioning Fields (new Customer Network):**
- Customer Network Name, Customer Network URL (subdomain — must be globally unique)
- Admin email (initial admin for the network)
- Business Legal Name, Business Address, Business URL, Point of Contact

**Network Statuses:**
- **POC** -- within the initial 14-day free trial
- **Active** -- on an active subscription (auto-transition after trial)
- **Non-renewing** -- scheduled for deletion at end of billing cycle

**Key Operations:**
- Delete a trial network: ellipsis menu → Delete Network (immediate, no charge)
- Delete an active network: ellipsis menu → Delete Network (access continues until end of billing cycle, then deleted)
- Deleted networks are not shown in the Customer Networks tab

**Gotchas:**
- MSP Portal URL and Customer Network URL must be different subdomains (e.g., `companymsp` vs `company`)
- Cannot convert an MSP Customer Network to a standalone Twingate Network
- No refunds for deleted Customer Networks
- End users receive no deletion notification; only the Customer Network Admin Console shows a banner

**Related Docs:**
- /docs/msp-billing -- MSP billing and license calculation
- /docs/msp -- MSP portal overview
