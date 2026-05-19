# Best Practices for Configuring Private DNS with Twingate

## Summary
Twingate recommends using private DNS for Resources instead of IP addresses or public DNS entries. The Connector handles FQDN resolution using the DNS servers configured on its host. Structuring DNS zones to match permission boundaries enables automatic Resource coverage for new hosts.

## Key Information
- Private DNS preferred over public DNS (avoids information leakage) and IP addresses (avoids overlap/ambiguity)
- IP overlap (e.g., same 10.0.1.34 on two networks) is resolved by using DNS names
- DNS zone can be mapped as a single Twingate Resource, covering all hosts underneath automatically
- Connector resolves FQDNs the same way any host on its subnet would
- Cloud options: AWS Route 53, Azure DNS (no dedicated DNS server needed)
- On-premises: deploy DNS server on internal network host

## Prerequisites
- Connector deployed and accessible on the target network
- Private DNS zone configured (cloud-managed or on-premises)
- Connector host must be able to resolve target FQDNs via its configured DNS servers

## Step-by-Step: DNS Zone-Based Resource Setup
1. Define a private DNS zone aligned to a role/permission boundary (e.g., `.engineering.yourcompany.com`)
2. Add all relevant hosts to that zone (`host1.engineering.yourcompany.com`, etc.)
3. Create a single Twingate Resource pointing to the DNS zone wildcard
4. Assign the Resource to the corresponding Twingate Group (e.g., Engineering)
5. New hosts added to the DNS zone are automatically accessible—no additional Resource config needed

## Verification
Test Connector DNS resolution by running on the Connector host:
```bash
nslookup hostX.Y.mycompany.com
```

## Configuration Values
| Option | Recommendation |
|--------|---------------|
| DNS server for Connector | Use host's configured DNS servers (default) |
| Custom DNS server on Connector | Supported but increases complexity—not recommended |
| Resource definition | Point to DNS zone (e.g., `*.engineering.yourcompany.com`) |

## Gotchas
- Custom DNS server on Connector is possible but complicates configuration—prefer inheriting host DNS settings
- Public DNS entries for private Resources expose internal topology; avoid this
- DNS zone must be resolvable from the Connector host's network position; verify with `nslookup` before troubleshooting Twingate config
- Resource must be defined at the DNS zone level (not individual hostnames) to get automatic coverage of new hosts

## Related Docs
- IP Overlap documentation
- AWS Route 53
- Azure DNS
- Twingate Connector configuration
- Twingate Groups and Resource access control