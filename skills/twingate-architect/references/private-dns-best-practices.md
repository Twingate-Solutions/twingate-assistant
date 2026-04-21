## Best Practices for Private DNS with Twingate

Private DNS is recommended (not required) for Twingate deployments. It eliminates public DNS leaks for private Resources, provides user-friendly FQDNs, and resolves IP overlap ambiguity. DNS zones aligned with Twingate Groups (e.g. `*.engineering.yourcompany.com`) enable automatic access expansion as new hosts are added under the zone.

**Key Information**
- DNS resolution is performed by the Connector, using whatever DNS servers are configured on the Connector host
- Cloud-managed DNS options: AWS Route 53, Azure DNS (no dedicated server needed)
- On-prem: deploy a DNS server on the internal network
- Zone-to-Group alignment pattern: create one DNS zone per team/role (e.g. `*.engineering.yourcompany.com`), create one Twingate Resource matching that zone, assign to the corresponding Group -- new hosts under the zone are automatically included
- Verify Connector DNS resolution: SSH into Connector host and run `nslookup hostX.Y.mycompany.com`
- Custom DNS server for Connector is possible but adds configuration complexity; recommended to use the host's default DNS servers

**Key Benefits Over IP-based Resources**
- No public DNS records needed for private Resources (avoids information leakage)
- Eliminates IP overlap ambiguity when same IP exists in multiple Remote Networks
- More human-readable and maintainable for users and admins

**Gotchas**
- If the Connector host cannot resolve the FQDN, users will get DNS failures -- verify resolution from the Connector host itself, not just from a workstation
- DNS zone-based Resources are powerful but must match the actual DNS zones used by the Connector's DNS server; wildcards like `*.engineering.yourcompany.com` require that zone to actually exist in the DNS server the Connector uses

**Related Docs**
- /docs/ip-overlap
- /docs/how-twingate-forwards-dns
- /docs/how-dns-works-with-twingate
- /docs/resources
