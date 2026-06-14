# Location Requirements

## Summary
Twingate's geoblocking feature restricts access to protected Resources based on country-level IP geolocation. Admins configure allowlists or denylists on Resource Policies to control which countries can reach assigned Resources. This feature is Enterprise plan only.

## Key Information
- Restriction is configured per **Resource Policy**, not per individual Resource
- Two modes: **Allowlist** (whitelist specific countries) or **Denylist** (block specific countries)
- Location determined via IP address geolocation using MaxMind GeoLite2 + Google Cloud load balancer data
- Coordinates truncated to 2 decimal places, then mapped to country using Natural Earth boundary data
- Blocked users see an error message indicating location doesn't meet policy requirements

## Prerequisites
- Enterprise plan subscription
- Admin access to configure Resource Policies
- Resource Policy must exist before enabling location requirements

## Step-by-Step Configuration
1. Navigate to the target **Resource Policy**
2. Click **Enable** next to **Location Requirements**
3. Choose restriction type:
   - **Allowlist** – only listed countries can access; all others blocked
   - **Denylist** – listed countries are blocked; all others allowed
4. Select countries for the chosen restriction type
5. Save the policy

## Configuration Values
| Setting | Options |
|---|---|
| Restriction Type | `Allowlist` or `Denylist` |
| Country Selection | All countries except permanently blocked ones |

## Permanently Blocked Countries (cannot be overridden)
- Cuba
- Iran
- North Korea
- Syria

These countries do not appear in the selection UI. Certain non-country regions are also always blocked.

## Gotchas
- **IP geolocation accuracy varies** — VPNs, proxies, or regional ISP routing can cause incorrect country detection
- Permanently restricted countries cannot be allowlisted under any circumstances
- Location requirements apply at the **policy level**, affecting all Resources assigned to that policy
- Feature unavailable on non-Enterprise plans — upgrade required

## Common Use Cases
- Compliance blocking for high-risk countries
- Restricting access to countries with physical offices
- Limiting contractor access to known locations

## Related Docs
- [Resource Policies](https://www.twingate.com/docs/resource-policies)
- [Twingate Pricing](https://www.twingate.com/pricing)