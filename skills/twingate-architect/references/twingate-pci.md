# Twingate & PCI DSS Compliance

## Summary
Twingate is not itself validated as PCI DSS compliant but does not need to be for organizations subject to PCI DSS to use it. Twingate relays only route end-to-end encrypted traffic and cannot decrypt it, limiting PCI DSS scope implications. Organizations should identify which specific PCI DSS requirements Twingate helps fulfill.

## Key Information
- Twingate uses end-to-end encryption between user device and destination resource; relays cannot decrypt, store, or process traffic content
- Traffic may route peer-to-peer (no Twingate infrastructure) or via Twingate Relays depending on network conditions
- Per PCI DSS v4.0.1 (p.15): a TPSP routing only encrypted cardholder data without access to keys may have **no PCI DSS responsibility** for that data
- Per PCI DSS v4.0.1 (p.16): **TPSPs do not need to be PCI DSS validated** for customers to meet Requirement 12.8 — only monitoring of TPSP compliance status is required
- "In scope" ≠ "must be fully PCI DSS compliant"

## Scope Determination

| Scenario | Relay PCI Scope |
|---|---|
| No cardholder data transits Twingate | Out of scope |
| Cardholder data transits (encrypted) | Twingate acts as public/untrusted network; customer responsible for controls |
| Twingate provides access controls to CDE | In scope as TPSP for relevant requirements only |

## Relevant PCI DSS Requirements

- **Requirement 12.8** — Managing third-party service providers; does not require TPSPs to be PCI DSS compliant, only monitoring
- **Requirement 7.3** — Access control systems for in-scope components; Twingate can help fulfill this requirement
- **Requirement 1** — Network security controls (relevant if Twingate manages network security on customer's behalf)

## Gotchas
- If Twingate provides a service that meets a specific PCI DSS requirement on behalf of the customer, Twingate's compliance for **that service** directly impacts the customer's compliance assessment
- TPSPs that store cardholder data face stricter requirements — Twingate does not store cardholder data
- Organizations must still apply PCI DSS controls at the sending/receiving endpoints when using Twingate as a transit network
- Twingate has no way to determine if relay traffic contains cardholder data due to encryption

## Prerequisites
- Organizations must manage Twingate as a TPSP per Requirement 12.8 (vendor monitoring program)
- Organizations should document which PCI DSS requirements they intend Twingate to fulfill

## Related Docs
- [PCI DSS v4.0.1](https://www.pcisecuritystandards.org/) — pp. 15–16 (TPSP sections)
- [PCI SSC FAQ: Impact of TPSPs on PCI DSS compliance](https://www.pcisecuritystandards.org/)
- PCI DSS Requirements and Testing Procedures — "Use of Third-Party Service Providers" section