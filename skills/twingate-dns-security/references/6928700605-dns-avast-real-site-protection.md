---
source: https://help.twingate.com/articles/6928700605-dns-avast-real-site-protection
type: help
fetched: 2026-11-01
source_version: 54df3211825692e456d3cdb9ddb037f01719b49a49376d230745dfb3e2934998
trust: official
---

# DNS: Avast Real Site Protection Incompatibility

## Page Title
DNS: Avast Real Site Protection

## Summary
Avast Premium Security's "Real Site" feature conflicts with Twingate's DNS resolution mechanism. When both are active simultaneously, the Twingate client cannot access protected resources by FQDN. Disabling Real Site Protection resolves the conflict.

## Key Information
- **Affected component:** Twingate Client
- **Third-party product:** Avast Premium Security — Real Site Protection feature
- **Conflict type:** DNS resolution — both products attempt to control DNS handling at the system level
- **Real Site** routes DNS through Avast's encrypted DNS servers to prevent hijacking, which intercepts the DNS queries Twingate requires to route traffic to protected resources
- Avast antivirus itself (without Real Site) is compatible with Twingate

## Symptoms
- Twingate client is running but protected resources are unreachable via FQDN
- Both Twingate and Avast Real Site Protection are installed and active

## Resolution
Disable **Real Site Protection** in Avast Premium Security:
1. Open Avast Premium Security
2. Navigate to **Protection** → **Real Site**
3. Disable the feature

Avast can remain installed and active; only the Real Site component needs to be turned off.

## Gotchas
- This is a known incompatibility with no current workaround that allows both features to run simultaneously
- Accessing resources by IP address may still work when the conflict is present, but FQDN access will fail
- Users may not immediately associate Avast as the cause since Avast itself (outside of Real Site) works fine alongside Twingate

## Related Docs
- Twingate DNS troubleshooting (general)
- Other third-party DNS compatibility issues in Twingate help center