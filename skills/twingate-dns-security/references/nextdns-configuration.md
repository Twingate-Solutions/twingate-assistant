---
source: https://www.twingate.com/docs/nextdns-configuration
type: docs
fetched: 2026-08-14
source_version: e1b65e16a754cb326b66853ce186a2d6366298dc5a78b42fd1e82e655849847c
---

# NextDNS Integration with Twingate

## Page Title
NextDNS Configuration / Integration Guide

## Summary
Twingate integrates with NextDNS to provide DNS filtering via DNS-over-HTTPS (DoH) for desktop clients. Admins configure the integration through the Admin Console without additional app installs. DNS traffic is routed through a selected NextDNS profile automatically after setup.

## Key Information
- Integration enables DNS filtering/security via NextDNS as a DoH resolver
- Device details sent to NextDNS per request: user's **first name** + **device model**
- NextDNS profiles configured in NextDNS are automatically pulled into Twingate Admin Console
- No additional software or network config required beyond Admin Console setup
- Billing for NextDNS is **separate** from Twingate — managed in NextDNS account directly

## Prerequisites
- Twingate Admin Console access
- NextDNS account with API key (or create one at nextdns.io)
- At least one NextDNS profile configured in NextDNS
- **Desktop platforms only**: macOS, Windows, Linux — **mobile not supported**

## Step-by-Step Setup
1. Go to **Settings → Secure DNS** in Admin Console
2. Under **DNS Filtering Integrations**, click **Connect** next to NextDNS
3. Enter NextDNS API key (from NextDNS account page)
4. Select desired NextDNS profile as DoH Resolver
5. Confirm settings — client auto-routes all DNS traffic to selected profile

## Configuration Values
| Parameter | Location | Notes |
|-----------|----------|-------|
| NextDNS API Key | NextDNS account page | Required for integration |
| NextDNS Profile | Admin Console (pulled automatically) | Selects DNS filtering ruleset |

## Managing the Integration
- **Change profile**: Settings → Secure DNS → DoH Resolver section → **Change**
- **Disconnect**: Settings → Secure DNS → DNS Filtering Integrations → NextDNS options → **Disconnect**

## Gotchas
- Mobile clients (iOS/Android) are **not supported** — Secure DNS is desktop-only
- Data shared with NextDNS includes user first name and device model — consider privacy implications
- NextDNS billing is independent; Twingate does not manage or consolidate NextDNS costs
- Must have NextDNS profiles pre-configured before they appear in Twingate Admin Console

## Related Docs
- DNS-over-HTTPS (DoH) documentation (internal Twingate link)
- NextDNS account page: nextdns.io
- NextDNS pricing page