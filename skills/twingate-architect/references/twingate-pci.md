## Twingate & PCI Compliance

Detailed explanation of Twingate's position under PCI DSS for organizations with a cardholder data environment (CDE). Twingate is not PCI DSS validated but can be used in PCI-compliant environments.

**Cardholder Data:**
- Twingate relays only route end-to-end encrypted traffic; they cannot decrypt or store it
- PCI DSS v4.0.1 states: a TPSP that receives only encrypted cardholder data for routing purposes (without access to cryptographic keys) may not have PCI DSS responsibility for that data
- If no cardholder data is exchanged through Twingate-secured resources, Twingate relays are out of PCI scope entirely

**CDE Access Controls:**
- If Twingate secures access to CDE components, it may be considered "in scope" as a TPSP
- Being "in scope" does not require Twingate to be PCI DSS validated
- PCI DSS Requirement 12.8: customers must monitor TPSP compliance status; TPSPs do not need to be PCI DSS validated to satisfy this requirement
- Twingate can help meet Requirement 7.3 (access control system for in-scope system components)

**Action Required:**
- Identify which specific PCI DSS requirements you intend to satisfy using Twingate
- Verify how Twingate's controls meet those requirements
- Contact Twingate for further detail

**Related Docs:**
- /docs/pci-compliance -- PCI overview page
- /docs/twingate-security -- Security controls
- /docs/twingate-customer-data -- Data handling
