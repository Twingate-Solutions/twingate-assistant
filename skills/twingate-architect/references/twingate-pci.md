# Twingate & PCI DSS Compliance

## Summary
Twingate is not itself validated as PCI DSS compliant but does not need to be for organizations subject to PCI DSS to use it. Twingate acts as a third-party service provider (TPSP) and its PCI DSS obligations depend on its specific role in handling cardholder data. Organizations must manage Twingate under PCI DSS Requirement 12.8 (TPSP monitoring), not require full compliance validation.

## Key Information
- Twingate uses end-to-end encryption; Relays route encrypted traffic but **cannot decrypt, store, or process** cardholder data
- Connections are peer-to-peer when possible; Relays only involved under certain network conditions
- Per PCI DSS v4.0.1 (p.15): TPSPs that only route encrypted cardholder data without access to keys **may have no PCI DSS responsibility** for that data
- Per PCI DSS v4.0.1 (p.16): **Requirement 12.8 does not require TPSPs to be PCI DSS compliant** — only that customers monitor TPSP compliance status
- If Twingate provides access controls to CDE components, it is "in scope" but that doesn't require full PCI DSS validation
- Twingate can help satisfy **Requirement 7.3** (access control systems for in-scope components)

## Scope Determination

| Scenario | PCI DSS Impact |
|----------|---------------|
| No cardholder data transits Twingate | Relays out of scope |
| Encrypted cardholder data routed through Relays | Twingate has no decryption access; may be treated as untrusted network |
| Twingate provides access controls to CDE | In scope as TPSP; customer manages via Req. 12.8 |

## Prerequisites
- Identify which PCI DSS requirements you intend Twingate to fulfill
- Establish TPSP monitoring process per Requirement 12.8
- Document Twingate's role relative to your cardholder data environment

## Gotchas
- "In scope" ≠ "must be fully PCI DSS compliant" — these are distinct concepts
- If Twingate fulfills specific PCI DSS requirements on your behalf (e.g., network security controls), those requirements are in scope for your assessment and Twingate's compliance of **that service** affects your compliance
- Twingate cannot know if data transiting Relays contains cardholder data due to encryption
- TPSPs that store cardholder data have additional obligations — Twingate does not store cardholder data

## Configuration Values
No specific env vars or CLI flags. Relevant PCI controls:
- **Requirement 7.3**: Access control system management (Twingate can fulfill this)
- **Requirement 12.8**: TPSP monitoring and management obligations

## Related Docs
- [PCI DSS v4.0.1 Requirements and Testing Procedures](https://www.pcisecuritystandards.org) — "Use of Third-Party Service Providers" section
- PCI Security Standards Council FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"
- Contact Twingate directly for compliance questions