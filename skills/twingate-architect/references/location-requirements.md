# Location Requirements (Geoblocking)

## Page Title
Location Requirements via Geoblocking

## Summary
Twingate Enterprise allows admins to restrict Resource access based on user geolocation (country-level). Restrictions are configured via Resource Policies using either allowlists or denylists. IP-based geolocation is used for location determination, which may not be 100% accurate.

## Key Information
- **Tier**: Enterprise only
- Geoblocking is configured at the **Resource Policy** level, not per-Resource directly
- Two restriction modes: **allowlist** (permitted countries) or **denylist** (blocked countries)
- Location determined via IP address mapped to country using MaxMind GeoLite2 + Google Cloud load balancers
- Coordinates truncated to 2 decimal places before country mapping
- Country boundary data sourced from Natural Earth

## Prerequisites
- Enterprise tier Twingate subscription
- Admin access to configure Resource Policies

## Step-by-Step Configuration
1. Navigate to the target **Resource Policy**
2. Click **Enable** on the location requirements section
3. Choose restriction type: **Allowlist** or **Denylist**
4. Select countries to allow or deny access

## Permanently Blocked Countries
The following countries are **always blocked** regardless of policy configuration and cannot be overridden:
- Cuba
- Iran
- North Korea
- Syria

These countries do not appear in the country selection UI. Additional non-country regions are also permanently blocked.

## Gotchas
- IP geolocation is **not guaranteed accurate** — affected by VPNs, proxies, ISP routing, and database limitations
- Permanently restricted countries cannot be allowlisted — this is hardcoded and not user-configurable
- Blocked users see an error message on their device (no silent failure)
- Geoblocking applies at the Resource Policy level, so changes affect all Resources using that policy

## Related Docs
- Resource Policies (for associating policies with Resources)
- Twingate Pricing (for Enterprise tier details)