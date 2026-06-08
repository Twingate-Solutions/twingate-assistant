# Twingate & PCI DSS Compliance

## Summary
Twingate is not itself validated as PCI DSS compliant but does not need to be for customers to use it in PCI-scoped environments. As a TPSP (third-party service provider), Twingate's obligations are governed by PCI DSS Requirement 12.8, which only requires customers to monitor TPSP compliance status—not that TPSPs be fully PCI DSS validated.

## Key Information
- Twingate uses end-to-end encryption between user devices and destination resources; Relays cannot decrypt, store, or process traffic content
- If no cardholder data is exchanged through Twingate-secured resources, Twingate Relays are out of PCI DSS scope entirely
- Even when cardholder data transits Twingate Relays, Twingate qualifies under PCI DSS v4.0.1 (p.15) as a TPSP routing only encrypted data without access to keys—potentially treated as a public/untrusted network
- "In scope" for PCI DSS ≠ must be fully PCI DSS compliant
- Twingate can help customers meet specific PCI DSS requirements (e.g., **Requirement 7.3**: access control systems for in-scope components)

## PCI DSS Standard References
- **PCI DSS v4.0.1, p.15**: TPSPs routing only encrypted cardholder data without decryption access may have no PCI DSS responsibility for that data
- **PCI DSS v4.0.1, p.16 / Requirement 12.8**: Customers must monitor TPSP compliance status; TPSPs are not required to be PCI DSS compliant themselves
- **Requirement 7.3**: Managing access to in-scope system components via access control system (area where Twingate directly assists)

## Gotchas
- If Twingate provides security services or access controls to CDE components, it may be "in scope"—but that only triggers specific requirement evaluation, not full PCI DSS validation
- If a TPSP service fulfills a specific PCI DSS requirement on the customer's behalf, that requirement's compliance depends on the TPSP's capability—customers must verify Twingate meets any specific requirements they're delegating
- Twingate has no way to know if relay traffic contains cardholder data due to E2E encryption
- Peer-to-peer connections (no relay involvement) keep Twingate infrastructure entirely out of the data path

## Customer Action Items
1. Identify which PCI DSS requirements you intend to fulfill using Twingate
2. Verify Twingate's capability to meet those specific requirements
3. Implement TPSP monitoring per Requirement 12.8
4. Ensure your organization applies PCI DSS controls for data transmitted through Twingate's network (your responsibility as the sending/receiving entity)

## Related Docs
- [PCI DSS Requirements and Testing Procedures](https://www.pcisecuritystandards.org) — "Use of Third-Party Service Providers" section
- PCI Security Standards Council FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"
- Contact Twingate directly for compliance questions