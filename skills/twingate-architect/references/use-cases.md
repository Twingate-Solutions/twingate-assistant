# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
This page catalogs the primary deployment scenarios for Twingate, spanning enterprise network security to personal homelab setups. Each use case links to dedicated documentation with implementation details.

## Key Use Cases

- **VPN Replacement** – Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access** – Engineers/DevOps manage and automate secure access to on-prem and cloud infrastructure
- **Device Security Controls** – Policy-based access screening by OS type, screen lock status, MDM/EDR enrollment, and other device attributes
- **Application Gating** – IP whitelisting support for SaaS apps, staging servers, and lightweight CASB deployments
- **Homelab/Personal Use** – Remote access to home networks and self-hosted services (Home Assistant, Plex, cameras); free Starter plan available
- **Internet Security** – DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic on employee devices
- **Compliance** – Security controls supporting CPRA, GDPR, PCI DSS, SOC 2

## Configuration Notes

- **DNS Resolvers Supported**: Google, Cloudflare, OpenDNS (configurable)
- **Connector Platforms (Homelab)**: Raspberry Pi, major NAS devices
- **Device Policy Attributes**: OS type, screen lock, MDM enrollment, EDR status

## Prerequisites by Use Case

| Use Case | Notes |
|----------|-------|
| Homelab | Free Starter plan sufficient; setup ~15 minutes |
| Device Security | Requires device posture checking configuration |
| Application Gating | Target service must support IP-based access restrictions |
| Internet Security | DNS filtering must be enabled in admin settings |

## Gotchas

- Homelab use eliminates need for port forwarding or dynamic DNS management — no inbound ports required
- Application Gating requires the third-party service to support IP whitelisting; Twingate provides the stable egress IP
- This page is an index only — each use case links to a dedicated implementation guide

## Related Docs

- VPN Replacement (linked)
- Infrastructure Access (linked)
- Device Security Controls (linked)
- Application Gating (linked)
- Homelab & Personal Use (linked)
- Internet Security (linked)
- Compliance (linked)