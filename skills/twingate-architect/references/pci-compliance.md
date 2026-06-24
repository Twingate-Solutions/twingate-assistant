# PCI Compliance with Twingate

## Page Title
PCI Compliance — Using Twingate for PCI DSS Requirements

## Summary
Twingate can be used by PCI DSS-compliant organizations even though Twingate itself is not PCI DSS validated. When used to secure access to a cardholder data environment (CDE), Twingate is treated as a third-party service provider under PCI DSS Requirement 12.8. Organizations must identify which PCI requirements Twingate fulfills and verify Twingate meets those specific controls.

## Key Information
- Twingate is **not** PCI DSS validated, but PCI DSS does not require third-party service providers to be validated
- When securing a CDE, Twingate is considered "in scope" as a **third-party service provider**
- Relevant standard: **PCI DSS Requirement 12.8** (managing third-party service providers)
- Twingate can help meet **Requirement 7.3** — access control systems for in-scope system components
- "In scope" does not equal "must be fully validated" — the service only needs to meet the specific requirements it is responsible for
- If Twingate fails to meet the specific PCI requirements assigned to it, the organization's compliance is affected

## Prerequisites
- Organization must identify which PCI DSS requirements they intend to fulfill using Twingate
- Must understand how Twingate technically accomplishes those specific requirements
- Must implement Twingate as part of CDE access controls

## Configuration Considerations
- Use Twingate to control access to CDE components (maps to Requirement 7.3)
- Document Twingate's role as a service provider per Requirement 12.8 obligations
- Maintain agreements and monitoring of Twingate as required under Requirement 12.8

## Gotchas
- Twingate's compliance status affects the organization's PCI compliance only for the specific requirements Twingate is responsible for — not wholesale
- Organizations bear responsibility for correctly scoping what Twingate covers vs. other controls
- PCI DSS compliance determination is ultimately the organization's and their QSA's responsibility — Twingate does not provide compliance guarantees

## Related Docs
- PCI Security Standards Council guidance on Requirement 12.8
- Contact Twingate directly for detailed PCI DSS compliance inquiries