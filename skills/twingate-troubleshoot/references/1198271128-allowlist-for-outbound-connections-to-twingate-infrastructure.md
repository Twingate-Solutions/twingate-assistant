---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-10-04
source_version: 913743894acc48e66e2ab6d32f545dc1cbd1abd4a4fe25d8a1968b7c8398b4c9
trust: official
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Twingate Clients and Connectors require specific outbound ports and FQDNs to communicate with Twingate's Controller and Relay infrastructure. Both FQDNs and (optionally) IP ranges must be allowlisted; IP ranges alone are insufficient. The FQDN list is subject to change.

## Key Information

- **Applies to:** Twingate Client and Connector components
- **Wildcard option:** `*.twingate.com` covers all required FQDNs if wildcards are supported
- **IP block:** `167.254.176.0/21` (Twingate-owned; Enterprise customers only for static IPs)
- **IPs alone are not sufficient** — FQDNs must also be allowlisted
- Relay connections use ephemeral IPs within Google Cloud IP ranges

## Required Ports

| Protocol | Destination | Purpose |
|----------|-------------|---------|
| TCP (outbound) | `*:443` | Controller and Relay communication |
| TCP (outbound) | `*:30000–31000` | Relay fallback when peer-to-peer unavailable |
| UDP (outbound) | `*:*` | Peer-to-peer connectivity (optimal performance) |

## FQDN Allowlist (Explicit, Non-Wildcard)

**Core domains:**
- `[your-network-name].twingate.com`
- `[your-network-name].[region].twingate.com` (e.g., `mynet.us1.twingate.com`)
- `admin`, `analytics`, `api`, `binaries`, `dns`, `get`, `oauth`, `relays`, `relays-prm`, `saml`, `sst`, `support`, `twingate.com`
- PubNub: `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com`

**Relay/STUN — GCP:** `relays443.twingate.com`, `relays443-prm.twingate.com`, plus `stun[‑alt].<region>.twingate.com` for each GCP region needed

**Relay/STUN — Digital Ocean:** `relays-do.twingate.com`, `relays-prm-do.twingate.com`, plus `stun[‑alt].<datacenter>.twingate.com`

## Regional URLs

- Regions currently: `us1`, `us2` (more planned)
- Format: `[your-network-name].[region].twingate.com`
- Find your region from your admin console URL
- If using `*.twingate.com` wildcard, regional URLs are already covered

## Gotchas

- **IPs-only allowlisting will not work** — FQDNs are required regardless of IP allowlisting
- Static IP ranges (`167.254.176.0/21`) are **Enterprise-only**
- The FQDN list **changes without notice** — prefer the wildcard `*.twingate.com` where possible
- UDP `*:*` outbound is needed for peer-to-peer; blocking it forces relay fallback (higher latency)
- GCP relay IPs are ephemeral — consult [Google's maintained IP list](https://cloud.google.com/compute/docs/faq#find_ip_range) rather than hardcoding

## Prerequisites

- Enterprise plan required for static IP allowlisting
- Admin console access to identify your tenant's regional URL

## Related Docs

- Twingate Relay Cluster Locations
- Google Cloud external IP ranges for GCP relay IPs
- Twingate Connector deployment documentation