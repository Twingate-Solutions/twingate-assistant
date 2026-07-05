# Protect Access to Elasticsearch and Kibana

## Summary
Twingate adds SSO and MFA to Elasticsearch and Kibana without modifying the applications or upgrading to paid Elastic security tiers. Resources are added via the Twingate admin console, leveraging your existing identity provider for authentication and authorization.

## Key Information
- Elastic's security features (SSO, user auth/management) require higher-tier paid plans by default
- Twingate wraps SSO/MFA around Elasticsearch/Kibana at the network layer — no app-level changes needed
- Servers hosting Elastic are hidden from the public internet within a private network
- User provisioning/deprovisioning managed centrally through your identity provider — no separate Elastic user accounts required

## Prerequisites
- Twingate account with admin access
- Elasticsearch and/or Kibana deployed (on-premise or self-hosted)
- Identity provider (IdP) configured with Twingate
- Twingate Connector deployed in the same private network as Elastic instances

## Step-by-Step
1. Open the Twingate admin console
2. Add Elasticsearch/Kibana servers as Resources (see Twingate Resources documentation)
3. Configure access policies on those Resources (enforce MFA via IdP if desired)
4. Assign users or groups from your IdP to the Resources
5. Users access Elastic through Twingate client — no direct internet exposure

## Configuration Values
- No specific env vars or API params documented on this page
- Access policy settings: configured per Resource in admin console
- MFA enforcement: set at the Resource access policy level, delegated to IdP

## Gotchas
- Elasticsearch has no built-in authentication by default — misconfiguration can lead to full data exposure even with paid plans
- This approach does **not** modify Elastic's internal auth — it restricts network-level access only
- Deprovisioning must happen at the IdP level; ensure IdP-Twingate sync is active to avoid orphaned access

## Related Docs
- [Add Resources in Twingate Admin Console](https://www.twingate.com/docs) — linked as "add the relevant servers as resources"
- Step-by-step resource setup instructions (referenced inline, URL not provided on this page)
- Twingate Connectors documentation (implicit prerequisite)
- Identity Provider / SSO integration docs