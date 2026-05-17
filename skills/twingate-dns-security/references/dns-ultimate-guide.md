# The Ultimate Guide to DNS & Twingate

## Page Title
The Ultimate Guide to DNS & Twingate

## Summary
This is an index/navigation page that consolidates Twingate's DNS documentation into categorized links. It routes users to specific guides based on their DNS knowledge level and use case, covering DNS basics, private DNS setup, FQDN resolution, query troubleshooting, and DNS encryption.

## Key Information
- Acts as a table of contents for all DNS-related Twingate documentation
- Five distinct topic areas, each with a dedicated guide
- Twingate Client assigns CGNAT IP addresses to private FQDNs (not the actual private IP)
- `dig`/`nslookup` queries require a specific forwarding approach to retrieve actual private IPs
- Twingate can encrypt DNS traffic for both private Resources and general internet traffic

## Topic Map

| User Need | Guide |
|-----------|-------|
| New to DNS entirely | Complete introduction to DNS |
| Know DNS, no private DNS server | DNS best practices guide |
| How Twingate resolves private FQDNs | In-depth practical guide on DNS with Twingate |
| Troubleshooting with `dig`/`nslookup` | Guide on DNS query forwarding |
| DNS traffic encryption | Guide to DNS security |

## Key Concepts Referenced
- **CGNAT IP**: Twingate Client returns a CGNAT address for matched private FQDNs, not the actual Resource IP
- **Private FQDN resolution**: Twingate Client intercepts traffic and handles FQDN-to-IP resolution
- **DNS forwarding**: Required to retrieve actual private IP addresses during troubleshooting
- **DNS encryption**: Twingate can protect unencrypted DNS traffic for all queries

## Gotchas
- Running `dig` or `nslookup` against a Twingate Resource FQDN will return the CGNAT IP, not the actual private IP — requires DNS query forwarding configuration to get real IPs
- Users new to Twingate DNS commonly misunderstand the CGNAT address behavior

## Prerequisites
None — page is an entry point for all DNS knowledge levels

## Related Docs
- Complete introduction to DNS
- DNS best practices guide
- In-depth practical guide on DNS with Twingate
- Guide on DNS query forwarding
- Guide to DNS security