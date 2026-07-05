# AWS: Reference Network Architecture

## Page Title
AWS: Reference Network Architecture for Secure Access with Twingate

## Summary
Describes a reference VPC architecture for deploying Twingate Connectors in AWS with minimal attack surface. Architecture uses a private subnet for Connectors and a public subnet for NAT/egress only. Covers deployment options (EC2, ECS), NAT considerations for P2P, and IaC tooling.

## Key Information
- **Public subnet**: NAT gateway (Elastic IP) + Internet Gateway — egress only, no private resources
- **Private subnet**: Twingate Connector + internal Resources
- No inbound connections into VPC; NAT gateway is the only public IP resource
- Connector communicates with Resources via TCP, UDP, ICMP within private subnet
- Minimum **2 Connectors** recommended for production redundancy

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Security Groups configured to allow **outbound** connections to Twingate servers
- Twingate Admin Console access to define access control policies

## Deployment Options

### Connector Placement
| Option | Description |
|--------|-------------|
| Public Subnet | Assign Elastic IPs directly to Connectors; enables direct P2P |
| Private Subnet + NAT | Connectors in private subnet; NAT handles egress (recommended) |

### Compute Options
- **EC2**: Manual launch or automated via CloudFormation, Terraform, user data scripts
- **ECS**: EC2 launch type (self-managed nodes) or Fargate (serverless)

## P2P Connectivity Gotchas
- **AWS native NAT Gateway is NOT fully NAT-traversal friendly** — breaks Twingate P2P in some scenarios
- Use alternative NAT solutions for reliable P2P:
  - **AMI-based**: Cohesive Networks VNS3, alterNAT
  - **Self-hosted EC2**: fck-nat (open source)
- Same outbound port/protocol rules apply regardless of deployment type

## Configuration Values
- Outbound Security Group rules must permit traffic to Twingate's relay servers (see Twingate network requirements docs for specific ports)
- NAT gateway must allow outbound connections to Twingate servers

## IaC / Terraform
- Official Terraform config: [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws-deployment)
- Example repo: [Twingate Solutions Engineering Terraform Demo Repository](https://github.com/Twingate-Solutions)
- Recommended for repeatable, version-controlled deployments

## Gotchas
- AWS NAT Gateway limitations affect P2P — plan NAT strategy before deployment
- NAT gateway should be in a **dedicated subnet without private resources**
- Routing + Security Groups must block **all inbound** VPC connections

## Related Docs
- Twingate Connector on Amazon EC2
- Twingate Connector on Amazon ECS
- Terraform AWS Deployment Guide
- Twingate P2P / NAT Traversal documentation
- Twingate network outbound requirements