# Twingate Compliance Use Cases

## Page Title
Compliance

## Summary
Twingate provides security controls supporting multiple compliance frameworks including SOC 2, PCI DSS, HIPAA, GDPR, and others. It centralizes access management, enables granular least-privilege controls, and provides audit logging to satisfy compliance requirements. It replaces traditional VPNs with application-level access controls.

## Key Information
- **Supported frameworks**: SOC 2, PCI DSS, HIPAA, HITRUST, SOX, FIPS 140-2/140-3, FedRAMP, GDPR, CPRA
- **Access controls**: Granular, per-resource MFA and device posture policies—even for apps without native support
- **Audit support**: Centralized logging and analytics for access reviews and compliance evidence
- **Offboarding**: Revoke access to all Twingate-secured resources in a few clicks
- **Network security**: Eliminates public-facing gateways; hides internal network from public internet
- **FIPS compatibility**: Does not compromise end-to-end FIPS 140-2/140-3 encrypted communications

## Framework-Specific Notes
| Framework | Relevant Controls |
|-----------|------------------|
| PCI DSS | Requirement 7.3 (access control system for cardholder data environment) |
| HIPAA | Technical safeguards: access controls, authentication, transmission security |
| HITRUST CSF | Network traffic ACLs, remote/mobile access, audit logging, record protection |
| FedRAMP | AC, AU, CA, IA control families |
| SOX | Access/auth, user account management, network security, monitoring |
| GDPR/CPRA | "Appropriate" technical measures; accountability via logging |

## Prerequisites
- Twingate deployment (Connectors, Clients, Resources configured)
- Identity provider integration for centralized user management
- Device posture policies configured (if required by compliance program)

## Gotchas
- Twingate *assists* with compliance controls but is not a complete compliance solution on its own
- FIPS compatibility noted but no detail on which cipher suites or specific module certifications
- No mention of built-in compliance reporting exports—logging/analytics must be configured separately

## Related Docs
- [Guide to GDPR Compliance for IT Teams](https://www.twingate.com/docs/gdpr-guide)
- [Guide to SOC 2](https://www.twingate.com/docs/soc2-guide)
- [Guide to SOX Compliance for IT Teams](https://www.twingate.com/docs/sox-guide)
- Twingate & GDPR
- Twingate & HIPAA
- Twingate & PCI DSS
- Twingate & SOC 2