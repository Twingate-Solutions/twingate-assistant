## Deploy Connector on AWS

Multiple deployment options for Twingate Connectors on AWS, ranging from one-click CloudFormation to manual EC2 and ECS Fargate.

**Deployment Options:**

**CloudFormation (easiest):**
- Admin Console → Remote Network → Add Connector → AWS Quick Start
- Select region (use same region as Resources) → Open AWS → select SSH key and Subnet ID → Create stack
- Live within minutes

**EC2 (Linux VM):**
- Follow standard Linux Connector deployment instructions (Docker or systemd)
- Supported on any 64-bit Linux distro (Docker) or Ubuntu/Fedora/Debian/CentOS (systemd)
- Recommended instance: t3a.micro (sufficient for hundreds of users under typical usage)
- For remote access: AMI pre-installed with systemd service + AWS SSM Agent (no SSH key required)

**AMI Deployment:**
- Admin Console → Connector → AMI option → Generate Tokens → fill AWS environment info → copy and run CLI command

**ECS Fargate:**
- Admin Console → Connector → ECS option → Generate Tokens → fill environment info → copy task definition command → launch command
- For ICMP/ping support: add `systemControls` with `net.ipv4.ping_group_range: 0 2147483647` to the task definition
- Each Connector needs its own task definition (tokens are Connector-specific)

**EKS:**
- Use the official Twingate Helm chart; see Kubernetes Best Practices Guide

**IaC:**
- Terraform, Pulumi, or Twingate API

**Gotchas:**
- Subnet must have outbound internet access for image pull and Twingate connectivity
- Do not reuse tokens across Connector instances

**Related Docs:**
- /docs/connectors-on-linux -- Linux deployment details
- /docs/connector-best-practices -- Hardware recommendations and network requirements
- /docs/upgrading-connectors -- Update process for systemd and ECS connectors
