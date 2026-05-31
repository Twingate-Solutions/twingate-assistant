# Twingate PCI DSS Compliance

## Page Title
PCI Compliance - Twingate for Companies Requiring PCI DSS Compliance

## Summary
Twingate is not itself validated as PCI DSS compliant, but organizations can use it while maintaining PCI compliance. Twingate operates as a third-party service provider when securing access to a cardholder data environment (CDE), falling under PCI DSS Requirement 12.8. Organizations must understand which PCI requirements Twingate helps fulfill and verify Twingate meets those specific requirements.

## Key Information
- Twingate **is not validated** as PCI DSS compliant
- PCI DSS does **not require** third-party service providers to be independently validated as PCI DSS compliant
- When used to secure CDE access, Twingate is considered "in scope" as a third-party service provider
- Relevant standard: **PCI DSS Requirement 12.8** (third-party service provider management)
- Twingate can help meet **Requirement 7.3** (access control system for in-scope system components)
- If Twingate fails to meet applicable PCI requirements relevant to its service, the customer's compliance is impacted

## Prerequisites
- Organization must identify which specific PCI DSS requirements they intend to fulfill using Twingate
- Organization must understand how Twingate technically meets those requirements
- Twingate must be used to secure access to CDE components for it to be considered in scope

## Configuration / Compliance Scope
| Use Case | PCI Requirement | Notes |
|----------|----------------|-------|
| Securing CDE access | Requirement 12.8 | Third-party service provider obligations |
| Access control to in-scope systems | Requirement 7.3 | Access control system management |

## Gotchas
- "In scope" ≠ "must be fully PCI DSS validated" — these are distinct concepts
- If Twingate is managing services that touch PCI requirements (e.g., acting like a firewall manager), Twingate must meet the applicable requirements for those functions or the customer's compliance is at risk
- PCI DSS compliance responsibility is not fully transferred to Twingate — organizations retain obligation to verify the service meets relevant requirements

## Related Docs
- PCI Security Standards Council guidance on Requirement 12.8
- Contact Twingate directly for organization-specific PCI DSS compliance questions

---
*For detailed or organization-specific guidance, contact Twingate support directly.*