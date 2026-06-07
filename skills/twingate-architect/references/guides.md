# Twingate Guides Index

## Page Title
Twingate Guides — Documentation Index

## Summary
This is the top-level index page for all Twingate deployment, configuration, and management guides. It organizes documentation into categories covering infrastructure deployment, client management, integrations, Kubernetes, security policies, and architectural best practices.

## Key Information

**Deployment Targets:**
- Cloud: AWS EC2, GCP Compute, Azure Compute, Kubernetes, DigitalOcean
- On-premises: Docker Compose, Ubiquiti, Firewalla, Synology, QNAP, TrueNAS, Proxmox
- Homelab: Home Assistant, Unraid, ZimaOS, CasaOS
- IaC: Terraform, Pulumi

**Client Deployment (MDM):**
- Jamf, Iru, Omnissa Workspace ONE, Microsoft Intune/Endpoint Manager

**Identity/Service Integrations:**
- IdP for SaaS App Gating: Google Workspace, JumpCloud, Microsoft Entra ID, Okta, OneLogin
- Complementary services: Active Directory, Cisco Umbrella, Cloudflare DNS, Netskope DLP, Zscaler

**Database Access:**
- MongoDB, AWS, GCP, Azure, Oracle, Snowflake, Redis

**Kubernetes-Specific:**
- Route traffic from K8s, private/public resource exposure, kubectl management

## Notable Use Cases Covered
- AI/LLM access control
- CI/CD pipeline security
- IoT headless client gateway
- Site-to-site connections
- Replace AWS VPN
- SSH resource access management
- Vendor/contractor access management
- SaaS App Gating with exit nodes (AWS CloudFront, AWS Exit Nodes)
- Self-hosted VPN via Exit Networks

## Architecture & Best Practices Topics
- Private DNS configuration
- Connector placement
- Overlapping IP address handling
- Non-production environment access
- Security policy design
- Peer-to-peer/local connections

## Technical Reference Topics
- NAT traversal mechanics
- Encryption implementation
- Firewall behavior
- Connector shutdown process
- Service accounts
- Windows Start Before Logon
- Performance evaluation

## Related Docs
- `/docs/internet-security` — DNS-over-HTTPS, DNS filtering
- `/docs/saas-app-gating` — IP-based SaaS access control
- `/docs/security-policies` — Policy configuration
- `/docs/kubernetes` — K8s deployment guides
- `/docs/logging` — Audit log export
- `/docs/connector-best-practices` — Connector optimization
- `/docs/remote-network-best-practices` — Network organization

---
*This page serves as a navigation index only — no configuration values or step-by-step procedures are directly contained here.*