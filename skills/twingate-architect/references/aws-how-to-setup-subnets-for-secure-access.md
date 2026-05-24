# AWS: Reference Network Architecture

## Summary
Reference architecture for deploying Twingate Connectors in AWS VPC with minimal attack surface. Covers two deployment topologies (public subnet vs. private subnet with NAT) and P2P connectivity considerations specific to AWS NAT limitations.

## Key Information
- **Goal**: Minimize attack surface using layered security; no inbound connections into VPC
- **Core components**: Internet Gateway + NAT Gateway (public subnet), Twingate Connector (private subnet)
- **NAT Gateway caveat**: Standard AWS NAT Gateway is not fully NAT traversal-friendly, which breaks P2P connections
- **Production minimum**: Deploy at least 2 Connectors for redundancy

## Deployment Options

### Topology
| Option | Description |
|--------|-------------|
| Public Subnet | Connector gets Elastic IP; enables direct P2P |
| Private Subnet + NAT | Connector in private subnet; NAT handles egress; P2P may require alternative NAT |

### Compute
- **EC2**: Full control; supports CloudFormation, Terraform, user data scripts
- **ECS**: Containerized; supports EC2 launch type or Fargate (serverless)

## Configuration Requirements
- NAT Gateway/Security Groups: **outbound-only** rules to Twingate servers
- Same outbound port/protocol rules apply to both topology options (see [Twingate outbound rules](https://www.twingate.com/docs))
- NAT gateway should be in a subnet **without** private resources

## P2P NAT Traversal Fix
Standard AWS NAT Gateway breaks P2P in some scenarios. Alternatives:

| Solution | Type |
|----------|------|
| Cohesive Networks VNS3 | AMI-based |
| alterNAT | AMI-based |
| fck-nat | Self-hosted EC2 (open-source) |

## Infrastructure as Code
- Twingate provides Terraform configs: [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- Example repo: [Twingate Solutions Engineering Terraform Demo Repository](https://github.com/Twingate-Solutions)

## Gotchas
- AWS NAT Gateway **does not support** reliable NAT traversal for P2P — use alternative NAT for P2P functionality
- NAT Gateway must explicitly allow outbound to Twingate servers or Connector will fail
- Placing NAT in a shared subnet with resources increases attack surface

## Related Docs
- [Amazon EC2 Connector Deployment](https://www.twingate.com/docs/aws-ec2)
- [Amazon ECS Connector Deployment](https://www.twingate.com/docs/aws-ecs)
- [Terraform AWS Deployment Guide](https://www.twingate.com/docs/terraform-aws)
- [Twingate Outbound Connection Rules](https://www.twingate.com/docs/connector-requirements)