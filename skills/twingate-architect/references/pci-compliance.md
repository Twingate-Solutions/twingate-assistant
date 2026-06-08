# Twingate PCI DSS Compliance

## Summary
Twingate can be used by PCI DSS-compliant organizations as a third party service provider, though Twingate itself is not validated as PCI DSS compliant. Organizations using Twingate to secure their cardholder data environment (CDE) should identify which PCI requirements Twingate helps fulfill and verify Twingate meets those specific requirements.

## Key Information
- Twingate is **not** validated as PCI DSS compliant, but PCI DSS does not require third party service providers to be validated
- When used to secure CDE access, Twingate is considered "in scope" as a third party service provider
- Being "in scope" does not mean Twingate must be fully PCI DSS validated
- **Requirement 12.8** governs third party service provider relationships
- Twingate can help meet **Requirement 7.3** (access control system for in-scope system components)
- If Twingate fails to meet applicable requirements it's being used to fulfill, those requirements are not considered "in place" for the merchant's compliance

## Prerequisites
- Organization must identify which specific PCI DSS requirements they intend to fulfill using Twingate
- Organization must verify Twingate meets those specific applicable requirements

## Configuration Considerations
- Twingate is relevant when used to **secure access to CDE components**
- Use case determines scope: only applies when Twingate is part of CDE security architecture

## Gotchas
- The compliance of Twingate's service directly impacts the organization's compliance for requirements Twingate is being used to fulfill (per PCI SSC guidance)
- Organizations bear responsibility for understanding how Twingate accomplishes each PCI requirement they rely on it for
- Twingate being "in scope" ≠ Twingate must be independently PCI DSS certified

## Related Docs
- [PCI Security Standards Council guidance on service providers](https://www.pcisecuritystandards.org/)
- Contact Twingate directly for detailed PCI DSS compliance information