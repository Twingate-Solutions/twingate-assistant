# Protect Access to Elasticsearch and Kibana

## Summary
Twingate adds SSO and MFA to Elasticsearch and Kibana without modifying the applications or requiring paid Elastic security tiers. It hides Elastic servers from the public internet and centralizes user provisioning through your identity provider.

## Key Information
- Elasticsearch and Kibana lack built-in authentication/authorization on free/lower tiers
- Twingate overlays your existing IdP's SSO and MFA onto Elastic instances
- No changes required to Elasticsearch or Kibana configuration
- Works across multiple Elastic instances in multiple environments
- Users provisioned/deprovisioned centrally via IdP — no separate Elastic user accounts needed
- Servers are hidden within private network, not directly accessible from internet

## Prerequisites
- Twingate account with admin console access
- Identity provider (IdP) configured with Twingate
- Elasticsearch/Kibana deployed (on-premise or private network)
- Twingate Connector deployed in the same network as Elastic servers

## Step-by-Step
1. Add Elasticsearch and Kibana servers as Resources in the Twingate admin console
2. Configure access policy on those Resources to enforce MFA via your IdP
3. Assign user groups to the Resources
4. Users access Elastic only through Twingate client — servers remain private

## Configuration Values
- No Elasticsearch/Kibana config changes required
- Access control managed entirely in Twingate admin console
- MFA enforcement set via Twingate access policy on the Resource

## Gotchas
- Elastic's built-in SSO/auth features require paid plans; Twingate bypasses this requirement entirely but does not replace Elastic-native security if you have it configured
- Misconfiguring Elastic security (without Twingate) has historically caused large data exposures — Twingate network-level hiding reduces this risk
- Deprovisioning must happen at the IdP level; ensure IdP-to-Twingate sync is configured to avoid orphaned access

## Related Docs
- [Add Resources in Twingate admin console](https://www.twingate.com/docs/add-a-resource)
- Twingate Connector deployment
- Identity provider / SSO configuration
- Access policy and MFA setup