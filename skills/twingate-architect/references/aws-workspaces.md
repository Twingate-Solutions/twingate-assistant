# How to Use Twingate with AWS Workspaces

## Summary
Two workflows exist for Twingate + AWS Workspaces: installing Twingate inside a Workspace to access protected resources, or using Twingate to gate access to the Workspace itself. The second workflow requires creating specific Twingate Resources and restricting AWS Workspaces to Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Protect access *to* AWS Workspaces by routing traffic through Twingate tunnel and whitelisting Connector egress IPs in AWS

## Prerequisites
- Twingate Remote Network configured and associated with Connectors
- AWS Workspaces environment deployed with a VPC
- Twingate Connectors have known public egress IPs
- Access to AWS Workspaces IP Group settings

## Step-by-Step (Workflow 2: Protecting AWS Workspaces Access)

### In Twingate
1. Select the Remote Network applicable for AWS Workspaces access
2. Create Resources for:
   - Private AWS IPv4 CIDR block used during VPC creation for the Workspace
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
3. Grant access to these Resources via Group membership for applicable users

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a rule to the IP Group
3. Add the public egress IP(s) of Twingate Connectors associated with the Remote Network

## Configuration Values
| Item | Example |
|------|---------|
| Broker Service DNS | `ws-broker-service.us-east-1.amazonaws.com` |
| IP source to whitelist | Public egress IP of Twingate Connector(s) |

## Gotchas
- Must cover all required AWS Workspaces endpoints (Auth, Broker, general endpoints) — missing any will break connectivity
- Connector egress IPs must be static/known; dynamic IPs require IP Group updates when they change
- Use [AWS IP address and port requirements docs](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) to find current endpoint IPs/DNS

## Related Docs
- AWS IP address and port requirements documentation (linked in source)
- Twingate MDM deployment guides (for Workflow 1)
- Twingate Connector egress IP documentation
- Twingate Remote Networks and Groups/Resources configuration