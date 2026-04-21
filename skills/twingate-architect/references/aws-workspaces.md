## Page Title
How to Use Twingate with AWS Workspaces

## Summary
Covers two distinct integration patterns for Twingate and AWS Workspaces: (1) installing the Twingate Client inside a Workspace to access protected resources from within it, and (2) using Twingate to gate access to the Workspace itself by restricting Workspace network access to Twingate Connector egress IPs.

## Key Information
- **Pattern 1 -- Access from inside Workspace**: Install Twingate Client inside the Workspace VM (can be deployed via MDM); standard Client deployment, no special configuration
- **Pattern 2 -- Gate access to the Workspace**: More complex; requires Resources defined for Workspace network endpoints and AWS IP Group restrictions
  - Resources to create in Twingate:
    - Private AWS VPC IPv4 CIDR block (used when Workspace VPC was created)
    - AWS Workspaces Endpoints
    - AWS Workspaces Auth Service
    - AWS Workspaces Broker Service (e.g., `ws-broker-service.us-east-1.amazonaws.com`)
  - In AWS: create IP Group, add rule allowing the internet egress IP of the Twingate Connectors associated with the Remote Network

## Prerequisites
- Twingate Remote Network set up
- AWS Workspaces environment running
- For Pattern 2: know the Connector egress public IP(s)

## Step-by-Step
**Pattern 2 (gate access to Workspace):**
1. In Twingate: create Resources for Workspace VPC CIDR, endpoints, auth service, broker service
2. In AWS: create an IP Group
3. Add a rule to the IP Group allowing the Connector egress IP(s)
4. Associate the IP Group with the Workspace directory

## Configuration Values
- Workspace Broker endpoint format: `ws-broker-service.<region>.amazonaws.com`
- See AWS IP address and port requirements documentation for full endpoint list

## Gotchas
- Pattern 2 requires knowing the Connector's public egress IP -- if using NAT, this is the NAT gateway's EIP
- The AWS Workspaces IP/port requirements doc must be consulted for the complete list of endpoints that need to be allowed

## Related Docs
- `/docs/aws` -- AWS Connector deployment
- `/docs/resources` -- Resource configuration
- `/docs/whitelisting-traffic-to-public-services` -- gating access to public services
