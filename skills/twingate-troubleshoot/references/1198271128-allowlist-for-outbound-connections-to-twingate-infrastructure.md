---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-08-16
source_version: f389a1131e5f68e6aa624dd531728c9a9cd21d6d5fb7a603b9ccba6427b6cf3b
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Defines required outbound firewall rules and FQDN allowlists for Twingate Client and Connector components. Covers TCP/UDP port requirements and a full list of domains/IPs to permit. Relay connections use ephemeral GCP IPs unless static IPs are configured (Enterprise only).

## Key Information
- **Upcoming change (July 10, 2026):** Add `167.254.176.0/21` (Twingate-owned) to allowlist alongside existing GCP IP ranges
- Static IP ranges available to **Enterprise customers only**
- Applies to both Twingate **Client** and **Connector** components
- Relay connections use ephemeral IPs within Google Cloud IP ranges by default
- Wildcard `*.twingate.com` is the simplest FQDN allowlist if supported

## Required Outbound Ports

| Protocol | Port | Purpose |
|----------|------|---------|
| TCP | `*:443` | Controller and Relay communication |
| TCP | `*:30000-31000` | Relay fallback (when P2P unavailable) |
| UDP | `*:*` | Peer-to-peer connectivity (optimal performance) |

## FQDN Allowlist

**Recommended:** `*.twingate.com` (wildcard)

**Required non-Twingate domains:**
- `h2.pubnubapi.com`
- `pubsub.pubnub.com`
- `ps.pndsn.com`

**Key Twingate domains (partial list):**
- `<subdomain>.twingate.com` (your network name)
- `api.twingate.com`, `relays.twingate.com`, `relays-prm.twingate.com`
- `relays443.twingate.com`, `relays-do.twingate.com`
- `stun.<region>.twingate.com` and `stun-alt.<region>.twingate.com` for all GCP/DigitalOcean relay regions
- Full list includes 40+ STUN endpoints across GCP and DigitalOcean regions

## IP Ranges

- **GCP IP ranges:** Use [Google's maintained list](https://cloud.google.com/compute/docs/faq#find_ip_range) for Relay Cluster Locations
- **Upcoming (July 2026):** `167.254.176.0/21` (static, Enterprise only)

## Gotchas
- FQDN list **is subject to change at any time** — wildcard is safer for long-term maintenance
- UDP `*:*` is required for P2P; restricting it forces relay path (higher latency)
- TCP 30000–31000 is only needed when P2P is unavailable
- Must replace `subdomain` in `subdomain.twingate.com` with your actual network name
- PubNub domains are required (third-party, not `*.twingate.com`)
- Both `stun.*` and `stun-alt.*` variants must be allowed for all regions used

## Related Docs
- Endpoint Requirements - Firewall Rules (referenced internally)
- Google Cloud external IP ranges for GCP relay IPs