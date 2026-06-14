# How to Use Twingate with AWS Workspaces

## Summary
Two workflows exist for Twingate with AWS Workspaces: installing Twingate inside a Workspace to access protected resources, or using Twingate to protect access to the Workspace itself. The second workflow requires configuring Twingate Resources and restricting AWS Workspaces to only allow Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Gate access to AWS Workspaces through Twingate by combining Resource configuration + AWS IP Group restrictions

## Prerequisites
- Twingate Remote Network configured with Connectors deployed
- AWS Workspaces environment already set up with a VPC
- Twingate Connector egress IP addresses (for AWS IP Group rules)

## Step-by-Step: Protecting AWS Workspaces Access (Workflow 2)

### In Twingate
1. Select the applicable Remote Network for AWS Workspaces access
2. Create Resources for:
   - Private AWS IPv4 CIDR block used during VPC creation for AWS Workspaces
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
3. Grant access to these Resources via Group Membership

### In AWS
1. Create an IP Group in AWS Workspaces
2. Add a rule to the IP Group
3. Add the internet egress IP address(es) used by the Twingate Connectors associated with the Remote Network

## Configuration Values
| Item | Value/Notes |
|------|-------------|
| Broker Service DNS pattern | `ws-broker-service.<region>.amazonaws.com` |
| VPC CIDR | Private IPv4 CIDR from Workspaces VPC setup |
| Egress IPs | Twingate Connector outbound IPs for the Remote Network |

## Gotchas
- IP and DNS requirements vary by AWS region — consult [AWS IP address and port requirements documentation](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) for exact values
- Must include **all** required endpoints (Auth, Broker, general Workspaces endpoints) or connectivity will fail
- The egress IP added to the AWS IP Group must be the **Connector's internet-facing IP**, not the internal IP

## Related Docs
- AWS IP address and port requirements (external AWS documentation)
- Twingate MDM deployment (for Workflow 1 Client deployment)
- Twingate Remote Networks and Connectors configuration
- Twingate Group Membership and Resource access control