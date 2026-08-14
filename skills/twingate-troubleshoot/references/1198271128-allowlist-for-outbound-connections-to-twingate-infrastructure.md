---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-08-14
source_version: a220be033be5f333e19e2f48869797177327e9610c9184eb8a8705a811326fc2
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Twingate Clients and Connectors require specific outbound ports and endpoints to communicate with Twingate's Controller and Relay infrastructure. Organizations with strict egress filtering must allowlist specific FQDNs and/or IP ranges. A wildcard `*.twingate.com` is preferred; granular FQDN lists are provided as an alternative.

## Key Information
- **Applies to:** Twingate Client and Connector components
- **Upcoming change (July 10, 2026):** Add Twingate-owned IP block `167.254.176.0/21` to allowlists alongside existing GCP IP ranges
- **Static IP ranges:** Enterprise customers only — contact Twingate representatives
- Relay connections use ephemeral IPs within Google Cloud IP ranges; see [GCP's published IP range list](https://cloud.google.com/compute/docs/faq#find_ip_range)

## Required Outbound Ports

| Protocol | Port | Purpose |
|----------|------|---------|
| TCP | `*:443` | Controller and Relay communication |
| TCP | `*:30000-31000` | Relay fallback (when P2P unavailable) |
| UDP | `*:*` | Peer-to-peer connectivity (optimal performance) |

## FQDN Allowlist

**Preferred:** `*.twingate.com`

**Required core FQDNs (if wildcards not supported):**
- `<yournetwork>.twingate.com` — replace with your network subdomain
- `admin.twingate.com`, `api.twingate.com`, `dns.twingate.com`
- `relays.twingate.com`, `relays-prm.twingate.com`
- `sst.twingate.com`, `saml.twingate.com`, `oauth.twingate.com`
- `binaries.twingate.com`, `get.twingate.com`
- `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com` *(third-party)*

**GCP relay/STUN endpoints:** `relays443.twingate.com`, `relays443-prm.twingate.com`, plus `stun[/-alt].<gcp-region>.twingate.com` for all configured relay cluster regions.

**Digital Ocean relay/STUN endpoints:** `relays-do.twingate.com`, `relays-prm-do.twingate.com`, plus `stun[/-alt].<do-region>.twingate.com`.

## Gotchas
- **FQDN list is subject to change at any time** — wildcard approach is safer for maintenance
- PubNub domains (`h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com`) are third-party dependencies that must be included
- Relay IPs are ephemeral within GCP ranges — IP-based allowlisting for relays requires allowing entire GCP IP blocks, not specific IPs
- TCP port range `30000-31000` is only used when P2P is unavailable; blocking UDP entirely forces relay-only mode
- Forgetting to update allowlists before **July 10, 2026** will break connectivity — add `167.254.176.0/21` proactively

## Prerequisites
- Knowledge of your Twingate network subdomain (replaces `<subdomain>` in FQDN list)
- Enterprise plan required for static IP allowlisting
- Access to egress firewall/proxy configuration for Client and Connector host environments

## Related Docs
- [Endpoint Requirements - Firewall Rules](https://help.twingate.com/articles/endpoint-requirements)
- [Relay Cluster Locations](https://help.twingate.com/articles/relay-cluster-locations)
- [GCP IP Ranges](https://cloud.google.com/compute/docs/faq#find_ip_range)