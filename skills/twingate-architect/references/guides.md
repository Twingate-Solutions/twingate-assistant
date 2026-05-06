# Twingate Guides Index

## Page Title
Twingate Guides Overview

## Summary
This is the documentation hub for Twingate deployment, configuration, and management guides. It categorizes all available guides across deployment targets, use cases, integrations, and architectural best practices. Use this page to navigate to specific implementation documentation.

## Key Information

### Deployment Targets
- **Cloud**: AWS EC2, GCP Compute, Azure Compute, DigitalOcean, Kubernetes
- **On-premises**: Docker Compose, Synology, QNAP NAS, Proxmox, TrueNAS SCALE, Firewalla
- **Homelabs**: Home Assistant, Proxmox, Unraid
- **IaC**: Terraform, Pulumi

### Client Deployment (MDM)
- Jamf, Kandji, Omnissa Workspace ONE, Microsoft Intune & Endpoint Manager

### Service Compatibility
- Active Directory, Cisco Umbrella, Cloudflare DNS filtering, Netskope DLP, Zscaler

### SaaS App Gating Integrations
- Google Workspace, JumpCloud, Microsoft Entra ID, Okta, OneLogin
- AWS Exit Nodes, AWS CloudFront, Office 365

### Kubernetes Topics
- Traffic routing, private/public resources, kubectl management

### Key Use Cases
- AI/LLM access, database access, SSH access, CI/CD pipelines
- Site-to-site connections, IoT headless client gateway
- Vendor/contractor access management, bastion server cloaking
- Replace AWS VPN, AWS Workspaces integration

## Technical Reference Docs
- NAT traversal mechanics
- Encryption implementation
- Connector shutdown process
- Firewall behavior
- Service accounts
- Windows Start Before Logon
- Peer-to-peer connection troubleshooting
- Performance evaluation

## Best Practices Docs
- Private DNS configuration
- Connector placement
- Overlapping IP addresses
- Security policies
- Non-production environment access
- Whitelisting public resources
- Local peer-to-peer (LAN) connections
- Remote Network and Connector setup

## Gotchas
- This page is an index only — no configuration values or step-by-step instructions are present here
- Use this page to identify which sub-guide to consult for a specific task

## Related Docs
- `/docs/internet-security` — DNS-over-HTTPS and filtering
- `/docs/saas-app-gating` — SaaS IP-based access control
- `/docs/security-policies` — Policy configuration
- `/docs/logging` — Audit log access and export
- `/docs/kubernetes` — K8s-specific deployment and management