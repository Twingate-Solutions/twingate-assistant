# Twingate Responsible Disclosure Policy

## Summary
Twingate's responsible disclosure policy outlines how security researchers should report vulnerabilities. Reports are submitted via email, with a commitment to resolve critical issues within 5 business days. Researchers must follow strict rules around data access, confidentiality, and scope.

## Key Information
- **Contact**: security@twingate.com
- **Resolution target**: Critical issues within 5 business days of disclosure
- **Acknowledgement**: Receipt confirmed within 5 business days
- **All assessments are final**

## Rules for Researchers
- Only test against accounts you own or have explicit permission to access
- Do not exploit discovered vulnerabilities
- Keep all bug disclosure communications confidential (no third-party disclosure without Twingate consent)
- Destroy all artifacts (POC code, videos, screenshots) after bug report is closed
- Do not proceed further if a severe vulnerability granting system access is found — report immediately
- Twingate has sole discretion over bug prioritization and remediation approach

## Out of Scope — Endpoints/Systems
- twingate.com (company site)
- docs.twingate.com
- forum.twingate.com
- status.twingate.com
- help.twingate.com
- trust.twingate.com
- Subdomains: `email`, `packages`, `sales`
- Third-party hosted sites (unless they expose an in-scope weakness)

## Out of Scope — Vulnerability Types
- DDoS attacks
- Spamming
- Physical property/data center attacks

## Reporting Requirements
Include in your email:
- Detailed vulnerability description
- Step-by-step reproduction steps
- Do not include out-of-scope issues

## Gotchas
- Policy does **not** authorize access to any data that isn't yours, including Twingate internal data or other users' data
- Threatening behavior toward Twingate personnel is prohibited
- Third-party site vulnerabilities only qualify if they demonstrably affect an in-scope endpoint
- Scope is limited — most public-facing Twingate web properties are explicitly excluded

## Related Docs
- [Vulnerability Reporting Acknowledgements](https://www.twingate.com/docs/responsible-disclosure-policy) (linked from policy page)
- Policy updates tracked at: `https://docs.twingate.com/docs/responsible-disclosure-policy`