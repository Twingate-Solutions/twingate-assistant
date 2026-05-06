# PCI Compliance with Twingate

## Summary
Twingate can be used by PCI DSS-compliant organizations even though Twingate itself is not validated as PCI DSS compliant. When used to secure access to a cardholder data environment (CDE), Twingate is treated as a third-party service provider under PCI DSS Requirement 12.8. Organizations must identify which PCI requirements they intend to fulfill using Twingate.

## Key Information
- Twingate is **not** validated as PCI DSS compliant, but this is not required for customer compliance
- PCI DSS Requirement 12.8 governs third-party service providers — validation is not mandatory under this requirement
- Twingate being "in scope" does not mean it must be fully PCI DSS validated
- Twingate can help satisfy **Requirement 7.3** (access control system for in-scope system components)
- If Twingate fails to meet applicable PCI requirements for services it provides, those requirements are considered unmet for the merchant's compliance

## Prerequisites
- Organization must identify which specific PCI DSS requirements they intend to fulfill using Twingate
- Organization must understand how Twingate technically meets those requirements
- Twingate must be used to secure access to CDE components for it to be considered in scope as a service provider

## Configuration Guidance
- Deploy Twingate to control access to CDE components
- Map Twingate's access control capabilities to specific PCI requirements (e.g., Req. 7.3)
- Document Twingate as a third-party service provider in your PCI DSS compliance documentation per Requirement 12.8

## Gotchas
- Twingate's compliance impact is **scoped to the services it provides** — if Twingate doesn't meet requirements relevant to its role, those requirements are unmet for the merchant
- "In scope" ≠ "must be fully PCI DSS validated" — distinguish these concepts when working with auditors
- Organizations bear responsibility for understanding and documenting how Twingate fulfills each targeted requirement

## Related Docs
- PCI Security Standards Council guidance on Requirement 12.8
- Contact Twingate directly for compliance-specific questions