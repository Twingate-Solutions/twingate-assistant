# Protect Access to Elasticsearch and Kibana

## Summary
Twingate secures Elasticsearch and Kibana by layering SSO and MFA from your identity provider without modifying the Elastic applications or requiring a paid Elastic security tier. Resources are added via the Twingate admin console, hiding servers from public internet access entirely.

## Key Information
- Elastic's built-in security features (SSO, user auth) require higher-tier paid plans — Twingate bypasses this requirement
- Twingate adds SSO and MFA at the network access layer, not the application layer
- No changes required to Elasticsearch or Kibana configuration
- Users provisioned/deprovisioned centrally via your identity provider — no separate Elastic user accounts needed
- Servers are hidden within a private network, invisible to the public internet

## Prerequisites
- Twingate account with admin console access
- Identity provider configured with Twingate (for SSO/MFA enforcement)
- Twingate Connector deployed on the network hosting Elasticsearch/Kibana
- Elasticsearch and/or Kibana already deployed

## Step-by-Step
1. Log into the Twingate admin console
2. Add Elasticsearch and Kibana servers as Resources (see Twingate resource configuration docs)
3. Assign Resources to the appropriate Group(s) tied to your identity provider
4. (Optional) Configure access policy to enforce MFA via your identity provider

## Configuration Values
- No specific env vars, CLI flags, or API params documented on this page
- Configuration is UI-driven through the Twingate admin console

## Gotchas
- Elastic's free/open tiers lack native auth — without Twingate (or similar), instances may be exposed with no authentication at all
- Misconfiguring Elastic security directly has historically caused major data exposures; Twingate sidesteps this by not touching Elastic config
- Deprovisioning must be done at the identity provider level — this removes Twingate access, but Elastic itself has no separate auth to clean up

## Related Docs
- [Add Resources in Twingate Admin Console](https://www.twingate.com/docs/resources) — step-by-step for adding servers as resources
- Twingate Connector deployment documentation
- Identity provider SSO integration guides