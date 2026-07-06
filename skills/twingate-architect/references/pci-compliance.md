# PCI Compliance with Twingate

## Page Title
PCI Compliance – Twingate for PCI DSS Requirements

## Summary
Twingate can be used by organizations requiring PCI DSS compliance without itself being validated as PCI DSS compliant. When used to secure access to a cardholder data environment (CDE), Twingate is treated as a third-party service provider under PCI DSS Requirement 12.8.

## Key Information
- Twingate is **not** validated as PCI DSS compliant, but this is not required for organizations to remain compliant
- PCI DSS Requirement 12.8 governs third-party service providers; validation as PCI DSS compliant is not mandatory under this requirement
- If Twingate secures access to CDE components, it is considered **in scope** as a third-party service provider
- Twingate can help meet **Requirement 7.3** (access control system for in-scope system components)
- Organizations must identify which PCI requirements they intend to fulfill using Twingate and verify Twingate meets those specific requirements

## Prerequisites
- Organization must map their PCI DSS obligations before deploying Twingate for CDE access
- Organizations should understand which specific PCI requirements Twingate will help satisfy

## Gotchas
- Being "in scope" does not mean Twingate must be fully PCI DSS validated—these are distinct concepts
- If Twingate is used to fulfill a specific PCI requirement (e.g., firewall management equivalent), Twingate must actually meet the applicable sub-requirements for that control—otherwise the merchant's compliance gap remains
- PCI DSS compliance responsibility is **shared**: Twingate covers certain controls, but the organization remains accountable for requirements outside Twingate's scope

## Configuration Values
No specific environment variables, CLI flags, or API parameters documented on this page.

## Related Docs
- [Twingate Contact Page](https://www.twingate.com/contact) – for organization-specific PCI DSS compliance questions
- PCI Security Standards Council guidance on Requirement 12.8 (external reference)
- Twingate access control documentation (for Requirement 7.3 implementation)