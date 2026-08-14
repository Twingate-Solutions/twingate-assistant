---
source: https://www.twingate.com/docs/twingate-pci
type: docs
fetched: 2026-08-14
source_version: e2a50f776def5a225e5d2eeb59d780b344465cac3a499c6eb28242b327f80678
---

# Twingate & PCI DSS Compliance

## Summary
Twingate is not itself PCI DSS validated, but organizations subject to PCI DSS can still use it. Its end-to-end encryption architecture means Twingate Relays cannot decrypt cardholder data, limiting PCI scope implications. Organizations using Twingate for CDE access controls must manage it as a TPSP under PCI DSS Requirement 12.8.

## Key Information
- Twingate is **not PCI DSS validated/certified**, but this doesn't prevent PCI-regulated organizations from using it
- Traffic uses end-to-end encryption; Relays route encrypted data but **cannot decrypt it, do not store it, and cannot access cardholder data**
- Connections are peer-to-peer when possible; Relays only involved under certain network conditions
- Twingate qualifies under PCI DSS v4.0.1 as a TPSP that receives only encrypted cardholder data for routing — may have **no PCI DSS responsibility** for that encrypted data
- Per PCI DSS v4.0.1 p.15: TPSPs routing-only encrypted data with no key access may be treated as a public/untrusted network

## PCI DSS Scope Analysis

### Cardholder Data (Relay Scope)
- If no cardholder data transits Twingate: Relays are **out of scope**
- If cardholder data does transit: Twingate's role is encrypted routing only → limited/no PCI responsibility per v4.0.1 guidance

### CDE Security (Access Control Scope)
- If Twingate provides access controls to CDE components → Twingate may be **in scope** as a TPSP
- Being "in scope" ≠ requiring full PCI DSS compliance for Twingate itself
- PCI DSS Requirement 12.8: Customers must **monitor** TPSP compliance status, but TPSPs don't need to be PCI DSS compliant themselves
- Exception: If a TPSP fulfills specific PCI requirements on behalf of the customer (e.g., Requirement 1 network security controls), that TPSP's compliance *does* impact the customer's assessment

## Relevant PCI DSS Requirements
| Requirement | Relevance |
|---|---|
| 12.8 | Manage and monitor TPSPs; does not require TPSP PCI compliance |
| 7.3 | Access control systems — Twingate can help meet this requirement |
| Requirement 1 | Network security controls — if Twingate manages these, its compliance impacts customer assessment |

## Implementation Guidance
1. Determine whether cardholder data will transit Twingate Relays
2. Identify which PCI DSS requirements Twingate is intended to fulfill (e.g., Req 7.3 access controls)
3. Manage Twingate as a TPSP per Requirement 12.8 (monitor compliance status)
4. Assess whether Twingate's role in your CDE triggers any specific requirement responsibilities

## Gotchas
- If Twingate is managing network security controls (Req 1) on your behalf and cannot demonstrate compliance, those requirements are **not in place** for your assessment
- TPSPs storing cardholder data on behalf of customers face additional requirements — Twingate does not store cardholder data
- Cryptographic key access is the critical differentiator; Twingate holds no decryption keys for customer traffic

## Related Docs
- [PCI DSS v4.0.1 Requirements and Testing Procedures](https://www.pcisecuritystandards.org) — "Use of Third-Party Service Providers" section
- PCI SSC FAQ: "How is an entity's PCI DSS compliance impacted by using TPSPs?"
- Contact Twingate directly for compliance questions