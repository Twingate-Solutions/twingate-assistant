---
source: https://www.twingate.com/docs/use-cases
type: docs
fetched: 2026-08-14
source_version: 9508dcf7a39e95e9f13fdeecf87498384f6bb2c78d594058f9b10053489382fb
---

# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
This page catalogs Twingate's primary deployment scenarios across enterprise and personal contexts. It serves as a navigation hub linking to detailed documentation for each use case. Twingate positions itself as a Zero Trust Network Access (ZTNA) solution covering network access, device security, DNS filtering, and compliance.

## Key Use Cases

- **VPN Replacement** – Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access** – Engineer/DevOps access management and automation for on-prem and cloud infrastructure
- **Device Security Controls** – Policy enforcement based on device attributes (OS type, screen lock, MDM/EDR status)
- **Application Gating** – IP allowlisting for SaaS apps and private services; lightweight CASB alternative for staging servers
- **Homelab/Personal Use** – Remote access to home networks and self-hosted services (Home Assistant, Plex, cameras); free Starter plan available
- **Internet Security** – DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic on employee devices
- **Compliance** – Controls supporting CPRA, GDPR, PCI DSS, SOC 2

## Configuration Values / Supported Integrations

- **DNS Resolvers supported**: Google, Cloudflare, OpenDNS (configurable)
- **Connector platforms**: Raspberry Pi, major NAS devices, standard cloud/on-prem hosts
- **Compliance frameworks**: CPRA, GDPR, PCI DSS, SOC 2

## Notable Implementation Details

- Homelab setup target: under 15 minutes
- No port forwarding or inbound open ports required
- No dynamic IP management needed for home use
- Device policy screening attributes: OS type, screen lock, MDM enrollment, EDR status
- Application gating supports IP-based restrictions for third-party services

## Gotchas

- Free Starter plan is personal use only; enterprise features require paid plans
- Application gating (IP whitelisting use case) requires the third-party service to support IP-based access controls — Twingate doesn't bypass services that lack this feature
- Device security controls require compatible MDM/EDR integrations to report device posture

## Related Docs

- VPN Replacement (linked from page)
- Infrastructure Access (linked from page)
- Device Security Controls (linked from page)
- Application Gating (linked from page)
- Homelab & Personal Use (linked from page)
- Internet Security (linked from page)
- Compliance (linked from page)