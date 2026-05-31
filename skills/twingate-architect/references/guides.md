# Twingate Guides Index

## Page Title
Twingate Guides – Documentation Index

## Summary
This is the top-level guides index for Twingate documentation, organizing deployment, configuration, and management topics. It serves as a navigation hub covering infrastructure deployment, client rollout, policy configuration, service integrations, and architecture best practices.

## Key Information

### Deployment Targets
- **Cloud**: AWS EC2, GCP Compute, Azure Compute, Kubernetes, DigitalOcean
- **On-premises**: Docker Compose, Ubiquiti, Firewalla, Synology, QNAP, TrueNAS, Proxmox
- **Homelab**: Home Assistant, Unraid, ZimaOS, CasaOS
- **IaC**: Terraform, Pulumi

### Client Deployment (MDM)
- Jamf, Iru, Omnissa Workspace ONE, Microsoft Intune & Endpoint Manager

### Service Compatibility
- Active Directory, Cisco Umbrella, Cloudflare DNS filtering, Netskope DLP, Zscaler

### Database Access
- MongoDB, AWS, GCP, Azure, Oracle, Snowflake, Redis

### SaaS App Gating IDPs
- Google Workspace, JumpCloud, Microsoft Entra ID, Okta, OneLogin

### Kubernetes-Specific
- Route traffic from Kubernetes, private/public resources, `kubectl` management

## Notable Use Cases
- Cloak bastion servers / strongDM
- Secure CI/CD pipelines
- IoT headless client gateway
- Vendor/contractor access management
- SSH resource access
- Replace AWS VPN
- Site-to-site connections
- AI/LLM access control
- Remote game streaming

## Architecture & Best Practices Topics
- Private DNS configuration
- Connector placement
- Overlapping IP addresses
- Security policies
- Non-production environment access
- Whitelisting public resources
- Local peer-to-peer connections

## Technical Reference Topics
- NAT traversal mechanics
- Encryption internals
- Firewall behavior
- Service accounts
- Windows Start Before Logon
- Connector shutdown process
- Performance evaluation
- Release stages

## Related Docs
- Individual deployment guides linked per platform (see sections above)
- `Best Practices for Connector Placement` – critical for routing/performance
- `Best Practices for Security Policies` – policy design reference
- `How NAT Traversal Works` – useful for troubleshooting connectivity
- `Troubleshooting Peer-to-peer Connections` – P2P debugging reference

## Gotchas
- This page is navigation-only; no configuration values or CLI flags are present here
- Specific implementation details require navigating to individual guide pages
- "Iru" MDM listing is likely a niche/regional MDM tool—verify compatibility before planning rollout