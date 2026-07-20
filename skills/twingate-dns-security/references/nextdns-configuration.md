# NextDNS Integration with Twingate

## Page Title
NextDNS Configuration / Integration Guide

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH) for desktop clients. Admins configure the integration entirely within the Twingate Admin Console; no additional app or network changes are required on endpoints.

## Key Information
- Integration enables NextDNS as the DoH resolver for all Twingate desktop users
- NextDNS profiles (configured in NextDNS) are automatically pulled into Twingate Admin Console for selection
- Device details sent per DNS request: **user's first name** and **device model**
- Billing for NextDNS is **separate** from Twingate; managed at NextDNS account level

## Prerequisites
- Twingate Admin Console access
- NextDNS account with at least one profile configured
- NextDNS API key (from NextDNS account page)
- Desktop clients only (macOS, Windows, Linux) — **mobile not supported**

## Step-by-Step Setup

1. Admin Console → **Settings** → **Secure DNS**
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter NextDNS API key (retrieve from NextDNS account page)
4. Select the desired NextDNS profile as the DoH Resolver
5. Confirm settings — clients automatically route DNS traffic to selected profile

**Change profile:** Secure DNS → DoH Resolver section → **Change** next to NextDNS

**Disconnect:** DNS Filtering Integrations → NextDNS options → **Disconnect**

## Configuration Values
| Parameter | Source | Notes |
|-----------|--------|-------|
| NextDNS API Key | NextDNS account page | Required for integration |
| NextDNS Profile | Pulled automatically via API | Selected in Admin Console |

## Gotchas
- **Mobile (iOS/Android) not supported** — Secure DNS/NextDNS only works on macOS, Windows, Linux
- Twingate sends user first name and device model to NextDNS with every DNS request — privacy consideration for users
- NextDNS billing is independent; Twingate does not manage or display NextDNS costs
- Profile changes require going to the DoH Resolver section (separate from the initial integration setup location)

## Related Docs
- DNS-over-HTTPS (DoH) documentation (linked internally in Twingate docs)
- NextDNS account page: [nextdns.io](https://nextdns.io)
- NextDNS pricing page