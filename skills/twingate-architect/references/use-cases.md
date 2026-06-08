# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
This page provides a high-level overview of the primary use cases Twingate supports, from VPN replacement to compliance. Each use case links to dedicated documentation. Covers both enterprise and personal/homelab scenarios.

## Key Use Cases

- **VPN Replacement** – Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access** – Engineers/DevOps manage and automate secure access to on-prem and cloud infrastructure
- **Device Security Controls** – Policy enforcement based on device attributes (OS type, screen lock, MDM/EDR status, etc.)
- **Application Gating** – IP whitelisting support for SaaS apps, staging servers; lightweight CASB deployment
- **Homelab/Personal Use** – Remote access to home networks, self-hosted apps (Home Assistant, Plex, cameras); free Starter plan available; setup under 15 minutes
- **Internet Security** – DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic on employee devices
- **Compliance** – Controls supporting CPRA, GDPR, PCI DSS, SOC 2

## Configuration Notes

- **DNS Resolvers supported**: Google, Cloudflare, OpenDNS (configurable)
- **Connector platforms**: Raspberry Pi, major NAS devices, cloud/on-prem environments
- **Device policy attributes**: OS type, screen lock, MDM enrollment, EDR status

## Prerequisites
- Twingate account (free Starter plan available for personal use)
- Twingate Connector deployed on target network
- Twingate Client installed on end-user devices

## Gotchas

- Application Gating requires the third-party service to support IP-based access restrictions; Twingate provides the stable egress IP
- Homelab use eliminates need for port forwarding or dynamic DNS management — no inbound ports required
- Internet Security (DNS filtering/DoH) applies at the device level, not per-resource

## Related Docs
- VPN Replacement (linked from page)
- Infrastructure Access (linked from page)
- Device Security Controls (linked from page)
- Application Gating (linked from page)
- Homelab & Personal Use (linked from page)
- Internet Security (linked from page)
- Compliance (linked from page)