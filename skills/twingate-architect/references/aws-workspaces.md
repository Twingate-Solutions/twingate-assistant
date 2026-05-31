# How to Use Twingate with AWS Workspaces

## Summary
Twingate integrates with AWS Workspaces in two ways: installing Twingate inside a Workspace to access protected resources, or using Twingate to restrict/protect access to AWS Workspaces itself. The second workflow requires configuring Twingate Resources and AWS IP Groups to enforce tunnel-based access.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Gate access *to* AWS Workspaces through Twingate by combining Twingate Resource rules with AWS IP Group restrictions

## Prerequisites
- Twingate Remote Network configured and associated with Connectors that have known egress IPs
- AWS Workspaces environment with VPC details available
- Access to AWS Workspaces console to create/manage IP Groups

## Step-by-Step: Protecting AWS Workspaces Access (Workflow 2)

### In Twingate
1. Select the Remote Network that will route traffic to AWS Workspaces
2. Create Resources for the following and assign to Groups:
   - Private AWS IPv4 CIDR block used in the VPC during Workspaces setup
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
3. Reference [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) for correct IPs and DNS names

### In AWS
1. Create an IP Group in AWS Workspaces console
2. Add a rule to the IP Group
3. Add the internet egress IP(s) used by the Twingate Connectors associated with the Remote Network

## Configuration Values
| Item | Details |
|------|---------|
| Broker Service format | `ws-broker-service.<region>.amazonaws.com` |
| IP to allowlist | Twingate Connector egress IP(s) for the Remote Network |
| VPC CIDR | Private IPv4 CIDR from Workspaces VPC setup |

## Gotchas
- Must use the **Connector egress IPs** (not user IPs) in the AWS IP Group — traffic exits through the Connector
- Multiple Resources are required (CIDR + endpoints + auth + broker); missing any can break Workspaces connectivity
- Region-specific broker service URLs — confirm correct region in the DNS name
- Workflow 1 (Twingate inside Workspace) and Workflow 2 (Twingate protecting Workspace) are independent use cases and can coexist

## Related Docs
- [AWS IP address and port requirements for Workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)
- Twingate MDM deployment (for Workflow 1 at scale)
- Twingate Remote Networks and Connectors configuration
- Twingate Resources and Group access management