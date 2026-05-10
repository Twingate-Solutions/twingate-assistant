# Twingate Guides Index

## Page Title
Twingate Guides — Deployment, Configuration, and Management Reference

## Summary
This is the top-level index page for all Twingate documentation guides. It organizes deployment, configuration, management, and best practice content across infrastructure types, platforms, and use cases. Use this page to navigate to specific implementation guides.

## Key Information

### Deployment Targets
- **Cloud**: AWS EC2, GCP Compute, Azure Compute, Kubernetes, DigitalOcean
- **On-premises**: Docker Compose, Ubiquiti, Firewalla, Synology, QNAP NAS, TrueNAS SCALE, Proxmox
- **Homelabs**: Home Assistant, Unraid, ZimaOS, CasaOS
- **Client MDM**: Jamf, Kandji, Omnissa Workspace ONE, Microsoft Intune

### Core Feature Guides
- DNS encryption (DoH) and DNS filtering
- SaaS App Gating (IP-based access control for SaaS)
- Security Policies (network-wide and per-resource)
- Audit logging (view and export)
- Kubernetes resource management

### IaC Automation
- Terraform and Pulumi providers available

### Service Integrations
- Identity: Active Directory, Okta, JumpCloud, Microsoft Entra ID, OneLogin
- Security tools: Cisco Umbrella, Cloudflare DNS, Netskope DLP, Zscaler
- SIEM: Connector log ingestion guide available

### Use Case Guides
- CI/CD pipeline security
- SSH resource access
- Database access
- IoT headless client gateway
- Vendor/contractor access management
- Site-to-site connections
- AWS VPN replacement
- Self-hosted VPN with Exit Networks

### Architecture & Best Practices
- Connector placement and routing
- Private DNS configuration
- Overlapping IP address handling
- Non-production environment security
- Security policy design
- SaaS App Gating design

### Technical Reference
- NAT traversal mechanics
- Encryption implementation
- Firewall interaction
- Peer-to-peer troubleshooting
- Service accounts
- Windows Start Before Logon
- Connector shutdown process

## Prerequisites
None — this is an index/navigation page.

## Gotchas
- Page is updated frequently ("last updated 1 day ago"); specific sub-guide URLs should be verified directly
- SaaS App Gating requires identity provider integration for full functionality (Okta, Entra ID, etc.)

## Related Docs
- Connector Best Practices
- Remote Network Best Practices
- Best Practices for Security Policies
- AWS Reference Network Architecture
- Twingate Release Stages