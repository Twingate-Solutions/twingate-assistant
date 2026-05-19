# NextDNS Configuration - Twingate Integration

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH) for desktop platforms. Admins enable the integration from the Admin Console to route all user DNS traffic through a selected NextDNS profile. No additional app installation or network configuration is required on client devices.

## Key Information
- Integration available on **macOS, Windows, and Linux** only — not mobile
- Automatically pulls NextDNS profiles into Twingate Admin Console
- Sends device details with DNS requests: **user's first name** and **device model**
- Billing for NextDNS is **separate** from Twingate; managed in NextDNS account directly

## Prerequisites
- Twingate Admin Console access
- NextDNS account with API key (or create one during setup)
- At least one NextDNS profile configured in NextDNS

## Step-by-Step Setup
1. Go to **Settings → Secure DNS** in Admin Console
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter NextDNS API key (from NextDNS account page)
4. Select the NextDNS profile to use as the DoH Resolver
5. Confirm settings — client automatically routes all DNS traffic to selected profile

## Management Operations
- **Change profile**: Select **Change** next to NextDNS under DoH Resolver section
- **Disconnect**: Settings → Secure DNS → DNS Filtering Integrations → NextDNS options → **Disconnect**

## Configuration Values
| Parameter | Value/Location |
|-----------|---------------|
| NextDNS API Key | NextDNS account page |
| DoH Resolver | Selected NextDNS profile |
| Device data sent | User first name + device model |

## Gotchas
- **Mobile not supported** — Secure DNS/NextDNS integration is desktop-only (macOS, Windows, Linux)
- Billing is entirely separate; Twingate has no visibility into NextDNS billing
- Integration sends user PII (first name) and device model to NextDNS by default — review data sharing implications before enabling

## Related Docs
- [DNS-over-HTTPS (DoH)](https://www.twingate.com/docs/) — Twingate's DNS resolution feature overview
- [NextDNS Pricing](https://nextdns.io/pricing)
- [NextDNS Account Page](https://my.nextdns.io/account)