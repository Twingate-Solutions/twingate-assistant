# AWS: Reference Network Architecture

## Page Title
AWS: Reference Network Architecture for Secure Access with Twingate

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Uses a public subnet (NAT gateway only) and private subnet (Connectors + Resources). Two main deployment topologies: public subnet with Elastic IPs or private subnet behind NAT.

## Key Information
- **Public subnet**: NAT gateway + Elastic IP + Internet Gateway (egress only)
- **Private subnet**: Twingate Connector(s) + internal Resources
- No inbound connections into VPC; NAT gateway is the only resource with public IP
- Minimum 2 Connectors recommended for production redundancy
- Standard AWS NAT gateway is **not** fully NAT-traversal friendly for P2P connections

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Security Groups configured to allow outbound connections to Twingate servers
- Twingate Admin Console access for Resource/policy configuration

## Deployment Options

### Connector Placement
| Option | Description |
|--------|-------------|
| Public Subnet | Connectors get Elastic IPs; enables direct P2P |
| Private Subnet + NAT | Connectors behind NAT; NAT handles egress |

### Compute Options
- **EC2**: Manual launch or via CloudFormation/Terraform/user-data scripts
- **ECS**: EC2 launch type (self-managed) or Fargate (serverless)

## Configuration Values
- Outbound Security Group rules must permit Twingate relay server traffic (specific ports/protocols per [outbound rules docs])
- Same outbound rules apply regardless of public vs. private subnet deployment

## Gotchas
- **AWS NAT Gateway P2P limitation**: Standard AWS NAT gateway does not support NAT traversal reliably; use alternatives for P2P:
  - AMI-based: Cohesive Networks VNS3, alterNAT
  - Self-hosted EC2: fck-nat
- NAT gateway should reside in a subnet without private Resources
- Missing outbound rules on NAT gateway will break Connector functionality

## Related Docs
- [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- [Twingate SE Terraform Demo Repository (GitHub)](https://github.com/Twingate-Labs)
- [EC2 Connector Deployment](https://www.twingate.com/docs/aws-ec2)
- [ECS Connector Deployment](https://www.twingate.com/docs/aws-ecs)
- Twingate P2P / NAT Traversal documentation