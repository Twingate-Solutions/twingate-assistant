## NextDNS Integration

How to use **NextDNS** as Twingate's DoH resolver -- delegates DNS filtering to NextDNS while leveraging Twingate's network-level interception.

### What This Adds

- NextDNS profile-based filtering applied to all Twingate-secured device DNS
- Per-device attribution in NextDNS logs (Twingate sends device name + user first name)
- Profile selection from the Twingate Admin Console

### Platform Support

- **macOS, Windows, Linux** Client only
- Mobile Clients (iOS, Android) **NOT** supported for any Secure DNS feature, including this integration

### Setup

**Step 1: Get NextDNS API Key**

- NextDNS account page -> generate API key
- Or sign up for NextDNS first if you don't have an account

**Step 2: Connect in Twingate**

1. Twingate Admin Console -> **Settings -> Secure DNS**
2. **DNS Filtering Integrations** section -> click **Connect** next to NextDNS
3. Paste the NextDNS API key
4. Select a NextDNS profile to use as the DoH resolver
5. Confirm

After this:
- All Twingate Client DNS traffic routes through the selected NextDNS profile
- NextDNS rules apply (block lists, content categories, etc.)
- NextDNS logs show traffic per-device

### Managing the Integration

**Change profile**: Secure DNS page -> next to NextDNS under DoH Resolver -> **Change**

**Disconnect**: DNS Filtering Integrations -> NextDNS options -> **Disconnect**

### Information Shared with NextDNS

- Device name (Twingate device name)
- User's first name
- Device model

NextDNS does not see Twingate Resources / private IPs -- only public DNS lookups that the Client routes through the resolver.

### Billing

NextDNS billing is **separate** from Twingate -- managed via the NextDNS account page. Free and paid tiers available.

### Decision Notes

- Use NextDNS if you already have a NextDNS account or want their profile-based filter library
- Alternative: Twingate-native DNS Filtering (/docs/dns-filtering) -- bundled in Business/Enterprise plans
- Alternative: Cloudflare Zero Trust (/docs/doh-cloudflare) -- similar pattern with Cloudflare's filtering

### Gotchas

- NextDNS profile selection is per-Twingate-account -- if you need different filtering per Group, NextDNS profile-based delegation may be limiting; consider Twingate's native filtering (which supports per-Group profiles)
- API key is sensitive -- treat as a credential
- Disconnecting reverts users to whatever DoH resolver was selected before -- have a fallback plan (e.g., Twingate native DNS Filtering)

### Related Docs

- /docs/dns-security -- DoH overview
- /docs/dns-filtering -- Twingate-native DNS Filtering (alternative)
- /docs/doh-cloudflare -- Cloudflare integration (sibling pattern)
- /docs/internet-security -- IS overview
