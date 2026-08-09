---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-08-09
source_version: cebbc527d07fc415bd44a0b7208d1c9fbb50e024d33ab39168986f2d6c64f09b
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Defines required outbound ports and FQDNs for Twingate Client and Connector components to communicate with Twingate's Controller and Relay infrastructure. Use `*.twingate.com` wildcard where possible; explicit FQDN list provided when wildcards aren't supported. Relay connections use ephemeral GCP IPs unless static IPs are configured (Enterprise only).

## Key Information
- **Upcoming change (July 10, 2026):** Add `167.254.176.0/21` (Twingate-owned) to allowlists alongside existing GCP IP ranges
- Static IP ranges are **Enterprise customers only**
- Relay connections use ephemeral IPs within Google Cloud IP ranges by default
- Wildcard `*.twingate.com` is the simplest FQDN allowlist approach

## Required Outbound Ports

| Protocol | Port | Purpose |
|----------|------|---------|
| TCP | `*:443` | Controller and Relay communication |
| TCP | `*:30000-31000` | Relay fallback (when P2P unavailable) |
| UDP | `*:*` | Peer-to-peer connectivity (optimal performance) |

## FQDN Allowlist (if wildcards unavailable)

**Core domains:**
- `<yournetwork>.twingate.com`, `*.twingate.com` (wildcard preferred)
- `admin`, `api`, `analytics`, `binaries`, `dns`, `get`, `oauth`, `relays`, `relays-prm`, `saml`, `sst`, `support` — all `.twingate.com`
- `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com` (PubNub for signaling)

**GCP Relay/STUN endpoints:** `relays443.twingate.com`, `relays443-prm.twingate.com`, plus `stun.[region].twingate.com` and `stun-alt.[region].twingate.com` for all supported GCP regions

**Digital Ocean Relay/STUN endpoints:** `relays-do.twingate.com`, `relays-prm-do.twingate.com`, plus `stun.[datacenter].twingate.com` and `stun-alt.[datacenter].twingate.com`

## Gotchas
- Replace `subdomain` in `subdomain.twingate.com` with your actual Twingate network name
- FQDN list **subject to change at any time** — wildcard preferred for stability
- TCP `30000-31000` range only needed when P2P is unavailable; blocking UDP `*:*` degrades to relay mode
- Must add `167.254.176.0/21` **before July 10, 2026** if restricting outbound to GCP ranges today
- GCP relay IP list reference: [Google's external IP ranges](https://cloud.google.com/compute/docs/faq#find_ip_range)

## Prerequisites
- Enterprise plan required for static IP allowlisting
- Contact Twingate representative to enable static IP feature

## Related Docs
- Endpoint Requirements - Firewall Rules
- Relay Cluster Locations
- Google Cloud external IP ranges for relay IP allowlisting