---
source: https://help.twingate.com/articles/1198271128-allowlist-for-outbound-connections-to-twingate-infrastructure
type: help
fetched: 2026-09-13
source_version: 367c9e467acc62f09a2cb595291b93906009a0c7b325938e8dbf4ea41a44afd5
---

# Allowlist for Outbound Connections to Twingate Infrastructure

## Summary
Twingate Clients and Connectors require specific outbound ports and FQDNs to be allowlisted for proper operation. Both IP ranges and FQDNs are needed — IP allowlisting alone is insufficient. Wildcard `*.twingate.com` is the simplest approach; explicit FQDN lists are also supported but subject to change.

## Key Information
- Applies to: Twingate Client and Connector components
- Static IP ranges available to **Enterprise customers only**
- FQDN list is **subject to change at any time**
- Relay connections use ephemeral IPs within Google Cloud IP ranges

## Required Outbound Ports

| Protocol | Port | Purpose |
|----------|------|---------|
| TCP | `*:443` | Controller and Relay communication |
| TCP | `*:30000-31000` | Relay fallback (when P2P unavailable) |
| UDP | `*:*` | Peer-to-peer connectivity (optimal performance) |

## IP Allowlist
- **Twingate-owned block:** `167.254.176.0/21`
- ⚠️ **IPs alone are not sufficient** — FQDNs must also be allowlisted
- Valid configurations: FQDNs only, or IPs + FQDNs together

## FQDN Allowlist

**Simplest option:** `*.twingate.com` (covers all cases including regional URLs)

**Explicit FQDNs (if wildcards not supported):**
- `[your-network-name].twingate.com` — replace with actual tenant name
- `[your-network-name].[region].twingate.com` — check admin console URL for your region (e.g., `us1`, `us2`)
- `admin.twingate.com`, `api.twingate.com`, `binaries.twingate.com`
- `dns.twingate.com`, `oauth.twingate.com`, `relays.twingate.com`, `relays-prm.twingate.com`
- `saml.twingate.com`, `sst.twingate.com`
- PubNub: `h2.pubnubapi.com`, `pubsub.pubnub.com`, `ps.pndsn.com`
- GCP relay: `relays443.twingate.com`, `relays443-prm.twingate.com`
- GCP STUN: `stun.[region].twingate.com` and `stun-alt.[region].twingate.com` (multiple GCP regions)
- DigitalOcean relay: `relays-do.twingate.com`, `relays-prm-do.twingate.com`
- DigitalOcean STUN: `stun.[datacenter].twingate.com` (ams3, fra1, lon1, nyc1/2, sgp1, syd1, tor1, etc.)

## Gotchas
- **IP-only allowlisting will not work** — FQDNs are mandatory
- Regional URLs (`[network].[region].twingate.com`) must be explicitly added if not using wildcard; identify your region from the admin console URL
- FQDN list changes without notice — prefer wildcard when possible
- Third-party domains required: PubNub (`pubnubapi.com`, `pubnub.com`, `pndsn.com`)
- Relay fallback TCP port range `30000-31000` must be open or relay connections will fail

## Related Docs
- GCP IP ranges: [Google Cloud external IP ranges](https://cloud.google.com/compute/docs/faq#find_ip_range)
- Relay Cluster Locations (referenced in source)
- Endpoint Requirements - Firewall Rules (referenced in source)