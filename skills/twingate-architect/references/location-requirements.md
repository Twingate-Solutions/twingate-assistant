# Location Requirements (Geoblocking)

## Page Title
Location Requirements via Geoblocking

## Summary
Twingate allows admins to control Resource access based on user geolocation using IP address-based country mapping. Admins can configure allowlists or denylists per Resource Policy. This feature is Enterprise tier only.

## Key Information
- **Tier**: Enterprise only
- Location determined via IP geolocation (MaxMind GeoLite2 + Google Cloud load balancers)
- Coordinates truncated to 2 decimal places, then mapped to country using Natural Earth boundary data
- IP geolocation is not guaranteed to be 100% accurate
- Geoblocking is configured at the **Resource Policy** level, not per-Resource directly

## Permanently Blocked Countries (Non-Configurable)
These countries are always blocked due to embargoes/legal restrictions and cannot be overridden:
- Cuba
- Iran
- North Korea
- Syria

Certain non-country regions are also always blocked.

## Prerequisites
- Enterprise tier Twingate account
- Existing Resource Policy to attach location requirements to

## Step-by-Step Configuration
1. Navigate to the Resource Policy you want to configure
2. Click **Enable** for location requirements
3. Choose restriction type:
   - **Allowlist** — only listed countries can access Resources using this policy
   - **Denylist** — listed countries are blocked from Resources using this policy
4. Select the countries to allow or deny
5. Save configuration

## Configuration Values
| Option | Description |
|--------|-------------|
| Allowlist | Whitelist specific countries; all others blocked |
| Denylist | Blacklist specific countries; all others allowed |

## Gotchas
- Permanently blocked countries (Cuba, Iran, North Korea, Syria) do not appear in the country selection UI and cannot be allowlisted under any circumstances
- IP geolocation accuracy varies — VPNs, proxies, or mobile networks may cause incorrect country mapping
- Geoblocking is applied at the Resource Policy level; ensure the correct policy is targeted
- Blocked devices receive an error message but no granular location feedback to the user

## Related Docs
- Resource Policies documentation
- Twingate pricing page (Enterprise tier requirements)