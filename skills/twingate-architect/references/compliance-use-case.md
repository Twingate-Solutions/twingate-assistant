# Twingate Compliance Use Case

## Page Title
Compliance Use Cases

## Summary
Twingate provides security controls supporting multiple compliance frameworks including SOC 2, PCI DSS, HIPAA, GDPR, and others. It centralizes access management, enables granular least-privilege policies, and provides audit logging. It can replace or supplement VPN-based access with application-level controls.

## Key Information
- Supports compliance for: SOC 2, PCI DSS, HIPAA, HITRUST, SOX, FIPS 140-2/140-3, FedRAMP, GDPR, CPRA
- Controls access at the application level (not network level)
- Hides internal network from public internet (no public-facing gateways)
- MFA and device posture policies can be applied to resources that don't natively support them
- Compatible with FIPS 140-2/140-3 end-to-end encryption (does not break validated crypto)

## Compliance Program Specifics

| Framework | Relevant Controls |
|-----------|------------------|
| SOC 2 | Access controls, network security, risk assessments |
| PCI DSS | Requirement 7.3 (access control system for cardholder data environment) |
| HIPAA | Access controls, entity authentication, transmission security |
| HITRUST | CSF objectives: network/app/remote access controls, audit logging |
| SOX | Access/auth, user account management, network security, monitoring |
| FIPS 140-2/3 | Compatible with required encrypted communications |
| FedRAMP | Access control, audit/accountability, continuous monitoring, identity |
| GDPR | Technical measures for personal data protection, accountability logging |
| CPRA | Reasonable security procedures for personal information |

## Core Capabilities for Compliance
- **Access reviews**: Single interface showing who accesses which resources
- **Offboarding**: Disable all resource access in a few clicks
- **Logging/analytics**: Network activity visibility for anomaly detection and audit evidence
- **Least privilege**: Granular per-resource access policies
- **Overprovision reduction**: Centralized view simplifies access cleanup

## Prerequisites
- Twingate deployment (Connectors, Clients, Admin console)
- Resources defined within Twingate
- Identity provider integration for user management and MFA enforcement

## Gotchas
- Twingate assists with compliance controls but does not itself certify or guarantee compliance
- FIPS compatibility note: Twingate does not compromise FIPS-validated encryption but does not itself provide FIPS-certified modules
- PCI DSS reference is specifically to Requirement 7.3 (access control systems); other PCI requirements may need separate controls

## Related Docs
- [Guide to GDPR Compliance for IT Teams](https://www.twingate.com/docs)
- [Guide to SOC 2](https://www.twingate.com/docs)
- [Guide to SOX Compliance for IT Teams](https://www.twingate.com/docs)
- Twingate & GDPR
- Twingate & HIPAA
- Twingate & PCI DSS
- Twingate & SOC 2