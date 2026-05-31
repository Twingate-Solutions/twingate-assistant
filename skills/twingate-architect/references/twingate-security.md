# Twingate Security Posture

## Page Title
Twingate Security – Customer-Facing Security Practices and Architecture Overview

## Summary
Documents Twingate's information security program, internal practices, and product architecture security. Covers people/data/infrastructure security controls and product-level architectural decisions. Last updated October 2024.

## Key Information

### Certifications & Audits
- SOC 2 Type 2 report (annual audits); request via Twingate account contact
- Third-party security testing via Hacker House (white-box, reverse engineering, fuzzing, threat modeling)

### Data Handling
- Customer data stored on GCP, encrypted at rest with AES-256+, symmetric keys
- Master keys stored in secure keystore, rotated regularly
- In-transit: TLS/SSL; cipher selection follows NIST SP 800-52 Rev. 2
- No customer passwords stored; authentication delegated to third-party IdP
- Daily automated database backups; tested regularly
- Data deletion available on request per contractual commitments

### Access Controls
- Least-privilege, role-based access provisioning
- Internal resource access secured via Twingate itself + IdP SSO + MFA
- Developers lack direct database access and generally lack SSH access to production
- Automated CI/CD pipeline reduces human production access needs

### Infrastructure
- Multi-region GCP deployment (redundancy + load balancing)
- Docker containers on Kubernetes; GCP pre-hardened servers
- Secrets managed via commercial secrets management system
- All production changes require approval; logged via CI/CD pipeline
- 24/7 monitoring; status available at `status.twingate.com`

### Product Architecture Principles
- No single component can independently authorize traffic
- User data flows and authentication flows handled by **separate components** with separate validation
- User data encrypted **end-to-end**; relay nodes cannot decrypt traffic
- No public gateway exposure; customer networks invisible to public internet
- Resource-level (not network-level) access restrictions

## Prerequisites
- N/A (informational document)

## Configuration Values
- None specified (architecture/policy document)

## Gotchas
- Penetration testing against Twingate systems requires **prior written approval** and advance notice to security team; agreement may be required—contact account manager
- Subdomain allocation is at Twingate's discretion; trademark/spoofing violations can result in remediation action
- Background checks outside the U.S. vary by local law

## Related Docs
- [Twingate Customer Agreement](https://www.twingate.com/docs/customer-agreement)
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [Service Status](https://status.twingate.com)
- NIST SP 800-52 Rev. 2 (cipher guidance)