# Twingate & PCI DSS Compliance

## Summary
Twingate is not independently validated as PCI DSS compliant, but this is not required for organizations using it within their PCI DSS compliance programs. Twingate operates as a Third-Party Service Provider (TPSP) and its scope within PCI DSS depends on how it is used relative to the cardholder data environment (CDE).

## Key Information
- Twingate traffic uses **end-to-end encryption** between user device and destination resource
- When Relays are used: they route encrypted traffic but **cannot decrypt, store, or process** the content
- PCI DSS v4.0.1 (p.15): A TPSP that only routes encrypted cardholder data without access to keys **may have no PCI DSS responsibility** for that data
- PCI DSS v4.0.1 (p.16) / Requirement 12.8: TPSPs **do not need to be PCI DSS compliant** — customers only need to monitor TPSP compliance status
- Organizations must identify which specific PCI DSS requirements Twingate fulfills on their behalf

## Scope Determination

| Scenario | PCI DSS Scope |
|---|---|
| No cardholder data transits Twingate | Relays out of scope |
| Encrypted cardholder data transits Relays (no key access) | May be treated as public/untrusted network |
| Twingate provides access controls to CDE components | In scope as TPSP; specific requirements apply |

## Relevant PCI DSS Requirements
- **Requirement 7.3**: Access control system for in-scope system components — Twingate can help meet this requirement
- **Requirement 12.8**: TPSP management and monitoring obligations

## Gotchas
- "In scope" ≠ "must be fully PCI DSS compliant" — these are distinct concepts
- If Twingate fulfills a specific PCI DSS requirement on your behalf (e.g., network access controls), Twingate's implementation of **that requirement** will impact your compliance assessment
- TPSPs that store cardholder data have stricter obligations — Twingate does not store cardholder data
- Peer-to-peer connections bypass Relays entirely; only certain network conditions invoke Relay routing

## Prerequisites
- Review PCI DSS v4.0.1 sections on TPSP scope (pages 15–16)
- Identify which CDE components Twingate secures access to
- Document Twingate as a TPSP per Requirement 12.8 obligations

## Related Docs
- [PCI DSS Requirements and Testing Procedures](https://www.pcisecuritystandards.org) — "Use of Third-Party Service Providers" section
- PCI Security Standards Council FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"
- Contact Twingate directly for compliance-specific questions