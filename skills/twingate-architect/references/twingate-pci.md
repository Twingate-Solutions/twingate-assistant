# Twingate & PCI DSS Compliance

## Summary
Twingate is not itself PCI DSS validated, but does not need to be for organizations that must comply with PCI DSS. Twingate acts as a Third-Party Service Provider (TPSP) with limited scope: relays only route end-to-end encrypted traffic and cannot decrypt cardholder data. Organizations using Twingate must manage it per PCI DSS Requirement 12.8.

## Key Information
- Twingate relays **cannot decrypt** traffic passing through them due to end-to-end encryption
- Connections are peer-to-peer when possible; relays only used under certain network conditions
- Twingate has no ability to know if relayed traffic contains cardholder data
- PCI DSS v4.0.1 explicitly states TPSPs routing only encrypted data without key access **may not have PCI DSS responsibility** for that data
- PCI DSS Requirement 12.8 does **not** require TPSPs to be PCI DSS compliant—only that customers monitor their compliance status
- Twingate can help meet **Requirement 7.3** (access control system for in-scope system components)

## PCI DSS Scope Analysis

| Scenario | Twingate Scope |
|---|---|
| No cardholder data transits Twingate | Out of scope |
| Encrypted cardholder data transits relays (no key access) | May be treated as public/untrusted network |
| Twingate provides access controls to CDE components | In scope as TPSP (limited requirements) |

## Gotchas
- "In scope" for PCI DSS ≠ must be fully PCI DSS compliant
- If Twingate fulfills specific PCI DSS requirements on a customer's behalf (e.g., network access controls), **those specific requirements** are tied to Twingate's service quality and will impact the customer's assessment
- Organizations must still apply PCI DSS controls at the sending/receiving entities when routing through Twingate relays
- Customers must manage Twingate as a TPSP per Requirement 12.8 (monitor compliance status, maintain agreements, etc.)

## Action Items for Compliance Teams
1. Identify which PCI DSS requirements you intend to fulfill using Twingate
2. Document Twingate as a TPSP per Requirement 12.8
3. Monitor Twingate's compliance status as required by 12.8
4. Assess whether cardholder data transits Twingate relays and apply appropriate controls at endpoints
5. Reference PCI DSS v4.0.1 page 15–16 for TPSP encrypted data guidance

## Relevant PCI DSS References
- **PCI DSS v4.0.1, p.15**: Encrypted cardholder data and TPSP scope
- **PCI DSS v4.0.1, p.16**: Requirement 12.8 and TPSP compliance obligations
- **Requirement 7.3**: Access control system management (Twingate can assist)
- PCI SSC FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"

## Related Docs
- [PCI DSS Requirements and Testing Procedures](https://www.pcisecuritystandards.org) — "Use of Third-Party Service Providers" section
- Contact Twingate directly for organization-specific PCI DSS guidance