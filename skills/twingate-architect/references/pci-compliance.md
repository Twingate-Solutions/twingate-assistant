# PCI Compliance with Twingate

## Page Title
PCI Compliance – Twingate for PCI DSS Requirements

## Summary
Twingate can be used by PCI DSS-regulated organizations without being validated as PCI DSS compliant itself, as PCI DSS does not require third-party service providers to hold that validation. When used to secure cardholder data environment (CDE) access, Twingate is treated as an in-scope third-party service provider under Requirement 12.8.

## Key Information
- Twingate is **not** validated as PCI DSS compliant, but this does not prevent organizations from using it in a compliant manner
- PCI DSS Requirement 12.8 governs third-party service providers; validation as PCI DSS compliant is **not required** to satisfy this requirement
- Being "in scope" ≠ needing full PCI DSS validation
- Twingate can help satisfy **Requirement 7.3** (access control system for managing access to in-scope system components)
- If Twingate is used to secure CDE access, its compliance posture directly affects the organization's overall PCI compliance

## Prerequisites
- Organization must identify which specific PCI DSS requirements they intend to fulfill using Twingate
- Organization must understand how Twingate technically fulfills those requirements

## Configuration / Use Case Mapping

| PCI DSS Requirement | Twingate Role |
|---|---|
| Requirement 7.3 | Access control system for CDE components |
| Requirement 12.8 | Third-party service provider managing CDE access |

## Gotchas
- If Twingate is managing services tied to specific PCI requirements (e.g., acting like a firewall replacement for Requirement 1), and those requirements aren't being met, the organization's compliance is impacted
- Organizations bear responsibility for mapping Twingate's capabilities to their specific compliance obligations—Twingate does not do this automatically
- "In scope" designation triggers documentation and oversight obligations under Requirement 12.8 (vendor management program, agreements, monitoring)

## Steps for PCI-Compliant Twingate Deployment
1. Determine if Twingate will be used to secure CDE access
2. If yes, classify Twingate as an in-scope third-party service provider
3. Identify the specific PCI DSS requirements Twingate will help fulfill
4. Document how Twingate meets those requirements technically
5. Establish vendor management controls per Requirement 12.8
6. Contact Twingate for supporting documentation if needed

## Related Docs
- PCI Security Standards Council – Requirement 12.8 guidance (referenced in page)
- Twingate Access Control configuration docs (Requirement 7.3 implementation)
- Contact Twingate directly for compliance documentation: twingate.com/contact