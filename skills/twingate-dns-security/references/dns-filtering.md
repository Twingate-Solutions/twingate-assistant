---
source: https://www.twingate.com/docs/dns-filtering
type: docs
fetched: 2026-11-13
source_version: 5383e71cd0c8097e533bbd3246a0239928414710a657118667f5824b3529b2b7
trust: official
---

# DNS Filtering Overview

## Summary
Twingate DNS filtering is a native add-on (Business and Enterprise plans) that filters DNS traffic over DNS-over-HTTPS for users running the macOS, Windows, or Linux Client. It blocks security threats and restricted content categories by refusing to resolve blocked domains. Rules are managed through ranked profiles assigned to Groups.

## Key Information
- Platforms: macOS, Windows, Linux only. Mobile is not supported.
- Works at the DNS layer, so all traffic types (HTTPS, SSH, etc.) to blocked domains fail.
- No config changes are needed beyond running the Twingate Client.
- Block pages appear only for HTTP. HTTPS blocked domains behave as nonexistent (site can't be reached). HTTPS block pages need the Twingate Browser Extension (early access; contact your account manager).
- Security categories: threat intelligence feeds, Google Safe Browsing, DNS rebinding, IDN homograph, typosquatting, DGA, newly registered domains (<30 days), parked domains. All are on by default except newly registered domains.
- Content categories: gambling, dating, adult, piracy, social media (excludes messaging apps), games, streaming, Force Safe Search, YouTube safe mode.
- Privacy options: block disguised third-party trackers, affiliate and tracking links, ads and trackers.
- The allowlist overrides all other rules. TLDs can be denylisted (e.g., `.zip`).

## Prerequisites
- Business or Enterprise plan with the DNS filtering add-on.
- Admin Console access.
- Twingate Client on macOS, Windows, or Linux.

## Step-by-Step: Enable
1. Admin Console → **Internet Security** → **Secure DNS**.
2. If Secure DNS is disabled, enable it and choose **Twingate DNS Filtering**.
3. If it's already enabled, change the DoH resolver to **Twingate DNS Filtering**.
4. Click a profile name (or **Manage** → **Edit Filtering Rules**) to configure rules. Use **Security Categories**, **Content Restrictions**, and **Privacy Protection** for the category modals.

## Profile Behavior
- Default: one profile with the Everyone Group assigned.
- Profiles are ranked; higher rank wins when a user is in multiple Groups.
- A Group can be assigned to only one profile.
- Users in no assigned Group are not filtered.
- Exception Groups override profile assignment (the user gets no filtering). A Group can't be both assigned and an exception.
- Recommended: a lowest-ranked default profile with Everyone assigned.
- Maximum of 10 profiles.
- Signed-out devices set to always run Internet Security use the lowest-ranked profile.

## Configuration Values (S3 log export)
JSON, one event per line, with `event_type: "dns_filtering"`. Event fields:
- `version`, `time` (UTC), `domain`, `root`
- `device.id` (Twingate device ID if the device has ever logged in, otherwise hardware ID), `device.name`
- `connection.client_ip`, `connection.protocol` (`DNS-over-HTTPS`)
- `status`: `default`, `blocked`, or `allowed`
- `reasons[]`: `id` (e.g., `category:social-networks`) and `name`

## Gotchas
- Blocking ads, trackers, and tracking links can break sites. It can also break email unsubscribe links.
- By default, filtering runs only while a user is signed in. To keep it running when signed out, configure Internet Security Client Configuration.
- Removing Everyone from the default profile leaves unassigned users unfiltered.
- To unblock a domain, add it to the allowlist.
- To exempt users, add them to an Exception Group.
- Check blocked domains under "Recent DNS Activity" on the Secure DNS page.

## Related Docs
- DNS-over-HTTPS (Secure DNS) documentation
- Filtering Analytics
- AI Usage Overview
- Syncing data to S3
- Internet Security Client Configuration
- Exception Groups