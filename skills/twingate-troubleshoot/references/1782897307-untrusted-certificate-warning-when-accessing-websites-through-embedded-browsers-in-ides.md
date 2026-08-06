---
source: https://help.twingate.com/articles/1782897307-untrusted-certificate-warning-when-accessing-websites-through-embedded-browsers-in-ides
type: help
fetched: 2026-08-06
source_version: 94862c5c6837fc4d341d9495147e60580d29c47cfe95121054abc20299bac847
---

# Untrusted Certificate Warning in IDE Embedded Browsers

## Summary
IDE embedded browsers show "Untrusted Certificate" warnings when Twingate's internet security policies block a website and display a NextDNS-signed block page. IDEs maintain separate certificate stores from the OS/standard browsers, so the NextDNS root CA is not automatically trusted.

## Key Information
- Affects IDEs with embedded browsers (IntelliJ, VS Code, etc.) on Linux, Windows, macOS
- Block pages use SSL certificates issued by NextDNS
- Standard browsers (Chrome, Firefox, Edge) typically trust NextDNS root CA automatically
- Issue only occurs on sites blocked by Twingate internet security policies

## Prerequisites
- Twingate Client with internet security policies enabled
- Access to the IDE's embedded browser certificate store

## Symptoms
- "Untrusted Certificate" warning appears only in IDE embedded browser
- Warning does not appear in standard system browsers
- Occurs when navigating to a URL blocked by Twingate policy

## Resolution Steps
1. Trigger the warning by accessing a blocked site in the IDE embedded browser
2. Note the certificate store location displayed at the bottom of the warning window
3. Download the **NextDNS Blockpage CA** certificate
4. Navigate to the certificate store path shown in the warning
5. Import the NextDNS Blockpage CA into the IDE's trusted root certificate store
6. Restart the IDE if required; warning should no longer appear

## Configuration Values
- **Correct cert to import:** `NextDNS Blockpage CA`
- **Do NOT rely on:** `NextDNS Blockpage Edge CA` or `blockpage.nextdns.io` — these rotate frequently on short cycles

## Gotchas
- Importing the wrong certificate (`NextDNS Blockpage Edge CA` or `blockpage.nextdns.io`) will not provide a lasting fix due to short rotation schedules — always use the root `NextDNS Blockpage CA`
- Standard browsers may also show warnings if NextDNS Blockpage CA is not trusted; verify trust in all browsers if issues persist
- Each IDE may have a different process for importing trusted root certificates; consult IDE-specific documentation

## Related Docs
- Twingate Internet Security policies documentation
- NextDNS Blockpage CA certificate download (NextDNS support)
- IDE-specific certificate store management (JetBrains, VS Code, etc.)