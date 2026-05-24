# Location Requirements (Geoblocking)

## Page Title
Location Requirements via Geoblocking

## Summary
Twingate Enterprise allows admins to control Resource access based on user geolocation using IP address-based country detection. Admins configure allowlists or denylists at the Resource Policy level. Certain countries are permanently blocked regardless of configuration.

## Key Information
- **Tier**: Enterprise only
- **Mechanism**: IP address geolocation mapped to country via latitude/longitude (truncated to 2 decimal places)
- **Data sources**: MaxMind GeoLite2 + Google Cloud load balancers for coordinate data; Natural Earth for country boundary mapping
- **Accuracy caveat**: IP geolocation is not guaranteed accurate in all cases

## Prerequisites
- Enterprise tier Twingate subscription
- Existing Resource Policy to attach location requirements to

## Step-by-Step Configuration
1. Select the target **Resource Policy**
2. Click **Enable** on location requirements
3. Choose restriction type:
   - **Allowlist** — only listed countries can access Resources using this policy
   - **Denylist** — listed countries are blocked from Resources using this policy
4. Select countries to allow or deny

## Configuration Values
| Option | Description |
|--------|-------------|
| Allowlist | Whitelist specific countries; all others blocked |
| Denylist | Blacklist specific countries; all others allowed |

## Permanently Blocked Countries
Always blocked, non-configurable, cannot be overridden (due to embargoes/legal restrictions):
- Cuba
- Iran
- North Korea
- Syria

These countries do not appear in the country selection UI. Additional non-country regions are also permanently blocked.

## Gotchas
- IP geolocation accuracy varies — VPNs, proxies, or ISP routing can cause incorrect country detection
- Permanently blocked countries cannot be added to allowlists or overridden by any admin action
- Geoblocking applies at the **Resource Policy** level, not per individual Resource — all Resources sharing a policy inherit the same rules
- Blocked users see a specific error message on their device

## Related Docs
- Resource Policies (configuration entry point)
- Twingate Pricing Page (tier comparison)