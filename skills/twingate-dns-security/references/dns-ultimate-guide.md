# The Ultimate Guide to DNS & Twingate

## Page Title
The Ultimate Guide to DNS & Twingate

## Summary
This is an index/navigation page that aggregates Twingate's DNS documentation into a single reference. It directs users to specific guides based on their DNS knowledge level and use case, covering everything from DNS basics to Twingate-specific resolution behavior and security.

## Key Information
- **Five distinct topic areas** covered via linked sub-guides:
  1. DNS fundamentals (general introduction)
  2. DNS best practices (private DNS server benefits)
  3. DNS resolution in Twingate (how FQDNs resolve through the Client)
  4. DNS query troubleshooting (`dig`/`nslookup` against actual private IPs)
  5. DNS traffic encryption/security

## Topic Map

| Question | Guide | Key Learning |
|----------|-------|--------------|
| What is DNS? | Complete intro to DNS | DNS basics, record types, internet usage |
| Should I run a private DNS server? | DNS best practices | Benefits of private DNS, UX improvements |
| How does Twingate resolve private FQDNs? | In-depth practical DNS guide | Client traffic interception, FQDN resolution flow |
| How do I get actual private IPs (not CGNAT)? | DNS query forwarding guide | Using `dig`/`nslookup` for troubleshooting |
| How is DNS traffic encrypted? | DNS security guide | Encrypting all DNS traffic including non-private resources |

## Critical Concept
The Twingate Client returns **CGNAT IP addresses** for private FQDNs matching a Resource—not the actual private IP. To retrieve the real private IP for troubleshooting, use the DNS query forwarding guide.

## Gotchas
- Running `dig` or `nslookup` directly on a machine with the Twingate Client will return CGNAT addresses, not actual Resource IPs—consult the forwarding guide to work around this
- DNS encryption covers all traffic, not just Twingate private resources

## Related Docs
- Complete Introduction to DNS
- DNS Best Practices Guide
- In-depth Practical Guide on DNS with Twingate
- DNS Query Forwarding Guide
- DNS Security Guide