# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
This page catalogs the primary deployment scenarios for Twingate, covering both enterprise and personal use cases. It serves as a navigation hub linking to detailed documentation for each use case category.

## Key Information

- **7 distinct use cases** are documented
- Covers enterprise, DevOps, and personal/homelab scenarios
- Each use case links to dedicated detailed documentation

## Use Cases at a Glance

| Use Case | Core Function |
|---|---|
| **VPN Replacement** | Remote access to office networks, cloud VPCs, private resources |
| **Infrastructure Access** | Engineer/DevOps access to on-prem and cloud infrastructure; supports automation |
| **Device Security Controls** | Policy enforcement based on OS type, screen lock, MDM/EDR status |
| **Application Gating** | IP whitelisting support for SaaS apps, staging servers, lightweight CASB |
| **Homelab & Personal** | Home network access (Home Assistant, Plex, NAS, cameras); free Starter plan |
| **Internet Security** | DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic |
| **Compliance** | Controls supporting CPRA, GDPR, PCI DSS, SOC 2 |

## Configuration Notes

- **Device policy filters**: OS type, screen lock, MDM enrollment, EDR status
- **DNS resolvers supported**: Google, Cloudflare, OpenDNS (configurable)
- **DNS features**: Native filtering + device-level DoH
- **Connector platforms**: Raspberry Pi, major NAS devices, standard cloud/on-prem

## Prerequisites

- Free Starter plan available for personal/homelab use
- Connectors required for private resource access
- MDM/EDR integrations needed for device security control policies

## Gotchas

- Application Gating requires the third-party service to support IP-based access restrictions — Twingate provides a stable egress IP, not protocol-level app inspection
- Homelab setup (~15 min) eliminates port forwarding but still requires Connector deployment on local hardware
- Internet Security (DNS filtering/DoH) applies at device level, not just tunnel traffic

## Related Docs

- VPN Replacement → `/docs/vpn-replacement`
- Infrastructure Access → `/docs/infrastructure-access`
- Device Security Controls → `/docs/device-security-controls`
- Application Gating → `/docs/application-gating`
- Homelab & Personal → `/docs/homelab`
- Internet Security → `/docs/internet-security`
- Compliance → `/docs/compliance`