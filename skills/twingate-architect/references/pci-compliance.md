# PCI Compliance with Twingate

## Page Title
PCI Compliance – Twingate for PCI DSS Requirements

## Summary
Twingate can be used by PCI DSS-compliant organizations without itself being PCI DSS validated, as PCI DSS does not require third-party service providers to hold their own validation. When used to secure cardholder data environments (CDE), Twingate is classified as a third-party service provider under PCI DSS Requirement 12.8.

## Key Information
- Twingate is **not validated as PCI DSS compliant**, but this does not prevent its use in PCI-compliant environments
- Twingate may be considered **"in scope"** as a third-party service provider when securing CDE access
- Being "in scope" ≠ requiring full PCI DSS validation for the service provider
- Relevant standard: **PCI DSS Requirement 12.8** (third-party service provider management)
- Twingate can assist with **Requirement 7.3** (access control systems for in-scope system components)
- If Twingate fails to meet applicable PCI requirements it claims to fulfill, those requirements are not considered met for the customer's compliance

## Prerequisites
- Organization must identify which specific PCI DSS requirements they intend to fulfill using Twingate
- Organization must understand how Twingate technically accomplishes those requirements
- Standard Twingate deployment securing access to CDE components

## Configuration Considerations
- Twingate should be deployed to control access to **CDE components specifically**
- Use Twingate's access control features to satisfy **Requirement 7.3** (access control system for in-scope components)

## Gotchas
- The customer organization retains responsibility for verifying Twingate meets the specific PCI requirements they rely on it for
- If Twingate doesn't meet the applicable sub-requirements (e.g., equivalent of Requirement 1 for firewall management), those requirements are **not considered met** for the merchant
- Twingate's compliance posture directly impacts the customer's PCI compliance for any requirement Twingate is used to fulfill
- No blanket coverage — organizations must map each PCI requirement to Twingate's specific capabilities

## Related Docs
- PCI Security Standards Council guidance on Requirement 12.8
- Contact Twingate directly for detailed PCI DSS compliance documentation

## Additional Notes
For detailed mapping of Twingate capabilities to specific PCI DSS requirements, contact Twingate sales/support directly — no public compliance matrix is available in this documentation.