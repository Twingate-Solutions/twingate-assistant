---
source: https://www.twingate.com/docs/twingate-security
type: docs
fetched: 2026-08-14
source_version: d034365335a7dc3ffc715c106ee787ff2333701ecf85d3b440ea75d13b377f2b
---

# Twingate Security Posture

## Page Title
Twingate Security (Last updated October 2024)

## Summary
Documents Twingate's internal information security practices and product security architecture for customer due diligence. Covers people security, data handling, infrastructure controls, and product design principles. Twingate holds SOC 2 Type 2 certification and undergoes annual audits.

## Key Information

### Certifications & Audits
- SOC 2 Type 2 report (annual audits) — request copy from Twingate contact
- Third-party security testing via Hacker House (penetration testing, fuzzing, reverse engineering, threat modeling)
- Service status at `status.twingate.com`

### Data Handling
- Customer data stored in GCP-managed databases encrypted at rest with **AES-256**
- In transit: **TLS/SSL**; keys encrypted with master key in secure keystore
- Twingate does **not** store customer passwords (delegates auth to IdP)
- Data types collected: user details (email, name, group membership), infrastructure info (network/resource details, ACLs), event logs, crash reports
- Customer data **not** used for testing
- Daily automated backups; stored limited period; regularly tested

### Access Controls
- Production access secured via Twingate itself + IdP SSO + MFA
- Principle of least privilege; resource-level (not network-level) access control
- Developers have no direct database access; no SSH access to production servers
- Automated CI/CD deployment removes need for human production access

### Cipher Policy
- Follows **NIST SP 800-52 Rev. 2** recommendations

### Infrastructure
- Hosted on **Google Cloud Platform** across multiple physically separated data centers
- Servers run Docker containers orchestrated with **Kubernetes**
- GCP provides pre-hardened servers and DDoS protection

## Product Architecture Principles
- No single component can independently authorize traffic — multiple components perform separate validation checks
- User data flows and authentication flows handled by **separate components**
- End-to-end encrypted data flows — relay infrastructure **cannot decrypt** user data
- Authentication delegated to third-party IdP (separation of concerns)
- Networks not publicly exposed; customer infrastructure invisible to public internet

## Gotchas
- Penetration testing by customers requires **prior written approval** and advance notice to Twingate security team; may require signed agreement
- Subdomain allocation is at Twingate's discretion under the Customer Agreement
- Background checks outside the U.S. vary by local law
- Employee offboarding access revocation is documented but timing described only as "timely manner"

## Configuration Values / Standards
| Control | Standard/Tool |
|---|---|
| Encryption at rest | AES-256 |
| Encryption in transit | TLS/SSL |
| Cipher selection | NIST SP 800-52 Rev. 2 |
| Infrastructure | GCP + Kubernetes + Docker |
| Secrets management | Commercial vendor (unnamed) |
| MDM | Yes (vendor unnamed) |
| SAST | Multiple tools (unnamed) |

## Related Docs
- [Twingate Customer Agreement](https://www.twingate.com/customer-agreement)
- [GCP Physical Security](https://cloud.google.com/security/infrastructure)
- [status.twingate.com](https://status.twingate.com)