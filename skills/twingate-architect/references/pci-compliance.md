## PCI Compliance

Guidance on using Twingate in a PCI DSS-compliant environment. Twingate is not itself PCI DSS validated but can be used by PCI-compliant organizations.

**Key Points:**
- PCI DSS does not require third-party service providers like Twingate to be independently validated
- When used to secure cardholder data environment (CDE) access, Twingate is considered "in scope" as a third-party service provider under Requirement 12.8
- Service providers do not need PCI DSS validation to satisfy Requirement 12.8, but their controls must meet applicable requirements
- Twingate can help satisfy specific PCI requirements (e.g., Requirement 7.3: access control system for in-scope system components)

**Action Required for Customers:**
- Identify which PCI DSS requirements you intend to satisfy using Twingate
- Verify how Twingate's controls address each requirement
- Contact Twingate for detailed PCI compliance guidance

**Related Docs:**
- /docs/twingate-security -- Twingate security controls
- /docs/twingate-pci -- Twingate PCI detail page
