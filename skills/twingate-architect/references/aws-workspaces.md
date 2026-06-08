# Twingate with AWS Workspaces

## Summary
Two workflows exist for Twingate + AWS Workspaces: installing Twingate *inside* a Workspace to access protected resources, or using Twingate to *protect access to* AWS Workspaces. The second workflow requires creating specific Twingate Resources and restricting AWS Workspaces to Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Route AWS Workspaces traffic through Twingate tunnel and lock down access to Twingate egress IPs only

## Prerequisites
- Twingate Remote Network configured with Connectors deployed
- AWS Workspaces environment with VPC
- Twingate Connector egress IP addresses (for AWS IP Group configuration)

## Step-by-Step: Protecting AWS Workspaces with Twingate

### In Twingate
1. Select the Remote Network associated with your AWS Workspaces environment
2. Create Resources for the following (assign access via Group Membership):
   - Private AWS IPv4 CIDR block used when the VPC was created
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a rule to the IP Group
3. Add the Twingate Connector egress IP address(es) for the associated Remote Network

## Configuration Values
| Resource Type | Example |
|---|---|
| Broker Service DNS | `ws-broker-service.us-east-1.amazonaws.com` |
| VPC CIDR | Private IPv4 CIDR from VPC creation |

## Gotchas
- You must add **all** Twingate Connector egress IPs for the Remote Network to the AWS IP Group — missing one will break connectivity
- Refer to [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) for the full list of IPs/DNS entries needed as Twingate Resources
- Broker Service endpoint is region-specific — adjust region slug accordingly

## Related Docs
- [Twingate MDM deployment](https://www.twingate.com/docs/mdm)
- [Creating Resources in Twingate](https://www.twingate.com/docs/resources)
- [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)