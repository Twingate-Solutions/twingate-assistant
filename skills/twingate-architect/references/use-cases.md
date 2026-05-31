# Twingate Use Cases

## Page Title
Use Cases Overview

## Summary
Twingate supports seven primary deployment scenarios ranging from VPN replacement to compliance enforcement. The platform provides zero-trust network access for both enterprise and personal use cases. Each use case leverages Twingate's connector-based architecture without requiring open inbound ports.

## Key Use Cases

- **VPN Replacement**: Remote access to office networks, cloud VPCs, and private corporate resources from any device
- **Infrastructure Access**: Engineer/DevOps access management and automation for on-prem and cloud infrastructure
- **Device Security Controls**: Policy enforcement based on device attributes (OS type, screen lock, MDM/EDR status)
- **Application Gating**: IP allowlisting for SaaS apps, staging servers, and lightweight CASB deployment
- **Homelab/Personal**: Home network access for self-hosted apps (Home Assistant, Plex, cameras); free Starter plan available
- **Internet Security**: DNS filtering, DNS-over-HTTPS (DoH) for public internet traffic protection
- **Compliance**: Controls supporting CPRA, GDPR, PCI DSS, SOC 2

## Prerequisites
- Twingate account (free Starter plan available for personal use)
- Twingate Connector deployed on target network
- Client installed on user devices

## Configuration Notes

| Use Case | Key Config |
|---|---|
| Device Security | Device posture policies (OS, screen lock, MDM, EDR) |
| Application Gating | IP allowlist integration with third-party services |
| Internet Security | DNS resolver selection (Google, Cloudflare, OpenDNS supported) |
| Homelab | Connector on Raspberry Pi or NAS devices |

## Gotchas
- Homelab setup eliminates need for port forwarding and dynamic DNS management—no open inbound ports required
- DNS filtering and DoH are device-level controls, applied per-device not per-resource
- Application Gating requires the third-party service to support IP-based access restrictions

## Related Docs
- VPN Replacement detail page
- Infrastructure Access detail page
- Device Security Controls detail page
- Application Gating detail page
- Homelab & Personal Use Cases detail page
- Internet Security detail page
- Compliance detail page