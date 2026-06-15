# NextDNS Integration Guide

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH). Admins enable the integration from the Admin Console, routing all desktop client DNS traffic through a selected NextDNS profile. No additional app installation or network configuration is required.

## Key Information
- **Platform support**: macOS, Windows, Linux only — mobile devices not supported
- **DNS method**: DNS-over-HTTPS (DoH)
- **Device data sent to NextDNS**: user's first name + device model (per DNS request)
- **NextDNS profiles**: automatically pulled into Twingate Admin Console once API key is connected
- **Billing**: NextDNS billed separately through NextDNS account; not through Twingate

## Prerequisites
- Twingate Admin Console access
- NextDNS account with at least one configured profile
- NextDNS API key (found at NextDNS account page)

## Step-by-Step Setup
1. Go to **Settings → Secure DNS** in Admin Console
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter NextDNS API key (or create a NextDNS account)
4. Select the desired NextDNS profile as the DoH Resolver
5. Confirm settings — clients automatically route DNS traffic to selected profile

## Change / Disconnect
- **Change profile**: Select **Change** next to NextDNS under the DoH Resolver section
- **Disconnect**: Go to DNS Filtering Integrations → NextDNS options → **Disconnect**

## Configuration Values
| Parameter | Source | Notes |
|-----------|--------|-------|
| NextDNS API Key | NextDNS account page | Required for integration |
| NextDNS Profile | Pulled automatically via API | Selected in Admin Console |

## Gotchas
- Mobile (iOS/Android) clients do **not** support Secure DNS/NextDNS integration
- User first name and device model are automatically shared with NextDNS — no opt-out mentioned
- NextDNS pricing/billing is entirely separate from Twingate

## Related Docs
- Twingate DNS-over-HTTPS (DoH) documentation
- NextDNS account page
- NextDNS pricing page