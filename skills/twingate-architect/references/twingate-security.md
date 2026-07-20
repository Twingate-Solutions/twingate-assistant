# Twingate Security Posture

## Page Title
Twingate Security (Last updated October 2024)

## Summary
Documents Twingate's internal information security practices and product security architecture for customer transparency. Covers people security, data protection, infrastructure, and product design principles. Includes SOC 2 Type 2 compliance and third-party security testing details.

## Key Information

### Compliance & Audits
- SOC 2 Type 2 report available (annual audits); request via Twingate contact
- Third-party security testing by Hacker House (penetration testing, reverse engineering, fuzzing, threat modeling)
- NIST SP 800-52 Rev. 2 cipher recommendations followed

### Data Encryption
- **In transit**: TLS/SSL
- **At rest**: GCP-managed database, AES-256+, symmetric keys with master key in secure keystore
- No custom/proprietary cryptographic implementations
- Twingate does **not** store customer passwords

### Data Handling
- Customer data types: user details (email, names, group membership), infrastructure info (network/resource details, ACLs), event logs, crash reports
- Automated daily database backups, stored for limited period, regularly tested
- Customer data permanently deleted upon request per contractual terms
- Customer data **not** used for testing

### Access Control
- Principle of least privilege; role-based provisioning
- Internal access secured via Twingate + IdP SSO + MFA
- Developers have **no** direct database access; generally no SSH access to production servers
- Automated CI/CD removes need for manual production changes

### Infrastructure
- Hosted on GCP, multi-region for redundancy
- Docker containers orchestrated with Kubernetes
- Pre-hardened GCP server infrastructure
- Commercial secrets management system for tokens, passwords, API credentials, certificates
- Service status: `status.twingate.com`

## Product Architecture Principles
- No single component can independently authorize traffic — multiple components run multiple checks
- User data flows and authentication flows handled by **separate** components with separate validation
- Authentication delegated to third-party IdP (separation of concerns)
- End-to-end encrypted user data flows; relay infrastructure **cannot decrypt** traffic
- Networks not publicly exposed; invisible to public internet

## Prerequisites
- Penetration testing requires prior written approval from Twingate security team + advance notice of timing/scope; may require signed agreement
- Subdomain allocation governed by Twingate Customer Agreement

## Configuration Values
- None (security posture document, not implementation guide)

## Gotchas
- Twingate relays handle traffic but **cannot decrypt** it — architecture by design
- Subdomain names ultimately controlled by Twingate; trademark/spoofing violations can result in action
- Background checks outside the U.S. vary by local law

## Related Docs
- [Twingate Customer Agreement](https://www.twingate.com/customer-agreement)
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [status.twingate.com](https://status.twingate.com)