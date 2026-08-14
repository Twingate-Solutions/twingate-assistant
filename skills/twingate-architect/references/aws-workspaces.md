---
source: https://www.twingate.com/docs/aws-workspaces
type: docs
fetched: 2026-08-14
source_version: 9ef13a56e642504f852f68afb81432d17c5f5fb4802072db6d2a3bc0974ddebf
---

# How to Use Twingate with AWS Workspaces

## Summary
Twingate integrates with AWS Workspaces in two ways: installing the Twingate Client inside a Workspace to access protected resources, or using Twingate to gate access to AWS Workspaces itself. The second workflow requires creating specific Twingate Resources and restricting AWS Workspaces to only allow Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Protect access *to* AWS Workspaces by routing traffic through Twingate tunnels and allowlisting Connector egress IPs in AWS

## Prerequisites
- Twingate Remote Network configured and associated with Connectors
- AWS Workspaces environment with a VPC
- Twingate Connector egress IP addresses (internet-facing IPs of Connectors in the Remote Network)
- AWS IP address and port requirements reference: [AWS documentation](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)

## Step-by-Step: Protecting AWS Workspaces Access (Workflow 2)

### In Twingate
1. Select the applicable Remote Network for AWS Workspaces access
2. Create Resources for the following (assign access via Group membership):
   - Private AWS IPv4 CIDR block used when the VPC was created
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a Rule to the IP Group
3. Add the internet egress IP address(es) used by Twingate Connectors associated with the Remote Network

## Configuration Values

| Item | Value/Example |
|------|---------------|
| Broker Service DNS pattern | `ws-broker-service.<region>.amazonaws.com` |
| IP source for allowlist | Twingate Connector egress IPs (per Remote Network) |
| VPC CIDR | Private IPv4 CIDR assigned during AWS Workspaces VPC setup |

## Gotchas
- You must allowlist **Connector egress IPs**, not user/Client IPs — traffic exits through the Connector
- The AWS Workspaces Broker Service hostname is region-specific; use the correct region suffix
- Consult AWS IP/port requirements docs to find all required endpoints — the list includes Auth Service, Broker Service, and other endpoints that must all be covered as Twingate Resources
- Workflow 1 (Client inside Workspace) may require MDM for deployment at scale

## Related Docs
- [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)
- Twingate MDM deployment documentation
- Twingate Remote Networks and Connectors documentation
- Twingate Groups and Resource access documentation