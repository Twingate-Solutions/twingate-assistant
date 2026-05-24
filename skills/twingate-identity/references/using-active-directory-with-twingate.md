# Active Directory Configuration with Twingate

## Summary
Configure Twingate to expose Active Directory services (LDAP, SMB/CIFS, Kerberos) by adding domain controllers and service discovery records as Resources. Clients need access to domain controller IPs/hostnames and SRV records to authenticate via AD over Twingate.

## Key Information
- Must add multiple Resource types: AD domain, individual DCs, and wildcard service discovery
- Resources should be assigned to the "Everyone" group (or all Windows users group)
- NetBIOS name resolution does **not** work over Twingate — use IP or DNS names for file sharing
- Domain joins require additional **Windows Start Before Logon** configuration

## Prerequisites
- Twingate admin access to create Resources and Groups
- AD domain name (e.g., `yourcompany.com`)
- `nslookup` access to query SRV records
- If domain joining: Windows Start Before Logon configured separately

## Step-by-Step

1. **Discover domain controller hostnames** — run nslookup against SRV records:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

2. **Add Resources in Twingate Admin Console**:

| Label | Address | Purpose |
|---|---|---|
| AD Domain | `yourcompany.com` | Base AD domain |
| Domain Controller N | `<hostname>.yourcompany.com` | One entry per DC returned by nslookup |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | SRV-based service discovery |

3. **Assign all Resources** to the "Everyone" group or equivalent Windows users group

4. **Verify** Resources appear in client Resource lists

5. **Optionally restrict ports** per [Microsoft's firewall guidance for AD](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c7a8bcd-abb5-b6b9-0e73-75c4db0a0cba)

## Configuration Values

| Resource Address Pattern | Purpose |
|---|---|
| `yourcompany.com` | AD domain root |
| `*_tcp*.yourcompany.com` | Service discovery wildcard |
| `*.yourcompany.com` | Debug/catch-all (troubleshooting only) |

## Gotchas

- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP during deployment — Azure Containers don't inherit correct DNS automatically. Linux VM Connectors handle DNS correctly without extra config.
- **NetBIOS**: Requires LAN broadcast; not supported over Twingate. Use IP or FQDN instead.
- **Multiple DCs**: Add each DC hostname returned by nslookup as a separate Resource.
- **Wildcard `*.yourcompany.com`**: Use only for debugging (check Resource Activity in Admin Console); too broad for production.

## Related Docs
- Windows Start Before Logon (required for domain joins)
- Microsoft: How to configure a firewall for Active Directory domains and trusts