# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by layering SSO and MFA from your identity provider without modifying the Elastic applications or requiring paid Elastic security tiers. It hides Elastic servers from the public internet within a private network and centralizes user provisioning/deprovisioning through your IdP.

## Key Information
- Elasticsearch and Kibana have no built-in authentication/authorization on free/lower tiers
- Elastic SSO support requires higher-tier paid plans — Twingate bypasses this requirement
- Twingate adds SSO + MFA without any changes to Elastic application configuration
- Servers running Elastic are hidden from the public internet entirely
- User provisioning and deprovisioning managed centrally via identity provider — no separate Elastic user accounts needed

## Prerequisites
- Twingate account with admin console access
- Identity provider (IdP) configured with Twingate
- Elasticsearch and/or Kibana deployed (on-premise or private network)
- Twingate Connector deployed in the same network as Elastic servers

## Step-by-Step
1. Open the Twingate admin console
2. Add Elasticsearch and Kibana servers as **Resources** in Twingate
3. Configure access policies on those Resources to enforce MFA via your IdP
4. Assign user groups to the Resources as needed
5. Users access Elastic only through Twingate — direct internet access is blocked

*Full step-by-step instructions linked from the docs page: "See here for step-by-step instructions"*

## Configuration Values
- No Elastic-side configuration changes required
- No specific env vars or CLI flags documented on this page
- Access policy settings configured in Twingate admin console (MFA enforcement, group assignments)

## Gotchas
- Elastic security features (SSO, user auth) are **not available by default** — misconfiguration has historically caused major data exposures
- This approach provides network-level access control, not application-level authentication within Elastic itself
- Deprovisioning users must be done at the IdP level; ensure IdP-Twingate sync is active to prevent orphaned access

## Related Docs
- [Add Resources in Twingate Admin Console](https://www.twingate.com/docs) — referenced as prerequisite step
- Twingate Connector deployment documentation
- Identity Provider / SSO configuration for Twingate
- Access Policy and MFA configuration in Twingate