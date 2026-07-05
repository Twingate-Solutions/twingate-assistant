# Twingate Security Overview

## Page Title
Twingate Security Posture, Practices, and Processes

## Summary
Documents Twingate's internal security practices and product security architecture for customer transparency. Covers organizational security controls, data handling, and the product's zero-trust architectural principles. Last updated October 2024.

## Key Information

### Organizational Security
- CTO holds primary responsibility for information security program
- Annual SOC 2 Type 2 audit (request copy from Twingate contact)
- All employees complete security training at onboarding + periodic refreshers
- U.S. employees undergo third-party background checks (SSN trace, criminal, OFAC/SDN)
- Written DRP/BCP maintained; infrastructure hosted across multiple GCP data centers

### Data Protection
- **In transit**: TLS/SSL
- **At rest**: AES-256+ on GCP-managed databases; data keys encrypted with rotating master key stored in secure keystore
- Cipher selection follows **NIST SP 800-52 Rev. 2**
- Twingate does **not** store customer passwords
- Daily automated database backups; tested regularly
- Permanent data deletion available on request

### Access Control
- Production access via Twingate itself + IdP SSO + MFA
- Least privilege provisioning; resource-level (not network-level) access control
- Developers have **no direct database access** and generally no SSH access to production servers
- Automated CI/CD removes need for human production environment changes

### Vendor Management
- Security due diligence and risk assessment required before vendor engagement
- Written contracts required covering confidentiality, security, privacy, SLAs

## Product Architecture (Zero Trust)

- No single component can unilaterally authorize traffic — multiple components run independent checks
- User data flows and authentication flows handled by **separate components**
- Authentication delegated to third-party IdP (separation of concerns)
- **End-to-end encrypted user data flows** — relay nodes on Twingate infrastructure cannot decrypt traffic
- No public gateway exposure; customer networks invisible to public internet
- Extensive logging for monitoring and audit

## Security Testing
- All code requires peer review via PR before merge
- Static analysis tooling for proprietary code and third-party library CVEs
- Third-party testing by **Hacker House**: white-box analysis, reverse engineering, fuzzing, threat modeling, source code review
- Customer penetration testing permitted with **prior written approval** from Twingate security team

## Configuration Values / Policies
| Control | Value |
|---|---|
| Encryption at rest | AES-256 minimum |
| Cipher standard | NIST SP 800-52 Rev. 2 |
| Backup frequency | Daily |
| Policy review cycle | Annual minimum |
| Audit type | SOC 2 Type 2 (annual) |

## Gotchas
- Penetration testing requires advance approval and may require a signed agreement — contact your account manager first
- Subdomain allocation is at Twingate's discretion; they can revoke subdomains for trademark/spoofing violations
- Customer data is **never** used in test environments
- No custom cryptographic implementations used

## Related Docs
- [Twingate Customer Agreement](https://www.twingate.com/docs/customer-agreement)
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [Service Status](https://status.twingate.com)