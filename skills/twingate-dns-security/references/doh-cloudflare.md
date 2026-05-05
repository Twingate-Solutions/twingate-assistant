## Cloudflare DoH + DNS Filtering with Twingate

How to point Twingate's DoH at a Cloudflare Zero Trust Gateway DNS Location, enabling Cloudflare's DNS filtering policies for DNS traffic flowing through Twingate.

### Prerequisites

- Cloudflare **Zero Trust** account (a trial account works)
- Twingate tenant with DoH support

### Setup

**Step 1: Add a DNS Location in Cloudflare**

- Cloudflare Zero Trust dashboard -> **Gateway -> DNS Locations**
- Add a new DNS location
- Save and close

**Step 2: Retrieve the DoH URL**

- Open the newly created DNS location
- Copy the **DNS over HTTPS** URL (the custom DoH endpoint Cloudflare assigns to your location)

**Step 3 (Optional): Set Up DNS Filtering Rules**

- **Gateway -> Policies**
- Create policies for content blocking, security filters, etc.
- These policies apply to all traffic flowing through this DNS Location

**Step 4: Configure Twingate with the Cloudflare DoH URL**

- Twingate Admin Console
- Add the Cloudflare custom DoH URL as a custom DoH provider
- See /docs/dns-security for the Custom DoH resolver configuration steps

### Result

When users connect to Twingate, their DNS traffic flows:
- Twingate Client -> Cloudflare DoH endpoint -> Cloudflare Gateway -> filter decision -> resolution

Cloudflare's filter decisions apply (block, allow, log) before the DNS response returns.

### Decision Notes

- Use this pattern when you want **DNS-layer security policies** without standing up your own filter infrastructure
- Cloudflare's free tier covers basic filtering; advanced features (custom rules, identity-based policies) require paid Zero Trust plans
- For NextDNS-based filtering: see /docs/nextdns-configuration (similar pattern)
- For Twingate-native DNS filtering on Business/Enterprise plans: see /docs/dns-filtering

### Gotchas

- DoH URLs are **per DNS Location** in Cloudflare -- if you have multiple locations, each has its own URL; pick one for Twingate or use Cloudflare's network-detection feature
- DNS-only filtering doesn't catch direct-IP traffic -- combine with HTTPS inspection or block at firewall layer for full coverage
- The Cloudflare Zero Trust trial is time-limited -- plan paid subscription before relying on this in production

### Related Docs

- /docs/dns-security -- Twingate Custom DoH resolver setup
- /docs/dns-filtering -- Twingate-native DNS filtering
- /docs/nextdns-configuration -- NextDNS sibling pattern
- /docs/internet-security -- Internet Security overview (DoH context)
- /docs/internet-security-client-configuration -- Client-side DoH config
