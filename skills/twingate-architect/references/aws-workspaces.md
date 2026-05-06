# How to Use Twingate with AWS Workspaces

## Summary
Twingate integrates with AWS Workspaces in two modes: installing Twingate inside a Workspace to access protected resources, or using Twingate to protect access to AWS Workspaces itself. The second workflow requires creating specific Twingate Resources and restricting AWS access to Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Gate access to AWS Workspaces through Twingate tunnels by configuring Resources and AWS IP Groups

## Prerequisites
- Twingate Remote Network configured and associated with Connectors
- AWS Workspaces environment already provisioned
- Knowledge of Twingate Connector egress IP addresses
- Access to AWS console to create/manage IP Groups

## Step-by-Step: Protecting AWS Workspaces Access (Workflow 2)

### Twingate Configuration
1. Select the Remote Network that will provide access to AWS Workspaces
2. Create Resources for the following and assign via Group Membership:
   - Private AWS IPv4 CIDR block (from VPC created during Workspaces setup)
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
3. Reference [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) for applicable IPs and DNS entries

### AWS Configuration
1. Create an IP Group in AWS
2. Add a Rule to the IP Group
3. Add the Internet egress IP(s) used by the Twingate Connectors associated with the Remote Network

## Configuration Values
| Item | Details |
|------|---------|
| Broker Service format | `ws-broker-service.<region>.amazonaws.com` |
| IP source | Twingate Connector egress IPs for the associated Remote Network |

## Gotchas
- Must include **all** required AWS Workspaces endpoints (Auth, Broker, general endpoints) — missing any will break connectivity
- Egress IPs added to AWS IP Group must match the Connectors tied to the specific Remote Network used for Workspaces
- The VPC CIDR block must be the private IPv4 range used **at Workspaces VPC creation time**
- Workflow 1 (Twingate inside Workspace) is independent from Workflow 2 — they serve different purposes and can coexist

## Related Docs
- [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)
- Twingate MDM deployment documentation (for Workflow 1 at scale)
- Twingate Remote Networks and Connectors configuration
- Twingate Resources and Group Membership management