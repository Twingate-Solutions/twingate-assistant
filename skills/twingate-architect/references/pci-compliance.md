# PCI Compliance with Twingate

## Page Title
PCI Compliance — Twingate for PCI DSS Requirements

## Summary
Twingate is not PCI DSS validated itself, but can be used by organizations needing PCI compliance. PCI DSS does not require third-party service providers to be independently validated. When used to secure a cardholder data environment (CDE), Twingate is classified as a third-party service provider under Requirement 12.8.

## Key Information
- Twingate **is not** validated as PCI DSS compliant, but this is not required for customer compliance
- When securing CDE access, Twingate is considered "in scope" as a **third-party service provider**
- PCI DSS **Requirement 12.8** governs third-party service provider relationships
- PCI DSS **Requirement 7.3** (access control systems for in-scope components) is a specific requirement Twingate can help satisfy
- The service provider's compliance with *specific applicable requirements* affects the merchant's compliance — not blanket full validation

## Prerequisites
- Organization must identify which PCI DSS requirements they intend to fulfill using Twingate
- Organization must understand how Twingate technically satisfies those specific requirements
- Standard Twingate deployment securing access to CDE components

## Configuration Considerations
- Deploy Twingate to control access to CDE system components
- Map Twingate capabilities to specific PCI requirements (e.g., Req 7.3 for access control)
- Document Twingate as a third-party service provider per Requirement 12.8 obligations

## Gotchas
- **Scope creep risk**: If Twingate manages something like firewall rules and doesn't meet Requirement 1, the merchant fails those requirements — the service provider's gaps become the merchant's gaps
- "In scope" ≠ "must be fully PCI DSS certified" — these are distinct concepts
- Organizations bear responsibility for identifying and verifying which PCI requirements Twingate fulfills; Twingate does not provide a blanket compliance guarantee
- No Attestation of Compliance (AOC) or Report on Compliance (ROC) is mentioned as available from Twingate

## Related Docs
- [Twingate Contact Page](https://www.twingate.com/contact) — for detailed PCI DSS compliance inquiries
- [PCI Security Standards Council guidance on Requirement 12.8](https://www.pcisecuritystandards.org)
- Internal Twingate docs: Access Control configuration, Resource permissions, Zero Trust architecture