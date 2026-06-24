# Active Directory Configuration with Twingate

## Summary
Configure Twingate to expose Active Directory domain controllers and service discovery endpoints as Resources. Clients must have access to specific DNS names and IPs to authenticate against AD services (LDAP, SMB/CIFS, Kerberos, etc.).

## Key Information
- Four Resource types are required for full AD functionality
- Resources should be assigned to the "Everyone" group (or all Windows users group)
- Domain joins require additional "Windows Start Before Logon" configuration
- NetBIOS name resolution does not work over Twingate (broadcast-dependent)

## Prerequisites
- AD domain name (e.g., `yourcompany.com`)
- Access to run `nslookup` to discover domain controller hostnames/IPs
- Twingate Admin Console access to create Resources

## Step-by-Step Configuration

1. **Discover domain controllers** via DNS SRV lookup:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`
   - Note returned hostnames (e.g., `zr5cdi61eltc73z.yourcompany.com`)

2. **Add four Resources** in Twingate Admin Console:

| Resource Label | Resource Address | Purpose |
|---|---|---|
| AD Domain | `yourcompany.com` | Base AD domain |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | DC hostname from nslookup |
| Domain Controller 2 | `a1ks10fndwoyhax.yourcompany.com` | Additional DC (varies) |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | AD service discovery |

3. **Assign all Resources** to the "Everyone" group or equivalent Windows users group

4. **Verify** Resources appear in client Resource lists

## Gotchas
- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP; Azure Containers don't inherit VNet DNS settings automatically. Linux VM Connectors don't have this issue.
- **NetBIOS**: Won't work over Twingate—use IP or DNS name for Windows file sharing instead
- **Domain joins**: Require "Windows Start Before Logon" setup in addition to these steps
- **Port restriction**: After verifying connectivity, optionally restrict to required ports per [Microsoft's AD firewall guidance](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c7a8bca-bf36-e06b-e1c0-b40e14f0437b)
- **Debugging**: Add `*.yourcompany.com` as a temporary Resource to capture all AD traffic; check Resource Activity in Admin Console

## Related Docs
- Windows Start Before Logon
- Microsoft: How to configure a firewall for Active Directory domains and trusts