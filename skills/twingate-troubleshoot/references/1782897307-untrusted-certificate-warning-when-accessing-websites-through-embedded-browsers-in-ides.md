---
source: https://help.twingate.com/articles/1782897307-untrusted-certificate-warning-when-accessing-websites-through-embedded-browsers-in-ides
type: help
fetched: 2026-09-06
source_version: f2a34c7e63e2e478c63414c1ae90d924ec8a0d55ab8585938571c509c980e1b4
---

# Untrusted Certificate Warning in IDE Embedded Browsers

## Page Title
Untrusted Certificate Warning When Accessing Websites through Embedded Browsers in IDEs

## Summary
IDE embedded browsers maintain separate certificate stores from the OS/standard browsers, so Twingate's internet security block pages (served with a NextDNS SSL certificate) trigger untrusted certificate warnings. Standard browsers (Chrome, Firefox, Edge) typically trust the NextDNS root cert automatically. Fix requires manually importing the NextDNS Blockpage CA into the IDE's embedded browser certificate store.

## Key Information
- **Affected components**: Twingate Client on Linux, Windows, macOS
- **Root cause**: Block pages use SSL cert issued by NextDNS; IDE embedded browsers have isolated cert stores
- **Not affected**: Standard browsers (Chrome, Firefox, Edge) generally trust NextDNS root cert automatically
- **Certificate to import**: `NextDNS Blockpage CA` specifically — not `NextDNS Blockpage Edge CA` or `blockpage.nextdns.io` (those rotate frequently)

## Prerequisites
- Twingate internet security policy actively blocking a resource
- Access to IDE's embedded browser certificate store
- NextDNS Blockpage CA certificate (downloadable from the SSL block page)

## Step-by-Step Resolution

1. Trigger the untrusted certificate warning by accessing a blocked site in the IDE embedded browser
2. Note the **certificate store location** displayed at the bottom of the warning window
3. Download the **NextDNS Blockpage CA** cert from the SSL block page (do not use Edge CA or blockpage.nextdns.io certs)
4. Navigate to the certificate store location shown in the warning
5. Import the NextDNS Blockpage CA using the IDE's trusted root store import process
6. Verify warning no longer appears on blocked sites

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Correct cert to import | `NextDNS Blockpage CA` |
| Certs to avoid | `NextDNS Blockpage Edge CA`, `blockpage.nextdns.io` (short rotation) |
| Cert store location | Shown at bottom of warning dialog (varies by IDE) |

## Gotchas
- **Wrong cert**: Importing `NextDNS Blockpage Edge CA` or `blockpage.nextdns.io` will not provide a lasting fix due to short rotation cycles
- **Per-IDE action required**: Each IDE with an embedded browser needs the cert imported separately
- **Standard browser trust ≠ IDE trust**: Even if standard browsers show no warning, the IDE embedded browser still needs the cert

## Related Docs
- Twingate Internet Security policies documentation
- NextDNS Blockpage CA certificate download (linked from SSL block page)