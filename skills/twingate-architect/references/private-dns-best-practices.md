# Private DNS Best Practices with Twingate

## Page Title
Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS exclusively for Resources rather than IP addresses or public DNS entries. DNS zones can be mapped to Twingate Resources and Groups to enable automatic access for new hosts added to a zone. The Connector handles FQDN resolution using its host's configured DNS servers.

## Key Information
- Private DNS preferred over public DNS (security) and IP addresses (usability, overlap issues)
- DNS zone-based Resources automatically include new hosts added to that zone—no manual Resource updates needed
- Connector resolves FQDNs the same way any host on the same subnet would
- Managed DNS services (AWS Route 53, Azure DNS) eliminate need for dedicated DNS server deployment

## Prerequisites
- A private DNS zone configured (cloud-managed or on-premises DNS server)
- Connector deployed on host with access to the internal network's DNS servers

## Setup Pattern (DNS Zone → Resource → Group)

1. Define a DNS zone (e.g., `.engineering.yourcompany.com`)
2. Place all relevant hosts as records under that zone (e.g., `host1.engineering.yourcompany.com`)
3. Create a single Twingate Resource pointing to the DNS zone wildcard
4. Map that Resource to the appropriate Twingate Group (e.g., Engineering group)

**Result:** Any new host added under `.engineering.yourcompany.com` is automatically accessible to the Engineering group without additional Resource configuration.

## Configuration Values
| Item | Value/Example |
|------|---------------|
| DNS zone format | `.engineering.yourcompany.com` |
| Resource definition | Wildcard DNS zone (e.g., `*.engineering.yourcompany.com`) |
| Custom DNS server | Optional on Connector (not recommended) |

## Verification Command
Test Connector DNS resolution by logging into the Connector host:
```bash
nslookup hostX.Y.mycompany.com
```

## Gotchas
- **IP overlap is real:** The same private IP (e.g., `10.0.1.34`) can exist across multiple Networks—DNS names resolve this ambiguity
- **Public DNS for private Resources is a security risk:** Avoid exposing internal hostnames publicly
- **Custom DNS on Connector adds complexity:** Use the Connector host's existing DNS configuration instead
- **Connector placement matters:** Connector must be on a subnet where it can resolve the private DNS zone; verify with `nslookup` before assuming it works
- **DNS zone design is hard to change later:** Plan zone structure to align with permission/role boundaries upfront

## Related Docs
- IP Overlap handling
- AWS Route 53 integration
- Azure DNS integration
- Twingate Resources configuration
- Twingate Groups configuration
- Connector deployment