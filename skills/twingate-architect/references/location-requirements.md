# Location Requirements

## Summary
Twingate's Location Requirements feature restricts access to protected Resources based on country-level geolocation using IP address mapping. Admins configure allowlists or denylists on Resource Policies to control which countries can or cannot reach assigned Resources. This is an Enterprise-only feature.

## Key Information
- Geoblocking operates at the **country level** only (no city/region granularity)
- Two modes: **Allowlist** (whitelist specific countries) or **Denylist** (blacklist specific countries)
- Location determined via IP address → geographic coordinates (truncated to 2 decimal places) → country boundary lookup
- Geolocation data sources: MaxMind GeoLite2 + Google Cloud load balancers
- Country boundary data from Natural Earth
- Configured per **Resource Policy**, not per individual Resource

## Prerequisites
- Enterprise plan subscription
- Admin access to Twingate admin console
- Resource Policy must exist before enabling Location Requirements

## Step-by-Step Configuration
1. Open target Resource Policy in admin console
2. Click **Enable** next to **Location Requirements**
3. Choose restriction type:
   - **Allowlist**: only listed countries permitted; all others blocked
   - **Denylist**: listed countries blocked; all others permitted
4. Select countries for the chosen restriction type
5. Save the policy

## Configuration Values
| Setting | Options |
|---|---|
| Restriction Type | `Allowlist` or `Denylist` |
| Country Selection | Any country except permanently blocked ones |

## Permanently Blocked Countries (cannot be overridden)
- Cuba
- Iran
- North Korea
- Syria
- Certain non-country regions (unspecified)

These do not appear in the country selection list.

## Gotchas
- **IP geolocation accuracy varies** — may misclassify VPNs, proxies, satellite connections, or users near borders
- Permanently restricted countries cannot be allowlisted regardless of configuration
- Blocked devices see an error message indicating location does not meet policy requirements (no silent fail)
- Feature is scoped to Resource Policies — changes affect all Resources assigned to that policy

## Related Docs
- Resource Policies
- Twingate pricing page (Enterprise plan required)