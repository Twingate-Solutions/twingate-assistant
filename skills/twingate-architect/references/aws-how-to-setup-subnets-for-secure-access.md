# AWS: Reference Network Architecture

## Page Title
AWS: Reference Network Architecture for Secure Access with Twingate

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Covers subnet design, NAT considerations for P2P connectivity, and deployment options (EC2, ECS, Terraform).

## Key Information
- **Public subnet**: NAT gateway with Elastic IP + Internet Gateway (egress only)
- **Private subnet**: Twingate Connector + internal Resources
- No inbound connections into VPC; NAT gateway is the only public IP resource
- Minimum 2 Connectors recommended for production redundancy

## Deployment Options

### Connector Placement
| Option | Description |
|--------|-------------|
| Public subnet | Connector gets Elastic IP; enables direct P2P |
| Private subnet + NAT | Connector alongside Resources; NAT handles egress |

### Compute Options
- **EC2**: Manual launch or automated via CloudFormation, Terraform, user-data scripts
- **ECS**: EC2 launch type (self-managed) or Fargate (serverless)
- **IaC**: Terraform recommended for repeatable deployments

## Prerequisites
- AWS VPC with at least one public and one private subnet
- Internet Gateway attached to VPC
- Security Groups configured to allow outbound to Twingate servers
- Twingate Admin Console access for Resource/policy configuration

## Configuration Values
- Outbound rules must permit Twingate relay server ports/protocols (see Twingate network requirements docs)
- NAT gateway must allow outbound connections to Twingate servers
- Same outbound rules apply regardless of public vs. private subnet deployment

## Gotchas
- **AWS NAT Gateway is NOT fully NAT-traversal friendly** — breaks P2P connections in some scenarios
- Use alternative NAT products for reliable P2P:
  - [VNS3 cloud NAT](https://cohesivenet.com) (AMI-based)
  - [alterNAT](https://github.com/1debit/alternat) (AMI-based)
  - [fck-nat](https://github.com/AndrewGuenther/fck-nat) (self-hosted EC2)
- NAT gateway should be in a subnet **without** private resources
- Standard AWS NAT Gateway may still work for relay-only (non-P2P) connections but degrades performance

## Related Docs
- [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- [Twingate Solutions Engineering Terraform Demo Repository](https://github.com/Twingate-Labs/twingate-terraform-demo)
- EC2 Connector deployment guide
- ECS Connector deployment guide
- Twingate network requirements (outbound ports/protocols)