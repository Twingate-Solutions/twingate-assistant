# Twingate Security Posture

## Page Title
Twingate Security — Customer-Facing Security Documentation

## Summary
Documents Twingate's internal security practices and product security architecture for customer due diligence. Covers people security, data handling, infrastructure controls, and product design principles. Last updated October 2024.

## Key Information

### Certifications & Audits
- SOC 2 Type 2 report (annual audits) — request via account contact
- Third-party security testing by Hacker House (pen testing, fuzzing, reverse engineering, threat modeling)

### Data Handling
- Customer data encrypted in transit (TLS/SSL) and at rest (AES-256+)
- GCP-managed database with envelope encryption (data keys encrypted by master key in secure keystore)
- No custom cryptographic implementations
- Follows NIST SP 800-52 Rev. 2 cipher recommendations
- No customer passwords stored (auth delegated to IdP)
- Daily automated backups; tested regularly
- Data types collected: user details (email, name, group), infrastructure info (network/resource details, ACLs), logs, crash/error reports

### Access Controls
- Production access secured via Twingate + IdP SSO + MFA
- Least privilege provisioning; resource-level (not network-level) access control
- Developers have no direct database access; no SSH to production servers
- Automated CI/CD removes need for manual production changes

### Infrastructure
- Multi-region GCP deployment for redundancy and DDoS protection
- Kubernetes/Docker on pre-hardened GCP infrastructure
- 24/7 automated monitoring; status at `status.twingate.com`
- Commercial secrets management system for tokens, passwords, API credentials

### People Security
- CTO owns information security program
- US employee background checks: SSN trace, criminal, OFAC/SDN
- Security training at onboarding + periodic refreshers
- Documented offboarding process with timely access revocation

## Product Architecture Security Principles
- No single component can independently authorize traffic — multiple components, multiple checks
- Auth flows and data flows separated, handled by different components
- User data flows encrypted end-to-end; relay nodes cannot decrypt traffic
- Authentication fully delegated to third-party IdP
- No public gateway exposure — networks invisible to public internet
- Extensive logging built in

## Configuration Values / Policies
- Cipher selection: NIST SP 800-52 Rev. 2
- Encryption at rest: AES-256 minimum
- Backup retention: limited period (specific duration not disclosed)

## Gotchas
- Penetration testing requires **prior written approval** and advance notice to security team; may require signing an agreement — contact account manager
- Subdomain allocation (`*.twingate.com`) is at Twingate's discretion; they can revoke for trademark/spoofing violations
- SOC 2 report not publicly available — must be requested from Twingate contact
- Specific backup retention period and RTO/RPO targets not disclosed publicly

## Prerequisites
- N/A (reference/informational document)

## Related Docs
- [Twingate Customer Agreement](https://www.twingate.com/customer-agreement)
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [Twingate Status Page](https://status.twingate.com)
- NIST SP 800-52 Rev. 2