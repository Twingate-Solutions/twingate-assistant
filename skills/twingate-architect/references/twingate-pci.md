# Twingate & PCI DSS Compliance

## Summary
Twingate is not validated as PCI DSS compliant but does not need to be for organizations subject to PCI DSS to use it. Twingate's role as a TPSP (third-party service provider) is limited: relays route end-to-end encrypted traffic without decryption capability, and PCI DSS Requirement 12.8 does not mandate that TPSPs themselves be PCI DSS compliant.

## Key Information
- Twingate traffic uses end-to-end encryption; Relays cannot decrypt, store, or process cardholder data content
- Connections are peer-to-peer when possible; Relays only used under specific network conditions
- Per PCI DSS v4.0.1 (p.15): TPSPs that route-only encrypted data without cryptographic key access **may have no PCI DSS responsibility** for that data
- Per PCI DSS v4.0.1 (p.16) and PCI SSC FAQ: Requirement 12.8 requires customers to **monitor** TPSP compliance status, not require TPSPs to be PCI DSS compliant
- Twingate being "in scope" ≠ Twingate must be fully PCI DSS compliant
- Twingate can help fulfill **Requirement 7.3** (access control system for in-scope system components)

## Scope Determination

| Scenario | Twingate Relay PCI Scope |
|----------|--------------------------|
| No cardholder data transits Twingate | Out of scope |
| Encrypted cardholder data transits Relays (no key access) | May be treated as public/untrusted network |
| Twingate provides access controls to CDE components | In scope as TPSP (limited requirements) |

## Prerequisites
- Organization must identify which PCI DSS requirements they intend to fulfill using Twingate
- Must manage Twingate as a TPSP per **Requirement 12.8** (monitoring compliance status)

## Gotchas
- If Twingate fulfills a specific PCI DSS requirement on behalf of a customer (e.g., network security controls), that service's compliance **directly impacts the customer's assessment**
- TPSPs storing cardholder data on behalf of customers face stricter obligations — Twingate does **not** store cardholder data
- Twingate has no visibility into whether relay traffic contains cardholder data due to end-to-end encryption

## Configuration Values
None applicable — compliance posture is architectural, not configuration-dependent.

## Related Docs
- [PCI DSS v4.0.1 Requirements and Testing Procedures](https://www.pcisecuritystandards.org) — "Use of Third-Party Service Providers" section
- PCI SSC FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"
- Twingate contact: support for PCI-specific questions