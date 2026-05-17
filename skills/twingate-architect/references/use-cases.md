# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
This page catalogs the primary deployment scenarios for Twingate, covering both enterprise and personal use cases. It serves as a navigation hub linking to detailed documentation for each use case category.

## Key Information

- **VPN Replacement** – Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access** – Engineer/DevOps access management and automation for on-prem and cloud infrastructure
- **Device Security Controls** – Policy enforcement based on device attributes (OS type, screen lock, MDM/EDR status, etc.)
- **Application Gating** – IP whitelisting support for SaaS apps, staging servers, and lightweight CASB deployments
- **Homelab/Personal Use** – Home network remote access; supports Raspberry Pi and major NAS devices; free Starter plan available; setup under 15 minutes
- **Internet Security** – DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic; supports Google, Cloudflare, OpenDNS resolvers
- **Compliance** – Controls mapped to CPRA, GDPR, PCI DSS, SOC 2 requirements

## Prerequisites
- None specific to this overview page; prerequisites vary by use case

## Configuration Values
| Use Case | Notable Config Options |
|---|---|
| Device Security | OS type, screen lock, MDM status, EDR status |
| Internet Security | DNS filtering rules, DoH resolver (Google, Cloudflare, OpenDNS) |
| Homelab | Connector platforms: Raspberry Pi, NAS devices |

## Gotchas
- Homelab/personal use requires the free **Starter plan** — confirm plan eligibility before deploying
- Application Gating relies on IP whitelisting support in the third-party service — not all SaaS apps support this
- Internet Security features (DNS filtering, DoH) apply at the device level, not per-resource

## Related Docs
- VPN Replacement detail page
- Infrastructure Access detail page
- Device Security Controls detail page
- Application Gating detail page
- Homelab & Personal Use detail page
- Internet Security detail page
- Compliance detail page