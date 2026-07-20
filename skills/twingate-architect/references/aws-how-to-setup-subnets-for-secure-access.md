# AWS Reference Network Architecture for Twingate

## Page Title
AWS: Reference Network Architecture

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Covers subnet design, NAT considerations, deployment options (EC2/ECS), and IaC tooling. Standard AWS NAT Gateway has P2P traversal limitations requiring alternative solutions.

## Key Information
- **Public subnet**: NAT Gateway with Elastic IP + Internet Gateway (egress only)
- **Private subnet**: Twingate Connector + internal Resources
- No inbound connections should be allowed into VPC from outside
- NAT Gateway should be the **only** resource with a public IP
- Minimum **2 Connectors** recommended for production redundancy

## Deployment Options

### Connector Placement
| Option | Description |
|--------|-------------|
| Public Subnet | Connectors get Elastic IPs; enables direct P2P |
| Private Subnet + NAT | Connectors behind NAT; NAT is egress point |

### Compute Options
- **EC2**: Manual launch or automated via CloudFormation, Terraform, user data scripts
- **ECS**: EC2 launch type or Fargate (serverless); better for containerized workflows

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Twingate Admin Console access (for defining access control policies)
- Outbound firewall rules configured for Twingate server connectivity

## P2P Connectivity Gotcha ⚠️
**Standard AWS NAT Gateway is NOT fully NAT traversal-friendly** — breaks Twingate P2P connections in some scenarios.

### Recommended Alternatives for P2P Support
- **AMI-based**: Cohesive Networks VNS3, alterNAT
- **Self-hosted EC2**: fck-nat (open-source)
- These also typically cost less than AWS NAT Gateway

## Configuration Values
- Outbound Security Group rules must allow traffic to Twingate servers (specific ports/protocols per P2P requirements — see linked outbound rules doc)
- Connector needs outbound TCP/UDP/ICMP access to private Resources within subnet

## IaC / Terraform
- Official Terraform config available: [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws-deployment)
- Community examples: [Twingate SE Terraform Demo Repo (GitHub)](https://github.com/Twingate-Solutions)

## Gotchas
- NAT Gateway subnet should contain **no private resources** (reduces attack surface)
- Same outbound port/protocol rules apply regardless of public vs. private subnet deployment
- Standard AWS NAT Gateway will cause P2P fallback to relay — use alternative NAT for true P2P

## Related Docs
- Outbound connection requirements (ports/protocols)
- Twingate Connector on Amazon EC2
- Twingate Connector on Amazon ECS
- Terraform AWS Deployment Guide
- NAT Traversal documentation