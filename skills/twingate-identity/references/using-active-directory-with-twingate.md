# Active Directory Configuration with Twingate

## Summary
Configures Twingate to support Active Directory services (SMB/CIFS, LDAP, domain joins) by exposing domain controllers and service discovery endpoints as Twingate Resources. Requires adding specific DNS names and IPs as Resources so clients can authenticate against AD infrastructure.

## Key Information
- All AD-dependent clients must have access to domain controller Resources
- Four Resource types are required for full AD functionality
- Resources should be assigned to the "Everyone" group (or all Windows users group)
- For domain joins over Twingate, also configure **Windows Start Before Logon**

## Prerequisites
- Active AD domain (e.g., `yourcompany.com`)
- Admin access to Twingate console
- Ability to run `nslookup` to identify domain controller hostnames/IPs

## Step-by-Step Configuration

1. **Discover domain controllers** — run nslookup to find DC hostnames:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

2. **Add four Resources** in Twingate admin console:

| Label | Resource Address | Purpose |
|-------|-----------------|---------|
| AD Domain | `yourcompany.com` | AD domain |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | DC hostname from nslookup |
| Domain Controller 2 | `a1ks10fndwoyhax.yourcompany.com` | Additional DC |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | SRV record discovery |

3. **Assign all Resources** to the "Everyone" group or equivalent Windows users group.

4. **Verify** Resources appear in client Resource lists.

5. **Optionally restrict ports** per [Microsoft's AD firewall guidance](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7e1db5dc-0cbf-5a06-b13a-4cfea5a9badb).

## Gotchas
- **NetBIOS name resolution** does not work over Twingate (requires LAN broadcast). Use IP or DNS names for file sharing instead.
- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP during deployment. Azure Containers don't inherit correct DNS settings automatically. Linux VM Connectors do not have this issue.
- **Debugging**: Add `*.yourcompany.com` as a wildcard Resource temporarily; uncaptured AD traffic will appear in Resource Activity logs in Admin Console.
- Number of domain controllers varies by domain — repeat nslookup step to find all DCs.

## Related Docs
- Windows Start Before Logon (required for domain joins)
- Microsoft: How to configure a firewall for Active Directory domains and trusts