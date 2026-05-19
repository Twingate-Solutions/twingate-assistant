# Twingate Security Overview

## Page Title
Twingate Security Posture, Practices, and Processes

## Summary
Documents Twingate's internal security practices and product security architecture as of October 2024. Covers people security, data protection, infrastructure controls, and product-level security design. Intended for customers and prospects evaluating Twingate's security posture.

## Key Information

### Compliance & Auditing
- SOC 2 Type 2 report available (annual audits) — request via Twingate contact
- Third-party security testing by Hacker House (pen testing, reverse engineering, fuzzing, threat modeling)
- Customer penetration testing permitted with prior written approval from security team

### Data Handling
- Customer data stored: email addresses, names, group membership, network/resource details, ACLs, event logs
- **Passwords not stored** — authentication delegated to third-party IdPs
- Encryption at rest: AES-256+ (GCP managed database, envelope encryption with master key rotation)
- Encryption in transit: TLS/SSL
- Cipher selection follows NIST SP 800-52 Rev. 2
- Daily automated database backups; retention limited to disaster recovery window
- Data deletion on request per contractual commitments

### Access Controls
- Principle of least privilege; role-based access provisioning
- Production access via Twingate + IdP SSO + MFA
- Developers lack direct database access and SSH access to production servers
- Automated CI/CD deployment reduces need for human production access

### Infrastructure
- Hosted on GCP across multiple physically separated data centers
- Docker containers orchestrated with Kubernetes
- Secrets managed via commercial secrets management system
- Service status: [status.twingate.com](https://status.twingate.com)

### Product Architecture Security Principles
- No single component independently authorizes traffic — multiple components required
- User data flows and authentication flows are separate with independent validation
- End-to-end encrypted user data flows; Twingate **cannot decrypt** relay traffic
- No public-facing gateway exposed; customer networks invisible to public internet
- Resource-level access (not network-level)

## Prerequisites
- SOC 2 report: requires contacting Twingate account team
- Customer pen testing: requires advance notice, scope approval, and possible agreement signing

## Configuration Values
- None (architecture/policy document, not implementation guide)

## Gotchas
- Twingate controls subdomain allocation under twingate.com; customers cannot unilaterally claim subdomains
- Relay infrastructure is Twingate-controlled but cannot decrypt user data flows
- Customer data must not be used in test environments (Twingate policy)
- Background checks outside the U.S. vary by local law

## Related Docs
- [Twingate Customer Agreement](https://www.twingate.com/customer-agreement)
- [GCP Physical Security](https://cloud.google.com/security/physical-security)
- [status.twingate.com](https://status.twingate.com)
- NIST SP 800-52 Rev. 2 (cipher guidance)