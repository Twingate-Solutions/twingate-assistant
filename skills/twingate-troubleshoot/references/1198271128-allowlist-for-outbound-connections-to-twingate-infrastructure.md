---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-09-20
source_version: 4b2c3ee3d9de31b2d4a32d482d0b8a636bc3a8c834cb9c79c1b66c02289de059
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Twingate Clients and Connectors require specific outbound ports and FQDNs to communicate with Twingate's Controller and Relay infrastructure. A Twingate-owned IP block exists but is insufficient alone—FQDNs must also be allowlisted. Wildcard `*.twingate.com` is the simplest approach when supported.

## Key Information
- **Components affected**: Twingate Client and Connector
- **IP block**: `167.254.176.0/21` (Twingate-owned; Enterprise customers only for static IPs)
- **IP-only allowlisting is NOT sufficient**—FQDNs required alongside IPs
- Relay connections use ephemeral IPs within Google Cloud IP ranges
- FQDN list is subject to change at any time
- Regional URLs follow pattern: `[network-name].[region].twingate.com` (e.g., `mynet.us1.twingate.com`)

## Required Ports

| Protocol | Port | Purpose |
|----------|------|---------|
| TCP (outbound) | `*:443` | Controller and Relay communication |
| TCP (outbound) | `*:30000-31000` | Relay fallback when P2P unavailable |
| UDP (outbound) | `*:*` | Peer-to-peer connectivity (optimal performance) |

## FQDN Allowlist

**Preferred**: `*.twingate.com` (wildcard covers all including regional URLs)

**Explicit FQDNs** (if wildcards unavailable):
- `[your-subdomain].twingate.com`
- `[your-network-name].[region].twingate.com` (check admin console URL for your region)
- `admin.twingate.com`, `api.twingate.com`, `binaries.twingate.com`
- `dns.twingate.com`, `oauth.twingate.com`, `relays.twingate.com`
- `relays-prm.twingate.com`, `saml.twingate.com`, `sst.twingate.com`
- `twingate.com`, `get.twingate.com`, `analytics.twingate.com`
- PubNub: `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com`
- Relay clusters: `relays443.twingate.com`, `relays443-prm.twingate.com`
- `relays-do.twingate.com`, `relays-prm-do.twingate.com`
- GCP STUN endpoints: `stun.[region].twingate.com` + `stun-alt.[region].twingate.com`
- DigitalOcean STUN endpoints: `stun.[datacenter].twingate.com` + `stun-alt.[datacenter].twingate.com`

## Gotchas
- **IP-only allowlisting will not work**—must include FQDNs
- Static IP ranges require Enterprise plan; contact Twingate representative
- FQDN list changes without notice—prefer wildcard approach
- Regional URLs (e.g., `us1`, `us2`) are expanding; wildcard covers future regions automatically
- If using explicit FQDNs, identify your tenant's specific regional URL from the admin console URL
- PubNub domains (`pubnubapi.com`, `pubnub.com`, `pndsn.com`) are third-party and must be included

## Prerequisites
- Enterprise plan required for static IP allowlisting
- Know your network subdomain and region (visible in admin console URL)

## Related Docs
- [Relay Cluster Locations](#) — for GCP IP ranges used by Relay
- [Google Cloud external IP ranges](https://cloud.google.com/compute/docs/faq#find_ip_range) — ephemeral relay IPs