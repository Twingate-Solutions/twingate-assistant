---
source: https://help.twingate.com/articles/6928700605-dns-avast-real-site-protection
type: help
fetched: 2026-09-06
source_version: 361bab14e27c298da148afc732660f3728ccdec918e0c3e32e0f09a2bc3e1d5e
---

# DNS: Avast Real Site Protection Compatibility

## Page Title
DNS: Avast Real Site Protection

## Summary
Avast's Real Site Protection feature conflicts with Twingate's DNS resolution mechanism, preventing access to protected resources by FQDN. The conflict arises because both products attempt to control DNS resolution at the system level. Disabling Real Site Protection resolves the incompatibility while allowing Avast itself to continue running.

## Key Information
- **Affected component**: Twingate Client
- **Conflicting product**: Avast Premium Security — Real Site Protection feature
- **Conflict type**: DNS resolution hijacking; both products compete for DNS control
- **Impact**: Twingate cannot resolve protected resources by FQDN when Real Site Protection is active
- **Avast base product** (without Real Site Protection) is compatible with Twingate

## Prerequisites
- Avast Premium Security installed with Real Site Protection enabled
- Twingate Client installed

## Resolution Steps
1. Open Avast Premium Security
2. Navigate to the Real Site Protection settings
3. Disable the **Real Site** feature
4. Verify Twingate Client can now resolve and access protected resources by FQDN

*(Avast itself does not need to be uninstalled — only the Real Site feature must be disabled)*

## Configuration Values
None applicable — resolution is UI-based toggle within Avast settings.

## Gotchas
- Disabling Real Site Protection removes encrypted DNS routing through Avast's DNS servers; assess security implications before disabling in sensitive environments
- Simply installing both products without active Real Site Protection is fine — the conflict is feature-specific, not application-level
- No Twingate configuration changes are required; the fix is entirely on the Avast side

## Related Docs
- Other DNS compatibility pages in Twingate help center (search "DNS" in help.twingate.com for similar third-party conflicts)
- Twingate Client troubleshooting documentation