# Active Directory Configuration with Twingate

## Summary
Configure Twingate to expose Active Directory domain controllers and service discovery endpoints as Resources so clients can authenticate against AD services (SMB, CIFS, LDAP, etc.) while connected. Requires adding specific DNS patterns and DC hostnames as Twingate Resources.

## Key Information
- AD authentication requires domain controllers to be reachable as Twingate Resources
- Service discovery uses DNS SRV records (`_tcp` wildcards)
- Resources should typically be assigned to the "Everyone" group or all Windows users group
- Domain joins require additional **Windows Start Before Logon** configuration

## Prerequisites
- Twingate network with at least one Connector deployed
- Access to Twingate Admin Console to create Resources
- DNS access to query AD SRV records
- AD domain name (e.g., `yourcompany.com`)

## Step-by-Step

1. **Add service discovery resource**: Create Resource with address `*_tcp*.yourcompany.com`

2. **Query domain controllers via DNS SRV**:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

3. **Add returned DC hostnames as Resources** (e.g., `zr5cdi61eltc73z.yourcompany.com`)

4. **Assign all Resources** to the Everyone group (or Windows users group)

5. **Verify** connectivity; optionally restrict to required ports per Microsoft's AD firewall guidance

## Required Resources (Final Configuration)

| Label | Address | Purpose |
|-------|---------|---------|
| AD Domain | `yourcompany.com` | AD domain root |
| Domain Controller N | `<dc-hostname>.yourcompany.com` | One entry per DC returned by SRV query |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | SRV-based service discovery |

## Gotchas
- **NetBIOS name resolution** does not work over Twingate (requires LAN broadcast); use IP or DNS name for file sharing instead
- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP; Azure Containers don't inherit VNet DNS settings automatically. Linux VM Connectors handle DNS automatically
- **Domain joins**: Must also configure Windows Start Before Logon or the machine can't reach DCs pre-login
- **Debugging**: Add `*.yourcompany.com` as a catch-all Resource and inspect Resource Activity in Admin Console to find uncaptured AD traffic

## Related Docs
- Windows Start Before Logon (required for domain join scenarios)
- Microsoft: [How to configure a firewall for Active Directory domains and trusts](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c1a23b5-9f8f-cd89-9e8c-f8e6d02a1e1a) (for port restrictions)