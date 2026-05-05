## Deploying Connectors

Guide to selecting the right Connector deployment method based on your environment. All Connectors deploy as either a Linux systemd package or an OCI (Docker) container.

**Key Facts:**
- One Connector can serve all reachable Resources in its network — no need to deploy per-host
- Additional Connectors on separate hosts provide load balancing and failover

**Supported Linux Distributions (x86/AMD64 and ARM64):**
- Ubuntu 22.04 LTS, 24.04 LTS
- Debian 11+, Fedora 41+, CentOS Stream 9+, Oracle Linux 8+
- x64-only: Arch Linux, HP ThinPro, NixOS, Gentoo

**Deployment Options by Environment:**

**Cloud VMs (recommended for cloud):**
- AWS EC2, GCP Compute, Azure Compute, Kubernetes (Helm)

**Offices / Data Centers / On-Premises:**
- Docker Compose, Firewalla Box, Synology (DSM 6 or 7), QNAP NAS, Proxmox Container, TrueNAS SCALE
- No inbound firewall rules needed — only outbound internet access required
- Deploy a second Connector on a separate physical machine for HA

**Serverless / PaaS:**
- AWS ECS Fargate, Azure ACS, Aptible

**Infrastructure-as-Code:**
- Terraform, Pulumi

**Home Networks:**
- Mac (VM), Synology DSM 7.x, Raspberry Pi, Linux, Home Assistant, Proxmox, Unraid

**Related Docs:**
- /docs/connector-placement-best-practices -- Placement guidance
- /docs/deploy-connector-with-docker-compose -- Docker Compose reference
- /docs/terraform-getting-started -- Terraform deployment
