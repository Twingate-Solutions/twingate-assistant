# Active Directory Configuration with Twingate

## Summary
Configure Twingate to expose Active Directory domain controller resources so clients can use AD-dependent services (SMB, CIFS, LDAP, etc.) over Twingate. Requires adding specific DNS patterns and domain controller hostnames/IPs as Twingate Resources.

## Key Information
- All AD-dependent clients must have access to domain controller Resources in Twingate
- Four resource types needed: AD domain, individual DCs, and service discovery wildcard
- Assign these Resources to the "Everyone" group (or all Windows users group)
- Domain joins require additional **Windows Start Before Logon** configuration

## Prerequisites
- Twingate admin access to create Resources and Groups
- Knowledge of your AD domain name (e.g., `yourcompany.com`)
- Network access to run `nslookup` against your AD domain

## Step-by-Step

1. **Discover domain controllers** — Run nslookup to find DC hostnames:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

2. **Add Resources** in Twingate Admin Console:

| Resource Label | Resource Address |
|---|---|
| AD Domain | `yourcompany.com` |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` (from nslookup) |
| Domain Controller 2 | `a1ks10fndwoyhax.yourcompany.com` (from nslookup) |
| Domain Service Discovery | `*_tcp*.yourcompany.com` |

3. **Assign** all Resources to the "Everyone" group or equivalent Windows users group

4. **Verify** Resources appear in client Resource lists

5. **Optionally restrict ports** — See [Microsoft's firewall guide for AD](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c1a49bc-ad6e-3b4c-0ba1-9e8a2da5f029)

## Gotchas
- **NetBIOS name resolution** does not work over Twingate — use IP or DNS name for file sharing instead
- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP; Azure Containers don't inherit VNet DNS settings automatically. Linux VM Connectors don't have this issue.
- **Domain joins**: Require Windows Start Before Logon setup in addition to these steps
- **Debugging**: Add `*.yourcompany.com` as a temporary Resource to capture uncategorized AD traffic; inspect via Resource Activity in Admin Console

## Related Docs
- Windows Start Before Logon
- Microsoft: How to configure a firewall for Active Directory domains and trusts