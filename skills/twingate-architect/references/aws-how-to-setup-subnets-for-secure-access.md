# AWS: Reference Network Architecture

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Uses a public subnet for NAT/egress and a private subnet for Connectors and Resources. Two main deployment topologies available: public subnet with Elastic IP or private subnet with NAT.

## Key Information
- **Public subnet**: NAT gateway + Elastic IP + Internet Gateway (egress only)
- **Private subnet**: Twingate Connector + internal Resources
- No inbound connections into VPC; NAT gateway is the only public IP resource
- Minimum 2 Connectors recommended for production redundancy
- Access control policies defined via Twingate Admin Console

## Deployment Options

### Connector Placement
| Option | Description |
|--------|-------------|
| Public Subnet | Connectors get Elastic IPs; enables direct P2P |
| Private Subnet + NAT | Connectors behind NAT; NAT handles egress |

### Compute Options
- **EC2**: Manual launch or automated via CloudFormation, Terraform, user data scripts
- **ECS**: EC2 launch type (self-managed) or Fargate (serverless)

## P2P Connectivity Gotchas
- AWS standard NAT Gateway is **not NAT traversal friendly** — breaks Twingate P2P connections in some situations
- Use alternative NAT solutions for P2P support:
  - **Cohesive Networks VNS3** (AMI-based)
  - **alterNAT** (AMI-based)
  - **fck-nat** (self-hosted EC2, open-source)
- Same outbound port/protocol rules apply regardless of deployment topology

## Security Group Requirements
- Block all inbound connections to VPC
- Allow outbound connections from NAT gateway to Twingate servers
- Connector can reach Resources via TCP, UDP, ICMP within private subnet

## Configuration Notes
- NAT gateway should reside in a subnet **without** private Resources
- Outbound rules for P2P traffic must be explicitly configured (specific ports/protocols — see Twingate firewall docs)

## Infrastructure as Code
- Terraform is the recommended deployment method
- Twingate provides official Terraform configs: [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws-deployment)
- Example repo: [Twingate Solutions Engineering Terraform Demo Repository](https://github.com/Twingate-Labs)

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Internet Gateway attached to VPC
- Twingate account with Admin Console access
- Connector tokens generated from Admin Console

## Related Docs
- Twingate Connector on Amazon EC2
- Twingate Connector on Amazon ECS
- Terraform AWS Deployment Guide
- NAT Traversal documentation
- Twingate firewall/outbound port requirements