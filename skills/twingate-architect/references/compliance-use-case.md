# Twingate Compliance Use Cases

## Page Title
Compliance

## Summary
Twingate provides security controls to support various compliance programs including SOC 2, PCI DSS, HIPAA, GDPR, and others. It centralizes access management, provides audit logging, and enforces least-privilege access policies. Twingate replaces traditional VPNs with application-level access controls that eliminate public-facing network exposure.

## Key Information
- Supports granular, least-privilege access with MFA and device posture enforcement per resource
- Single management plane for access reviews and compliance audit evidence
- Rapid offboarding: disable all resource access in a few clicks
- Network activity logging and analytics for anomaly detection
- Eliminates public-facing gateways; hides network from public internet
- Compatible with FIPS 140-2 and 140-3 (does not compromise end-to-end encrypted communications)

## Compliance Programs Covered

| Program | Relevant Controls |
|---|---|
| SOC 2 | Access controls, network security, risk assessments |
| PCI DSS | Requirement 7.3 (access control system for cardholder data environment) |
| HIPAA | Access controls, entity authentication, transmission security |
| HITRUST CSF | Network/app/remote access controls, audit logging, traffic monitoring |
| SOX | Access/auth, user account management, network security, monitoring |
| FIPS 140-2/3 | Compatible with required cryptographic modules |
| FedRAMP | Access control, audit/accountability, continuous monitoring, identity |
| GDPR | Technical measures for personal data protection, accountability logging |
| CPRA | Reasonable security procedures for personal information protection |

## Prerequisites
- Twingate deployment (Connectors, Resources, Groups configured)
- Identity provider integration for centralized user management
- Device posture policies configured (for MFA/device requirements)

## Gotchas
- Twingate *assists* with compliance controls but is not a complete compliance solution on its own
- FIPS compatibility means Twingate does not interfere with FIPS-validated encryption, but verify your full stack independently
- PCI DSS requirement 7.3 specifically is called out; other PCI requirements need separate controls

## Related Docs
- [Guide to GDPR Compliance for IT Teams](https://www.twingate.com/docs)
- [Guide to SOC 2](https://www.twingate.com/docs)
- [Guide to SOX Compliance for IT Teams](https://www.twingate.com/docs)
- Twingate & GDPR
- Twingate & HIPAA
- Twingate & PCI DSS
- Twingate & SOC 2