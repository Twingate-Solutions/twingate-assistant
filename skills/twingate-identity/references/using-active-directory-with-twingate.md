# Active Directory Configuration with Twingate

## Summary
Configures Twingate to support Active Directory services (SMB/CIFS, LDAP, domain joins) by exposing domain controller resources through Twingate. Requires adding specific DNS names and IPs as Twingate Resources so clients can discover and authenticate with AD.

## Key Information
- Domain joins over Twingate also require **Windows Start Before Logon** configuration
- NetBIOS name resolution does not work over Twingate (requires LAN broadcast); use IP or DNS names instead
- Resources should be assigned to the **Everyone** group (or all Windows users group)

## Prerequisites
- Active Directory domain name (e.g., `yourcompany.com`)
- Admin access to Twingate console
- `nslookup` available on a client machine

## Step-by-Step Configuration

1. **Discover domain controllers** via DNS SRV lookup:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

2. **Add four Resource types** in Twingate (assign all to Everyone group):

| Resource Label | Resource Address | Purpose |
|---|---|---|
| AD Domain | `yourcompany.com` | Base AD domain |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | DC hostname from SRV lookup |
| Domain Controller 2 | `a1ks10fndwoyhax.yourcompany.com` | DC hostname from SRV lookup |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | AD service discovery |

3. **Verify** Resources appear in client Resource lists

4. **Optionally restrict ports** per [Microsoft's firewall guide for AD](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c1a55c7-1b93-1e27-3d4a-1b620b6c5f2e)

## Gotchas
- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP during deployment; Azure Containers do not inherit correct DNS settings automatically. Linux VM Connectors handle this automatically.
- **NetBIOS**: Will not work over Twingate — use IP addresses or FQDN for file sharing instead.
- **Debugging**: If AD still fails, add `*.yourcompany.com` as a catch-all Resource and inspect Resource Activity in Admin Console to identify unmatched AD traffic.
- Number of domain controller Resources varies depending on your AD configuration.

## Related Docs
- Windows Start Before Logon (required for domain joins)
- Microsoft: How to configure a firewall for Active Directory domains and trusts