# Twingate Guides Index

## Page Title
Twingate Guides Overview

## Summary
This is the top-level guides index for Twingate documentation, covering deployment, configuration, and management across cloud, on-premises, homelab, and enterprise environments. It serves as a navigation hub linking to specific implementation guides organized by category and use case.

## Key Information

### Deployment Targets
- **Cloud**: AWS EC2, GCP Compute, Azure Compute, Kubernetes, DigitalOcean
- **On-premises**: Docker Compose, Ubiquiti, Firewalla, Synology, QNAP, TrueNAS SCALE
- **Homelab**: Home Assistant, Proxmox, Unraid, ZimaOS, CasaOS
- **IaC**: Terraform, Pulumi

### Client Deployment (MDM)
- Jamf, Iru, Omnissa Workspace ONE, Microsoft Intune & Endpoint Manager

### Service Integrations
- Identity/SSO: Active Directory, Okta, Microsoft Entra ID, JumpCloud, OneLogin
- Security tools: Cisco Umbrella, Cloudflare DNS filtering, Netskope DLP, Zscaler
- Databases: MongoDB, AWS, GCP, Azure, Oracle, Snowflake, Redis

### Core Feature Areas
- **Internet Security**: DNS-over-HTTPS (DoH), DNS filtering
- **SaaS App Gating**: IP-based access control for SaaS applications
- **Security Policies**: Per-network and per-resource policy configuration
- **Logging**: Audit log viewing and export

### Notable Use Cases
- AI/LLM access gating
- CI/CD pipeline security
- Site-to-site connections
- SSH resource access management
- IoT headless client gateway
- Replace AWS VPN
- Vendor/contractor access management
- GitHub Codespaces access

## Related Docs (Key Subcategories)
- Best Practices for Connector Placement
- Best Practices for Private DNS Configuration
- Best Practices for Overlapping IP Addresses
- Best Practices for Security Policies
- AWS Reference Network Architecture
- How NAT Traversal Works
- How Encryption Works in Twingate
- How Firewalls Work with Twingate
- Troubleshooting Peer-to-peer Connections
- How Service Accounts Work
- Twingate Release Stages

## Gotchas
- No implementation details on this page — it is navigation only; follow specific guide links for configuration values, prerequisites, and step-by-step instructions
- SaaS App Gating requires IdP integration (Okta, Entra ID, etc.) for most configurations