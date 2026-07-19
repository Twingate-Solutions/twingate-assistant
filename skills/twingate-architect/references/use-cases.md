# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
Twingate supports multiple network security and access control scenarios spanning VPN replacement, infrastructure access, device security, and internet filtering. It targets both enterprise and personal/homelab users. Each use case leverages Twingate's zero-trust architecture to replace or supplement traditional network security tools.

## Key Use Cases

- **VPN Replacement**: Remote access to office networks, cloud VPCs, and private corporate resources from computers and mobile devices
- **Infrastructure Access**: Secure, automated access management for engineers and DevOps to on-premises and cloud infrastructure
- **Device Security Controls**: Policy enforcement based on device characteristics (OS type, screen lock, MDM/EDR status, etc.)
- **Application Gating**: IP allowlisting for SaaS apps and private services; supports staging server security and lightweight CASB deployments
- **Homelab/Personal Use**: Remote access to home networks and self-hosted services (Home Assistant, Plex, cameras); free Starter plan available
- **Internet Security**: DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic on employee devices
- **Compliance**: Controls supporting CPRA, GDPR, PCI DSS, and SOC 2 requirements

## Configuration Values

- **Supported DNS Resolvers** (Internet Security): Google, Cloudflare, OpenDNS (configurable)
- **Connector Platforms** (Homelab): Raspberry Pi, major NAS devices
- **Pricing**: Free Starter plan for personal/homelab use

## Prerequisites

- Varies by use case; homelab setup advertised as under 15 minutes
- No inbound port forwarding required for homelab deployments
- MDM or EDR presence detectable for device security policy enforcement

## Gotchas

- Application Gating requires the third-party service to support IP address-based access or whitelisting — Twingate does not add this capability to services that don't support it
- Device security controls require device characteristics to be reported; MDM/EDR must be present on device for those checks to pass
- Homelab use eliminates need for VPN server management and dynamic IP handling, but requires running a Twingate Connector on local hardware

## Related Docs

- VPN Replacement (linked)
- Infrastructure Access (linked)
- Device Security Controls (linked)
- Application Gating (linked)
- Homelab & Personal Use Cases (linked)
- Internet Security (linked)
- Compliance (linked)