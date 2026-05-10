# The Ultimate Guide to DNS & Twingate

## Page Title
The Ultimate Guide to DNS & Twingate

## Summary
This is an index/navigation page that consolidates Twingate's DNS documentation into a single reference. It links to five separate guides covering DNS fundamentals, private DNS setup, Twingate DNS resolution mechanics, DNS query troubleshooting, and DNS encryption.

## Key Information
- **Five topic areas covered:**
  1. DNS fundamentals (for users new to DNS)
  2. Private DNS server benefits and best practices
  3. How Twingate resolves private FQDNs (CGNAT IP mechanics)
  4. Running `dig`/`nslookup` queries against actual private IPs (not CGNAT IPs)
  5. DNS traffic encryption via Twingate

- Twingate Client assigns **CGNAT IP addresses** to private FQDNs matching Resources — these differ from actual private IPs
- Twingate can forward DNS queries to retrieve real private IP addresses (useful for troubleshooting)
- Twingate can encrypt **all** DNS traffic, including traffic not related to private Resources

## Prerequisites
None — page serves as an entry point for all DNS knowledge levels.

## Step-by-Step
Not applicable — this is a navigation/index page only.

## Configuration Values
None defined on this page.

## Gotchas
- When using `dig` or `nslookup` from a machine running the Twingate Client, queries return CGNAT IPs, **not** the actual private IP of the Resource — requires a specific forwarding configuration to retrieve real IPs
- DNS encryption covers all traffic only when configured; not enabled by default implicitly

## Related Docs
- Complete introduction to DNS (linked internally)
- DNS best practices guide (private DNS server setup)
- In-depth practical guide on DNS with Twingate (FQDN resolution mechanics)
- Guide on forwarding DNS queries (troubleshooting with `dig`/`nslookup`)
- Guide to DNS security (encrypting DNS traffic)