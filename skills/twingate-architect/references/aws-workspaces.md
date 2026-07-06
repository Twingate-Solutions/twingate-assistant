# How to Use Twingate with AWS Workspaces

## Summary
Twingate supports two workflows with AWS Workspaces: installing the Twingate Client inside a Workspace to access protected resources, or using Twingate to gate access to AWS Workspaces itself. The second workflow requires configuring Twingate Resources and restricting AWS Workspaces to only allow Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Protect access to AWS Workspaces by routing traffic through Twingate and restricting AWS to Twingate egress IPs

## Prerequisites
- Twingate Remote Network configured and associated with Connectors that have internet egress IPs
- AWS Workspaces environment with a VPC
- AWS IP Group feature available in your Workspaces setup

## Step-by-Step: Protecting AWS Workspaces with Twingate

### In Twingate
1. Select the Remote Network applicable to AWS Workspaces access
2. Create Resources for the following (assign access via Group Membership):
   - Private AWS IPv4 CIDR block used during VPC creation
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
3. Reference [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) for applicable IPs and DNS entries

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a rule to the IP Group
3. Add the internet egress IP(s) used by the Twingate Connectors associated with the Remote Network

## Configuration Values
| Item | Example |
|------|---------|
| Broker Service DNS | `ws-broker-service.us-east-1.amazonaws.com` |
| VPC CIDR | Private IPv4 CIDR from Workspace VPC setup |
| Egress IP | Public IP of Twingate Connector(s) |

## Gotchas
- You must add **all** Connector egress IPs for the Remote Network to the AWS IP Group — missing one will break connectivity
- Both the VPC CIDR **and** AWS service endpoints/DNS names must be added as separate Twingate Resources
- Consult the AWS port requirements doc to get the full list of IPs/FQDNs needed — they vary by region

## Related Docs
- [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)
- Twingate MDM deployment (for Workflow 1)
- Twingate Remote Networks and Connectors
- Twingate Group Membership and Resource access control