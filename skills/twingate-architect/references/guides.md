# Twingate Guides Index

## Page Title
Twingate Guides Overview

## Summary
This is the Twingate documentation guides index page, organizing deployment, configuration, and management documentation across infrastructure types, use cases, and integrations. It serves as the top-level navigation hub for all Twingate implementation guides.

## Key Information

### Deployment Targets
- **Cloud**: AWS EC2, GCP Compute, Azure Compute, Kubernetes, DigitalOcean
- **On-premises**: Docker Compose, Ubiquiti, Firewalla, Synology, QNAP NAS, TrueNAS SCALE, Proxmox
- **Homelabs**: Home Assistant, Unraid, ZimaOS, CasaOS
- **IaC**: Terraform, Pulumi

### Client Deployment (MDM)
- Jamf, Iru, Omnissa Workspace ONE, Microsoft Intune & Endpoint Manager

### Service Integrations
- Identity: Active Directory, Okta, Microsoft Entra ID, JumpCloud, OneLogin
- DNS/Security: Cisco Umbrella, Cloudflare DNS filtering, Netskope DLP, Zscaler
- Databases: MongoDB, AWS RDS, GCP, Azure, Oracle, Snowflake, Redis

### SaaS App Gating
- IP-based access control for SaaS applications
- IdP integrations: Google Workspace, JumpCloud, Entra ID, Okta, OneLogin
- Use cases: AWS CloudFront, Office 365

### Kubernetes
- Route traffic from K8s, private/public resource exposure, kubectl management

### Notable Use Cases
- AI/LLM access, CI/CD pipeline security, site-to-site connections
- SSH resource management, IoT headless client gateway
- Replace AWS VPN, vendor/contractor access management
- Self-hosted VPN with Exit Networks

## Best Practices Docs Available
- Connector placement and configuration
- Private DNS configuration
- Overlapping IP addresses
- Security policies
- Non-production environment access
- SaaS App Gating
- Internal network design with peer-to-peer

## Technical Reference Docs Available
- NAT traversal, encryption, firewall behavior
- Peer-to-peer troubleshooting
- Connector shutdown process
- Service accounts, Windows Start Before Logon
- Performance evaluation
- Release stages

## Gotchas
- This page is navigation-only; no configuration values are defined here
- Specific implementation details require navigating to individual guide pages

## Related Docs
- `/docs/connector-best-practices`
- `/docs/remote-network-best-practices`
- `/docs/security-policies`
- `/docs/kubernetes`
- `/docs/saas-app-gating`
- `/docs/logging`
- `/docs/client-deployment`