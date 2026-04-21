## Page Title
AWS: Reference Network Architecture

## Summary
Reference architecture for deploying Twingate in an AWS VPC with minimal attack surface. One public subnet holds a NAT gateway; one private subnet holds the Twingate Connector and internal resources. No inbound connections into the VPC are required. Includes guidance on P2P compatibility issues with the AWS-managed NAT gateway.

## Key Information
- **Architecture**: Public subnet with NAT gateway + Elastic IP; private subnet with Connector and resources; Internet Gateway for egress; no inbound rules
- **Two Connector placement options**:
  1. Public subnet with Elastic IP -- direct P2P possible
  2. Private subnet + NAT -- Connector egresses via NAT; better isolation
- **AWS NAT gateway P2P limitation**: The standard AWS managed NAT gateway is NOT NAT-traversal friendly for P2P connections -- P2P will fall back to Relay more often
- **Alternative NAT solutions for P2P**: Cohesive VNS3, alterNAT, or self-hosted EC2 with `fck-nat` -- these support NAT traversal for P2P
- **Deployment options**: EC2 instances (manual or via CloudFormation/Terraform/user-data) or ECS tasks (EC2 or Fargate launch type)
- **Minimum 2 Connectors** recommended for redundancy in production
- Twingate provides a Terraform configuration for this architecture

## Prerequisites
- AWS VPC with appropriate address space
- Outbound rules allowing Connector to reach Twingate servers (Controller + Relay)

## Step-by-Step
See deployment options above; Terraform quick-start available at `/docs/terraform-aws`.

## Configuration Values
- NAT gateway must allow outbound to Twingate servers
- Inbound: no rules required (Connector uses outbound-only connections)

## Gotchas
- AWS managed NAT gateway causes P2P fallback to Relay; use alternative NAT if P2P performance matters
- Security Groups must explicitly allow Connector outbound to Twingate infrastructure
- Deploy minimum 2 Connectors per Remote Network for production HA

## Related Docs
- `/docs/terraform-aws` -- Terraform deployment guide for this architecture
- `/docs/aws` -- AWS Connector deployment guide
- `/docs/peer-to-peer-communication-in-twingate` -- P2P transport detail
- `/docs/connector-placement-best-practices` -- Connector sizing and placement
