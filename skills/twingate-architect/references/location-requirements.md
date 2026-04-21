## Location Requirements (Geoblocking)

Enterprise-only feature that enables country-based access control on Resource Policies. Admins configure allowlists or denylists per Resource Policy using IP-based geolocation.

**Key Information:**
- Available on Enterprise tier only
- Configured per Resource Policy (not per individual Resource); all Resources using the policy inherit the location rule
- Two modes: Allowlist (only listed countries permitted) or Denylist (listed countries blocked)
- Geolocation uses MaxMind GeoLite2 + Google Cloud load balancer data; accuracy is not guaranteed
- IP coordinates truncated to two decimal places before country mapping

**Always-Blocked Countries (non-configurable, not selectable in UI):**
- Cuba, Iran, North Korea, Syria

**Configuration Steps:**
1. Navigate to the Resource Policy to modify
2. Click Enable on location requirements
3. Choose restriction type: Allowlist or Denylist
4. Select target countries

**Gotchas:**
- IP-based geolocation can be inaccurate -- VPNs, proxies, and carrier NAT may cause incorrect country attribution
- Embargoed countries are always blocked regardless of admin configuration and cannot be overridden
- Geoblocking is a Policy-level setting -- changing it affects all Resources assigned to that Policy

**Related Docs:**
- /docs/resource-policies -- Resource Policy configuration
- /docs/security-policies -- Security policy overview
