# Twingate Security Overview

## Page Title
Twingate Security — Customer-Facing Security Posture Documentation

## Summary
Documents Twingate's internal security practices and product security architecture for customer/prospect evaluation. Covers people security, data handling, infrastructure, and product design principles. Last updated October 2024.

## Key Information

### Certifications & Audits
- SOC 2 Type 2 report (annual audits) — request via account contact
- Third-party security testing by Hacker House (penetration testing, white-box analysis, fuzzing, threat modeling)

### Data Handling
- Customer data encrypted in transit (TLS/SSL) and at rest (AES-256+)
- Hosted on Google Cloud Platform managed databases
- Encryption keys use envelope encryption with master keys rotated regularly
- No custom cryptographic implementations; follows NIST SP 800-52 Rev. 2
- Daily automated database backups with regular restore testing
- Twingate does **not** store customer passwords (delegated to IdP)
- Customer data types stored: user details (email, name, group membership), infrastructure info (network/resource details, ACLs), event logs, crash reports

### Access Controls
- Production access via Twingate + SSO + MFA
- Principle of least privilege enforced at resource level
- Developers have no direct database access; no SSH access to production servers
- Automated CI/CD removes need for human access to production environment

### Product Architecture Security Principles
- No single component can independently authorize traffic — multiple components run multiple checks
- User data flows and authentication flows handled by **separate components**
- Authentication delegated to third-party IdP (separation of concerns)
- User data flows encrypted end-to-end; Twingate **cannot decrypt** relay traffic
- No public gateway exposure — customer networks invisible to public internet
- Resource-level (not network-level) access restrictions

## Prerequisites
- For penetration testing: requires prior written approval from Twingate security team, advance notice of timing/scope, may require signed agreement

## Configuration Values / Policies
| Area | Detail |
|------|--------|
| Cipher standard | NIST SP 800-52 Rev. 2 |
| Encryption at rest | AES-256 or better |
| Backup frequency | Daily |
| Policy review cycle | At least annually |
| Code review requirement | Minimum 1 approver via PR for all production changes |

## Gotchas
- Penetration testing requires **pre-approval** — do not initiate without contacting account manager
- Subdomain allocation (`.twingate.com`) is at Twingate's discretion; they can revoke for trademark/spoofing violations
- Physical security relies on GCP data center security; Twingate has no fixed offices
- Background checks outside the U.S. vary by local law

## Related Docs
- [GCP Physical Security](https://cloud.google.com/security/infrastructure/design) (referenced externally)
- [Twingate Customer Agreement](https://www.twingate.com/docs/customer-agreement) (subdomain policy)
- [status.twingate.com](https://status.twingate.com) — service status and maintenance