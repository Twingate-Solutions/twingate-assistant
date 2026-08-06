---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-08-06
source_version: e197246e4e373ec414d51ea1c8f4588f4ab262c1adf032392626ec3420bacff8
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Defines required outbound ports and FQDNs for Twingate Client and Connector components to communicate with Twingate's Controller and Relay infrastructure. Relay connections use ephemeral IPs within Google Cloud ranges. Starting July 10, 2026, the IP block `167.254.176.0/21` must be added to allowlists.

## Key Information
- Applies to: **Twingate Client** and **Connector** components
- Wildcard `*.twingate.com` is the simplest allowlist approach if supported
- Relay IPs are ephemeral within GCP ranges — not static (static IPs are Enterprise-only)
- FQDN list is subject to change at any time
- Relay infrastructure spans both **GCP** and **Digital Ocean** regions

## Required Outbound Ports

| Protocol | Port/Range | Purpose |
|----------|-----------|---------|
| TCP | `*:443` | Controller and Relay communication |
| TCP | `*:30000-31000` | Relay fallback (when peer-to-peer unavailable) |
| UDP | `*:*` | Peer-to-peer connectivity (optimal performance) |

## IP Ranges
- **Current:** Google Cloud external IP ranges (see [GCP's maintained list](https://cloud.google.com/compute/docs/fqdn-address))
- **From July 10, 2026:** Add `167.254.176.0/21` (Twingate-owned) alongside GCP ranges

## FQDN Allowlist (Key Entries)
**Replace `subdomain` with your actual Twingate network name.**

Core:
- `<yournetwork>.twingate.com`, `api.twingate.com`, `auth.twingate.com`
- `relays.twingate.com`, `relays-prm.twingate.com`
- `dns.twingate.com`, `binaries.twingate.com`
- `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com` (PubNub for real-time messaging)

GCP Relay endpoints: `relays443.twingate.com`, `stun.<region>.twingate.com`, `stun-alt.<region>.twingate.com`

Digital Ocean Relay endpoints: `relays-do.twingate.com`, `stun.<datacenter>.twingate.com`, `stun-alt.<datacenter>.twingate.com`

## Gotchas
- **PubNub domains required:** `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com` are third-party but necessary
- **FQDN list changes without notice** — monitor for updates if using explicit FQDN allowlisting
- **Static IPs are Enterprise-only** — non-Enterprise customers cannot rely on stable relay IPs
- **Both `stun.*` and `stun-alt.*` subdomains** exist for each region — allowlist both
- **July 2026 breaking change:** Failing to add `167.254.176.0/21` before July 10, 2026 will break connectivity

## Prerequisites
- Enterprise plan required for static IP allowlisting
- Access to firewall/proxy configuration for your environment

## Related Docs
- [Endpoint Requirements - Firewall Rules](https://help.twingate.com/articles/endpoint-requirements-firewall-rules)
- GCP IP ranges: `https://www.gstatic.com/ipranges/cloud.json`