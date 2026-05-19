# Twingate Compliance Use Cases

## Page Title
Compliance

## Summary
Twingate provides security controls that support multiple compliance frameworks including SOC 2, PCI DSS, HIPAA, GDPR, and others. It centralizes access management, enables granular least-privilege controls, and provides audit logging to satisfy compliance requirements. No native compliance certification is claimed; Twingate assists in *implementing* required controls.

## Key Information
- Supports granular, per-application access policies (MFA, device posture) regardless of whether the app natively supports them
- Single management plane for access reviews and audit evidence production
- Hides network from public internet by eliminating public-facing gateways
- Rapid offboarding: disable all Twingate-secured resource access in one action
- Network activity logging and analytics for anomaly detection

## Compliance Program Coverage

| Framework | Primary Use |
|-----------|-------------|
| SOC 2 | Access controls, network security, risk assessments |
| PCI DSS | Secures cardholder data environment; fulfills Requirement 7.3 |
| HIPAA | Access controls, entity authentication, transmission security |
| HITRUST CSF | Access controls, audit logging, network traffic monitoring |
| SOX | Financial system access/auth, user account management, monitoring |
| FIPS 140-2/3 | Compatible with FIPS-validated encryption (does not break it) |
| FedRAMP | Access control, audit/accountability, continuous monitoring |
| GDPR | Technical measures for personal data protection, accountability logging |
| CPRA | "Reasonable" security procedures for personal information protection |

## Prerequisites
- Twingate deployed with Connectors protecting target resources
- Resources grouped and assigned to appropriate Access Policies
- Identity provider integrated for centralized user/group management
- Device posture checks configured if required by framework

## Gotchas
- Twingate *assists* compliance—it does not make an organization automatically compliant with any framework
- FIPS 140-2/3 compatibility means Twingate does not interfere with end-to-end encrypted communications; verify your own crypto modules separately
- PCI DSS Requirement 7.3 specifically addressed; review other PCI DSS requirements independently
- Offboarding disables Twingate-secured access only—separate accounts on resources require independent deprovisioning

## Related Docs
- [Guide to GDPR Compliance for IT Teams](https://www.twingate.com/docs/)
- [Guide to SOC 2](https://www.twingate.com/docs/)
- [Guide to SOX Compliance for IT Teams](https://www.twingate.com/docs/)
- Twingate & GDPR
- Twingate & HIPAA
- Twingate & PCI DSS
- Twingate & SOC 2