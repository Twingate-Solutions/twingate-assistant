# Twingate Compliance Use Case

## Page Title
Compliance Use Cases

## Summary
Twingate provides security controls that help organizations meet requirements across multiple compliance frameworks including SOC 2, PCI DSS, HIPAA, GDPR, and others. It centralizes access management, enables least-privilege controls, and provides audit logging to satisfy compliance auditors. It replaces traditional VPNs with application-level access controls.

## Key Information
- Supports granular, least-privilege access with MFA and device posture enforcement per resource
- Single management plane for access reviews and audit evidence generation
- Rapid offboarding: disable all resource access in a few clicks
- Network activity logging and analytics for anomaly detection
- Hides network from public internet; eliminates public-facing gateways

## Compliance Frameworks Supported

| Framework | Relevant Controls |
|-----------|------------------|
| **SOC 2** | Access controls, network security, risk assessments |
| **PCI DSS** | Requirement 7.3 – access control system for cardholder data environment |
| **HIPAA** | Access controls, entity authentication, transmission security |
| **HITRUST CSF** | Network/application/remote access controls, audit logging, network monitoring |
| **SOX** | Access/authentication, user account management, network security, monitoring |
| **FIPS 140-2/140-3** | Compatible with FIPS-validated cryptography; does not break end-to-end encryption |
| **FedRAMP** | Access control, audit/accountability, continuous monitoring, identification/authentication |
| **GDPR** | Technical measures for personal data protection; accountability via logging |
| **CPRA** | "Reasonable" security procedures for personal information protection |

## Prerequisites
- Twingate deployment (Connectors, Relays, Admin console)
- Identity provider integration for centralized user management
- Device posture configuration (if required by compliance policy)

## Gotchas
- Twingate assists with compliance controls but does not provide full compliance certifications on its own — organizations must implement additional program-specific controls
- PCI DSS coverage is specifically called out for **Requirement 7.3** (access control systems); other PCI requirements may need separate tooling
- FIPS 140-2/3 compatibility means Twingate won't break FIPS-required encryption, but verify your specific cryptographic module configurations independently

## Configuration Values
No specific CLI flags or API parameters documented on this page. Relevant features to configure:
- MFA enforcement (per resource or group policy)
- Device posture checks (policy settings in Admin console)
- Activity logs / analytics (enable in Admin console for audit trails)

## Related Docs
- [Guide to GDPR Compliance for IT Teams](https://www.twingate.com/docs)
- [Guide to SOC 2](https://www.twingate.com/docs)
- [Guide to SOX Compliance for IT Teams](https://www.twingate.com/docs)
- Twingate & GDPR
- Twingate & HIPAA
- Twingate & PCI DSS
- Twingate & SOC 2