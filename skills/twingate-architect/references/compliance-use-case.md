# Twingate Compliance Use Cases

## Page Title
Compliance Use Case Overview

## Summary
Twingate supports implementation of security controls for major compliance frameworks including SOC 2, PCI DSS, HIPAA, GDPR, FedRAMP, and others. It provides centralized access control, audit logging, least-privilege enforcement, and network visibility to satisfy technical requirements across regulatory regimes.

## Key Information

**Core Capabilities for Compliance:**
- Granular least-privilege access controls per resource/application
- MFA and device posture enforcement (including on apps that don't natively support them)
- Centralized access management and review dashboard
- Audit logging and network activity analytics
- Application-level access control (replaces VPN/network-level)
- Eliminates public-facing gateways

**Supported Compliance Frameworks:**
| Framework | Key Coverage Area |
|-----------|------------------|
| SOC 2 | Access controls, network security, risk assessments |
| PCI DSS | Cardholder data environment, Requirement 7.3 (access control system) |
| HIPAA | Access controls, authentication, transmission security |
| HITRUST CSF | Access controls, network monitoring, audit logging |
| SOX | Access/auth, user account management, network security, monitoring |
| FIPS 140-2/3 | Compatible; does not compromise FIPS-validated encrypted communications |
| FedRAMP | Access control, audit/accountability, continuous monitoring, identity |
| GDPR | Technical measures for personal data protection, accountability logging |
| CPRA | Reasonable security procedures for personal information protection |

## Prerequisites
- Twingate deployed with Connectors and Relays configured
- Resources defined within Twingate for access control enforcement
- Identity provider integration for centralized user management and offboarding

## Gotchas
- Twingate assists with compliance controls but does not itself certify or guarantee compliance — organizations must implement controls appropriately
- FIPS compatibility is noted as non-compromising, not as a certified FIPS module itself
- PCI DSS coverage is specifically scoped to Requirement 7.3; other PCI requirements need separate controls

## Related Docs
- [Guide to GDPR Compliance for IT Teams](https://www.twingate.com/docs)
- [Guide to SOC 2](https://www.twingate.com/docs)
- [Guide to SOX Compliance for IT Teams](https://www.twingate.com/docs)
- Twingate & GDPR
- Twingate & HIPAA
- Twingate & PCI DSS
- Twingate & SOC 2