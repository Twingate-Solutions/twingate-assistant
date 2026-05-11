# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
This page provides a high-level overview of the primary use cases Twingate supports, from VPN replacement to compliance. Each use case links to dedicated documentation for deeper implementation guidance.

## Key Use Cases

- **VPN Replacement** – Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access** – Secure, automated access to on-prem and cloud technical infrastructure for engineers/DevOps
- **Device Security Controls** – Policy enforcement based on device characteristics (OS type, screen lock, MDM/EDR status, etc.)
- **Application Gating** – IP whitelisting support for SaaS apps, staging servers, and lightweight CASB deployments
- **Homelab/Personal Use** – Remote access to home networks (Home Assistant, Plex, NAS, cameras); free Starter plan available; setup under 15 minutes
- **Internet Security** – DNS filtering, DNS-over-HTTPS (DoH) to configurable resolvers (Google, Cloudflare, OpenDNS)
- **Compliance** – Controls supporting CPRA, GDPR, PCI DSS, SOC 2

## Prerequisites
- None specified at this level; see individual use case pages for specific requirements
- Free Starter plan available for personal/homelab use

## Configuration Notes
- Connectors run on Raspberry Pi and major NAS devices (homelab)
- DNS resolvers supported: Google, Cloudflare, OpenDNS (configurable)
- Device policies can screen on: OS type, screen lock, MDM enrollment, EDR status

## Gotchas
- This is a navigation/overview page only — no implementation details here; follow "Learn more" links for each use case
- Homelab use requires no port forwarding or dynamic IP management, but Connector must be deployed on local hardware

## Related Docs
- VPN Replacement → `/docs/vpn-replacement`
- Infrastructure Access → `/docs/infrastructure-access`
- Device Security Controls → `/docs/device-security-controls`
- Application Gating → `/docs/application-gating`
- Homelab → `/docs/homelab`
- Internet Security → `/docs/internet-security`
- Compliance → `/docs/compliance`