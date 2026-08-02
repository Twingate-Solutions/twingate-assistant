# Twingate Guides Index

## Page Title
Twingate Guides — Documentation Index

## Summary
This is the top-level index page for Twingate's documentation guides, organizing all deployment, configuration, and management topics. It serves as a navigation hub covering infrastructure deployment, client setup, policy configuration, service integrations, and architectural best practices.

## Key Information

### Deployment Targets
- **Cloud**: AWS EC2, GCP Compute, Azure Compute, Kubernetes, DigitalOcean
- **On-premises**: Docker Compose, Ubiquiti, Firewalla, Synology, QNAP, TrueNAS, Proxmox
- **Homelabs**: Home Assistant, Unraid, ZimaOS, CasaOS
- **IaC**: Terraform, Pulumi

### Client Deployment (MDM)
- Jamf, Iru, Omnissa Workspace ONE, Microsoft Intune & Endpoint Manager

### Service Integrations
- **Identity/Directory**: Active Directory, Okta, Microsoft Entra ID, JumpCloud, OneLogin
- **Security tools**: Cisco Umbrella, Cloudflare DNS filtering, Netskope DLP, Zscaler
- **Databases**: MongoDB, AWS, GCP, Azure, Oracle, Snowflake, Redis

### Key Feature Areas
- **Internet Security**: DNS-over-HTTPS (DoH), DNS filtering
- **SaaS App Gating**: IP-based access control for SaaS apps
- **Security Policies**: Per-network and per-resource policy definitions
- **Logging**: Audit log export and SIEM ingestion

## Notable Use Cases
- Replace AWS VPN with Twingate
- Secure CI/CD pipelines
- Site-to-site connections
- IoT headless client gateway
- Vendor/contractor access management
- SSH resource access management
- GitHub Codespaces integration
- AI/LLM access control

## Best Practices Docs Available
- Connector placement and routing optimization
- Private DNS configuration
- Overlapping IP address handling
- Security policy design
- Non-production environment access
- SaaS App Gating architecture
- Internal network with local peer-to-peer

## Technical Reference Topics
- NAT traversal mechanics
- Encryption implementation
- Firewall interaction
- Connector shutdown process
- Service accounts
- Windows Start Before Logon
- Performance evaluation

## Related Docs
- Individual guide pages linked throughout (no direct URLs provided on this index page)
- Start with **Client Deployment** for end-user rollout
- Start with **Cloud Infrastructure** or **On-premises Networks** for Connector setup
- See **Best Practices** section before production deployment

## Gotchas
- This page is navigation-only; no configuration values or step-by-step procedures are present here
- SaaS App Gating requires separate IdP configuration (Okta, Entra ID, etc.)
- Kubernetes deployment has multiple sub-guides depending on whether resources are private or publicly exposed