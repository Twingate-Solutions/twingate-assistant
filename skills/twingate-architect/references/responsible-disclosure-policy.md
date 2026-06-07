# Twingate Responsible Disclosure Policy

## Page Title
Responsible Disclosure Policy

## Summary
Twingate's responsible disclosure policy outlines how security researchers should report vulnerabilities found in Twingate's service. Reports are submitted via email, and Twingate aims to resolve critical issues within 5 business days. Researchers must follow strict rules around data access, confidentiality, and artifact destruction.

## Key Information
- **Contact**: security [at] twingate.com
- **Response SLA**: Acknowledgement within 5 business days; critical issues resolved within 5 business days of disclosure
- **Scope**: Only in-scope systems (primarily the Twingate service itself, not marketing/docs/support sites)
- All assessments are considered final
- Policy may be revised; canonical URL is `https://docs.twingate.com/docs/responsible-disclosure-policy`

## Rules for Researchers
- Only test against accounts you own or have explicit permission to test
- Do not exploit discovered vulnerabilities for any benefit
- Do not access data belonging to other users
- Keep all bug communications confidential; no third-party disclosure without Twingate consent
- Destroy all artifacts (POC code, videos, screenshots) after bug report is closed
- Report severe/system-access vulnerabilities immediately and stop further investigation
- Bug prioritization is at Twingate's sole discretion

## Out-of-Scope Systems
- twingate.com (company site)
- docs.twingate.com
- forum.twingate.com
- status.twingate.com
- help.twingate.com
- trust.twingate.com
- Subdomains: `email`, `packages`, `sales`
- Third-party hosted sites (unless they expose an in-scope endpoint)

## Out-of-Scope Vulnerability Types
- DDoS attacks
- Spamming
- Physical property or data center attacks

## Reporting Steps
1. Email security [at] twingate.com
2. Describe the vulnerability in detail
3. Include step-by-step reproduction instructions
4. Allow reasonable time for resolution before public disclosure
5. Destroy all documentation artifacts after closure

## Gotchas
- Out-of-scope systems include most of Twingate's public-facing web properties — the core **service/product** is in scope, not the marketing/docs infrastructure
- Third-party site vulnerabilities are only in scope if they lead back to a Twingate endpoint
- Researchers have no rights to retain artifacts post-closure
- No public or third-party disclosure permitted without explicit Twingate consent

## Related Docs
- [Vulnerability Reporting Acknowledgements](https://www.twingate.com/docs/responsible-disclosure-policy) (linked from policy page)