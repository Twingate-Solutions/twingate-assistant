# The Ultimate Guide to DNS & Twingate

## Page Title
The Ultimate Guide to DNS & Twingate

## Summary
This is a navigation/index page that consolidates Twingate's DNS documentation into a single reference hub. It links to five separate guides covering DNS fundamentals, private DNS benefits, Twingate DNS resolution mechanics, DNS query troubleshooting, and DNS traffic encryption.

## Key Information

- **Five topic areas covered:**
  1. **DNS fundamentals** → "Complete introduction to DNS" (for users new to DNS)
  2. **Private DNS benefits** → "DNS best practices guide" (for users without a private DNS server)
  3. **Twingate FQDN resolution** → "In-depth practical guide on DNS with Twingate" (how Client intercepts traffic and resolves private FQDNs)
  4. **DNS query troubleshooting** → "Guide on DNS query forwarding" (running `dig`/`nslookup` to get actual private IPs)
  5. **DNS encryption** → "Guide to DNS security" (encrypting all DNS traffic)

## Critical Concepts Referenced

- Twingate Client returns a **CGNAT IP address** for each private FQDN matching a Twingate Resource — this is *not* the actual private IP
- To retrieve the **actual private IP** of a Resource (not the CGNAT address), use the DNS query forwarding guide
- Tools for troubleshooting DNS resolution: `dig`, `nslookup`

## Gotchas

- Users running `dig` or `nslookup` against a Resource FQDN via the Twingate Client will receive a CGNAT IP, not the real private IP — consult the forwarding guide to get actual addresses
- DNS traffic encryption applies to both private Resource DNS and general DNS traffic

## Related Docs

- Complete Introduction to DNS
- DNS Best Practices Guide
- In-Depth Practical Guide on DNS with Twingate
- Guide on DNS Query Forwarding
- Guide to DNS Security (DNS encryption)