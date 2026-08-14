---
source: https://www.twingate.com/docs/aws-how-to-setup-subnets-for-secure-access
type: docs
fetched: 2026-08-14
source_version: 5e870409d862ec2ce852ced19fab922597d5960e440b66d85ce9270f91392473
---

# AWS: Reference Network Architecture

## Page Title
AWS: Reference Network Architecture for Secure VPC Access with Twingate

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Covers subnet design, NAT considerations, and deployment options (EC2, ECS, Terraform). Key constraint: standard AWS NAT gateway is not fully NAT-traversal friendly for Twingate P2P connections.

## Key Information
- **Public subnet**: NAT gateway with Elastic IP + Internet Gateway (egress only)
- **Private subnet**: Twingate Connector + internal resources
- No inbound connections into VPC; NAT gateway is the only resource with public IP
- Connector accesses private resources via TCP, UDP, ICMP
- Minimum **2 Connectors** recommended for production redundancy

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Outbound connectivity from NAT gateway to Twingate servers
- Twingate Admin Console access to define access control policies

## Deployment Options

### Subnet Placement
| Option | Description |
|--------|-------------|
| Public Subnet | Connector gets Elastic IP; enables direct P2P connections |
| Private Subnet + NAT | Connector in private subnet; NAT handles egress (recommended for isolation) |

### Compute Options
- **EC2**: Manual or automated via CloudFormation, Terraform, user data scripts
- **ECS**: EC2 launch type (self-managed) or Fargate (serverless)
- **IaC**: Terraform recommended for repeatable deployments

## NAT Gateway Gotchas

> ⚠️ **Critical**: Standard AWS NAT Gateway is **not NAT traversal-friendly** in all situations — this breaks Twingate P2P connections.

### Recommended Alternative NAT Solutions
- **Cohesive Networks VNS3** (AMI-based)
- **alterNAT** (AMI-based)
- **fck-nat** (self-hosted EC2, open-source)

These alternatives support NAT traversal required for stable P2P between Twingate Clients and Connectors.

## Configuration Values
- NAT gateway security group: allow **outbound** connections to Twingate servers
- Same outbound port/protocol rules apply regardless of subnet deployment option
- NAT gateway should reside in subnet **without** private resources

## Gotchas
- Routing and Security Groups must block **all inbound** connections to VPC
- Standard AWS NAT gateway breaks P2P — use alternative NAT for P2P functionality
- Two Connectors minimum for production; add more for capacity scaling
- NAT gateway subnet isolation reduces attack surface further

## Related Docs
- [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- [Twingate Solutions Engineering Terraform Demo Repository](https://github.com/Twingate-Solutions)
- Twingate Connector EC2 deployment guide
- Twingate Connector ECS deployment guide
- NAT Traversal documentation
- Outbound firewall rules for Connectors