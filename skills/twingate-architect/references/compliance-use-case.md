# Twingate Compliance Use Case

## Summary
Twingate supports implementation of security controls required by major compliance frameworks including SOC 2, PCI DSS, HIPAA, GDPR, and others. It provides centralized access management, granular least-privilege controls, and audit logging capabilities that map to specific compliance requirements.

## Key Information

- **Supported Frameworks**: SOC 2, PCI DSS, HIPAA, HITRUST, SOX, FIPS 140-2/140-3, FedRAMP, GDPR, CPRA
- **Core Capabilities**: Least-privilege access, MFA enforcement, device posture checks, centralized access management, network activity logging
- **FIPS Compatibility**: Twingate does not break FIPS 140-2/140-3 end-to-end encrypted communications
- **PCI DSS**: Specifically addresses Requirement 7.3 (access control system for cardholder data environment)
- **Access Reviews**: Single pane of glass for analyzing who accesses which resources; supports audit evidence generation
- **Offboarding**: Disable access to all Twingate-secured resources in a few clicks regardless of per-resource account state

## Compliance Framework Mapping

| Framework | Primary Control Areas |
|-----------|----------------------|
| SOC 2 | Access controls, network security, risk assessments |
| PCI DSS | Cardholder data environment, Requirement 7.3 |
| HIPAA | Access controls, entity authentication, transmission security |
| HITRUST CSF | Network/app/remote access controls, audit logging, traffic monitoring |
| SOX | Access/authentication, user account management, network security, monitoring |
| FedRAMP | Access control, audit/accountability, continuous monitoring, identity |
| GDPR | Personal data protection, accountability, technical safeguards |
| CPRA | Reasonable security procedures for personal information |

## Gotchas

- Twingate assists with compliance controls but does not itself provide certification — organizations still need to complete their own compliance programs
- FIPS compatibility is noted as non-breaking, but verify specific cryptographic module requirements for your environment independently
- Offboarding efficiency applies only to resources secured by Twingate; resources outside Twingate require separate management

## Related Docs

- [Guide to GDPR Compliance for IT Teams](https://www.twingate.com/docs)
- [Guide to SOC 2](https://www.twingate.com/docs)
- [Guide to SOX Compliance for IT Teams](https://www.twingate.com/docs)
- Twingate & GDPR
- Twingate & HIPAA
- Twingate & PCI DSS
- Twingate & SOC 2