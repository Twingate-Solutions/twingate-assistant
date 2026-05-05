## Configuring Active Directory with Twingate

How to make Active Directory services (SMB/CIFS, LDAP, Kerberos, GPO, domain join) work cleanly when client traffic flows through Twingate.

**Concepts:**
- AD requires clients to discover and reach Domain Controllers (DCs)
- Discovery uses DNS SRV records under `_msdcs.<domain>` and `_tcp.<domain>` namespaces
- Twingate must be configured as Resources for both **DC IPs/FQDNs** and **service-discovery wildcards**

### Domain Join Considerations

If joining a Windows machine to AD over Twingate:
- Follow the **Windows Start Before Logon** documentation in addition to the steps below
- Ensures the Windows machine can connect to DCs **before** user logon (otherwise GPO / domain auth fails)
- See /docs/windows-sbl

### Setting Up DC Resources

**Step 1 -- Discover DCs**
On a machine connected to AD (or that can resolve the AD DNS), run:
- macOS / Linux: `nslookup -type=any _ldap._tcp.dc._msdcs.yourcompany.com`
- Windows: `nslookup -type=all _ldap._tcp.dc._msdcs.yourcompany.com`

Replace `yourcompany.com` with your AD domain. Output lists DC FQDNs (e.g., `zr5cdi61eltc73z.yourcompany.com`).

**Step 2 -- Add Twingate Resources**

| Resource Label | Resource Address | Purpose |
|---|---|---|
| AD Domain | `yourcompany.com` | The base AD domain |
| Domain Controller 1 | `zr5cdi61eltc73z.yourcompany.com` | First DC FQDN from nslookup |
| Domain Controller 2 | `a1ks10fndwoyhax.yourcompany.com` | Second DC FQDN (if applicable) |
| Domain Service Discovery | `*_tcp*.yourcompany.com` | SRV record discovery wildcard |

Add additional DCs as needed -- one Resource per DC.

**Step 3 -- Assign to "Everyone" Group**
- These Resources should be accessible to **all Twingate users** (or all Windows users)
- Per /docs/security-policies-best-practices, the **Everyone Group** with a no-auth + device-trust Resource Policy is the recommended pattern -- lets clients reach DCs **before** user logon

### Port Restrictions

After basic connectivity works, restrict Resource ports to AD-required ones (LDAP 389/636, SMB 445, Kerberos 88, RPC, dynamic high ports). See Microsoft's "How to configure a firewall for Active Directory domains and trusts" doc.

### Troubleshooting

**NetBIOS name resolution will not work over Twingate** -- broadcast-based, requires LAN. Use FQDNs / IPs instead. SMB file sharing still works via FQDN/IP.

**DC in Azure + Connector as Azure Container:**
- Check **Custom DNS Server** when deploying the Container -- specify a DC IP
- Ensure the container's subnet is in the same VNet as the DC (or has connectivity)
- Azure Containers do **not** inherit DNS automatically
- Linux VM Connectors generally inherit DNS correctly with no special config

**Catch-all Debugging Rule:**
- Add `*.yourcompany.com` as a Twingate Resource and test
- Any traffic that wasn't already covered by the more specific rules will show up in **Resource Activity** in the Admin Console -- gives you a list of names you may have missed

**Gotchas:**
- Don't skip the Service Discovery wildcard -- DC IPs alone fail if clients use SRV lookups (most do)
- DCs added by FQDN are preferred over IP -- DC IPs can change; FQDNs are stable
- Group Policy / SYSVOL access uses SMB to DCs -- if you restrict ports, port 445 must be open to all DCs
- Time sync (NTP, port 123) for Kerberos -- if clients drift > 5 min from DC, auth fails

**Related Docs:**
- /docs/windows-sbl -- Windows Start Before Logon (required for domain join over Twingate)
- /docs/private-dns-best-practices -- FQDN-based Resource patterns
- /docs/security-policies-best-practices -- Everyone Group + Resource Policy for AD
- /docs/network-overview -- Resource Activity for debugging
