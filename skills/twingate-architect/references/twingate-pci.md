# Twingate & PCI DSS Compliance

## Summary
Twingate is not validated as PCI DSS compliant but does not need to be for organizations subject to PCI DSS to use it. Twingate's role as a TPSP is limited: relays only route end-to-end encrypted traffic and cannot decrypt cardholder data. When used for CDE access controls, Twingate may be "in scope" but PCI DSS does not require TPSPs themselves to be fully compliant.

## Key Information
- Twingate traffic uses **end-to-end encryption**; relays cannot decrypt, store, or process content
- If no cardholder data transits Twingate, relays are **out of PCI DSS scope**
- If cardholder data does transit relays (encrypted), Twingate qualifies as a TPSP routing encrypted data without cryptographic key access — per PCI DSS v4.0.1 p.15, such TPSPs **may not have PCI DSS responsibility** for that data
- PCI DSS **Requirement 12.8** requires customers to *monitor* TPSP compliance status — it does **not** require the TPSP to be PCI DSS compliant
- Twingate can help meet specific requirements, e.g., **Requirement 7.3** (access control systems for in-scope components)

## Prerequisites
- Understand whether your use case involves cardholder data transiting Twingate relays
- Identify which PCI DSS requirements you intend Twingate to fulfill
- Have a TPSP monitoring process per Requirement 12.8

## Scope Determination Logic
| Scenario | PCI DSS Impact |
|---|---|
| No cardholder data through Twingate | Relays out of scope |
| Encrypted CHD routed through relays, no key access | Twingate treated as public/untrusted network; sending entity responsible for controls |
| Twingate used for CDE access controls | Twingate "in scope" as TPSP; specific requirements apply |

## Gotchas
- "In scope" ≠ "must be fully PCI DSS compliant" — these are distinct concepts
- If Twingate fulfills a PCI DSS requirement on your behalf (e.g., network security controls), **that service's compliance directly impacts your assessment** — you must verify Twingate meets those specific requirements
- TPSPs storing CHD on behalf of customers have additional obligations; Twingate does not store CHD
- Peer-to-peer connections may not involve Twingate infrastructure at all, but relay-assisted connections do route traffic through Twingate systems

## Configuration Values
No specific env vars or CLI flags. Implementation-specific: ensure access policies for CDE resources are configured to satisfy Requirement 7.3 (access control system management).

## Related Docs
- [PCI DSS v4.0.1](https://www.pcisecuritystandards.org/) — pp. 15–16 (TPSP sections)
- [PCI SSC FAQ: TPSP impact on compliance](https://www.pcisecuritystandards.org/)
- PCI DSS Requirements and Testing Procedures — "Use of Third-Party Service Providers" section
- Twingate: contact support for compliance questions