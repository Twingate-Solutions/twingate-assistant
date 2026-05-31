# Twingate & PCI Compliance

## Summary
Twingate is not itself validated as PCI DSS compliant but does not need to be for organizations subject to PCI DSS to use it. Twingate's end-to-end encryption means Relays cannot decrypt traffic, limiting PCI scope. Organizations using Twingate to secure CDE access must manage it as a TPSP under PCI DSS Requirement 12.8.

## Key Information
- Twingate is **not PCI DSS validated/certified**
- Traffic through Twingate Relays is end-to-end encrypted — Relays cannot decrypt, store, or process cardholder data content
- Many connections are peer-to-peer (no Twingate infrastructure involved at all)
- PCI DSS v4.0.1 (p.15): TPSPs routing only encrypted data without access to keys or plaintext **may have no PCI DSS responsibility** for that data
- PCI DSS v4.0.1 (p.16): TPSPs do **not** need to be PCI DSS compliant for customers to meet Requirement 12.8
- Being "in scope" ≠ must be fully PCI DSS compliant

## PCI DSS Scope Analysis

| Scenario | Twingate Relay Scope |
|---|---|
| No cardholder data transits Twingate | Out of scope |
| Encrypted cardholder data transits Relays, no key access | May be treated as public/untrusted network |
| Twingate provides access controls to CDE components | In scope as TPSP; specific requirements apply |

## Compliance Obligations for Organizations
- Manage Twingate under **Requirement 12.8** (TPSP monitoring)
- Identify which PCI requirements Twingate fulfills on your behalf
- Example: Twingate can help meet **Requirement 7.3** (access control system for in-scope components)
- If Twingate meets a PCI requirement on your behalf, that service's compliance **impacts your assessment**

## Gotchas
- Twingate has no way to know if relay traffic contains cardholder data (due to E2E encryption)
- If Twingate manages network security controls on your behalf, you must obtain evidence it meets applicable requirements (e.g., Requirement 1) or those requirements are not satisfied
- TPSPs storing cardholder data on behalf of customers have stricter obligations — Twingate does not store cardholder data

## Related Docs
- [PCI DSS v4.0.1 Requirements and Testing Procedures](https://www.pcisecuritystandards.org)
- PCI SSC FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"
- [Contact Twingate](https://www.twingate.com/contact) for compliance questions