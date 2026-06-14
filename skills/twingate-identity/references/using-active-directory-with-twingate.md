# Active Directory Configuration with Twingate

## Summary
Configures Twingate to support Active Directory services (SMB/CIFS, LDAP, domain joins) by exposing domain controller resources. Requires adding specific DNS patterns and domain controller addresses as Twingate Resources so clients can discover and authenticate against AD.

## Key Information
- Four Resources needed for full AD support (see table below)
- All AD Resources should be assigned to the **Everyone** group (or all Windows users group)
- NetBIOS name resolution does NOT work over Twingate — use IP or DNS names instead
- For domain joins, also configure **Windows Start Before Logon**

## Prerequisites
- Twingate admin access
- AD domain name (e.g., `yourcompany.com`)
- DNS SRV lookup capability to identify domain controller hostnames

## Step-by-Step

1. **Discover domain controllers** — run nslookup to find DC hostnames:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

2. **Add four Resources** in Twingate Admin Console:

| Label | Resource Address | Purpose |
|-------|-----------------|---------|
| AD Domain | `yourcompany.com` | AD domain root |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | DC hostname from SRV lookup |
| Domain Controller 2 | `a1ks10fndwoyhax.yourcompany.com` | DC hostname from SRV lookup |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | AD service discovery |

3. **Assign all Resources** to the Everyone group
4. **Verify** Resources appear in client Resource lists
5. **Optionally restrict ports** per [Microsoft AD firewall requirements](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c7a8bcd-bf73-c2d8-3fc6-f24b8f1d4ec4)

## Configuration Values
- Service discovery wildcard pattern: `*_tcp*.yourcompany.com`
- Debug wildcard (if AD still fails): `*.yourcompany.com` — then check Resource Activity in Admin Console

## Gotchas
- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP; Azure Containers don't inherit VNet DNS settings automatically. Linux VM Connectors configure DNS correctly by default.
- **NetBIOS**: Requires LAN broadcast — not supported over Twingate. Use IP/DNS instead.
- **Domain joins**: Require Windows Start Before Logon configuration in addition to these steps.
- Number of domain controllers (Resources) varies by domain — check SRV query output for all returned hostnames.

## Related Docs
- Windows Start Before Logon
- Microsoft: How to configure a firewall for Active Directory domains and trusts
- Resource Activity (Admin Console) — for debugging AD traffic