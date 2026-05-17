# Twingate Guides Index

## Page Title
Twingate Guides — Documentation Hub

## Summary
Index page listing all Twingate documentation guides organized by category. Covers deployment, configuration, management, and integration topics across cloud, on-premises, homelab, and enterprise environments. Serves as the primary navigation reference for Twingate implementation.

## Key Information

### Deployment Targets
- **Cloud**: AWS EC2, GCP Compute, Azure Compute, Kubernetes, DigitalOcean
- **On-premises**: Docker Compose, Ubiquiti, Firewalla, Synology, QNAP, TrueNAS SCALE
- **Homelab**: Home Assistant, Proxmox, Unraid, ZimaOS, CasaOS
- **IaC**: Terraform, Pulumi

### Client Deployment (MDM)
- Jamf, Kandji, Omnissa Workspace ONE, Microsoft Intune & Endpoint Manager

### Service Integrations
- Identity/SSO: Active Directory, Okta, JumpCloud, Microsoft Entra ID, OneLogin
- Security tools: Cisco Umbrella, Cloudflare DNS filtering, Netskope DLP, Zscaler
- SIEM log ingestion for Connector logs

### Key Feature Guides
- **Internet Security**: DNS-over-HTTPS (DoH), DNS filtering
- **SaaS App Gating**: IP-based access control for SaaS apps
- **Security Policies**: Per-network and per-resource policies
- **Kubernetes**: Traffic routing, private/public resources, kubectl management
- **Exit Networks**: Self-hosted VPN replacement

### Specific Use Cases
- AI/LLM access, database access, SSH resource management
- CI/CD pipeline security, site-to-site connections
- IoT headless client gateway
- Vendor/contractor access management
- AWS VPN replacement, AWS Workspaces
- Bastion server cloaking

### Architecture & Planning
- Private DNS configuration best practices
- Connector placement optimization
- Overlapping IP address handling
- Non-production environment access
- Peer-to-peer local connections

### Technical Reference
- NAT traversal mechanics
- Encryption implementation
- Firewall compatibility
- Service accounts
- Windows Start Before Logon
- Connector shutdown process

## Prerequisites
- None (index page only)

## Gotchas
- Page is a navigation index only — no implementation details here; follow specific guide links for actionable steps
- "SaaS App Gating" requires separate IdP configuration (Okta, Entra ID, etc.) depending on provider

## Related Docs
- `/docs/connector-best-practices` — Connector placement and routing
- `/docs/remote-network-best-practices` — Remote Network organization
- `/docs/security-policies` — Policy configuration
- `/docs/kubernetes` — K8s deployment
- `/docs/client-deployment` — MDM rollout guides