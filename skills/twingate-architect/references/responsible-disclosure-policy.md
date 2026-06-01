# Twingate Responsible Disclosure Policy

## Summary
Twingate's responsible disclosure policy outlines how security researchers should report vulnerabilities. Reports are submitted via email, with a commitment to resolve critical issues within 5 business days. Researchers must follow defined rules and scope limitations.

## Key Information
- **Contact**: security@twingate.com
- **Response time**: Acknowledgment within 5 business days; critical issues resolved within 5 business days of disclosure
- **All assessments are final**
- Prioritization of bug fixes is at Twingate's sole discretion

## Rules for Researchers
- Only test against accounts you own or have explicit permission to access
- Do not exploit discovered vulnerabilities for any benefit
- Keep all bug communications confidential (no third-party disclosure without Twingate consent)
- Destroy all artifacts (POC code, videos, screenshots) after bug report is closed
- Report severe system-access vulnerabilities immediately and stop further investigation
- No threatening behavior toward Twingate personnel

## Out of Scope — Endpoints
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
- Step-by-step reproduction instructions
- Do not reference out-of-scope items

## Gotchas
- Policy explicitly does **not** authorize access to other users' data, Twingate internal data, or any personal data
- Researchers may not disclose bug details publicly before Twingate resolves the issue
- Artifacts must be destroyed after closure — not just upon request

## Related Docs
- Vulnerability Reporting Acknowledgements (linked from policy page)
- Policy updates tracked at: `https://docs.twingate.com/docs/responsible-disclosure-policy`