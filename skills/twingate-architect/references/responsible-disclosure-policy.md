# Twingate Responsible Disclosure Policy

## Summary
Twingate's responsible disclosure policy outlines how security researchers should report vulnerabilities. Reports are submitted via email, with a commitment to resolve critical issues within 5 business days. Researchers must follow specific rules to avoid unauthorized access, data destruction, or service disruption.

## Key Information
- **Contact**: security@twingate.com
- **Response SLA**: Acknowledgement within 5 business days; critical issues resolved within 5 business days of disclosure
- **All assessments are final**
- Vulnerability prioritization is at Twingate's sole discretion

## Rules for Researchers
- Only test against accounts you own or have explicit permission to test
- Do not exploit discovered vulnerabilities for any benefit
- Keep all bug disclosure communications confidential (no third-party disclosure without Twingate consent)
- Destroy all artifacts (POC code, videos, screenshots) after bug report is closed
- Report severe system-access vulnerabilities immediately and stop further investigation
- No threatening behavior toward Twingate personnel

## Out-of-Scope Endpoints
- twingate.com (company site)
- docs.twingate.com
- forum.twingate.com
- status.twingate.com
- help.twingate.com
- trust.twingate.com
- Subdomains: `email`, `packages`, `sales`
- Third-party hosted sites (unless they expose an in-scope weakness)

## Out-of-Scope Vulnerability Types
- DDoS attacks
- Spamming
- Physical property or data center attacks

## Reporting Steps
1. Email security@twingate.com
2. Describe the vulnerability in detail
3. Include step-by-step reproduction instructions
4. Allow reasonable time for resolution before any public disclosure
5. Do not include out-of-scope items in the report

## Gotchas
- This policy **does not authorize access** to any data that is not yours
- Researchers cannot disclose bug details publicly or to third parties without Twingate's explicit consent
- Artifacts must be destroyed after report closure — not just deleted from public view
- Third-party site vulnerabilities are out of scope unless they directly expose an in-scope Twingate system

## Related Docs
- [Vulnerability Reporting Acknowledgements](https://www.twingate.com/docs/responsible-disclosure-policy) (linked from policy page)