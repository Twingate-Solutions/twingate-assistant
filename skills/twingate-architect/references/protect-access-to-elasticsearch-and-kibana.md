# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by layering SSO and MFA from your identity provider without modifying the applications or requiring paid Elastic security tiers. It hides Elastic servers from the public internet and centralizes user provisioning/deprovisioning through your IdP.

## Key Information
- Elasticsearch and Kibana have **no built-in authentication/authorization** on free/lower tiers
- SSO and MFA features in Elastic require expensive paid plans — Twingate bypasses this requirement
- No changes required to Elasticsearch or Kibana configurations
- Users managed centrally via IdP; no separate Elastic user accounts needed
- Servers are hidden within private network, invisible to public internet

## Prerequisites
- Twingate account with admin console access
- Identity provider (IdP) configured with Twingate
- Elasticsearch/Kibana deployed on-premise or in private network
- Twingate Connector deployed in the same network as Elastic instances

## Step-by-Step
1. Deploy Twingate Connector in the network hosting Elasticsearch/Kibana
2. Add Elasticsearch server as a Resource in the Twingate admin console
3. Add Kibana server as a Resource in the Twingate admin console
4. Configure access policies on each Resource (assign groups, enforce MFA via IdP)
5. Users access Elastic only through Twingate client — no direct internet exposure

## Configuration Values
- No Elasticsearch/Kibana-specific config changes required
- Resource configuration done entirely in Twingate admin console
- MFA enforcement set at the Twingate **access policy** level, delegated to IdP

## Gotchas
- SSO/MFA enforcement is at the **network access layer** (Twingate), not application layer — Elastic itself remains unauthenticated internally
- Ensure Connectors are placed correctly so Elastic ports are not exposed externally before Twingate is configured
- Deprovisioning works only if user management flows through the IdP connected to Twingate; manual Elastic accounts bypass this

## Related Docs
- [Add Resources in Twingate Admin Console](https://www.twingate.com/docs/add-resources)
- Twingate Connector deployment guide
- Identity Provider (SSO) integration with Twingate
- Access Policy configuration (MFA enforcement)