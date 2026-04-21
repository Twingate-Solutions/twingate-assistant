## Best Practices for Whitelisting Traffic to Public Resources

Describes a pattern for replacing IP-based access control to public or SaaS resources with Twingate, using Connector static public IPs as the allowlisted egress point. Eliminates per-user IP management while enabling location-independent access.

**Key Information:**
- Connectors act as the egress point: their static public IPs are allowlisted with the public service
- Only Twingate-authenticated users with Resource access can route traffic through the allowlisted Connectors
- Users can access the resource from any network or location without admin IP updates
- Access is tied to IdP-authenticated identity, not device IP

**Prerequisites:**
- Connectors deployed in a Remote Network with static public IP addresses (via NAT gateway Elastic IP, Azure Public IP, GCP static IP, etc.)
- Target public service must support source IP whitelisting or header-based access control

**Step-by-Step:**
1. Assign static public IP addresses to the NAT gateway (or equivalent) for the Remote Network
2. Allowlist those IP addresses with the public resource or SaaS application
3. In Twingate admin console, create a Resource for the public service's domain/IP, associated with that Remote Network
4. Create a Group, add the Resource and authorized users to it

**Gotchas:**
- The Connector's egress IP is the NAT gateway IP (or equivalent), not the Connector host's IP directly -- confirm the correct public IP before allowlisting
- Removing a user from the Twingate Group immediately revokes egress access without any IP list changes
- Static IP assignment is cloud-provider-specific: Elastic IP (AWS), Public IP (Azure), Static IP (GCP)

**Related Docs:**
- /docs/aws-exit-node -- Static IP setup on AWS
- /docs/remote-networks -- Remote Network configuration
- /docs/resources -- Resource configuration
- /docs/groups -- Group and access management
