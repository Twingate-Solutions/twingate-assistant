# How to Use Twingate with AWS Workspaces

## Summary
Two workflows exist for Twingate + AWS Workspaces: running Twingate inside a Workspace to access protected resources, or using Twingate to gate access to the Workspace itself. The second workflow requires creating specific Twingate Resources and restricting AWS Workspaces to only allow Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (optionally via MDM); no special configuration needed beyond standard deployment
- **Workflow 2**: Protect access *to* AWS Workspaces by routing Workspace traffic through Twingate tunnel and locking down AWS to Twingate egress IPs only

## Prerequisites
- Existing AWS Workspaces environment with a VPC
- Twingate Remote Network configured for the AWS environment
- Twingate Connectors deployed in that Remote Network
- Knowledge of Twingate Connector egress IP addresses

## Step-by-Step: Protecting AWS Workspaces with Twingate

### In Twingate
1. Select the Remote Network associated with AWS Workspaces access
2. Create Resources for the following (assign to Groups for user access):
   - Private AWS IPv4 CIDR block used when VPC was created for AWS Workspaces
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a Rule to the IP Group
3. Add the internet egress IP(s) used by Twingate Connectors associated with the Remote Network

## Configuration Values
| Item | Example |
|------|---------|
| Broker Service DNS | `ws-broker-service.<region>.amazonaws.com` |
| IP source to allowlist | Twingate Connector egress IP(s) |

## Gotchas
- Must allowlist **all** required AWS Workspaces endpoints (Auth, Broker, general endpoints) — missing any will break connectivity
- Use [AWS IP address and port requirements documentation](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) to find current IPs/DNS for all required services
- Egress IP to use is the **Connector's internet-facing IP**, not an internal IP

## Related Docs
- AWS IP address and port requirements (AWS documentation)
- Twingate MDM deployment (for Workflow 1 client deployment)
- Twingate Remote Networks and Connectors setup
- Twingate Groups and Resource access control