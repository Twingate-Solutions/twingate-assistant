# AWS: Reference Network Architecture

## Page Title
AWS: Reference Network Architecture (Subnet Setup for Secure Access)

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPCs using a layered security model. Uses a public subnet for NAT/egress and a private subnet for Connectors and resources. Minimizes attack surface by preventing all inbound connections to the VPC.

## Key Information
- **Public subnet**: NAT gateway (with Elastic IP) + Internet Gateway for egress only
- **Private subnet**: Twingate Connector + internal Resources
- No inbound connections allowed into VPC; NAT gateway is the only resource with a public IP
- Access control policies defined via Twingate Admin Console
- Minimum **two Connectors** recommended for production redundancy

## Deployment Options

### Connector Placement
| Option | Description |
|--------|-------------|
| Public Subnet | Connectors get Elastic IPs; supports direct P2P |
| Private Subnet + NAT | Connectors behind NAT; NAT is egress point |

### Compute Options
- **EC2**: Manual or automated via CloudFormation, Terraform, or user data scripts
- **ECS**: EC2 launch type or Fargate (serverless); recommended for containerized workflows

## NAT Gateway P2P Caveat (Critical)
AWS native NAT Gateway **is not NAT traversal-friendly** in all situations — breaks Twingate P2P connections. Use alternatives:
- **AMI-based**: Cohesive Networks VNS3, alterNAT
- **Self-hosted EC2**: fck-nat (open source)

Standard AWS NAT Gateway can still work for relay-based connections but degrades performance.

## Prerequisites
- AWS VPC with at least one public and one private subnet configured
- Internet Gateway attached to VPC
- Elastic IP for NAT gateway
- Security Groups configured to allow outbound connections to Twingate servers
- Twingate Admin Console access for Resource/policy configuration

## Configuration Values
- Outbound rules required for P2P traffic (specific ports/protocols — see Twingate network requirements docs)
- NAT gateway Security Group: allow outbound to Twingate relay/control servers
- No inbound rules needed on VPC perimeter

## Gotchas
- AWS NAT Gateway blocks P2P in some scenarios — use alternative NAT for reliable P2P
- NAT gateway should be in a subnet **without private resources** to reduce attack surface
- Both deployment models (public/private subnet) require the same outbound port rules
- Fargate launch type removes EC2 management overhead but reduces customization

## Infrastructure as Code
- Twingate provides Terraform configs: [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- Example repo: [Twingate Solutions Engineering Terraform Demo Repository](https://github.com/Twingate-Solutions)

## Related Docs
- Twingate Connector on Amazon EC2
- Twingate Connector on Amazon ECS
- Terraform AWS Deployment Guide
- NAT Traversal documentation
- Twingate network requirements (ports/protocols)