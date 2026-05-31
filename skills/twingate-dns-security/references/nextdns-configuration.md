# NextDNS Integration with Twingate

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH). Admins enable the integration through the Admin Console; no additional app installation or network configuration is required on client devices. Only desktop platforms (macOS, Windows, Linux) are supported.

## Key Information
- DNS filtering via NextDNS routes all client DNS traffic through a selected NextDNS profile
- Integration automatically imports configured NextDNS profiles into the Twingate Admin Console
- Device details sent to NextDNS per request: **user's first name** and **device model**
- Billing for NextDNS is separate and managed directly in NextDNS account

## Prerequisites
- Twingate Admin Console access
- NextDNS account with at least one configured profile
- NextDNS API key (from NextDNS account page)
- Desktop clients only (macOS, Windows, Linux) — **mobile not supported**

## Step-by-Step Setup

1. Go to **Settings → Secure DNS** in the Twingate Admin Console
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter the NextDNS API key from your [NextDNS account page](https://my.nextdns.io)
4. Select the NextDNS profile to use as the DoH Resolver
5. Confirm settings — clients will automatically route DNS traffic to the selected profile

**To change profile:** Select **Change** next to NextDNS in the DoH Resolver section.

**To disconnect:** Settings → Secure DNS → DNS Filtering Integrations → NextDNS options → **Disconnect**

## Configuration Values
| Parameter | Location | Notes |
|-----------|----------|-------|
| NextDNS API Key | NextDNS account page | Required for integration |
| NextDNS Profile | Pulled automatically via API | Selected in Admin Console |

## Gotchas
- **Mobile devices (iOS/Android) are not supported** — Secure DNS/NextDNS only works on macOS, Windows, and Linux clients
- NextDNS billing is entirely separate from Twingate; must be managed in NextDNS directly
- User first name and device model are shared with NextDNS for all DNS requests — consider privacy implications

## Related Docs
- [DNS-over-HTTPS (DoH) in Twingate](https://www.twingate.com/docs/dns-over-https)
- [NextDNS Pricing](https://nextdns.io/pricing)
- [NextDNS Account Page](https://my.nextdns.io)