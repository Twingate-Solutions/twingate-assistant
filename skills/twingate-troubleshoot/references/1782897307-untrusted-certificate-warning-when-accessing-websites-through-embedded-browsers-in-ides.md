---
source: https://help.twingate.com/articles/1782897307-untrusted-certificate-warning-when-accessing-websites-through-embedded-browsers-in-ides
type: help
fetched: 2026-11-01
source_version: 96afd30cd4d1406eb9c566991317e22d20289fc5c828e035bd963c1b42cae3e0
trust: official
---

# Untrusted Certificate Warning in IDE Embedded Browsers

## Page Title
Untrusted Certificate Warning When Accessing Websites through Embedded Browsers in IDEs

## Summary
When Twingate's internet security policies block a website, the block page uses an SSL certificate issued by NextDNS. IDE embedded browsers maintain separate certificate stores from the OS/standard browsers, so they may not trust this certificate, producing an "Untrusted Certificate" warning.

## Key Information
- **Affected components:** Twingate Client on Linux, Windows, macOS
- **Root cause:** NextDNS issues the SSL cert for block pages; IDE embedded browsers use isolated certificate stores that don't inherit OS or standard browser trust
- **Not affected:** Standard browsers (Chrome, Firefox, Edge) typically trust the NextDNS root cert automatically
- **Certificate to trust:** `NextDNS Blockpage CA` — import this specific cert, not `NextDNS Blockpage Edge CA` or `blockpage.nextdns.io` (those rotate frequently)

## Prerequisites
- Twingate Client configured with internet security policies
- Access to the IDE's embedded browser certificate store
- `NextDNS Blockpage CA` certificate file

## Step-by-Step Resolution
1. Trigger the block page in the IDE embedded browser and observe the "Untrusted Certificate" warning
2. Note the certificate store path displayed at the bottom of the warning window
3. Download the **NextDNS Blockpage CA** certificate from the SSL block page or NextDNS directly
4. Navigate to the certificate store location identified in step 2
5. Import the `NextDNS Blockpage CA` cert into the IDE's trusted root certificate store using the IDE's native import process
6. Restart the embedded browser session; the warning should no longer appear

## Gotchas
- **Import the correct cert:** Only import `NextDNS Blockpage CA`. The `NextDNS Blockpage Edge CA` and `blockpage.nextdns.io` certs are on short rotation and will not provide a lasting fix
- **IDE-specific import process:** Each IDE has its own certificate management UI — consult the specific IDE's documentation for exact import steps
- **Standard browsers may also need the cert** in some environments; verify by checking if the warning appears in regular browsers too

## Configuration Values
| Item | Value |
|------|-------|
| Certificate to trust | `NextDNS Blockpage CA` |
| Cert store location | Shown at bottom of the untrusted certificate warning dialog |

## Related Docs
- NextDNS Blockpage CA certificate (obtain from the block page or NextDNS support)
- IDE-specific documentation for managing trusted certificate stores