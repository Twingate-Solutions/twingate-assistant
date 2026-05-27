# NextDNS Integration with Twingate

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH). Admins enable the integration from the Admin Console, which routes all client DNS traffic through a selected NextDNS profile. No additional app installation or network configuration is required on client devices.

## Key Information
- Integration available on **macOS, Windows, and Linux** clients only (not mobile)
- Automatically pulls NextDNS profiles into Admin Console for selection
- Sends device details to NextDNS per request: **user's first name** and **device model**
- Billing for NextDNS is **separate** from Twingate — managed directly in NextDNS account

## Prerequisites
- Twingate Admin Console access
- NextDNS account with at least one configured profile
- NextDNS API key (from NextDNS account page)

## Step-by-Step Setup
1. Go to **Settings → Secure DNS** in the Admin Console
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter the NextDNS API key
4. Select the NextDNS profile to use as the DoH Resolver
5. Confirm settings — client will automatically route DNS traffic to selected profile

## Configuration Values
| Parameter | Source |
|-----------|--------|
| NextDNS API Key | NextDNS account page |
| NextDNS Profile | Pulled automatically after API key entry |

## Management Operations
- **Change profile**: Select **Change** next to NextDNS under the DoH Resolver section
- **Disconnect**: Navigate to DNS Filtering Integrations → NextDNS options → **Disconnect**

## Gotchas
- Mobile devices (iOS/Android) are **not supported** — Secure DNS is desktop-only
- NextDNS billing is independent; Twingate does not manage or consolidate it
- Device metadata (first name + device model) is shared with NextDNS automatically — no opt-out documented

## Related Docs
- [DNS-over-HTTPS (DoH)](https://www.twingate.com/docs/doh) — core DNS resolution feature
- [NextDNS Pricing](https://nextdns.io/pricing)
- [NextDNS Account Page](https://my.nextdns.io/account)