# Twingate with AWS Workspaces

## Summary
Two workflows exist for Twingate + AWS Workspaces: installing Twingate inside a Workspace to access protected resources, or using Twingate to gate access to the Workspace itself. The second workflow requires creating specific Twingate Resources and restricting AWS Workspaces to Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Protect access *to* AWS Workspaces by routing traffic through Twingate tunnel and allowlisting Connector egress IPs in AWS

## Prerequisites
- Twingate Remote Network configured and associated with Connectors that have known egress IPs
- AWS Workspaces environment with VPC
- Access to AWS IP Group settings in the Workspaces console

## Step-by-Step (Workflow 2: Protecting AWS Workspaces Access)

### In Twingate
1. Select the Remote Network applicable for AWS Workspaces access
2. Create Resources for the following (assign access via Group membership):
   - Private AWS IPv4 CIDR block used when the VPC was created for Workspaces
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a rule to the IP Group
3. Add the internet egress IP(s) used by Twingate Connectors on that Remote Network

## Configuration Values
| Item | Example |
|------|---------|
| Broker Service DNS | `ws-broker-service.us-east-1.amazonaws.com` |
| VPC CIDR | Private IPv4 CIDR from Workspaces VPC setup |
| Egress IPs | Connector internet egress IPs for the Remote Network |

## Gotchas
- Egress IPs must be the **internet-facing** IPs of the Twingate Connectors, not internal/private IPs
- Multiple AWS Workspaces endpoints exist (Auth, Broker, general endpoints) — all must be added as Resources or connections will fail
- Consult [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) to get current IP ranges and DNS names — these can change

## Related Docs
- AWS IP address and port requirements (AWS documentation)
- Twingate MDM deployment (for Workflow 1 Client distribution)
- Twingate Remote Networks and Connectors configuration
- Twingate Groups and Resource access control