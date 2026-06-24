# Private DNS Best Practices for Twingate

## Summary
Twingate recommends configuring Resources via private DNS exclusively rather than IP addresses or public DNS. The Connector handles FQDN resolution using its host's configured DNS servers. Structuring DNS zones to align with permission groups enables scalable Resource management.

## Key Information
- Private DNS preferred over public DNS (avoids information leakage) and IP addresses (avoids overlap issues, improves usability)
- DNS zones can map directly to Twingate Groups, enabling wildcard Resource coverage
- Connector resolves FQDNs using the DNS servers configured on its host machine
- Adding hosts under a DNS zone automatically makes them accessible if zone is defined as a Resource

## Prerequisites
- A private DNS zone (AWS Route 53, Azure DNS, or self-hosted DNS server for on-prem)
- Connector deployed on a host with network access to the DNS server

## Setup Pattern

### DNS Zone → Resource → Group Mapping
1. Define DNS zone aligned to a team/role (e.g., `.engineering.yourcompany.com`)
2. Add all relevant hosts under that zone (`host1.engineering.yourcompany.com`, etc.)
3. Create a single Twingate Resource pointing to the DNS zone wildcard
4. Assign that Resource to the corresponding Twingate Group (e.g., Engineering)

**Result:** New hosts added under the zone are automatically accessible to the group—no manual Resource updates needed.

## Configuration Values
| Item | Value/Command |
|------|---------------|
| DNS zone format | `*.engineering.yourcompany.com` |
| Verify Connector DNS resolution | `nslookup hostX.Y.mycompany.com` (run on Connector host) |
| Custom DNS for Connector | Supported but not recommended |

## Gotchas
- **IP overlap is a real risk**: Two Resources on separate Networks can share the same private IP (e.g., `10.0.1.34`); DNS names eliminate this ambiguity
- **Custom DNS servers on Connector** increase configuration complexity—use host's native DNS configuration instead
- **Connector resolves DNS, not the client**: Test resolution by running `nslookup` on the Connector host, not the end-user machine
- Public DNS entries for private Resources expose internal network topology unnecessarily

## Related Docs
- IP Overlap handling
- AWS Route 53 (external)
- Azure DNS (external)
- Twingate Groups and Resource assignment
- Connector deployment