# Active Directory Configuration with Twingate

## Summary
Configure Twingate to work with Active Directory by adding domain controllers and service discovery as Resources. This enables AD-dependent services (SMB/Samba, CIFS, LDAP) to function through Twingate without disruption.

## Key Information
- Domain joins over Twingate require additional "Windows Start Before Logon" configuration
- Clients need access to domain controller Resources for any AD authentication to work
- Assign AD Resources to the "Everyone" group (or all-Windows-users group) to simulate physical domain membership

## Prerequisites
- Twingate network with at least one Connector deployed
- Access to AD domain name (e.g., `yourcompany.com`)
- Admin access to Twingate Admin Console
- For Azure Container Connectors: manual Custom DNS Server configuration required

## Step-by-Step Configuration

**1. Discover Domain Controllers**
```bash
# Linux/Mac
nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com

# Windows
nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com
```

**2. Add Required Resources in Twingate**

| Resource Label | Resource Address | Notes |
|---|---|---|
| AD Domain | `yourcompany.com` | Base AD domain |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | From nslookup SRV records |
| Domain Controller N | `a1ks10fndwoyhax.yourcompany.com` | Add all returned DCs |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | Enables service discovery |

**3. Assign Resources**
Assign all AD Resources to the "Everyone" group or equivalent Windows-users group.

**4. Verify Connectivity**
Confirm Resources appear in client Resource lists and AD authentication works.

**5. (Optional) Restrict Ports**
Limit to required ports only — reference [Microsoft's firewall guide for AD domains](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts-7c7a8bcd-61f5-e9c3-2b8a-1e2a4e9a82ed).

## Configuration Values
- **Service discovery wildcard pattern**: `*_tcp*.yourcompany.com`
- **SRV lookup target**: `_ldap._tcp.dc._msdcs.yourcompany.com`
- **Debug wildcard resource**: `*.yourcompany.com` (broad fallback for troubleshooting)

## Gotchas
- **NetBIOS name resolution does not work** over Twingate — use IP or DNS name for file sharing instead
- **Azure Container Connectors** do not inherit DNS settings automatically; must manually set Custom DNS Server to a DC IP, and the container subnet must be in the same VNet as the DC (or Linux VM Connectors avoid this issue entirely)
- Number of domain controller Resources varies by AD configuration — add all IPs/hostnames returned by nslookup
- Domain join scenarios require "Windows Start Before Logon" setup *in addition* to these steps

## Related Docs
- [Windows Start Before Logon](https://www.twingate.com/docs/windows-start-before-logon) — required for domain joins
- [Microsoft AD Firewall Ports](https://support.microsoft.com/en-us/topic/how-to-configure-a-firewall-for-active-directory-domains-and-trusts) — port restriction reference
- Twingate Admin Console → Resource Activity — for debugging uncaptured AD traffic