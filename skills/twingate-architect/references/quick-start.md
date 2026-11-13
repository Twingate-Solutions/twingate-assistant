---
source: https://www.twingate.com/docs/quick-start
type: docs
fetched: 2026-11-13
source_version: 12283b46c885bcef5b858151d3ec89cea831b77e15aa0f350166704f0cfc407a
trust: official
---

# Quick Start

## Summary
Walks through the minimum setup for a Twingate network: create a Remote Network, define a Resource, deploy a Connector, and connect with the Twingate Client. After completion, authorized users can reach private Resources from any network.

## Key Information
- Three phases: define Remote Network (with Resources), deploy and provision a Connector, install the Client.
- Connectors provide encrypted connectivity into a Remote Network and are deployed behind your firewall.
- A Resource is only accessible once it is added to at least one Group. The default option is "Everyone"; create a custom Group to limit access.
- The Connector host must be able to reach the Resources you want to expose.
- The "Connection Status" sidebar updates automatically once the Connector connects to both the Twingate Controller and Relay. At that point the Connector is ready to serve requests.
- Peer-to-peer connections improve user experience and help stay within the Fair Use Policy for bandwidth.

## Prerequisites
- A Twingate account (a free account is available).
- Permissions to deploy a Docker container or native Linux service on the Remote Network being configured.

## Step-by-Step
1. **Create a Remote Network** (skip if one already exists from signup):
   - Network → Remote Networks → Add.
   - Select a location (e.g., AWS).
   - Name it (e.g., "AWS Production VPC") → Add Remote Network.
2. **Define a Resource**:
   - Network → Add Resource.
   - Enter Resource details → Add Resource.
   - Select the Group(s) to authorize (e.g., Everyone) → "Add 1 Group".
3. **Deploy a Connector**:
   - Open the new Remote Network, then click an existing Connector or "Deploy Connector".
   - Choose a deployment option for your environment. The displayed steps change per option.
   - Run the deployment on the remote host and watch the Connection Status sidebar.
4. **Install the Client**:
   - Install from get.twingate.com, authenticate, and access the Resource.

## Configuration Values
No environment variables, CLI flags, or API parameters are given on this page. Connector deployment values are generated in the Admin Console for the option you choose.

## Gotchas
- Not adding a Resource to a Group makes it inaccessible to users.
- Only the "Everyone" Group is available until you create custom Groups.
- A Connector on a host that cannot reach the target Resources will not work for them.
- Peer-to-peer support needs separate setup (see the peer-to-peer connections doc).

## Related Docs
- Resource Definition (allowed address formats)
- Deploying Connectors
- Supporting peer-to-peer connections
- Fair Use Policy
- Twingate Client installation (get.twingate.com)
- Next steps: managing your team, Security Policies, Services (CI/CD automation), Use Cases