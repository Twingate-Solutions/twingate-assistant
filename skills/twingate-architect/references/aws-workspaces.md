# Twingate with AWS Workspaces

## Summary
Two workflows exist for Twingate + AWS Workspaces: installing Twingate inside a Workspace to access protected resources, or using Twingate to protect access to the Workspace itself. The second workflow requires creating specific Twingate Resources and restricting AWS Workspaces to only allow Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Gate access to AWS Workspaces through Twingate tunnel + AWS IP Group restrictions

## Prerequisites
- Twingate Remote Network configured with Connectors deployed
- AWS Workspaces environment set up with a VPC
- Twingate Connector egress IP addresses (for AWS IP Group allowlist)

## Step-by-Step: Protecting AWS Workspaces with Twingate

### In Twingate
1. Select the Remote Network associated with AWS Workspaces access
2. Create Resources for:
   - Private AWS IPv4 CIDR block used during VPC creation for AWS Workspaces
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
3. Grant user access to these Resources via Group Membership

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a Rule to the IP Group
3. Add the internet egress IP(s) used by Twingate Connectors on the associated Remote Network

## Configuration Values
| Item | Example |
|------|---------|
| Broker Service DNS | `ws-broker-service.<region>.amazonaws.com` |
| VPC CIDR | Private IPv4 CIDR from Workspaces VPC setup |
| Allowed IPs in AWS | Twingate Connector egress IPs |

## Gotchas
- Must add **all** Connector egress IPs for the Remote Network to the AWS IP Group — missing one breaks connectivity
- Refer to [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) for the full list of IPs/DNS names needed as Resources
- Region-specific broker service URLs — use the correct region in the DNS name

## Related Docs
- AWS IP address and port requirements (AWS documentation)
- Twingate MDM deployment (for Workflow 1 client distribution)
- Twingate Remote Networks and Connectors configuration
- Twingate Groups and Resource access control