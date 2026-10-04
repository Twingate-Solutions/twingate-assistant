---
source: https://help.twingate.com/articles/1782897307-untrusted-certificate-warning-when-accessing-websites-through-embedded-browsers-in-ides
type: help
fetched: 2026-10-04
source_version: 742d466fe58d6532038518c598f738e51c0d37c283186e250e355efe31edc60b
trust: official
---

# Untrusted Certificate Warning in IDE Embedded Browsers

## Page Title
Untrusted Certificate Warning When Accessing Websites through Embedded Browsers in IDEs

## Summary
When Twingate's internet security policies block a website, the block page uses an SSL certificate issued by NextDNS. IDE embedded browsers maintain separate certificate stores from the OS/system browsers, so they may not trust the NextDNS root certificate, causing an untrusted certificate warning.

## Key Information
- **Affected components:** Twingate Client on Linux, Windows, macOS
- **Root cause:** IDE embedded browsers use isolated certificate stores that don't inherit system or browser trust for the NextDNS Blockpage CA
- **Not affected:** Standard browsers (Chrome, Firefox, Edge) typically trust the NextDNS root certificate by default
- **Certificate to trust:** `NextDNS Blockpage CA` — this is the stable cert to import
- **Do NOT rely on:** `NextDNS Blockpage Edge CA` or `blockpage.nextdns.io` certs — these rotate frequently

## Prerequisites
- Twingate Client installed and enforcing an internet security policy
- Access to the IDE's certificate management settings
- The `NextDNS Blockpage CA` certificate (downloadable from the SSL block page itself)

## Step-by-Step Resolution

1. Attempt to access a blocked website inside the IDE's embedded browser to trigger the warning
2. Note the **certificate store location** displayed at the bottom of the untrusted certificate warning window
3. Download the **NextDNS Blockpage CA** certificate from the block page (not the Edge CA or leaf cert)
4. Navigate to the certificate store path shown in the warning
5. Use the IDE's certificate import process to add the `NextDNS Blockpage CA` to its trusted root store
6. Restart the embedded browser/IDE if required; the warning should no longer appear

## Gotchas
- Importing `NextDNS Blockpage Edge CA` or `blockpage.nextdns.io` will not provide a lasting fix — these certs rotate on a short schedule
- The certificate store location varies per IDE; the warning window itself identifies the correct path
- Standard browsers not showing the warning does **not** confirm the system trust store is correctly configured — verify explicitly if needed
- This issue only surfaces for sites actually blocked by a Twingate internet security policy, not all HTTPS sites

## Configuration Values
| Item | Value |
|------|-------|
| Certificate to import | `NextDNS Blockpage CA` |
| Certificate source | SSL block page presented by Twingate/NextDNS |
| Trust store location | Displayed at bottom of the IDE's untrusted cert warning |

## Related Docs
- Twingate Internet Security policies documentation
- NextDNS Blockpage CA certificate reference
- IDE-specific certificate management guides (varies by vendor: JetBrains, VS Code, etc.)