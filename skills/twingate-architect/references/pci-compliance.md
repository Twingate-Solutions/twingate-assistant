# PCI Compliance with Twingate

## Page Title
PCI Compliance – Twingate for PCI DSS Requirements

## Summary
Twingate can be used by PCI DSS-compliant organizations as a third-party service provider, even though Twingate itself is not validated as PCI DSS compliant. PCI DSS does not require third-party service providers to hold their own validation. Organizations must understand which PCI requirements Twingate fulfills and verify Twingate meets those specific controls.

## Key Information
- Twingate is **not** PCI DSS validated, but this does not prevent its use in PCI-compliant environments
- When used to secure cardholder data environment (CDE) access, Twingate is considered **in scope** as a third-party service provider
- Being "in scope" ≠ requiring full PCI DSS validation of the product itself
- **Requirement 12.8** governs third-party service provider relationships
- **Requirement 7.3** (access control systems for in-scope components) is a specific requirement Twingate can help satisfy
- If Twingate fails to meet applicable PCI requirements it is relied upon for, the customer's compliance is affected

## Prerequisites
- Identify which PCI DSS requirements your organization intends to fulfill using Twingate
- Understand how Twingate technically satisfies those specific requirements
- Maintain documentation of Twingate as a third-party service provider per Requirement 12.8

## Configuration Values
No specific env vars, CLI flags, or API parameters documented on this page.

## Gotchas
- Twingate's compliance impact is scoped to the requirements it is **relied upon** to fulfill — if Twingate is used to manage access control but doesn't meet Requirement 7.3 controls, the merchant fails those requirements
- Organizations bear responsibility for validating that Twingate meets the specific PCI controls they assign to it
- Twingate being "in scope" does not automatically mean it covers all PCI requirements — mapping is the customer's responsibility

## Related Docs
- PCI Security Standards Council guidance on Requirement 12.8
- Contact Twingate directly for compliance-specific documentation