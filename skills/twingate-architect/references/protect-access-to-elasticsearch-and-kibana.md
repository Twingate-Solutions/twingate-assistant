# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by layering SSO and MFA from your identity provider without modifying the applications or requiring paid Elastic security plans. It hides Elastic servers from the public internet within a private network and centralizes user provisioning/deprovisioning through your IdP.

## Key Information
- Elasticsearch and Kibana have **no built-in authentication/authorization** on free/lower tiers
- Twingate adds SSO + MFA without requiring Elastic's paid security features
- Servers are hidden from public internet — not directly accessible or discoverable
- User provisioning managed centrally via identity provider (no separate Elastic accounts needed)

## Prerequisites
- Twingate account with admin console access
- Identity provider configured in Twingate (for SSO/MFA enforcement)
- Elasticsearch/Kibana deployed on-premise or in a private network
- Twingate Connector deployed in the same network as Elastic instances

## Step-by-Step
1. Deploy a Twingate Connector in the network where Elasticsearch/Kibana reside
2. Add the Elasticsearch and Kibana servers as **Resources** in the Twingate admin console
3. Configure access policies on those Resources to enforce MFA via your identity provider
4. Assign users or groups to the Resources through your IdP

> Full step-by-step instructions linked from the page: "add the relevant servers as resources" → Twingate resource setup docs

## Configuration Values
- No specific env vars, CLI flags, or API params documented on this page
- Resource configuration done via Twingate Admin Console UI

## Gotchas
- No changes required to Elasticsearch or Kibana configuration
- SSO/MFA enforcement happens at the **network access layer**, not application layer — Elastic itself remains unmodified
- Deprovisioning a user in your IdP removes Elastic access automatically — but only if access was controlled solely through Twingate (no separate local Elastic accounts exist)
- Multiple Elasticsearch instances (e.g., dev/staging/prod) can each be added as separate Resources without additional Elastic licensing costs

## Related Docs
- [Adding Resources in Twingate](https://www.twingate.com/docs/resources) — referenced as primary setup guide
- Twingate Connector deployment documentation
- Identity Provider / SSO configuration in Twingate