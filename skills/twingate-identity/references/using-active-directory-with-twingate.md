---
source: https://www.twingate.com/docs/using-active-directory-with-twingate
type: docs
fetched: 2026-08-14
source_version: dd228a12778476473b9e0fa279bf2512b65a4ab4b355c6dc609d69003473fa19
---

# Active Directory Configuration with Twingate

## Summary
Configure Twingate to support Active Directory services (SMB/Samba, CIFS, LDAP) by adding domain controllers and service discovery resources. Clients must have access to specific Resources to enable AD authentication and domain discovery.

## Key Information
- Domain joins over Twingate also require **Windows Start Before Logon** configuration
- Four Resources typically needed per AD domain
- All Resources should be assigned to the **Everyone** group (or all Windows users group)
- NetBIOS name resolution does **not** work over Twingate (broadcast-based); use IP or DNS names instead

## Prerequisites
- Twingate deployed with at least one Connector on the AD network
- Access to run `nslookup` to discover domain controller hostnames
- AD domain name (e.g., `yourcompany.com`)

## Step-by-Step

1. **Discover domain controllers** — run nslookup to find DC hostnames:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

2. **Add four Resources** in Twingate Admin Console:

| Resource Label | Resource Address | Purpose |
|---|---|---|
| AD Domain | `yourcompany.com` | Base AD domain |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | DC hostname from nslookup |
| Domain Controller 2 | `a1ks10fndwoyhax.yourcompany.com` | DC hostname from nslookup |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | SRV record discovery |

3. **Assign all Resources** to the Everyone group (or Windows users group)

4. **Verify** Resources appear in client Resource lists

5. **Optionally restrict ports** per [Microsoft's AD firewall documentation](https://support.microsoft.com/en-us/help/179442)

## Gotchas
- **Azure Container Connectors**: Must enable **Custom DNS Server** option using a DC IP during deployment; containers don't inherit VNet DNS settings automatically. Linux VM Connectors handle DNS correctly without extra config.
- **Variable DC count**: Number of domain controllers returned by nslookup varies by domain — add all returned hostnames as Resources.
- **Debugging**: Add `*.yourcompany.com` as a wildcard Resource temporarily; uncaptured AD traffic appears in Resource Activity in Admin Console.
- **Port restrictions**: Only apply after verifying full connectivity first.

## Related Docs
- Windows Start Before Logon (required for domain joins)
- Microsoft: [How to configure a firewall for Active Directory domains and trusts](https://support.microsoft.com/en-us/help/179442)