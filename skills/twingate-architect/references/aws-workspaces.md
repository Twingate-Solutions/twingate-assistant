# How to Use Twingate with AWS Workspaces

## Summary
Twingate integrates with AWS Workspaces in two ways: installing Twingate inside a Workspace to access protected resources, or using Twingate to gate access to the Workspace itself. The second workflow requires configuring Twingate Resources and restricting AWS Workspaces to only accept connections from Twingate egress IPs.

## Key Information
- **Workflow 1**: Install Twingate Client inside the Workspace (standard install, optionally via MDM)
- **Workflow 2**: Protect access to AWS Workspaces by routing Workspace traffic through Twingate tunnel and locking down AWS to Twingate egress IPs

## Prerequisites
- Twingate Remote Network configured and associated with Connectors
- AWS Workspaces environment set up with a VPC
- Know the egress IP addresses of Twingate Connectors in the relevant Remote Network

## Step-by-Step (Workflow 2: Protecting AWS Workspaces Access)

### Twingate Configuration
1. Select the Remote Network that will provide access to AWS Workspaces
2. Create Twingate Resources for the following (assign access via Group Membership):
   - Private AWS IPv4 CIDR block used during VPC creation for AWS Workspaces
   - AWS Workspaces Endpoints
   - AWS Workspaces Auth Service
   - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
3. Reference [AWS IP address and port requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html) to identify applicable IPs and DNS names

### AWS Configuration
1. Create an IP Group in AWS Workspaces
2. Add a rule to the IP Group
3. Add the Twingate Connector egress IP address(es) for the associated Remote Network

## Configuration Values

| Item | Value/Notes |
|------|-------------|
| VPC CIDR | Private IPv4 CIDR from AWS Workspaces VPC setup |
| Broker Service DNS | `ws-broker-service.<region>.amazonaws.com` |
| Allowed IPs in AWS | Twingate Connector internet egress IPs |

## Gotchas
- You must add **all** required AWS Workspaces service endpoints as Twingate Resources — missing one (Auth, Broker, Endpoints) will break connectivity
- The egress IP to allowlist in AWS is the **Connector's internet egress IP**, not the client's IP
- Use AWS's official IP/port requirements doc to stay current — endpoints may vary by region

## Related Docs
- [AWS IP address and port requirements for Workspaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)
- Twingate Remote Networks configuration
- Twingate Resources and Group Membership
- Deploying Twingate Client via MDM