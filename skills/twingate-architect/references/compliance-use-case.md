## Page Title
Compliance

## Summary
Use case overview for using Twingate to implement security controls required by common compliance frameworks. Covers access control, audit logging, offboarding, and least-privilege patterns relevant to SOC 2, PCI DSS, HIPAA, GDPR, FedRAMP, and more.

## Key Information
- **SOC 2**: supports access controls, network security, and risk assessment security trust service criteria
- **PCI DSS**: supports Requirement 7.3 — access control system for cardholder data environment (CDE)
- **HIPAA**: supports technical safeguards: access controls, person/entity authentication, transmission security
- **HITRUST CSF**: supports access control for network traffic, apps, remote work, mobile; audit logging; network security controls
- **SOX**: supports information security controls for financial systems — access, authentication, user account management, monitoring
- **FIPS 140-2/3**: compatible; does not break end-to-end FIPS-validated encryption
- **FedRAMP**: supports access control, audit/accountability, continuous monitoring, identification and authentication control domains
- **GDPR**: supports "appropriate technical measures" requirement; logging supports accountability
- **CPRA**: supports "reasonable security procedures" for personal information protection
- Centralized access review: single console shows who accesses which resources
- Quick offboarding: disable all resource access for a user in one action

## Prerequisites
- Appropriate Twingate plan (Business/Enterprise for full audit log export and MDM/EDR integrations)

## Step-by-Step
Not applicable on this page — see framework-specific guides.

## Configuration Values
None on this page.

## Gotchas
- Twingate is a network access control layer — compliance requires additional controls beyond what Twingate provides (e.g. encryption at rest, application-level auth)
- FIPS 140 compatibility means Twingate does not interfere with FIPS-validated encryption, but Twingate's own encryption is not FIPS-certified independently

## Related Docs
- `/docs/gdpr-compliance` — GDPR guide for IT teams
- `/docs/soc-2` — SOC 2 guide
- `/docs/hipaa-compliance` — HIPAA guide
- `/docs/pci-compliance` — PCI DSS guide
- `/docs/twingate-fips140` — FIPS 140 detail
- `/docs/audit-logs` — audit log export
- `/docs/offboarding-users` — user offboarding
