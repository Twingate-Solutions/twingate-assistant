# Twingate Security Posture

## Page Title
Twingate Security (Last updated October 2024)

## Summary
Documents Twingate's internal information security practices and product security architecture for customer due diligence. Covers people/data/infrastructure security controls and product design principles. Relevant for security reviews, vendor assessments, and compliance evaluations.

## Key Information

### Compliance & Audits
- SOC 2 Type 2 report available (annual audits) — request via account manager
- Third-party pen testing by Hacker House (white-box, component-level analysis)
- Customer pen testing permitted with prior written approval from security team

### Data Handling
- **Encryption in transit**: TLS/SSL
- **Encryption at rest**: GCP-managed AES-256+, envelope encryption with rotating master keys
- **Cipher guidance**: NIST SP 800-52 Rev. 2
- Twingate stores: user details (email, name, group membership), infrastructure/network config, access logs, crash reports
- Twingate does **not** store customer passwords (auth delegated to IdP)
- Daily automated database backups; tested regularly
- Data deletion on request per contract terms

### Access Controls
- Production access via Twingate + IdP SSO + MFA
- Developers have no direct DB access; minimal/no SSH to production servers
- Least-privilege provisioning; automated deployment pipeline removes need for human production access

### Infrastructure
- Hosted on GCP across multiple physically separated data centers
- Docker containers on Kubernetes
- 24/7 automated monitoring; status at `status.twingate.com`
- Commercially available secrets management system (major vendor)

### Product Architecture Security Principles
- No single component can independently authorize resource access — multiple components/checks required
- User data flows and auth flows handled by **separate components**
- End-to-end encrypted user data flows; relay infrastructure **cannot decrypt** traffic
- Customer networks not publicly exposed (no public gateway)
- Access scoped to specific resources, not entire networks

## Prerequisites
- SOC 2 report requires contacting Twingate account manager
- Customer penetration testing requires prior approval + possible agreement signing

## Configuration Values
- N/A (architectural/policy document, no configurable parameters)

## Gotchas
- Subdomain allocation (`*.twingate.com`) is at Twingate's discretion per Customer Agreement — trademark/spoofing violations can result in action
- Customer data is **never** used in testing environments
- Background checks outside the U.S. vary by local law

## Related Docs
- [Twingate Customer Agreement](https://www.twingate.com/docs/customer-agreement)
- [GCP Physical Security](https://cloud.google.com/security/overview)
- [Service Status](https://status.twingate.com)
- NIST SP 800-52 Rev. 2 (cipher selection reference)