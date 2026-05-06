# Twingate & PCI DSS Compliance

## Summary
Twingate is not itself validated as PCI DSS compliant but does not need to be for organizations subject to PCI DSS to use it. Twingate's role as a TPSP (third-party service provider) is limited to routing end-to-end encrypted traffic it cannot decrypt, and PCI DSS Requirement 12.8 does not mandate that TPSPs be PCI DSS compliant.

## Key Information
- Twingate relays **cannot decrypt, store, or process** cardholder data due to end-to-end encryption between client device and destination resource
- Many connections are peer-to-peer with **no Twingate infrastructure involvement**
- Per PCI DSS v4.0.1 (p.15): a TPSP routing only encrypted cardholder data without access to keys **may have no PCI DSS responsibility** for that data
- Per PCI DSS v4.0.1 (p.16): **Requirement 12.8 does not require TPSPs to be PCI DSS compliant**, only that customers monitor TPSP compliance status
- If Twingate provides access controls to CDE components, it may be "in scope" — but "in scope" ≠ "must be fully PCI DSS compliant"
- Twingate can help meet **Requirement 7.3** (access control system for in-scope system components)

## Two Scope Scenarios

| Scenario | Twingate's Status |
|---|---|
| No cardholder data transits Twingate | Out of PCI DSS scope entirely |
| Encrypted cardholder data transits relays | May be treated as public/untrusted network; customer responsible for controls |
| Twingate provides access controls to CDE | In scope as TPSP; customer must manage per Req. 12.8 |

## Gotchas
- "In scope" for PCI DSS does **not** automatically require full PCI DSS validation of the system
- If a TPSP fulfills a specific PCI DSS requirement on a customer's behalf (e.g., network security controls per Req. 1), the TPSP's compliance of that service **does** impact customer's assessment
- Twingate has no visibility into whether relay traffic contains cardholder data (encrypted in transit)
- Organizations must still manage Twingate as a TPSP under Requirement 12.8 (monitor compliance status, maintain agreements, etc.)

## Customer Action Items
1. Identify which PCI DSS requirements you intend to fulfill using Twingate
2. Determine if cardholder data will transit Twingate relays
3. Manage Twingate under Requirement 12.8 (TPSP management program)
4. Document Twingate's role and scope in your PCI DSS assessment

## Reference Documents
- PCI DSS v4.0.1, p.15: "Encrypted Cardholder Data and Impact to PCI DSS Scope for Third-Party Service Providers"
- PCI DSS v4.0.1, p.16: "Using TPSPs and the Impact on Customers Meeting PCI DSS Requirement 12.8"
- PCI SSC FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"
- PCI DSS Requirements and Testing Procedures: "Use of Third-Party Service Providers" section

## Related Docs
- Twingate relay architecture documentation
- Contact Twingate directly for compliance-specific questions