# PCI Compliance with Twingate

## Summary
Twingate can be used by PCI DSS-compliant organizations even though Twingate itself is not validated as PCI DSS compliant. When used to secure access to a cardholder data environment (CDE), Twingate is considered a third-party service provider under PCI DSS Requirement 12.8.

## Key Information
- Twingate is **not** validated as PCI DSS compliant, but this is not required for customer compliance
- PCI DSS does not require third-party service providers to be independently validated as compliant
- Twingate is considered "in scope" as a third-party service provider when used to secure CDE access
- Being "in scope" ≠ requiring full PCI DSS validation of the service itself
- Twingate can help meet **Requirement 7.3** (access control system for in-scope system components)
- **Requirement 12.8** governs third-party service provider relationships

## Compliance Scope

| Aspect | Detail |
|--------|--------|
| Relevant PCI Requirement | 12.8 (third-party service providers) |
| Example Use Case Requirement | 7.3 (access control for system components) |
| Twingate's Role | Third-party service provider for CDE access security |

## Important Caveat
Per PCI Security Standards Council guidance: if Twingate fails to meet applicable PCI DSS requirements relevant to its service (e.g., access control), those requirements would **not** be considered met for the merchant's compliance. Organizations must verify Twingate's implementation satisfies the specific requirements they rely on it to fulfill.

## Implementation Guidance
1. Identify which specific PCI DSS requirements you intend to fulfill using Twingate
2. Understand how Twingate technically satisfies each identified requirement
3. Document Twingate as a third-party service provider per Requirement 12.8
4. Assess whether Twingate's controls meet the applicable sub-requirements for your use case

## Gotchas
- "In scope" does not mean Twingate must be PCI DSS certified — common misconception
- Compliance responsibility is shared: if Twingate's service doesn't meet applicable requirements, your compliance is affected
- Organizations must perform their own due diligence mapping Twingate capabilities to specific requirements

## Related Docs
- Contact Twingate directly for detailed PCI DSS compliance documentation
- [PCI Security Standards Council guidance on service providers](https://www.pcisecuritystandards.org)