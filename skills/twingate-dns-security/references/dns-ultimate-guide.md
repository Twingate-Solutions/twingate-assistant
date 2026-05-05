## The Ultimate Guide to DNS & Twingate

Index doc for DNS-related Twingate questions. Use this as a navigation hub for the deeper guides linked below.

### Common DNS Questions Answered Elsewhere

| Question | Where to Look |
|---|---|
| What exactly is DNS? | /docs/introduction-to-dns -- general DNS primer |
| I don't run a DNS server -- should I? | /docs/private-dns-best-practices -- benefits of private DNS |
| How does Twingate resolve private FQDNs? | /docs/how-twingate-forwards-dns or /docs/how-dns-works-with-twingate -- mechanics |
| How do I run `dig` / `nslookup` against private IPs through Twingate? | /docs/how-twingate-forwards-dns -- forwarding queries to retrieve real IPs |
| How does Twingate encrypt DNS traffic? | /docs/dns-security -- DoH and DNS encryption |

### Key Concepts to Understand

**CGNAT IPs in the Twingate Client:**
- The Client returns a Carrier-Grade NAT (CGNAT) IP for each private FQDN that maps to a Twingate Resource
- This is **not** the actual private IP -- it's a synthetic IP the Client uses for its own routing
- For troubleshooting (when you actually need the real IP): see /docs/how-twingate-forwards-dns

**DNS Encryption:**
- Twingate can encrypt all outbound DNS via DoH -- not just queries to private Resources
- Configurable per device or fleet-wide
- See /docs/dns-security and /docs/internet-security

**Private DNS Servers:**
- Optional but improves UX -- lets you use friendly hostnames (`prod-db.internal`) rather than IPs in Resource definitions
- See /docs/private-dns-best-practices for setup patterns

### Decision Notes

- Most teams **don't need** to run a private DNS server -- IP-based Resources work fine for small deployments
- Once you have more than ~10 Resources or your team rotates IPs, **set up a private DNS server** -- the management cost goes way down
- For DNS filtering / encryption: pair Twingate with NextDNS, Cloudflare DoH, or DNS Security profile (see /docs/dns-filtering, /docs/doh-cloudflare)

### Related Docs

- /docs/how-dns-works-with-twingate, /docs/how-twingate-forwards-dns -- Mechanics
- /docs/private-dns-best-practices -- Private DNS setup
- /docs/dns-security -- DNS encryption (DoH)
- /docs/dns-filtering, /docs/doh-cloudflare, /docs/nextdns-configuration -- DNS filtering integrations
- /docs/dns-failures -- DNS troubleshooting
