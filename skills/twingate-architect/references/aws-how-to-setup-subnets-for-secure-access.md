# AWS Reference Network Architecture for Twingate

## Page Title
AWS: Reference Network Architecture

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Covers subnet design, NAT options, P2P connectivity considerations, and deployment methods (EC2, ECS, Terraform).

## Key Information
- **Public subnet**: hosts NAT gateway (Elastic IP) + Internet Gateway for egress only
- **Private subnet**: hosts Twingate Connector + internal Resources
- No inbound connections into VPC; NAT gateway is the only resource with public IP
- Minimum two Connectors recommended for production redundancy

## Two Connector Deployment Options
| Option | Description |
|--------|-------------|
| Public Subnet | Connectors in public subnet with Elastic IPs; enables direct P2P |
| Private Subnet + NAT | Connectors alongside Resources; NAT in public subnet handles egress |

## P2P Connectivity Gotchas
- **AWS standard NAT gateway is NOT NAT traversal-friendly** — breaks Twingate P2P connections in some scenarios
- Use alternative NAT solutions for P2P support:
  - **AMI-based**: Cohesive Networks VNS3, alterNAT
  - **Self-hosted EC2**: fck-nat (open-source)
- Both deployment options require identical outbound port/protocol rules for P2P traffic

## Deployment Methods
- **EC2**: Manual install or automated via CloudFormation, Terraform, or user data scripts
- **ECS**: Deploy as tasks using EC2 launch type or Fargate (serverless)
- **Terraform**: Recommended for repeatable deployments; official configs available

## Configuration Values
- NAT gateway Security Group: must allow **outbound connections** to Twingate servers
- Connector access to Resources: TCP, UDP, ICMP within private subnet
- NAT gateway: place in subnet **without** private resources

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Internet Gateway attached to VPC
- Twingate Admin Console access (for defining access control policies)
- Elastic IP for NAT gateway

## Related Docs
- [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- [Amazon EC2 Connector deployment](https://www.twingate.com/docs/aws-ec2)
- [Amazon ECS Connector deployment](https://www.twingate.com/docs/aws-ecs)
- [Twingate Solutions Engineering Terraform Demo Repository (GitHub)](https://github.com/Twingate-Solutions)
- [NAT Traversal documentation](https://www.twingate.com/docs/nat-traversal)
- [P2P connections](https://www.twingate.com/docs/peer-to-peer)