## Twingate Security

Comprehensive security posture document covering Twingate's internal information security practices and product security architecture. Last updated October 2024.

**People & Governance:**
- CTO owns the information security program; cross-disciplinary security team includes senior management
- Written policies reviewed annually; periodic risk reviews feed ongoing improvements
- All US employees: background checks (SSN trace, criminal, OFAC/SDN); international: per local law
- All employees and contractors sign confidentiality agreements
- Annual security training + periodic refreshers; policy acknowledgement required

**Data Protection:**
- Least-privilege access provisioning; Twingate used internally to secure production resource access (with MFA via SSO)
- Production environment changes automated via CI/CD; developers have no direct database access and generally no SSH access to production
- Data encrypted in transit (TLS/SSL) and at rest (GCP managed database, AES-256+, with symmetric keys; master key stored in secure keystore)
- No custom cryptographic implementations; follows NIST SP 800-52 Rev. 2
- Automated daily database backups; stored for limited period; regularly tested
- Customer passwords never stored (delegated to IdPs)

**Infrastructure:**
- GCP multi-datacenter, redundant, geographically distributed; DDoS protection; 24/7 monitoring
- Docker containers on Kubernetes; pre-hardened GCP server infrastructure
- Commercially available secrets management system
- SOC 2 Type 2 report available (annual audits)

**Product Security:**
- All code changes require peer review via PR; production changes require at least one non-author approval
- Static analysis of proprietary code and third-party library CVEs
- Third-party security testing by Hacker House (white-box, reverse engineering, fuzzing, threat modeling, runtime/source code review)
- Customer pen testing permitted with prior approval and advance notice to the security team

**Architecture Principles:**
- No single component can independently authorize traffic; multiple components run independent checks
- Authentication delegated to IdP (separation of concerns); auth and data flows use separate components
- End-to-end encryption of data flows; Twingate relays cannot decrypt user traffic
- No public-facing gateway required; customer networks remain invisible to the internet
- Resource-level (not network-level) access control; extensive logging for audit and investigation

**Related Docs:**
- /docs/soc-2 -- SOC 2 report access
- /docs/twingate-customer-data -- Customer data processing details
- /docs/responsible-disclosure-policy -- Vulnerability reporting
- /docs/service-reliability -- Infrastructure availability
