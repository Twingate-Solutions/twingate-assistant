# The Ultimate Guide to DNS & Twingate

## Page Title
The Ultimate Guide to DNS & Twingate

## Summary
This page is an index/navigation guide to Twingate's DNS documentation. It organizes DNS topics by user knowledge level and use case, linking to dedicated sub-guides for each topic.

## Key Information
- Acts as a table of contents for all DNS-related Twingate documentation
- Covers five distinct DNS topics, each with its own dedicated guide
- Topics progress from foundational DNS concepts to Twingate-specific implementation details

## Sub-Guides Index

| Topic | Use Case |
|-------|----------|
| Complete Introduction to DNS | New to DNS entirely |
| DNS Best Practices Guide | Know DNS, no private DNS server yet |
| DNS with Twingate (In-depth) | How Twingate resolves private FQDNs |
| DNS Query Forwarding Guide | Running `dig`/`nslookup` for actual private IPs |
| DNS Security Guide | Encrypting DNS traffic via Twingate |

## Key Concepts Mentioned

- **CGNAT IP addresses**: Twingate Client returns a CGNAT IP (not the real private IP) for each private FQDN matching a Twingate Resource
- **FQDN resolution**: The Twingate Client intercepts traffic and resolves fully qualified domain names for private resources
- **DNS encryption**: Twingate can encrypt DNS traffic for both private Resources and general internet traffic
- **DNS query forwarding**: Mechanism to retrieve actual private IP addresses (bypassing CGNAT IPs) for troubleshooting

## Gotchas

- When using `dig` or `nslookup` from a Twingate Client, results return CGNAT IPs by default, **not** the real private IP — requires specific forwarding configuration to get actual IPs
- DNS encryption applies to all DNS traffic, not just traffic to private Resources

## Prerequisite Knowledge Path

1. No DNS knowledge → Read DNS Introduction first
2. Know DNS basics → Read DNS Best Practices
3. Know DNS, deploying Twingate → Read DNS with Twingate guide
4. Twingate deployed → Read DNS Query Forwarding for troubleshooting
5. Security focus → Read DNS Security guide

## Related Docs
- Complete Introduction to DNS
- DNS Best Practices Guide
- In-depth Practical Guide: DNS with Twingate
- Guide: How Twingate Forwards DNS Queries
- Guide: DNS Security with Twingate