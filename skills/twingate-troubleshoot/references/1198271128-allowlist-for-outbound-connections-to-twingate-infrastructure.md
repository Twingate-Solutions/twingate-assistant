---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-09-06
source_version: c546dc65984a72182ebf5fbf4c44ca2290241ac5bbbde2470597dcce779004c7
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Twingate Clients and Connectors require specific outbound ports and FQDNs to be allowlisted for proper operation. A Twingate-owned IP block exists but is insufficient alone—FQDNs must also be allowlisted. Static IP ranges are an Enterprise-only feature.

## Key Information
- Outbound connections only (no inbound required)
- Relay connections use ephemeral IPs within Google Cloud IP ranges
- FQDN list is subject to change at any time
- `*.twingate.com` wildcard is the recommended approach when possible
- Static IP ranges available to **Enterprise customers only**

## Required Ports

| Protocol | Port | Purpose |
|----------|------|---------|
| TCP (outbound) | `*:443` | Controller and Relay communication |
| TCP (outbound) | `*:30000-31000` | Relay fallback (when P2P unavailable) |
| UDP (outbound) | `*:*` | Peer-to-peer connectivity |

## IP Allowlist
- **Twingate IP block:** `167.254.176.0/21`
- ⚠️ **Not sufficient alone** — must combine with FQDN allowlist

## FQDN Allowlist

**Wildcard (preferred):** `*.twingate.com`

**Explicit FQDNs (if wildcards not possible):**
- `[your-network-name].twingate.com`
- `[your-network-name].[region].twingate.com` (e.g., `yournet.us1.twingate.com`)
- `admin.twingate.com`, `api.twingate.com`, `dns.twingate.com`
- `relays.twingate.com`, `relays-prm.twingate.com`
- `sst.twingate.com`, `oauth.twingate.com`, `saml.twingate.com`
- `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com`
- All regional `stun.*.twingate.com` and `stun-alt.*.twingate.com` endpoints

**Relay endpoints by provider:**
- GCP: `relays443.twingate.com`, `relays443-prm.twingate.com`
- DigitalOcean: `relays-do.twingate.com`, `relays-prm-do.twingate.com`

## Regional URLs
- Tenants resolve to region-specific domains: `[network-name].[region].twingate.com`
- Current regions: `us1`, `us2` (more planned)
- Find your region: check URL when logged into admin console
- If using `*.twingate.com` wildcard — no additional action needed

## Gotchas
- IP allowlist (`167.254.176.0/21`) **alone will not work** — FQDNs are required
- FQDN list changes without notice — wildcard approach is more resilient
- Third-party PubNub domains (`pubnubapi.com`, `pubnub.com`, `pndsn.com`) must also be allowlisted
- GCP relay IPs are ephemeral — reference [Google's maintained IP list](https://cloud.google.com/compute/docs/faq#find_ip_range) rather than hardcoding

## Related Docs
- Relay Cluster Locations
- Google Cloud external IP ranges for customers
- Twingate Connector deployment documentation