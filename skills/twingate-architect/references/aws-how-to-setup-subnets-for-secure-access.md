# AWS Reference Network Architecture for Twingate

## Page Title
AWS: Reference Network Architecture

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Covers subnet design, NAT options, P2P connectivity considerations, and deployment methods (EC2, ECS, Terraform).

## Key Information
- **Public subnet**: Hosts NAT gateway (with Elastic IP) and Internet Gateway only
- **Private subnet**: Hosts Twingate Connector(s) and internal Resources
- No inbound connections to VPC; NAT gateway is the only resource with a public IP
- Connector communicates outbound through NAT to Twingate's servers
- Minimum **two Connectors** recommended for production redundancy

## Two Deployment Topology Options
| Option | Description |
|--------|-------------|
| Public Subnet | Connector gets Elastic IP; enables direct P2P |
| Private Subnet + NAT | Connector behind NAT; NAT handles egress |

## P2P Connectivity Gotchas
- **AWS standard NAT Gateway is not fully NAT-traversal friendly** — breaks Twingate P2P in some scenarios
- Use alternative NAT solutions for reliable P2P:
  - [Cohesive Networks VNS3](https://cohesive.net) (AMI-based)
  - [alterNAT](https://github.com/1debit/alternat) (AMI-based)
  - [fck-nat](https://github.com/AndrewGuenther/fck-nat) (self-hosted EC2, open-source)
- Same outbound port/protocol rules apply regardless of topology

## Deployment Options
- **EC2**: Manual install or automated via CloudFormation, Terraform, or user-data scripts; full OS control
- **ECS**: Connector as container task; supports EC2 launch type or Fargate (serverless)
- **Terraform/IaC**: Recommended for repeatable deployments

## Configuration Values
- Outbound Security Group rules must allow Connector → Twingate servers (see [outbound rules](https://www.twingate.com/docs))
- Connector needs TCP/UDP/ICMP access to Resources within private subnet

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Elastic IP for NAT gateway or Connector (public subnet option)
- Twingate account with Admin Console access to define Resource policies

## Related Docs
- [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- [Twingate Solutions Engineering Terraform Demo Repository](https://github.com/Twingate-Labs)
- [Amazon EC2 Connector deployment](https://www.twingate.com/docs/aws-ec2)
- [Amazon ECS Connector deployment](https://www.twingate.com/docs/aws-ecs)
- Twingate P2P / NAT Traversal docs