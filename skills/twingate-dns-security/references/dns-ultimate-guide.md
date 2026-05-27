# The Ultimate Guide to DNS & Twingate

## Page Title
The Ultimate Guide to DNS & Twingate

## Summary
Index page linking to Twingate's DNS documentation series. Covers DNS fundamentals, private DNS server benefits, how Twingate resolves private FQDNs, running DNS queries from the client, and DNS traffic encryption.

## Key Information
- Acts as a navigation hub for all DNS-related Twingate documentation
- Five distinct topic areas, each with its own dedicated guide
- Twingate Client assigns CGNAT IP addresses to private FQDNs (not the actual private IP)
- DNS traffic encryption is available for all traffic, not just private Resources

## Documentation Map

| Topic | Use Case |
|-------|----------|
| DNS Introduction | New to DNS concepts entirely |
| DNS Best Practices Guide | Know DNS but haven't set up a private DNS server |
| DNS with Twingate (practical guide) | Understand how Twingate resolves private FQDNs |
| DNS Query Forwarding Guide | Troubleshoot by retrieving actual private IPs via `dig`/`nslookup` |
| DNS Security Guide | Encrypt all DNS traffic through Twingate |

## Key Concepts Referenced
- **CGNAT IP**: Twingate Client returns a CGNAT IP for each private FQDN matching a Resource (not the actual private IP)
- **FQDN resolution**: Twingate Client intercepts traffic and resolves private FQDNs
- **DNS forwarding**: Mechanism to retrieve actual private IP addresses for troubleshooting
- **DNS encryption**: Twingate can encrypt DNS traffic for both private Resources and general browsing

## Gotchas
- `dig` and `nslookup` against Twingate-managed FQDNs return CGNAT addresses by default, not actual private IPs — requires specific forwarding configuration for real IP lookup
- DNS encryption applies beyond just private Resources — covers all DNS traffic

## Related Docs
- Complete Introduction to DNS
- DNS Best Practices Guide
- In-depth Practical Guide on DNS with Twingate
- Guide on DNS Query Forwarding
- DNS Security Guide