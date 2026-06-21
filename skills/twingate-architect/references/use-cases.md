# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
This page catalogs the primary deployment scenarios for Twingate across enterprise and personal contexts. It covers seven distinct use cases ranging from VPN replacement to compliance enforcement. Each use case links to dedicated documentation for implementation details.

## Key Information

- **VPN Replacement**: Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access**: Secure access management and automation for engineers/DevOps targeting on-prem and cloud infrastructure
- **Device Security Controls**: Policy enforcement based on device characteristics (OS type, screen lock, MDM/EDR status)
- **Application Gating**: IP whitelisting support for SaaS apps, staging servers, and lightweight CASB deployments
- **Homelab/Personal Use**: Remote access to home networks (Home Assistant, Plex, cameras, self-hosted apps); setup under 15 minutes; free Starter plan available
- **Internet Security**: DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic; supports Google, Cloudflare, OpenDNS resolvers
- **Compliance**: Controls for CPRA, GDPR, PCI DSS, SOC 2 requirements

## Prerequisites
- Varies by use case; Homelab use requires a Connector installed on supported hardware (Raspberry Pi, major NAS devices)
- Free Starter plan available for personal/homelab use

## Configuration Values

| Use Case | Notable Config Options |
|---|---|
| Device Security | OS type, screen lock status, MDM enabled, EDR enabled |
| Internet Security | DNS filtering rules, DoH resolver (Google, Cloudflare, OpenDNS) |
| Application Gating | IP whitelist/allowlist entries |

## Gotchas

- Homelab use eliminates need for port forwarding and open inbound ports — no VPN server or dynamic DNS management required
- Application Gating is limited to services that support IP-based access restrictions
- Device security policies require compatible MDM/EDR integrations to report device state accurately

## Related Docs
- VPN Replacement → `/docs/vpn-replacement`
- Infrastructure Access → dedicated page linked from use cases
- Device Security Controls → dedicated page
- Application Gating → dedicated page
- Homelab & Personal Use → dedicated page
- Internet Security → dedicated page
- Compliance → dedicated page