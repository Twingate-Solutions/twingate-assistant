---
source: https://www.twingate.com/docs/use-cases
type: docs
fetched: 2026-11-15
source_version: b42d9628dbfd1f786bd694923a439c80ab4397d17f22c96a1d0043bdbb1a64d4
trust: official
---

# Page Title
Twingate Use Cases (https://www.twingate.com/docs/use-cases)

## Summary
Landing page listing the eight main scenarios Twingate supports, each linking to a detailed guide. It is an overview only, with no setup steps, commands, or configuration values.

## Key Information
- **VPN Replacement**: Remote access to the office network, cloud VPCs, and private resources from computers and mobile devices.
- **Infrastructure Access**: Lets engineers and DevOps manage and automate secure access to on-prem and cloud technical infrastructure.
- **Device Security Controls**: Fine-grained policies that screen users and devices against permitted characteristics, such as OS type, screen lock enabled, and MDM or EDR enabled.
- **Application Gating**: Secure access to SaaS apps and private services that require or support IP allowlisting. Examples include third-party services restricted by IP, staging servers, and a lightweight CASB.
- **Homelab & Personal Use**: Remote access to home services such as Home Assistant, Plex, and security cameras. It needs no port forwarding or open inbound ports, and no VPN server or dynamic IP management. Connectors run on platforms including Raspberry Pi and major NAS devices. A free Starter plan is offered for personal use, and setup is said to take under 15 minutes for most users.
- **Internet Security**: Native DNS filtering to block undesirable domains, plus device-level DNS-over-HTTPS (DoH) to a configurable resolver. Google, Cloudflare, and OpenDNS resolvers are supported.
- **Compliance**: Helps implement controls required by CPRA, GDPR, PCI DSS, and SOC 2.
- **Coding Agents**: Gives local, cloud, and self-hosted coding agents access to specific private Resources, such as internal package registries, without exposing them to the internet.

## Prerequisites
None stated on this page. See the individual use-case guides.

## Step-by-Step
Not applicable (overview page).

## Configuration Values
None listed on this page.

## Gotchas
- The page is a high-level index. Implementation details, such as device posture criteria, DNS filtering setup, and Connector deployment, are in the linked "Learn more" pages.
- The compliance entry says Twingate helps implement controls. It does not claim certification or compliance by itself.
- The "under 15 minutes" setup figure applies to homelab use and is not a guarantee for enterprise deployments.

## Related Docs
Each use case has a "Learn more" link on the source page: VPN Replacement, Infrastructure Access, Device Security Controls, Application Gating, Homelab & Personal, Internet Security, Compliance, Coding Agents. Also relevant are Twingate's Connector deployment docs and its device posture and security policy docs.