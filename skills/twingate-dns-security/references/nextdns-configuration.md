# NextDNS Configuration

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH). Admins enable the integration through the Admin Console, which routes all DNS traffic through a selected NextDNS profile. No additional app installation or network configuration is required on client devices.

## Key Information
- Integration available on **macOS, Windows, and Linux only** — mobile platforms not supported
- Twingate sends **user's first name** and **device model** to NextDNS with each DNS request
- NextDNS profiles configured in NextDNS are automatically pulled into the Twingate Admin Console
- All DNS traffic is routed through the selected NextDNS profile once configured
- **Billing is separate** — managed directly via NextDNS account, not through Twingate

## Prerequisites
- Twingate Admin Console access
- NextDNS account with API key (create at nextdns.io if needed)
- At least one NextDNS profile configured in NextDNS

## Step-by-Step Setup

1. Go to **Settings → Secure DNS** in the Twingate Admin Console
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter the NextDNS API key (found on the NextDNS account page)
4. Select the desired NextDNS profile as the DoH Resolver
5. Confirm settings — clients will immediately route DNS traffic to the selected profile

**Change profile:** Settings → Secure DNS → DoH Resolver section → **Change** next to NextDNS

**Disconnect:** Settings → Secure DNS → DNS Filtering Integrations → NextDNS options → **Disconnect**

## Configuration Values
| Parameter | Location | Notes |
|-----------|----------|-------|
| NextDNS API Key | NextDNS account page | Required for integration |
| NextDNS Profile | Selected in Twingate Admin Console | Pulled automatically after API key entry |

## Gotchas
- Mobile devices (iOS/Android) are **excluded** — Secure DNS only works on desktop platforms
- NextDNS billing is independent; Twingate does not manage or display NextDNS costs
- Device details (first name + device model) are shared with NextDNS by default — no opt-out mentioned

## Related Docs
- [DNS-over-HTTPS (DoH)](https://www.twingate.com/docs/dns-over-https) — underlying DNS resolution feature
- NextDNS account page — API key and billing management
- NextDNS pricing — separate subscription required