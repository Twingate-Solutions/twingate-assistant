---
source: https://www.twingate.com/docs/responsible-disclosure-policy
type: docs
fetched: 2026-08-14
source_version: 811c5f9f1be42878ff78b02d821313a21ed41324267bd4a4048642fa02da0324
---

# Twingate Responsible Disclosure Policy

## Summary
Twingate's responsible disclosure policy outlines how security researchers should report vulnerabilities. Reports are submitted via email, and Twingate aims to resolve critical issues within 5 business days. Researchers must follow specific rules around data access, confidentiality, and scope.

## Key Information
- **Contact**: security@twingate.com
- **Response SLA**: Acknowledgment within 5 business days; critical issues resolved within 5 business days of disclosure
- **All assessments are final**
- Prioritization of bug fixes is at Twingate's sole discretion

## Out-of-Scope Systems
- twingate.com (company site)
- docs.twingate.com
- forum.twingate.com
- status.twingate.com
- help.twingate.com
- trust.twingate.com
- Subdomains: email, packages, sales
- Third-party hosted sites (unless they expose an in-scope weakness)

## Out-of-Scope Vulnerability Types
- DDoS attacks
- Spamming
- Physical property/data center attacks

## Rules for Researchers
- Only test against accounts you own or have explicit permission to access
- Do not exploit discovered vulnerabilities for any benefit
- Do not disrupt services, violate user privacy, or alter/destroy data
- Report severe system-access vulnerabilities immediately; do not proceed further
- Keep all bug disclosure communications confidential unless Twingate consents to sharing
- **Destroy all artifacts** (POC code, videos, screenshots) after bug report is closed
- No threatening behavior toward Twingate personnel

## Reporting Requirements
Include in your email:
- Detailed vulnerability description
- Step-by-step reproduction instructions
- Do not include out-of-scope items

## Gotchas
- Policy explicitly does **not** authorize access to other users' data, Twingate internal data, or any personal data
- Researchers bear responsibility for destroying all documentation artifacts post-closure
- No public disclosure until Twingate resolves the issue and consents

## Related Docs
- [Vulnerability Reporting Acknowledgements](https://www.twingate.com/docs/responsible-disclosure-policy) (linked from policy page)