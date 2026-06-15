# AWS: Reference Network Architecture

## Page Title
AWS: Reference Network Architecture for Secure Access with Twingate

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Uses a private subnet for Connectors and a public subnet for NAT/egress only. Supports EC2, ECS, and Terraform deployment methods.

## Key Information
- **Public subnet**: NAT gateway (with Elastic IP) + Internet Gateway only — no private resources
- **Private subnet**: Twingate Connector + internal Resources
- **Zero inbound connections** into VPC; NAT gateway is the only resource with a public IP
- Minimum **two Connectors** recommended for production redundancy
- Access policies defined via Twingate Admin Console

## Deployment Options

### Connector Placement
| Option | Description |
|--------|-------------|
| Public subnet | Connector gets Elastic IP; enables direct P2P |
| Private subnet + NAT | Connector behind NAT; NAT handles egress |

### Compute Options
- **EC2**: Manual, CloudFormation, Terraform, or user data scripts
- **ECS**: EC2 launch type or Fargate (serverless)

## P2P Connectivity Gotchas
- **AWS standard NAT gateway is NOT fully NAT traversal friendly** — breaks Twingate P2P connections in some scenarios
- Use alternative NAT solutions for reliable P2P:
  - [Cohesive Networks VNS3](https://cohesivenet.com) (AMI-based)
  - [alterNAT](https://github.com/1debit/alternat) (AMI-based)
  - [fck-nat](https://github.com/AndrewGuenther/fck-nat) (self-hosted EC2, open-source)
- Same outbound port/protocol rules apply regardless of deployment option

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Internet Gateway attached to VPC
- Elastic IP for NAT gateway
- Twingate Admin Console access to define Resources and access policies

## Configuration Values
- **Security Groups**: Allow outbound to Twingate servers (specific ports per P2P docs)
- **Routing**: Block all inbound to VPC; route private subnet egress through NAT
- **NAT placement**: Separate subnet from private Resources

## Recommended IaC
- Terraform configs available via [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- [Twingate Solutions Engineering Terraform Demo Repo](https://github.com/Twingate-Labs) for quick starts

## Related Docs
- Twingate Connector on Amazon EC2
- Twingate Connector on Amazon ECS
- Terraform AWS Deployment Guide
- NAT Traversal documentation
- Outbound firewall rules (ports/protocols for P2P)