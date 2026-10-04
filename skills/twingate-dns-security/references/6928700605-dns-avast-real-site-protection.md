---
source: https://help.twingate.com/articles/6928700605-dns-avast-real-site-protection
type: help
fetched: 2026-10-04
source_version: e645589012a77991209ec9ebc3519892ea1673efa379dd11086e4e7098092579
trust: official
---

# DNS: Avast Real Site Protection Incompatibility

## Page Title
DNS: Avast Real Site Protection

## Summary
Avast Premium Security's "Real Site" feature conflicts with Twingate's DNS resolution mechanism. When both are active, the Twingate client cannot access protected resources by FQDN. Disabling Real Site Protection resolves the conflict.

## Key Information
- **Affected component:** Twingate Client
- **Conflicting product:** Avast Premium Security — "Real Site" feature
- **Root cause:** Both products compete for control of DNS resolution at the system level
- **Impact:** Twingate cannot resolve FQDNs for protected resources when Real Site is enabled
- **Scope:** Avast antivirus itself (without Real Site) is compatible with Twingate

## Prerequisites
- Avast Premium Security installed on the same machine as the Twingate client

## Resolution Steps
1. Open Avast Premium Security settings
2. Locate the **Real Site Protection** feature
3. **Disable** Real Site Protection
4. Twingate client DNS resolution should resume normal operation

## Gotchas
- Avast base product is fine — only the **Real Site** feature must be disabled, not Avast entirely
- Real Site routes DNS through Avast's own encrypted DNS servers, which intercepts Twingate's DNS-based resource routing
- No Twingate-side configuration change resolves this; the fix must be made in Avast

## Related Docs
- Other DNS compatibility issues in Twingate Help (search "DNS" in help.twingate.com)