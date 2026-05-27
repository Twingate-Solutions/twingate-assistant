# Twingate Security Posture

## Summary
Documents Twingate's security practices and product architecture for customers and prospects. Covers both organizational InfoSec practices and product-level security design. Updated October 2024.

---

## Key Information

### Organizational Security
- **Governance**: CTO owns InfoSec program; cross-disciplinary security team with senior management
- **Policies**: Written InfoSec plans reviewed annually + periodic risk reviews
- **Employee checks**: Background checks (SSN, criminal, OFAC/SDN) for US employees; local equivalents elsewhere
- **Access model**: Least privilege + RBAC; production access via Twingate + SSO + MFA
- **Developers**: No direct DB access to customer data; generally no SSH into production servers
- **Encryption in transit**: TLS/SSL; **at rest**: AES-256 on GCP-managed databases with rotating master keys
- **Cipher selection**: Follows NIST SP 800-52 Rev. 2
- **Backups**: Automated daily, tested regularly, retained for limited period
- **Compliance**: SOC 2 Type 2 (annual audits) — request via Twingate account contact

### Vendor & Infrastructure
- Vendor due diligence includes security risk assessment before engagement
- Infrastructure: GCP multi-region, Kubernetes/Docker, pre-hardened servers
- Secrets management via commercial third-party system
- DDoS protection via GCP; 24/7 monitoring; status at `status.twingate.com`

---

## Product Security Architecture

### Core Principles
- Zero-trust: every resource request authenticated, verified, authorized
- No single component can independently allow traffic — multiple components run multiple checks
- User data flows and authentication flows handled by **separate components**
- Authentication delegated to third-party IdP (separation of concerns)
- **End-to-end encrypted user data flows** — relay infrastructure cannot decrypt traffic

### Customer-Facing Security Benefits
- No public gateway exposure — network invisible to public internet
- Resource-level (not network-level) access restrictions
- Centralized access management with audit logging
- Extensive logging for monitoring and investigation

---

## Development & Testing
- All code requires peer review via PR; at least one approver other than author
- Static analysis tooling for proprietary code and third-party library CVEs
- Third-party security testing by **Hacker House**: white-box analysis, reverse engineering, fuzzing, threat modeling, source code review
- Customer data never used in testing

---

## Customer Data Handled
- User details: email, name, group membership (no passwords stored)
- Infrastructure info: network/resource details, ACLs
- Event logs: logins, token requests
- Crash/error reports for diagnostics

---

## Gotchas
- Penetration testing against Twingate systems requires **prior written approval** — contact account manager
- Subdomain allocation (tenant URLs) is at Twingate's discretion per Customer Agreement
- No custom cryptographic implementations used
- Twingate cannot decrypt customer data flows even through its own relay infrastructure

---

## Related Docs
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [Twingate Customer Agreement](https://www.twingate.com/customer-agreement)
- [Status Page](https://status.twingate.com)
- NIST SP 800-52 Rev. 2 (cipher guidance)