# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
Twingate supports seven primary use cases spanning enterprise network security, infrastructure access, and personal homelab setups. It replaces traditional VPNs with zero-trust network access (ZTNA) while adding device security controls, DNS filtering, and compliance capabilities.

## Key Information

- **VPN Replacement**: Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access**: Engineers/DevOps can manage and automate secure access to on-premises and cloud infrastructure
- **Device Security Controls**: Enforce fine-grained access policies based on OS type, screen lock status, MDM/EDR enrollment, and other device characteristics
- **Application Gating**: Enables IP whitelisting for SaaS apps and private services; supports CASB-style deployments for staging servers and third-party services
- **Homelab/Personal Use**: Free Starter plan; supports Raspberry Pi and major NAS devices; setup under 15 minutes; no port forwarding or dynamic IP management required
- **Internet Security**: DNS filtering to block domains, device-level DNS-over-HTTPS (DoH) to configurable resolvers (Google, Cloudflare, OpenDNS supported)
- **Compliance**: Supports CPRA, GDPR, PCI DSS, and SOC 2 control requirements

## Prerequisites
- Connector deployment required for private network access
- Free Starter plan available for personal/homelab use
- Supported platforms for Connectors: Raspberry Pi, major NAS devices, cloud VMs

## Configuration Values
- **DNS Resolvers Supported**: Google, Cloudflare, OpenDNS (configurable)
- **Device policy parameters**: OS type, screen lock enabled, MDM enrollment, EDR status
- **Access model**: IP whitelisting / address-based access for Application Gating use case

## Gotchas
- Application Gating requires the target service to support IP-based access restrictions — Twingate provides the static egress IP, not the whitelisting mechanism itself
- Homelab use requires Connector installation on local hardware (Raspberry Pi, NAS, etc.)
- Compliance coverage depends on which controls your specific program requires — Twingate assists implementation but does not certify compliance automatically

## Related Docs
- VPN Replacement details
- Infrastructure Access details
- Device Security Controls details
- Application Gating details
- Homelab & Personal Use details
- Internet Security details
- Compliance details