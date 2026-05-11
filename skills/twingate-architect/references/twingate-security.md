# Twingate Security Posture & Practices

## Page Summary
Documents Twingate's information security practices and product security architecture for customer evaluation. Covers organizational security controls, data handling, and product design principles. Last updated October 2024.

## Key Information

### Organizational Security
- **Governance**: CTO owns security program; cross-disciplinary security team includes senior management
- **SOC 2 Type 2**: Annual audits conducted; request report via Twingate contact
- **Employee controls**: Background checks (US: SSN trace, criminal, OFAC/SDN), NDAs, documented offboarding
- **Training**: Security training at onboarding + periodic refreshers; policy acknowledgment required

### Data Protection
- **Encryption in transit**: TLS/SSL for all client app communications
- **Encryption at rest**: GCP-managed database, AES-256+, symmetric keys with master key rotation
- **Cipher selection**: Follows NIST SP 800-52 Rev. 2 recommendations
- **No custom cryptography**: Uses only standard implementations
- **No password storage**: Authentication delegated to third-party IdPs
- **Backups**: Automated daily backups, regularly tested, limited retention period
- **Data deletion**: Permanent secure deletion on request or per contract

### Access Controls
- **Internal access**: Twingate + IdP SSO + MFA for all production resource access
- **Principle of least privilege**: Resource-level (not network-level) access controls
- **Developer access**: No direct database access; no SSH to production servers generally
- **Automated deployments**: CI/CD pipeline removes need for human production access

### Infrastructure
- **Platform**: Google Cloud Platform, multi-region for redundancy
- **Containers**: Docker + Kubernetes
- **Secrets**: Commercial secrets management system (major vendor)
- **DDoS**: GCP-provided protection
- **Status page**: `status.twingate.com`

## Product Security Architecture

### Core Design Principles
1. Every resource request must be authenticated, verified, and authorized
2. Users access only explicitly granted resources
3. Comprehensive logging for monitoring and investigation

### Key Architectural Properties
- **No single point of authorization**: Multiple components run multiple checks; data flow and auth flow are separate
- **End-to-end encryption**: User data encrypted even through Twingate-controlled relays — Twingate cannot decrypt traffic
- **IdP delegation**: Authentication handled by customer's identity provider
- **No public exposure**: Customer networks invisible to public internet

### Customer Data Handled
- User details: email, names, group membership (no passwords)
- Infrastructure info: network/resource details, ACLs
- Event logs: user logins, token requests
- Crash/error reports for diagnostics

## Development Practices
- All code requires peer review via PR; production changes require ≥1 approver
- Static analysis tools for proprietary code and third-party library vulnerabilities
- Third-party security testing by **Hacker House**: white-box analysis, reverse engineering, fuzzing, threat modeling
- Customer data never used in testing

## Penetration Testing
- Customer pen testing permitted with **prior written approval** from Twingate security team
- Must provide advance notice of timing and scope
- May require signed agreement
- Contact account manager to initiate

## Gotchas
- Subdomain allocation (`.twingate.com`) is at Twingate's discretion; they can reassign for policy violations
- Physical security relies entirely on GCP data centers (no Twingate-owned facilities)
- No fixed offices; physical security responsibility placed on individual employees

## Related Docs
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [Twingate Customer Agreement](https://www.twingate.com/docs/customer-agreement)
- [Status Page](https://status.twingate.com)
- NIST SP 800-52 Rev. 2