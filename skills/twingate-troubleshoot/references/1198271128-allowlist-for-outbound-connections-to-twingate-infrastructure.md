---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-09-27
source_version: 8d956436f6d6a754f54bce220a1ce026f6f42a17da496bc2451acd01c252eb79
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Twingate Clients and Connectors require specific outbound ports and FQDNs to be allowlisted for communication with Twingate's Controller and Relay infrastructure. IP allowlisting alone is insufficient — FQDNs must always be included. Wildcarding `*.twingate.com` is the simplest approach when supported.

## Key Information
- **Applies to**: Twingate Client and Connector components
- Static IP ranges available to **Enterprise customers only**
- FQDN list is **subject to change at any time**
- IP allowlist alone is **not sufficient** — must include FQDNs
- Relay connections route through ephemeral IPs within Google Cloud ranges

## Required Outbound Ports

| Protocol | Destination | Purpose |
|----------|-------------|---------|
| TCP | `*:443` | Communication with Twingate Controller and Relay |
| TCP | `*:30000-31000` | Relay fallback when peer-to-peer unavailable |
| UDP | `*:*` | Peer-to-peer connectivity (optimal performance) |

## IP Allowlist
- **Twingate-owned block**: `167.254.176.0/21` (Enterprise only; must also allowlist FQDNs)

## FQDN Allowlist

**Recommended wildcard** (if supported): `*.twingate.com`

**Required FQDNs if wildcards unavailable:**
- `<your-subdomain>.twingate.com` — your network name
- `<your-network-name>.[region].twingate.com` — tenant regional URL (check admin console URL)
- `admin`, `analytics`, `api`, `binaries`, `dns`, `get`, `oauth`, `relays`, `relays-prm`, `saml`, `sst`, `support` — all `.twingate.com`
- `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com` — PubNub endpoints
- Regional STUN endpoints: `stun.[region].twingate.com` and `stun-alt.[region].twingate.com`

**GCP relay endpoints**: `relays443.twingate.com`, `relays443-prm.twingate.com`  
**DigitalOcean relay endpoints**: `relays-do.twingate.com`, `relays-prm-do.twingate.com`

## Regional URLs
- Format: `[your-network-name].[region].twingate.com`
- Current regions: `us1`, `us2` (more planned)
- Find your region: check the URL when logged into admin console
- If using `*.twingate.com` wildcard — no additional action needed

## Gotchas
- **IP-only allowlisting will not work** — FQDNs are always required
- FQDN list changes without notice — monitor for updates
- PubNub domains (`pubnubapi.com`, `pubnub.com`, `pndsn.com`) are non-Twingate domains that must also be allowlisted
- STUN endpoints span both GCP and DigitalOcean infrastructure across many global regions
- Tenant regional subdomain (e.g., `network.us1.twingate.com`) must be explicitly added when not using wildcard

## Related Docs
- [Endpoint Requirements - Firewall Rules](#)
- [Relay Cluster Locations](#)
- [Google Cloud external IP ranges](https://cloud.google.com/compute/docs/faq#find_ip_range)