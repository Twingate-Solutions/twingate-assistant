---
source: https://help.twingate.com/articles/6928700605-dns-avast-real-site-protection
type: help
fetched: 2026-08-06
source_version: 4c82d0dfac505bac0df20045f70ed3bb0afd7d375fbb82cfa7b24744c2a35071
---

# DNS: Avast Real Site Protection Compatibility

## Page Title
DNS: Avast Real Site Protection

## Summary
Avast's Real Site Protection feature conflicts with Twingate's DNS resolution mechanism. When both are active simultaneously, Twingate cannot resolve FQDNs for protected resources. Disabling Real Site Protection resolves the conflict while Avast itself remains usable.

## Key Information
- **Conflict type**: DNS resolution incompatibility
- **Affected component**: Twingate Client
- **Third-party product**: Avast Premium Security (Real Site Protection feature)
- **Symptom**: Twingate client cannot access protected resources by FQDN when Real Site Protection is enabled
- **Root cause**: Real Site Protection routes DNS through Avast's encrypted DNS server, conflicting with Twingate's DNS interception

## Prerequisites
- Avast Premium Security installed with Real Site Protection enabled
- Twingate Client installed

## Resolution Steps
1. Open Avast Premium Security
2. Locate the **Real Site Protection** setting
3. Disable **Real Site Protection**
4. Verify Twingate client can resolve and access protected resources by FQDN

> Avast itself (without Real Site Protection) is compatible with Twingate.

## Configuration Values
None — resolution is a UI toggle in Avast settings, no CLI flags or API parameters involved.

## Gotchas
- Disabling Real Site Protection removes DNS hijacking protection from Avast; users should be aware of this security trade-off
- Issue is specific to **Real Site Protection** — other Avast features are not affected
- No workaround exists to run both simultaneously; one must be disabled

## Related Docs
- Twingate DNS compatibility documentation (other third-party DNS conflicts)
- Twingate Client troubleshooting guides