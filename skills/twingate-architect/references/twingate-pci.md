# Twingate & PCI DSS Compliance

## Summary
Twingate is not itself PCI DSS validated/certified, but this is not required for organizations using Twingate within a PCI DSS compliance program. Twingate functions as a Third-Party Service Provider (TPSP) under PCI DSS v4.0.1, and its role is limited to routing end-to-end encrypted traffic without access to cardholder data or cryptographic keys.

## Key Information
- Twingate is **not PCI DSS validated**, but does not need to be for customers to achieve compliance
- Traffic through Twingate Relays is end-to-end encrypted; Relays cannot decrypt, store, or process content
- Per PCI DSS v4.0.1 (p.15): TPSPs routing only encrypted cardholder data without access to keys **may have no PCI DSS responsibility** for that data
- Per PCI DSS v4.0.1 (p.16) and Requirement 12.8: TPSPs do **not** need to be PCI DSS compliant—customers only need to monitor TPSP compliance status
- If Twingate secures CDE access controls, it may be **in scope** for PCI DSS, but "in scope" ≠ "must be fully PCI DSS compliant"
- Twingate can help satisfy **Requirement 7.3** (access control system for in-scope system components)

## Cardholder Data Scope Analysis

| Scenario | Relay Scope |
|----------|-------------|
| No cardholder data transits Twingate | Out of PCI DSS scope |
| Encrypted cardholder data transits Relays (no key access) | May be treated as public/untrusted network |
| Twingate provides access controls to CDE components | In scope; assess against specific requirements only |

## Prerequisites
- Identify which PCI DSS requirements Twingate is intended to fulfill
- Manage Twingate as a TPSP per **Requirement 12.8** (monitor compliance status)
- Determine if cardholder data will transit Twingate infrastructure

## Gotchas
- Peer-to-peer connections bypass Twingate infrastructure entirely; Relays are only used under specific network conditions
- If a TPSP service fulfills a PCI DSS requirement on behalf of the customer, the TPSP's compliance of **that specific service** impacts the customer's assessment
- TPSPs that **store** cardholder data have additional obligations (access controls, physical security, etc.)—Twingate does not store cardholder data
- Twingate cannot determine if relay traffic contains cardholder data due to end-to-end encryption

## Relevant PCI DSS References
- PCI DSS v4.0.1, p.15: "Encrypted Cardholder Data and Impact to PCI DSS Scope for Third-Party Service Providers"
- PCI DSS v4.0.1, p.16: "Using TPSPs and the Impact on Customers Meeting PCI DSS Requirement 12.8"
- PCI DSS Requirement 7.3: Access control system management
- PCI DSS Requirement 12.8: TPSP management obligations
- PCI SSC FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"

## Related Docs
- [PCI DSS Requirements and Testing Procedures](https://www.pcisecuritystandards.org) — "Use of Third-Party Service Providers" section
- Contact Twingate directly for compliance-specific questions