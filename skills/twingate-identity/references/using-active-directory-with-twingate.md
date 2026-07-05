# Active Directory Configuration with Twingate

## Summary
Configures Twingate to allow clients to discover and authenticate with Active Directory domain controllers. Requires adding specific DNS/IP resources to Twingate so AD services (SMB, CIFS, LDAP, etc.) function transparently over the tunnel.

## Key Information
- Domain joins over Twingate also require **Windows Start Before Logon** configuration
- Four resource types must be added to Twingate for full AD functionality
- Resources should typically be assigned to the **Everyone** group (or all-Windows-users group)
- NetBIOS name resolution does **not** work over Twingate (requires LAN broadcast); use IP or DNS name instead

## Prerequisites
- Active AD domain (e.g., `yourcompany.com`)
- Access to Twingate Admin Console
- Ability to run `nslookup` to identify domain controller addresses
- For domain joins: Windows Start Before Logon configured separately

## Step-by-Step

1. **Discover domain controllers** — Run nslookup to find DC hostnames:
   - Linux/Mac: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
   - Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

2. **Add Resources** in Twingate Admin Console:

| Resource Label | Resource Address | Purpose |
|---|---|---|
| AD Domain | `yourcompany.com` | Base AD domain |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | DC from nslookup output |
| Domain Controller N | `a1ks10fndwoyhax.yourcompany.com` | Additional DCs as returned |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | SRV record discovery |

3. **Assign all resources** to the Everyone group (or equivalent Windows users group)

4. **Verify** resources appear in client Resource lists

5. **Optionally restrict ports** per [Microsoft's AD firewall guide](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c1a55bc-dab9-d7bc-c432-6a34bd1c8f08)

## Gotchas
- **Azure Container Connectors**: Must manually set Custom DNS Server to a DC IP if Connector is deployed as Azure Container in same VNet as DC. Linux VM Connectors on Azure do not have this issue.
- **NetBIOS**: Will not work — use IP addresses or DNS names for file sharing instead
- **Variable DC count**: Number of domain controllers in nslookup output varies by domain configuration; add all returned hostnames
- **Debugging**: Add `*.yourcompany.com` as a temporary resource, then check Resource Activity in Admin Console to catch uncaptured AD traffic

## Configuration Values
- Service discovery wildcard pattern: `*_tcp*.yourcompany.com`
- nslookup query target: `_ldap._tcp.dc._msdcs.<domain>`
- LDAP port: `389` (visible in SRV records)

## Related Docs
- Windows Start Before Logon
- Microsoft: How to configure a firewall for Active Directory domains and trusts