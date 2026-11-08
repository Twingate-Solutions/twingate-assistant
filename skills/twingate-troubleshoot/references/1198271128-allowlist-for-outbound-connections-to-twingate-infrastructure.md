---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-11-08
source_version: ba1b46b544f1b0110a84554e0319a28c6928ec89820290210ef4354cf6508e6b
trust: official
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Twingate Clients and Connectors require specific outbound ports and FQDNs to be allowlisted for communication with Twingate's Controller, Relay, and supporting infrastructure. FQDNs are mandatory; IP allowlisting alone is insufficient. A wildcard `*.twingate.com` is the simplest approach if supported by your firewall.

## Key Information
- Applies to: Twingate **Client** and **Connector** components
- Static IP ranges available to **Enterprise customers only**
- IP allowlist alone will **not** work — FQDNs must also be allowlisted
- Relay connections use ephemeral IPs within Google Cloud IP ranges
- FQDN list is **subject to change at any time**

## Required Ports

| Protocol | Port/Range | Purpose |
|----------|-----------|---------|
| TCP (outbound) | `*:443` | Controller and Relay communication |
| TCP (outbound) | `*:30000–31000` | Relay fallback (when P2P unavailable) |
| UDP (outbound) | `*:*` | Peer-to-peer connectivity (optimal performance) |

## IP Block
- Twingate-owned: `167.254.176.0/21` (Enterprise only; insufficient alone)

## FQDN Allowlist

**Wildcard (recommended if supported):** `*.twingate.com`

**Explicit FQDNs (if wildcards unavailable):**
- `<your-network-name>.twingate.com`
- `<your-network-name>.<region>.twingate.com` (e.g., `yournet.us1.twingate.com`)
- `admin`, `analytics`, `api`, `binaries`, `dns`, `get`, `oauth`, `relays`, `relays-prm`, `saml`, `sst`, `support`, `twingate.com`
- PubNub: `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com`
- GCP relay/STUN: `relays443.twingate.com`, `relays443-prm.twingate.com`, `stun.<gcp-region>.twingate.com`, `stun-alt.<gcp-region>.twingate.com`
- DigitalOcean relay/STUN: `relays-do.twingate.com`, `relays-prm-do.twingate.com`, `stun.<do-region>.twingate.com`, `stun-alt.<do-region>.twingate.com`

## Regional URLs
- Format: `[network-name].[region].twingate.com` (current regions: `us1`, `us2`)
- Find your region in the URL when logged into the admin console
- Required addition to explicit FQDN lists; already covered by `*.twingate.com` wildcard

## Gotchas
- **IP-only allowlisting will not work** — FQDNs are always required
- The explicit FQDN list changes without notice; prefer the wildcard where possible
- STUN endpoints span both GCP and DigitalOcean — both sets needed for full P2P support
- Blocking UDP `*:*` degrades performance (forces relay fallback) but doesn't break connectivity

## Related Docs
- [Google Cloud external IP ranges](https://cloud.google.com/compute/docs/faq#find_ip_range)
- Twingate Relay Cluster Locations (linked from Twingate admin docs)