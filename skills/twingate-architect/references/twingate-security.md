# Twingate Security Posture & Practices

## Page Title
Twingate Security Documentation

## Summary
Comprehensive overview of Twingate's information security posture covering organizational security practices and product-level security architecture. Documents controls for data protection, access management, vendor oversight, and product development security. Last updated October 2024.

## Key Information

### Certifications & Audits
- SOC 2 Type 2 report (annual audits) — request via account contact
- Third-party security testing by Hacker House (pen testing, fuzzing, reverse engineering, threat modeling)

### Data Handling
- Data encrypted **in transit**: TLS/SSL
- Data encrypted **at rest**: AES-256+ on GCP managed databases
- Key encryption: master key in secure keystore, rotated regularly
- Follows NIST SP 800-52 Rev. 2 cipher recommendations
- No customer passwords stored (auth delegated to IdP)
- Daily automated database backups, tested regularly
- Customer data types: user details (email, name, group membership), infrastructure info (network/resource details, ACLs), event logs

### Access Controls
- Production access gated by Twingate + IdP SSO + MFA
- Principle of least privilege enforced at resource (not network) level
- Developers have no direct database access
- No SSH access to production servers required
- Automated CI/CD removes need for human production access

### Infrastructure
- Hosted on GCP, multi-region for redundancy
- Docker containers orchestrated with Kubernetes
- Pre-hardened GCP server infrastructure
- Commercially available secrets management system (major vendor)
- Status page: `status.twingate.com`

### Product Architecture Principles
- No single component can independently authorize traffic — multiple components run multiple checks
- Auth flows and data flows handled by **separate components**
- User data flows encrypted **end-to-end**; relay nodes cannot decrypt traffic
- No public gateway exposure — customer networks invisible to public internet
- Extensive logging for monitoring/investigation

## Prerequisites
- Customers wanting penetration testing must obtain prior approval + give advance notice to security team; may require signed agreement
- Subdomain allocation governed by Twingate Customer Agreement

## Configuration Values
- Cipher selection: NIST SP 800-52 Rev. 2
- Encryption at rest: AES-256 minimum
- Backup retention: limited period (unspecified)

## Gotchas
- Twingate **cannot decrypt** user data flows even when passing through Twingate-controlled relays
- Customer data is **never used for testing**
- Penetration testing requires **advance approval** — unauthorized testing not permitted
- Subdomain claims subject to Twingate discretion; trademark squatting/spoofing addressed by Twingate

## Related Docs
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [Twingate Customer Agreement](https://www.twingate.com/docs/customer-agreement)
- [Status Page](https://status.twingate.com)
- Hacker House (third-party security partner)